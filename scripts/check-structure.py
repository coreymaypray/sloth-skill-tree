#!/usr/bin/env python3
"""Structural integrity checks for the Sloth Skill Tree.

Verifies (exit 1 on any FAIL):
  - every marketplace plugin source path exists;
  - every plugin has .claude-plugin/plugin.json whose name == directory name and
    whose name/version match the marketplace entry;
  - every skill dir has a SKILL.md whose frontmatter name == directory name, has a
    description, and carries no version: field;
  - every command .md has a description.

Complements normalize-frontmatter.py (description lint) and generate-counts.py
(count staleness). Run all three via scripts/validate.sh.
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"

fails, warns = [], []


def fail(msg):
    fails.append(msg)


def warn(msg):
    warns.append(msg)


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


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(REPO))
    except ValueError:
        return str(p)


def main():
    mkt = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    for entry in mkt["plugins"]:
        name, version = entry["name"], entry.get("version", "")
        src = (REPO / entry["source"]).resolve()
        if not src.exists():
            fail(f"marketplace source missing: {entry['source']} ({name})")
            continue

        # plugin.json
        pj = src / ".claude-plugin" / "plugin.json"
        if not pj.exists():
            fail(f"{name}: missing .claude-plugin/plugin.json")
        else:
            try:
                data = json.loads(pj.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                fail(f"{name}: plugin.json is not valid JSON ({e})")
                data = {}
            if data.get("name") != src.name:
                fail(f"{name}: plugin.json name '{data.get('name')}' != dir '{src.name}'")
            if data.get("name") != name:
                fail(f"{name}: plugin.json name '{data.get('name')}' != marketplace '{name}'")
            if data.get("version") != version:
                fail(f"{name}: plugin.json version '{data.get('version')}' != marketplace '{version}'")

        # skills
        sd = src / "skills"
        if sd.exists():
            for d in sorted(p for p in sd.iterdir() if p.is_dir()):
                sm = d / "SKILL.md"
                if not sm.exists():
                    fail(f"{rel(d)}: directory has no SKILL.md")
                    continue
                fm = parse_frontmatter(sm)
                if not fm:
                    fail(f"{rel(sm)}: no parseable frontmatter")
                    continue
                if fm.get("name") != d.name:
                    fail(f"{rel(sm)}: name '{fm.get('name')}' != dir '{d.name}'")
                if not fm.get("description"):
                    fail(f"{rel(sm)}: missing description")
                if "version" in fm:
                    warn(f"{rel(sm)}: stray version field")

        # commands
        cd = src / "commands"
        if cd.exists():
            for c in sorted(cd.glob("*.md")):
                fm = parse_frontmatter(c)
                if not fm.get("description"):
                    fail(f"{rel(c)}: command missing description")

    # global skills
    gd = REPO / "skills"
    if gd.exists():
        for d in sorted(p for p in gd.iterdir() if p.is_dir()):
            sm = d / "SKILL.md"
            if not sm.exists():
                fail(f"{rel(d)}: directory has no SKILL.md")
                continue
            fm = parse_frontmatter(sm)
            if fm.get("name") != d.name:
                fail(f"{rel(sm)}: name '{fm.get('name')}' != dir '{d.name}'")
            if not fm.get("description"):
                fail(f"{rel(sm)}: missing description")

    for w in warns:
        print(f"  [WARN] {w}")
    for f in fails:
        print(f"  [FAIL] {f}")
    print(f"\nStructure check: {len(fails)} FAIL, {len(warns)} WARN")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
