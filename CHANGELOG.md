# Changelog

All notable changes to the Sloth Skill Tree. Format follows
[Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- **`maycrest-method` plugin** — the Sloth Flow discipline engine: 10 process skills
  (`sloth-spec`, `sloth-blueprint`, `sloth-tdd`, `sloth-debug`, `sloth-build`,
  `sloth-review`, `sloth-receive-review`, `sloth-verify`, `sloth-worktree`,
  `sloth-ship`) forked and rebranded from the MIT-licensed obra/superpowers, plus the
  `/deliver` gated pipeline and `/discipline` fast router. Works standalone.
- Per-plugin `.claude-plugin/plugin.json` manifests and `README.md` catalogs (skill
  tables auto-generated).
- Validation tooling: `scripts/validate.sh`, `scripts/generate-counts.py` (single source
  of truth for counts), `scripts/check-structure.py`; lint mode added to
  `normalize-frontmatter.py`.
- `CONTRIBUTING.md`, `LICENSE` (proprietary), `NOTICE` (MIT attribution), CI workflow.

### Changed
- Rewrote all 117 skill descriptions to the third-person "Use when…" pattern (were
  first-person feature summaries + quoted-keyword dumps). 318 lint failures → 0.
- Reconciled all skill counts to a single generated source (was 113/34/37/22 across
  conflicting locations; real total is 124 specialist + 3 global = 127).
- Removed brittle hardcoded counts from `marketplace.json` plugin descriptions.

### Fixed
- `normalize-frontmatter.py` hardcoded macOS path, skill glob that skipped the 3 global
  skills, and command glob that skipped non-command plugins.
- 5 skill `name` fields that did not match their directory (`division-lead` ×3,
  `Data Analytics Reporter`, `Legal Compliance`); stripped stray `version:` fields.

## [v3.1.0] — 2026-03-21
- Upgraded Sloth Command with agent-orchestrator patterns (task classification, parallel
  execution, CI/PR reactions, lineage context).
- Added `/sloth-status` command; added `orchestration-patterns.md` reference.
- Upgraded Sloth Dispatch with reactive event routing.

## [v1.2.0] — 2026-03-28
- Skill audit & deduplication; removed 3 duplicate user skills from `~/.claude/skills/`.
- Migrated 8 unique skills from legacy anthropic-skills into the plugin system
  (docx, xlsx, pptx, pdf, theme-factory, canvas-design, web-artifacts-builder, deep-research).

## [v1.1.0] — 2026-03-21
- Consolidated all skill sources into sloth-skill-tree (from cyber-sloth-empire +
  anthropic-skills); migrated 7 skills.
- Added google-flow, chevelle-restoration, davinci-resolve-mcp.
- Full rebrand: "Cyber Sloth Empire" → "Maycrest Group" across 87+ files; renamed
  chief-of-staff to sloth-dispatch.
