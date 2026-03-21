---
name: sloth-status
description: "Quick status check — current work, CI state, PR reviews, and blockers"
---

Check the current state of work in progress and report a concise status dashboard.

Run these commands to gather state:
1. `git status --short` — working tree state
2. `gh pr list --state open --limit 5` — open PRs (if in a git repo with GitHub remote)
3. `gh run list --limit 5` — recent CI runs (if in a git repo with GitHub remote)
4. `gh pr view --json reviewDecision,title,number,url` — review status on current branch's PR (if one exists)

Then display a status dashboard:

```
📋 SLOTH STATUS
├── Working tree: [clean / N files modified / N untracked]
├── Open PRs: [count + titles, or "none"]
├── CI: [last run status — passing/failing/running, or "no runs"]
├── Reviews: [approved/changes requested/pending, or "no PR"]
└── Blockers: [list any failures, requested changes, or conflicts — or "none"]
```

If there are actionable items (CI failures, review comments, merge conflicts), suggest the appropriate next step:
- CI failure → "Run `/sloth-dispatch fix CI` to route the fix"
- Review comments → "Run `/sloth-dispatch address reviews` to handle feedback"
- Merge conflict → "Pull latest and resolve conflicts before continuing"
