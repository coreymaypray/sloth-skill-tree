# Orchestration Patterns — Sloth Command Reference

Patterns adapted from [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) for Claude Code plugin orchestration.

---

## 1. Task Classification Decision Tree

```
User request arrives
  │
  ├── Maps to exactly 1 specialist?
  │   └── YES → ATOMIC → Route via /sloth-dispatch
  │
  ├── Multiple specialists, all in same pillar?
  │   └── YES → Check dependencies
  │       ├── Sequential (each needs previous output) → COMPOSITE-SEQUENTIAL
  │       └── Independent (can run in any order) → COMPOSITE-PARALLEL
  │
  ├── Spans multiple pillars?
  │   └── YES → COMPOSITE → Full Sloth Command planning
  │
  └── Intent unclear?
      └── YES → AMBIGUOUS → Ask clarifying questions
```

---

## 2. Decomposition Examples

### Atomic (skip planning)
- "Write a Sigma rule for lateral movement" → `maycrest-secure:threat-detection-engineer`
- "Optimize this SQL query" → `maycrest-automate:backend-architect`
- "Design a carousel for LinkedIn" → `maycrest-create:carousel-engine`

### Composite-Sequential (phased execution)
```
"Build a booking API with auth"
  Phase 1: maycrest-automate:backend-architect → schema + API design
  Phase 2: maycrest-automate:backend-database → Supabase setup + RLS
  Phase 3: maycrest-automate:security-engineer → auth + security review
```

### Composite-Parallel (concurrent tracks)
```
"Launch a marketing campaign for TIE Platform"
  Track A (parallel): maycrest-create:content-creator → blog articles
  Track B (parallel): maycrest-create:social-strategist → social calendar
  Track C (parallel): maycrest-create:creative-strategist → ad creative
  Gate (after A+B+C): maycrest-create:brand-guardian → consistency review
```

### Mixed (parallel + sequential)
```
"Build and launch a new client app"
  Track A (sequential):
    maycrest-automate:backend-architect → architecture
    maycrest-automate:frontend-developer → implementation
  Track B (parallel with A):
    maycrest-create:ui-designer → design system
    maycrest-create:content-creator → marketing copy
  Track C (after A+B):
    maycrest-ops:reality-checker → QA
    maycrest-secure:security-engineer → security audit
    maycrest-automate:devops-automator → deployment
```

---

## 3. Parallel Execution with Agent Tool

When tracks are independent, use the Agent tool to run them concurrently:

```
# In a single message, launch multiple Agent calls:

Agent 1 (Track A): "You are maycrest-create:content-creator.
  Mission: Launch campaign for TIE Platform.
  Your role: Write 3 blog article drafts.
  Siblings: social-strategist is building the social calendar. creative-strategist is making ad creative.
  Dependencies: None — you can start immediately."

Agent 2 (Track B): "You are maycrest-create:social-strategist.
  Mission: Launch campaign for TIE Platform.
  Your role: Build a 4-week social content calendar.
  Siblings: content-creator is writing blog articles. creative-strategist is making ad creative.
  Dependencies: None — you can start immediately."
```

### Rules for Parallel Spawning
- **Max 3 concurrent agents** — more causes context thrashing
- **Each agent must be self-contained** — no shared mutable state
- **Collect all results before proceeding** — don't start dependent work until all parallel tracks complete
- **Pass lineage context** — each agent needs to know the overall mission and what siblings are doing

---

## 4. Lineage Context Template

When delegating to a specialist (especially in parallel), include this context:

```markdown
## Lineage Context
- **Mission**: [The overall goal from the execution brief]
- **Your role**: [What this specialist is expected to deliver]
- **Siblings**: [Other specialists running in parallel and what they're producing]
- **Upstream**: [What work has already been completed that you can build on]
- **Downstream**: [What work depends on your output]
- **Constraints**: [Timeline, tech stack, brand guidelines, etc.]
```

This prevents:
- Duplicate work (two specialists solving the same problem)
- Contradictory outputs (design says X, content says Y)
- Wasted effort (building something that doesn't fit the bigger picture)

---

## 5. Reaction Protocol Reference

### CI Failure Response

```
1. Detect: gh run list --limit 3 --status failure
2. Fetch logs: gh run view {run-id} --log-failed
3. Identify: Which specialist's code failed? (check recent commits)
4. Route: Send failure context + logs to that specialist
5. Instruction: "CI failed on your PR. Here are the errors: [logs]. Fix the failing tests/lint/build and push."
6. Track: If this is the 2nd+ failure, escalate to user
```

### Review Comment Response

```
1. Detect: gh pr view {pr-number} --comments
2. Parse: Extract actionable review feedback
3. Identify: Which specialist owns the reviewed code?
4. Route: Send review comments to that specialist
5. Instruction: "Reviewer requested changes: [comments]. Address each point, push fixes, and reply to the review."
6. Track: If review is blocking and specialist can't resolve, escalate
```

### Merge Conflict Response

```
1. Detect: git pull/merge/rebase fails with conflict markers
2. Identify: Which files conflict? Which specialist last touched them?
3. Route: Send conflict context to the specialist
4. Instruction: "Merge conflict detected. Conflicting files: [files]. Pull latest from main, resolve conflicts preserving both changes where possible, and push."
5. Escalate: If conflict involves shared code or architectural decisions, escalate to user
```

---

## 6. Escalation Decision Matrix

| Situation | Auto-Handle? | Max Retries | Then What? |
|-----------|-------------|-------------|------------|
| CI lint/format failure | Yes | 2 | Escalate to user |
| CI test failure | Yes | 2 | Escalate to user |
| CI build failure | Yes | 1 | Escalate — likely architectural |
| Simple review comment (typo, naming) | Yes | 1 | Escalate if reviewer insists |
| Architectural review comment | No | 0 | Escalate immediately — needs judgment |
| Merge conflict (single file) | Yes | 1 | Escalate if resolution unclear |
| Merge conflict (multi-file) | No | 0 | Escalate — too risky for auto-resolve |
| Specialist can't complete task | No | 0 | Propose alternative, escalate |
| Scope creep discovered | No | 0 | Update brief, get user buy-in |

---

## 7. Session Status Check Protocol

Quick health check for in-progress work:

```bash
# 1. Working tree state
git status --short

# 2. Open PRs
gh pr list --state open

# 3. Recent CI runs
gh run list --limit 5

# 4. PR review status (if PR exists)
gh pr view --json reviewDecision,reviews

# 5. Uncommitted changes
git diff --stat
```

Report format:
```
📋 SLOTH STATUS
├── Working tree: [clean / N files modified]
├── Open PRs: [count + titles]
├── CI: [passing / failing / running]
├── Reviews: [approved / changes requested / pending]
└── Blockers: [none / list]
```
