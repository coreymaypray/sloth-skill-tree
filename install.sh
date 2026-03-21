#!/bin/bash
# Maycrest Group — Claude Code Skills Installer
# Symlinks plugins and skills into your ~/.claude directory

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
PLUGINS_DIR="$CLAUDE_DIR/plugins/local"
SKILLS_DIR="$CLAUDE_DIR/skills"

echo "🦥 === Sloth Skill Tree Installer ==="
echo ""

# Ensure directories exist
mkdir -p "$PLUGINS_DIR"
mkdir -p "$SKILLS_DIR"

# Install plugin divisions
echo "Installing plugins..."
for plugin_dir in "$SCRIPT_DIR"/plugins/*/; do
  plugin_name=$(basename "$plugin_dir")
  target="$PLUGINS_DIR/$plugin_name"

  if [ -L "$target" ]; then
    echo "  Updating symlink: $plugin_name"
    rm "$target"
  elif [ -d "$target" ]; then
    echo "  WARNING: $plugin_name already exists as a directory. Skipping."
    echo "  Remove it manually if you want to use the repo version: rm -rf $target"
    continue
  else
    echo "  Installing: $plugin_name"
  fi

  ln -s "$plugin_dir" "$target"
done

# Install global skills
echo ""
echo "Installing global skills..."
for skill_dir in "$SCRIPT_DIR"/skills/*/; do
  skill_name=$(basename "$skill_dir")
  target="$SKILLS_DIR/$skill_name"

  if [ -L "$target" ]; then
    echo "  Updating symlink: $skill_name"
    rm "$target"
  elif [ -d "$target" ]; then
    echo "  WARNING: $skill_name already exists as a directory. Skipping."
    echo "  Remove it manually if you want to use the repo version: rm -rf $target"
    continue
  else
    echo "  Installing: $skill_name"
  fi

  ln -s "$skill_dir" "$target"
done

echo ""
echo "=== Installation complete ==="
echo ""
echo "Next steps:"
echo "  1. Enable plugins in ~/.claude/settings.json"
echo "  2. Restart Claude Code"
echo ""
echo "To enable all plugins, add this to settings.json under enabledPlugins:"
echo '  "maycrest-command@sloth-skill-tree": true'
echo '  "maycrest-create@sloth-skill-tree": true'
echo "  ... (see README.md for full list)"
