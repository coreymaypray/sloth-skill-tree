#!/usr/bin/env python3
"""Single source of truth for skill/command counts and per-plugin skill tables.

Walks the plugins declared in .claude-plugin/marketplace.json plus the global
skills/ directory, then:
  - injects a counts summary into the root README (AUTOGEN:counts region),
  - injects a count line + skills table into each plugin README
    (AUTOGEN:counts and AUTOGEN:skills regions),
  - writes counts.json.

Modes:
  python scripts/generate-counts.py          # write/inject + counts.json
  python scripts/generate-counts.py --check   # verify nothing is stale (CI); exit 1 if so
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
COUNTS_JSON = REPO / "counts.json"

CSTART, CEND = "<!-- AUTOGEN:counts:start -->", "<!-- AUTOGEN:counts:end -->"
SSTART, SEND = "<!-- AUTOGEN:skills:start -->", "<!-- AUTOGEN:skills:end -->"


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    out = {}
    for line in parts[1].strip().split("\n"):
        m = re.match(r"^([\w-]+):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def discover():
    mkt = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugins = []
    for entry in mkt["plugins"]:
        src = (REPO / entry["source"]).resolve()
        skills = []
        sd = src / "skills"
        if sd.exists():
            for d in sorted(p for p in sd.iterdir() if p.is_dir()):
                sm = d / "SKILL.md"
                if sm.exists():
                    fm = parse_frontmatter(sm)
                    skills.append((d.name, fm.get("description", "")))
        cd = src / "commands"
        commands = sorted(c.stem for c in cd.glob("*.md")) if cd.exists() else []
        plugins.append({
            "name": entry["name"],
            "version": entry.get("version", ""),
            "readme": src / "README.md",
            "skills": skills,
            "commands": commands,
        })
    globals_ = []
    gd = REPO / "skills"
    if gd.exists():
        for d in sorted(p for p in gd.iterdir() if p.is_dir()):
            sm = d / "SKILL.md"
            if sm.exists():
                fm = parse_frontmatter(sm)
                globals_.append((d.name, fm.get("description", "")))
    return plugins, globals_


def cell(text: str) -> str:
    return text.replace("|", "\\|").strip()


def root_counts_md(plugins, globals_) -> str:
    plugin_skills = sum(len(p["skills"]) for p in plugins)
    total_skills = plugin_skills + len(globals_)
    total_commands = sum(len(p["commands"]) for p in plugins)
    lines = [
        f"**{len(plugins)} plugins · {total_skills} skills "
        f"({plugin_skills} specialist + {len(globals_)} global) · {total_commands} commands**",
        "",
        "| Plugin | Version | Skills | Commands |",
        "|--------|--------:|-------:|---------:|",
    ]
    for p in plugins:
        lines.append(f"| `{p['name']}` | {p['version']} | {len(p['skills'])} | {len(p['commands'])} |")
    lines.append(f"| _global skills_ | — | {len(globals_)} | — |")
    return "\n".join(lines)


def plugin_counts_md(p) -> str:
    return f"**{len(p['skills'])} skills · {len(p['commands'])} commands**"


def plugin_skills_md(p) -> str:
    lines = ["| Skill | Triggers |", "|-------|----------|"]
    for name, desc in p["skills"]:
        lines.append(f"| `{name}` | {cell(desc)} |")
    if p["commands"]:
        lines.append("")
        lines.append("**Commands:** " + ", ".join(f"`/{c}`" for c in p["commands"]))
    return "\n".join(lines)


def inject(text: str, start: str, end: str, payload: str):
    """Replace the region between start/end markers. Returns (new_text, found)."""
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        return text, False
    return pattern.sub(f"{start}\n{payload}\n{end}", text), True


def apply_regions(path: Path, regions, check: bool, stale: list, missing: list):
    """regions: list of (start, end, payload). Mutates file or records staleness."""
    if not path.exists():
        missing.append(f"{path.relative_to(REPO)} (file missing)")
        return
    original = path.read_text(encoding="utf-8")
    text = original
    for start, end, payload in regions:
        text, found = inject(text, start, end, payload)
        if not found:
            missing.append(f"{path.relative_to(REPO)} (missing marker {start})")
    if text != original:
        if check:
            stale.append(str(path.relative_to(REPO)))
        else:
            path.write_text(text, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify regions are current; exit 1 if stale")
    args = ap.parse_args()

    plugins, globals_ = discover()
    plugin_skills = sum(len(p["skills"]) for p in plugins)
    totals = {
        "plugins": len(plugins),
        "specialist_skills": plugin_skills,
        "global_skills": len(globals_),
        "total_skills": plugin_skills + len(globals_),
        "total_commands": sum(len(p["commands"]) for p in plugins),
    }
    counts_payload = {
        "totals": totals,
        "plugins": [
            {"name": p["name"], "version": p["version"],
             "skills": len(p["skills"]), "commands": len(p["commands"])}
            for p in plugins
        ],
    }

    stale, missing = [], []

    # Root README
    apply_regions(
        REPO / "README.md",
        [(CSTART, CEND, root_counts_md(plugins, globals_))],
        args.check, stale, missing,
    )
    # Per-plugin READMEs
    for p in plugins:
        apply_regions(
            p["readme"],
            [(CSTART, CEND, plugin_counts_md(p)),
             (SSTART, SEND, plugin_skills_md(p))],
            args.check, stale, missing,
        )

    # counts.json
    new_json = json.dumps(counts_payload, indent=2) + "\n"
    if args.check:
        current = COUNTS_JSON.read_text(encoding="utf-8") if COUNTS_JSON.exists() else ""
        if current != new_json:
            stale.append("counts.json")
    else:
        COUNTS_JSON.write_text(new_json, encoding="utf-8")

    if missing:
        print("Missing markers / files (add the AUTOGEN markers):")
        for m in missing:
            print(f"  - {m}")
    if args.check:
        if stale or missing:
            print(f"\nSTALE: {len(stale)} file(s) out of date. Run: python scripts/generate-counts.py")
            for s in stale:
                print(f"  - {s}")
            sys.exit(1)
        print(f"Counts current: {totals['total_skills']} skills, {totals['total_commands']} commands.")
        sys.exit(0)
    print(f"Generated counts: {totals['plugins']} plugins, {totals['total_skills']} skills "
          f"({totals['specialist_skills']} specialist + {totals['global_skills']} global), "
          f"{totals['total_commands']} commands.")
    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
