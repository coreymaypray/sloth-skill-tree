#!/usr/bin/env python3
"""Normalize SKILL.md frontmatter to match Claude Code autocomplete expectations.

For each SKILL.md:
- Set name to kebab-case matching parent directory
- Remove version field
- Collapse multi-line descriptions to single-line
"""

import os
import re
import sys
from pathlib import Path


def normalize_skill(filepath: Path):
    """Normalize a single SKILL.md file."""
    # Derive expected name from parent directory
    expected_name = filepath.parent.name

    content = filepath.read_text()

    # Split into frontmatter and body
    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"  SKIP (no frontmatter): {filepath}")
        return False

    frontmatter = parts[1]
    body = parts[2]

    # Parse frontmatter lines
    lines = frontmatter.strip().split("\n")
    new_lines = []
    description_value = ""
    in_multiline_desc = False

    for line in lines:
        # Skip version lines
        if line.startswith("version:"):
            continue

        # Handle name - replace with directory name
        if line.startswith("name:"):
            new_lines.append(f"name: {expected_name}")
            continue

        # Handle description
        if line.startswith("description:"):
            rest = line[len("description:"):].strip()
            if rest == ">" or rest == "|":
                # Multi-line description starts
                in_multiline_desc = True
                description_value = ""
                continue
            elif rest.startswith('"') or rest.startswith("'"):
                # Already quoted single-line
                new_lines.append(line)
                continue
            else:
                # Unquoted single-line
                new_lines.append(f'description: "{rest}"')
                continue

        # Collect multi-line description content
        if in_multiline_desc:
            stripped = line.strip()
            if stripped and not line.startswith(" ") and not line.startswith("\t") and ":" in line:
                # This is a new field, not part of description
                in_multiline_desc = False
                # Emit the collected description
                desc = " ".join(description_value.split())
                # Escape internal quotes
                desc = desc.replace('"', '\\"')
                new_lines.append(f'description: "{desc}"')
                # Process this line as a regular field
                if line.startswith("version:"):
                    continue  # skip version
                new_lines.append(line)
            else:
                description_value += " " + stripped
            continue

        new_lines.append(line)

    # If we ended while still in multiline description
    if in_multiline_desc:
        desc = " ".join(description_value.split())
        desc = desc.replace('"', '\\"')
        new_lines.append(f'description: "{desc}"')

    new_frontmatter = "\n".join(new_lines)
    new_content = f"---\n{new_frontmatter}\n---{body}"

    filepath.write_text(new_content)
    return True


def normalize_command(filepath: Path):
    """Normalize a command .md file."""
    expected_name = filepath.stem  # filename without .md

    content = filepath.read_text()
    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"  SKIP (no frontmatter): {filepath}")
        return False

    frontmatter = parts[1]
    body = parts[2]

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
            if rest == ">" or rest == "|":
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
            if stripped and not line.startswith(" ") and not line.startswith("\t") and ":" in line:
                in_multiline_desc = False
                desc = " ".join(description_value.split())
                desc = desc.replace('"', '\\"')
                new_lines.append(f'description: "{desc}"')
                if line.startswith("version:"):
                    continue
                new_lines.append(line)
            else:
                description_value += " " + stripped
            continue

        new_lines.append(line)

    if in_multiline_desc:
        desc = " ".join(description_value.split())
        desc = desc.replace('"', '\\"')
        new_lines.append(f'description: "{desc}"')

    if not has_name:
        new_lines.insert(0, f"name: {expected_name}")

    new_frontmatter = "\n".join(new_lines)
    new_content = f"---\n{new_frontmatter}\n---{body}"

    filepath.write_text(new_content)
    return True


def main():
    repo = Path("/Users/coreymaypray/Desktop/Projects/sloth-skill-tree")

    # Process skills
    skills = sorted(repo.glob("plugins/*/skills/*/SKILL.md"))
    print(f"Found {len(skills)} SKILL.md files\n")

    changed = 0
    for skill in skills:
        rel = skill.relative_to(repo)
        result = normalize_skill(skill)
        if result:
            print(f"  OK: {rel}")
            changed += 1

    print(f"\nNormalized {changed} skills\n")

    # Process commands
    commands = sorted(repo.glob("plugins/cyber-sloth-suite/commands/*.md"))
    print(f"Found {len(commands)} command files\n")

    cmd_changed = 0
    for cmd in commands:
        rel = cmd.relative_to(repo)
        result = normalize_command(cmd)
        if result:
            print(f"  OK: {rel}")
            cmd_changed += 1

    print(f"\nNormalized {cmd_changed} commands")


if __name__ == "__main__":
    main()
