#!/usr/bin/env python3
"""Lint and normalize SKILL.md / command frontmatter for the Sloth Skill Tree.

Two modes:

  python normalize-frontmatter.py            # LINT (default): report FAIL/WARN, exit 1 on any FAIL
  python normalize-frontmatter.py --fix      # NORMALIZE: mechanically fix name/version/quoting

LINT enforces the description rule (see CONTRIBUTING.md):
  - skills: description must start with "Use when", be third-person, <= 240 chars,
    and contain no quoted-keyword dumps (> 3 double-quoted phrases).
  - commands are slash-invoked (not model-routed): relaxed profile (length + no
    first-person opener only; "Use when" not required).

--fix performs MECHANICAL normalization only (name -> directory name, strip version,
collapse multi-line descriptions, quote unquoted descriptions). It does NOT invent
"Use when" wording — that stays human/agent-authored.

Covers all five (six) plugins AND the 3 global skills under skills/.
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Lint rules
# ---------------------------------------------------------------------------
FIRST_PERSON_RE = re.compile(
    r"^\s*(I |I'm |I am |We |My |As an? (expert|senior|experienced)\b|You are\b|"
    r"Expert\b|Senior\b|Elite\b|World-class\b)",
    re.IGNORECASE,
)
USE_WHEN_RE = re.compile(r"^\s*Use (this skill )?when\b", re.IGNORECASE)
# Count DOUBLE-quoted phrases only (straight + curly); keyword dumps in this repo
# use double quotes, and this avoids false positives from apostrophes.
QUOTED_KW_RE = re.compile(r'"[^"]+"|“[^”]+”')

MAX_HARD = 240   # FAIL above this
MAX_SOFT = 200   # WARN above this
KW_MAX = 3       # > this many quoted phrases => keyword-dump FAIL


# ---------------------------------------------------------------------------
# Frontmatter parsing (read-only, tolerant of multi-line descriptions)
# ---------------------------------------------------------------------------
def parse_frontmatter(content: str):
    """Return {name, version, description} or None if no frontmatter."""
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    lines = parts[1].strip("\n").split("\n")
    name = version = description = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("name:"):
            name = line[len("name:"):].strip().strip('"').strip("'")
        elif line.startswith("version:"):
            version = line[len("version:"):].strip()
        elif line.startswith("description:"):
            rest = line[len("description:"):].strip()
            if rest in (">", "|", ">-", "|-", ">+", "|+"):
                collected = []
                j = i + 1
                while j < len(lines) and (
                    lines[j].startswith((" ", "\t")) or lines[j].strip() == ""
                ):
                    collected.append(lines[j].strip())
                    j += 1
                description = " ".join(s for s in collected if s)
                i = j
                continue
            else:
                description = rest.strip().strip('"').strip("'")
        i += 1
    return {"name": name, "version": version, "description": description}


def lint_description(desc, is_command=False):
    """Return list of (level, message) tuples for a description string.

    Skills use the strict profile (length, 'Use when', no keyword dumps all FAIL).
    Commands are slash-invoked, not model-routed, so they get a relaxed profile:
    only a first-person opener FAILs; length / keyword issues are WARN.
    """
    issues = []
    if not desc:
        issues.append(("FAIL", "missing description"))
        return issues
    d = desc.strip()
    # Commands never block on length/keyword density; skills do.
    length_kw_level = "WARN" if is_command else "FAIL"

    if len(d) > MAX_HARD:
        issues.append((length_kw_level, f"{len(d)} chars (hard max {MAX_HARD})"))
    elif len(d) > MAX_SOFT:
        issues.append(("WARN", f"{len(d)} chars (soft max {MAX_SOFT})"))

    if FIRST_PERSON_RE.search(d):
        issues.append(("FAIL", "first-person / persona opener"))

    if not is_command and not USE_WHEN_RE.search(d):
        issues.append(("FAIL", "must start with 'Use when'"))

    quoted = QUOTED_KW_RE.findall(d)
    if len(quoted) > KW_MAX:
        issues.append((length_kw_level, f"quoted-keyword dump ({len(quoted)} quoted phrases, max {KW_MAX})"))

    return issues


def lint_file(filepath: Path, is_command=False):
    """Return list of (level, message) for a SKILL.md or command .md file."""
    content = filepath.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    if fm is None:
        return [("FAIL", "no frontmatter")]
    expected = filepath.stem if is_command else filepath.parent.name
    issues = []
    if fm["name"] != expected:
        issues.append(("WARN", f"name '{fm['name']}' != expected '{expected}'"))
    if not is_command and fm["version"]:
        issues.append(("WARN", f"stray version field: {fm['version']}"))
    issues += lint_description(fm["description"], is_command=is_command)
    return issues


# ---------------------------------------------------------------------------
# Mechanical normalization (--fix)
# ---------------------------------------------------------------------------
def normalize_file(filepath: Path, is_command: bool):
    """Normalize a single SKILL.md or command .md file mechanically."""
    expected_name = filepath.stem if is_command else filepath.parent.name

    content = filepath.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"  SKIP (no frontmatter): {filepath}")
        return False

    frontmatter, body = parts[1], parts[2]
    lines = frontmatter.strip().split("\n")
    new_lines = []
    has_name = False
    description_value = ""
    in_multiline_desc = False

    for line in lines:
        if line.startswith("version:"):
            continue

        if line.startswith("name:"):
            new_lines.append(f"name: {expected_name}")
            has_name = True
            continue

        if line.startswith("description:"):
            rest = line[len("description:"):].strip()
            if rest in (">", "|", ">-", "|-", ">+", "|+"):
                in_multiline_desc = True
                description_value = ""
                continue
            elif rest.startswith('"') or rest.startswith("'"):
                new_lines.append(line)
                continue
            else:
                new_lines.append(f'description: "{rest}"')
                continue

        if in_multiline_desc:
            stripped = line.strip()
            if stripped and not line.startswith((" ", "\t")) and ":" in line:
                in_multiline_desc = False
                desc = " ".join(description_value.split()).replace('"', '\\"')
                new_lines.append(f'description: "{desc}"')
                if line.startswith("version:"):
                    continue
                new_lines.append(line)
            else:
                description_value += " " + stripped
            continue

        new_lines.append(line)

    if in_multiline_desc:
        desc = " ".join(description_value.split()).replace('"', '\\"')
        new_lines.append(f'description: "{desc}"')

    if is_command and not has_name:
        new_lines.insert(0, f"name: {expected_name}")

    new_content = f'---\n{chr(10).join(new_lines)}\n---{body}'
    filepath.write_text(new_content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------
def collect_files(repo: Path):
    skills = sorted(repo.glob("plugins/*/skills/*/SKILL.md")) + sorted(repo.glob("skills/*/SKILL.md"))
    commands = sorted(repo.glob("plugins/*/commands/*.md"))
    return skills, commands


# ---------------------------------------------------------------------------
# Modes
# ---------------------------------------------------------------------------
def run_fix(repo: Path):
    skills, commands = collect_files(repo)
    print(f"Normalizing {len(skills)} skills + {len(commands)} commands\n")
    for f in skills:
        if normalize_file(f, is_command=False):
            print(f"  OK: {f.relative_to(repo)}")
    for f in commands:
        if normalize_file(f, is_command=True):
            print(f"  OK: {f.relative_to(repo)}")
    print("\nDone.")


def run_lint(repo: Path) -> int:
    skills, commands = collect_files(repo)
    fails = warns = 0

    def report(group, files, is_command):
        nonlocal fails, warns
        printed_header = False
        for f in files:
            issues = lint_file(f, is_command=is_command)
            if not issues:
                continue
            if not printed_header:
                print(f"\n== {group} ==")
                printed_header = True
            for level, msg in issues:
                if level == "FAIL":
                    fails += 1
                else:
                    warns += 1
                print(f"  [{level}] {f.relative_to(repo)}: {msg}")

    report("Skills", skills, is_command=False)
    report("Commands (relaxed profile)", commands, is_command=True)

    print(f"\n{'-' * 60}")
    print(f"Linted {len(skills)} skills + {len(commands)} commands: {fails} FAIL, {warns} WARN")
    if fails:
        print("Description lint FAILED. Fix the FAILs above (see CONTRIBUTING.md).")
        return 1
    print("Description lint passed.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Lint/normalize Sloth Skill Tree frontmatter")
    parser.add_argument(
        "--fix",
        action="store_true",
        help="apply mechanical normalization (name=dir, strip version, quote/collapse description)",
    )
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent

    if args.fix:
        run_fix(repo)
        sys.exit(0)
    sys.exit(run_lint(repo))


if __name__ == "__main__":
    main()
