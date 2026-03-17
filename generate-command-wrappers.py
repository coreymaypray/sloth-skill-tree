#!/usr/bin/env python3
"""Generate ~/.claude/commands/ wrapper files for all Cyber Sloth skills and commands."""

import os
import re
from pathlib import Path

PLUGINS_DIR = Path(os.path.expanduser("~/.claude/plugins/cache/sloth-skill-tree"))
OUTPUT_DIR = Path(os.path.expanduser("~/.claude/commands"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Track names to handle collisions (e.g., division-lead exists in all 12 divisions)
used_names = {}


def extract_frontmatter(filepath):
    """Extract frontmatter fields from a markdown file using regex."""
    with open(filepath, "r") as f:
        content = f.read()
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    fm_text = match.group(1)
    result = {}
    for line in fm_text.split("\n"):
        m = re.match(r'^(\w+):\s*(.+)$', line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip().strip('"').strip("'")
            result[key] = val
    return result


def get_description(frontmatter):
    """Get description from frontmatter, truncate to 120 chars."""
    desc = frontmatter.get("description", "")
    if isinstance(desc, str):
        desc = desc.strip().strip('"').strip("'")
        if len(desc) > 120:
            desc = desc[:117] + "..."
        return desc
    return ""


def make_wrapper(filename, skill_ref, description):
    """Create a wrapper command file."""
    filepath = OUTPUT_DIR / filename
    content = f"""---
description: "{description}"
---

Invoke the skill `{skill_ref}` and follow its instructions exactly.
"""
    filepath.write_text(content)
    print(f"  Created: {filename} -> {skill_ref}")


def resolve_name(base_name, plugin_name, division):
    """Resolve naming collisions by appending division suffix."""
    if base_name in used_names and used_names[base_name] != plugin_name:
        # Collision - use division-specific name
        return f"cyber-sloth-{division}-{base_name}"
    used_names[base_name] = plugin_name
    return f"cyber-sloth-{base_name}"


# First pass: identify collisions
name_counts = {}
for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
    if not plugin_dir.is_dir():
        continue
    # Find the version directory
    version_dirs = [d for d in plugin_dir.iterdir() if d.is_dir()]
    if not version_dirs:
        continue
    version_dir = version_dirs[0]

    skills_dir = version_dir / "skills"
    if skills_dir.exists():
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                name = skill_dir.name
                name_counts[name] = name_counts.get(name, 0) + 1

collision_names = {name for name, count in name_counts.items() if count > 1}
print(f"Collision names (appear in multiple divisions): {collision_names}")

# Second pass: generate wrappers
total = 0
for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
    if not plugin_dir.is_dir():
        continue
    plugin_name = plugin_dir.name
    # Extract division name (e.g., "design" from "cyber-sloth-design")
    division = plugin_name.replace("cyber-sloth-", "")

    version_dirs = [d for d in plugin_dir.iterdir() if d.is_dir()]
    if not version_dirs:
        continue
    version_dir = version_dirs[0]

    print(f"\n[{plugin_name}]")

    # Process skills/
    skills_dir = version_dir / "skills"
    if skills_dir.exists():
        for skill_dir in sorted(skills_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            fm = extract_frontmatter(skill_md)
            skill_name = skill_dir.name
            desc = get_description(fm)
            skill_ref = f"{plugin_name}:{skill_name}"

            if skill_name in collision_names:
                filename = f"cyber-sloth-{division}-{skill_name}.md"
            else:
                filename = f"cyber-sloth-{skill_name}.md"

            make_wrapper(filename, skill_ref, desc)
            total += 1

    # Process commands/
    commands_dir = version_dir / "commands"
    if commands_dir.exists():
        for cmd_file in sorted(commands_dir.iterdir()):
            if not cmd_file.suffix == ".md":
                continue
            fm = extract_frontmatter(cmd_file)
            cmd_name = cmd_file.stem
            desc = get_description(fm)
            skill_ref = f"{plugin_name}:{cmd_name}"

            # For division dispatcher commands (design, engineering, etc.),
            # add "-dispatch" suffix to avoid collision with division skill names
            if cmd_name in [
                "design", "engineering", "gamedev", "marketing",
                "paid-media", "product", "project-mgmt", "spatial",
                "specialized", "support", "testing"
            ]:
                filename = f"cyber-sloth-{cmd_name}-dispatch.md"
            elif cmd_name == "ceo":
                filename = "cyber-sloth-ceo.md"
            else:
                filename = f"cyber-sloth-{cmd_name}.md"

            make_wrapper(filename, skill_ref, desc)
            total += 1

# Special: sloth-command gets its own top-level name too
make_wrapper(
    "sloth-command.md",
    "cyber-sloth-suite:sloth-command",
    "The CEO of the Cyber Sloth Empire. Describe any task and the CEO dispatches to the right specialists."
)
total += 1

print(f"\n✅ Generated {total} command wrappers in {OUTPUT_DIR}")
