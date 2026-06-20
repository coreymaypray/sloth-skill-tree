---
name: discipline
description: "Sloth Discipline — fast routing to a single Maycrest process discipline (spec, plan, TDD, debug, build, review, verify, ship) without the full delivery pipeline. Usage: /discipline [what you need]"
argument-hint: "[discipline or situation, e.g. 'debug this failing test']"
---

# Sloth Discipline — Fast Lane 🦥

You have one disciplined task, not a full client build. Route it and go.

| Signal | Route to |
|--------|----------|
| "spec this", "scope it", "what should we build", client intake | `maycrest-method:sloth-spec` |
| "write the plan", "break this down", "implementation plan" | `maycrest-method:sloth-blueprint` |
| "implement", "write the code", "build the feature" (plan in hand) | `maycrest-method:sloth-build` |
| "write a test", "TDD", "before I code this" | `maycrest-method:sloth-tdd` |
| "this is broken", "failing test", "bug", "unexpected behavior" | `maycrest-method:sloth-debug` |
| "is this actually done", "verify", "before I claim it passes" | `maycrest-method:sloth-verify` |
| "review this", "request code review" | `maycrest-method:sloth-review` |
| "got review feedback", "respond to the reviewer" | `maycrest-method:sloth-receive-review` |
| "isolate", "worktree", "new branch for this client" | `maycrest-method:sloth-worktree` |
| "merge", "ship it", "open the PR", "finish the branch" | `maycrest-method:sloth-ship` |

A full client deliverable from a fuzzy ask? Escalate to `/deliver`. 🦥
