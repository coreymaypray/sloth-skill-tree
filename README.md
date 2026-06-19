# Maycrest Group — Sloth Skill Tree 🦥

The official Claude Code plugin library for **Maycrest Group LLC** — powered by **Sloth Flow**.

<!-- AUTOGEN:counts:start -->
![Plugins](https://img.shields.io/badge/plugins-6-00E5CC?style=flat-square) ![Skills](https://img.shields.io/badge/skills-127-A855F7?style=flat-square) ![Commands](https://img.shields.io/badge/commands-43-22C55E?style=flat-square) ![License](https://img.shields.io/badge/license-Proprietary-FF4D6A?style=flat-square)

**6 plugins · 127 skills (124 specialist + 3 global) · 43 commands**

| Plugin | Version | Skills | Commands |
|--------|--------:|-------:|---------:|
| [`maycrest-command`](plugins/maycrest-command/README.md) | 3.1.0 | 2 | 4 |
| [`maycrest-create`](plugins/maycrest-create/README.md) | 1.2.0 | 37 | 10 |
| [`maycrest-automate`](plugins/maycrest-automate/README.md) | 1.2.0 | 39 | 14 |
| [`maycrest-secure`](plugins/maycrest-secure/README.md) | 1.1.0 | 10 | 6 |
| [`maycrest-ops`](plugins/maycrest-ops/README.md) | 1.2.0 | 26 | 7 |
| [`maycrest-method`](plugins/maycrest-method/README.md) | 1.0.0 | 10 | 2 |
| _global skills_ | — | 3 | — |
<!-- AUTOGEN:counts:end -->

Organized under the Maycrest pillars — **Create · Automate · Secure**, with **Ops**,
**Command** (orchestration), and **Method** (the Sloth Flow discipline engine).

## Start here

| I want to… | Run |
|------------|-----|
| Decompose a big, multi-pillar goal | `/sloth [describe your goal]` |
| Route one task to the right specialist | `/sloth-dispatch [describe your task]` |
| Run a full client build with discipline gates | `/deliver [client] [deliverable]` |
| Apply one discipline (TDD, debug, review…) | `/discipline [what you need]` |
| Hit a specialist directly | `maycrest-[pillar]:[skill]` |

## The plugins

Each plugin installs and reads standalone — click through for its full skill catalog.

| Plugin | What's inside |
|--------|---------------|
| [maycrest-command](plugins/maycrest-command/README.md) | Sloth Command orchestrator + Sloth Dispatch fast router |
| [maycrest-create](plugins/maycrest-create/README.md) | Design, brand, marketing, content, paid media, AI video |
| [maycrest-automate](plugins/maycrest-automate/README.md) | Engineering, AI, DevOps, spatial, gamedev, product |
| [maycrest-secure](plugins/maycrest-secure/README.md) | Security engineering, threat intel, IR, forensics, compliance |
| [maycrest-ops](plugins/maycrest-ops/README.md) | PM, QA, support, finance, analytics, document tooling |
| [maycrest-method](plugins/maycrest-method/README.md) | Sloth Flow discipline engine + `/deliver` pipeline |

Plus 3 global skills (`resume-career-coach`, `chevelle-restoration`, `davinci-resolve-mcp`).

<details>
<summary><b>Example invocations by pillar</b></summary>

```text
# Create
maycrest-create:seo-specialist     → "Audit organic search for maycrestdigital.com"
/launch-campaign                   → plan a multi-channel launch

# Automate
maycrest-automate:backend-architect → "Design the Supabase schema for a booking app"
/full-stack-build                   → scope and build an Expo + Supabase MVP

# Secure
maycrest-secure:threat-model        → "Threat model the client portal login flow"
/security-audit                     → run a posture assessment

# Ops
maycrest-ops:exec-summary           → "Board-ready summary of the Q2 engagement"
maycrest-ops:reality-checker        → certify a build production-ready

# Method (discipline engine)
/deliver "AOS Sober Living" "bed-availability booking flow"
/discipline "debug this failing RLS test"
```
</details>

## Installation

**Prerequisites:** [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code), Node.js 18+, Git.

```bash
# 1. Clone
git clone https://github.com/coreymaypray/sloth-skill-tree.git

# 2. Register the marketplace
claude plugin marketplace add /path/to/sloth-skill-tree

# 3. Install all plugins
for p in maycrest-command maycrest-create maycrest-automate maycrest-secure maycrest-ops maycrest-method; do
  claude plugin install "$p@sloth-skill-tree" --scope user
done

# 4. Install global skills
mkdir -p ~/.claude/skills && cp -R skills/* ~/.claude/skills/

# 5. Restart Claude Code; type / to see commands, /plugins to verify.
```

**Update:** `cd sloth-skill-tree && git pull origin main`, then restart. No reinstall needed.

## Repository layout

```
.claude-plugin/marketplace.json   Marketplace manifest (source of truth for plugins)
plugins/<plugin>/
  .claude-plugin/plugin.json       Per-plugin manifest
  README.md                        Per-plugin catalog (skills table auto-generated)
  skills/<name>/SKILL.md           Skills
  commands/<name>.md               Commands
skills/<name>/SKILL.md             Global (pillar-less) skills
scripts/                           validate.sh, generate-counts.py, check-structure.py
normalize-frontmatter.py           Description linter (--fix for mechanical normalization)
```

## Contributing & validation

Run `./scripts/validate.sh` before pushing — it lints descriptions, checks structure,
and verifies counts are current. See [CONTRIBUTING.md](CONTRIBUTING.md) for the SKILL.md
template and the description rule.

## Tech stack

Optimized for Expo (React Native) · Supabase · Stripe · Vercel · Claude (Anthropic SDK),
though most skills are framework-agnostic.

## License

Proprietary — © 2026 Maycrest Group LLC. See [LICENSE](LICENSE). The `maycrest-method`
plugin contains content adapted from the MIT-licensed
[obra/superpowers](https://github.com/obra/superpowers); see [NOTICE](plugins/maycrest-method/NOTICE).

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

**Maycrest Group LLC** · Indianapolis, IN · Create · Automate · Secure 🦥
