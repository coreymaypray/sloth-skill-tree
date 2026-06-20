# Contributing to the Sloth Skill Tree

This is a proprietary Maycrest Group repository. These conventions keep it consistent
and discoverable. Run `./scripts/validate.sh` before every push — it is the gate.

## Skills are nouns, commands are verbs

- A **skill** (`plugins/<plugin>/skills/<name>/SKILL.md`) is a reusable specialist or
  technique. Its `name` must equal its directory name (kebab-case).
- A **command** (`plugins/<plugin>/commands/<name>.md`) is a slash-invoked workflow that
  chains skills.

## The description rule (enforced by the linter)

A skill `description` describes **only *when* to use the skill** — never what it does or
its workflow. A description that summarizes the workflow trains the model to route on the
summary and skip the skill body.

- Third person, **starts with `Use when`**.
- Triggering conditions/contexts only — no feature tour, no workflow summary.
- No quoted-keyword dumps (≤ 3 quoted phrases; prefer none). Put long trigger lists in a
  body `## When to use this skill` section, not the frontmatter.
- ≤ 200 characters (hard fail at 240).

Commands are slash-invoked, so they use a relaxed profile (no `Use when` required).

### Good / bad examples

```yaml
# ❌ first-person feature dump + quoted keywords
description: "PostgreSQL/Supabase database design, schema setup, RLS... Trigger for
  \"design the database\", \"set up schema\", \"create tables\"..."

# ✅ third-person "Use when", triggers only
description: "Use when designing or reviewing a Postgres/Supabase schema, writing RLS
  policies, planning migrations or indexes, choosing a plan, or diagnosing slow queries."
```

More exemplars: `image-prompt-engineer`, `threat-intel-analyst`, `create-lead`, `docx`.

## SKILL.md template

```markdown
---
name: my-skill          # must equal the directory name; no version field
description: "Use when <triggering conditions>."
---

# My Skill

## Overview
Core principle in 1–2 sentences.

## When to use this skill
Symptoms / situations (and when NOT to use it).

## <Process, rules, examples, output format as needed>
```

Keep skills tight — aim under ~160 lines. Move heavy reference material into a
`references/` subdirectory.

## Adding or changing a skill

1. Create/edit the SKILL.md following the template.
2. `python normalize-frontmatter.py --fix` (mechanical: name=dir, strip version, quote).
3. `python scripts/generate-counts.py` (refresh README counts + tables).
4. `./scripts/validate.sh` — must pass (lint + structure + counts).
5. If you add a plugin, add it to `.claude-plugin/marketplace.json` and give it a
   `.claude-plugin/plugin.json` whose `name`/`version` match.

## MIT-derived content

The `maycrest-method` plugin adapts obra/superpowers (MIT). Keep the per-skill attribution
footer and `plugins/maycrest-method/NOTICE` intact on any change there.
