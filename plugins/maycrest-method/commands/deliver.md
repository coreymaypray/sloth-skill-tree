---
name: deliver
description: "Sloth Flow Delivery — the full Maycrest client-build pipeline: spec → blueprint → build → review → verify → ship, with a discipline gate at every handoff. Usage: /deliver [client] [what you're building]"
argument-hint: "[client name] [deliverable description]"
---

# Sloth Flow Delivery Pipeline 🦥

You are running the Maycrest Group's discipline-enforced delivery machine. A fuzzy
client ask goes in; a shipped-and-verified deliverable comes out. Every stage has a
GATE — you do not advance past a gate without meeting it. Speed comes from doing it
right once, not from skipping steps.

**Standing rule:** this pipeline references ONLY `maycrest-method:sloth-*` skills. Do
not silently fall back to generic disciplines.

## Stage 0 — Isolate the workspace
Invoke `maycrest-method:sloth-worktree`. One client engagement = one isolated branch.
**GATE:** clean test baseline (or Corey explicitly accepts a dirty baseline).

## Stage 1 — Spec the deliverable
Invoke `maycrest-method:sloth-spec`. Client intake: one question at a time, 2–3
approaches with a recommendation, then an approved written spec.
**GATE (HARD):** no build action until the spec is approved. No exceptions, no "this
one's simple."

## Stage 2 — Blueprint the work
Invoke `maycrest-method:sloth-blueprint`. Turn the approved spec into a bite-sized,
TDD-structured plan with exact file paths and complete code per step.
**GATE:** the plan covers every spec requirement (run its self-review).

## Stage 3 — Build it
Invoke `maycrest-method:sloth-build`. Fresh subagent per task; subagents follow
`maycrest-method:sloth-tdd`. After EACH task: two-stage review — spec compliance via
`maycrest-method:sloth-review`, then code quality. A reported bug routes to
`maycrest-method:sloth-debug` (root cause before fix).
**GATE:** every task green and every review resolved before the next task starts.

## Stage 4 — Verify against reality
Invoke `maycrest-method:sloth-verify` for evidence-based completion, then hand the
build to `maycrest-ops:reality-checker` for the production-readiness verdict.
**GATE:** fresh verification output exists. No "should pass." reality-checker defaults
to NEEDS WORK — clear it before shipping.

## Stage 5 — Ship / handoff
Invoke `maycrest-method:sloth-ship`. Verify tests, then present the merge / PR / keep /
discard menu and produce the client handoff package.
**GATE:** tests pass on the final result before any merge or PR.

## Output — Client Delivery Record
- Approved spec (path)
- Blueprint (path)
- Build log: tasks completed, reviews passed
- Verification evidence: commands run + output
- Ship decision + handoff notes

Maycrest delivers verified deliverables, not vibes. Move. 🦥
