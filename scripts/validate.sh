#!/usr/bin/env bash
# Single validation entrypoint for the Sloth Skill Tree.
# Runs the description linter, structural checks, and count-staleness check.
# Exits non-zero if any step fails. Run before pushing or opening a PR.
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

PY="${PYTHON:-python}"
status=0

echo "==> Description lint (normalize-frontmatter.py)"
"$PY" normalize-frontmatter.py || status=1

echo
echo "==> Structure check (scripts/check-structure.py)"
"$PY" scripts/check-structure.py || status=1

echo
echo "==> Count staleness (scripts/generate-counts.py --check)"
"$PY" scripts/generate-counts.py --check || status=1

echo
if [ "$status" -eq 0 ]; then
  echo "✅ validate: all checks passed"
else
  echo "❌ validate: one or more checks failed"
fi
exit "$status"
