# Maycrest Method 🦥 — The Sloth Flow Discipline Engine

> Process discipline + agency delivery, forked from the MIT-licensed obra/superpowers.

The home for Maycrest's process discipline. Standalone — no superpowers install needed.
MIT-derived, Maycrest-voiced.

<!-- AUTOGEN:counts:start -->
**10 skills · 2 commands**
<!-- AUTOGEN:counts:end -->

## The two commands

- `/deliver [client] [deliverable]` — the full gated client-build pipeline:
  worktree → spec (HARD-GATE) → blueprint → build (TDD + two-stage review) →
  verify (+ `maycrest-ops:reality-checker`) → ship (test-gate).
- `/discipline [need]` — fast route to a single discipline without the full pipeline.

## Skills

<!-- AUTOGEN:skills:start -->
| Skill | Triggers |
|-------|----------|
| `sloth-blueprint` | Use when an approved Maycrest spec needs turning into a bite-sized TDD implementation plan a contractor could execute cold — before any code is touched on a client build. |
| `sloth-build` | Use when the Maycrest deliver pipeline executes an implementation plan of independent tasks in the current session — one fresh subagent per task, two-stage review each. |
| `sloth-debug` | Use when a Maycrest build hits any bug, test failure, or unexpected behavior on the Expo/Supabase/Vercel stack — before proposing any fix. |
| `sloth-receive-review` | Use when review feedback lands on a Maycrest deliverable — before implementing any suggestion, especially an unclear or questionable one — demanding verification over performative agreement. |
| `sloth-review` | Use when completing a task or major feature on a Maycrest build, or before merging — dispatch an independent reviewer subagent as the internal QA gate before the client sees the work. |
| `sloth-ship` | Use when a Maycrest engagement branch is complete and tests pass — gating the handoff: verify the suite first, then choose merge, PR, keep, or discard, and produce a short client handoff package. |
| `sloth-spec` | Use when a Maycrest client request needs scoping before any build starts — turns a fuzzy ask into an approved written spec through collaborative dialogue, before code or scaffolding. |
| `sloth-tdd` | Use when building any Maycrest client deliverable, feature, or bug fix — before writing implementation code. |
| `sloth-verify` | Use when about to claim a Maycrest deliverable is complete, fixed, or passing — before committing, opening a PR, or telling the client, requiring fresh verification evidence first. |
| `sloth-worktree` | Use when starting client engagement work that needs isolation — an isolated workspace per engagement so one client's branch never bleeds into another's, via native tools or a git worktree fallback. |

**Commands:** `/deliver`, `/discipline`
<!-- AUTOGEN:skills:end -->

## Differentiation from superpowers

The `sloth-*` skills exist alongside `superpowers:*` deliberately: distinct names,
agency-framed triggers, no collision. Use `sloth-*` for Maycrest client builds;
`superpowers:*` for generic solo dev.

## Install just this plugin

```bash
claude plugin marketplace add coreymaypray/sloth-skill-tree
claude plugin install maycrest-method@sloth-skill-tree
```

## Attribution

Adapted from the MIT-licensed [obra/superpowers](https://github.com/obra/superpowers)
project (© 2025 Jesse Vincent). See [NOTICE](NOTICE).

Part of the [Sloth Skill Tree](../../README.md).
