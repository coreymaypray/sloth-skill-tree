---
name: sloth-update
description: "Sync memory systems with latest state from GitHub repos and local projects. Pulls sloth-memory repo, updates project states, and ensures both local auto-memory and sloth-memory are current. Run this at session start or before beginning new work to ensure you have the latest context. Trigger phrases: \"sloth update\", \"sync memory\", \"pull latest\", \"update memory\", \"refresh state\"."
---

# Sloth Update — Memory Sync & State Refresh

You are the **memory synchronization engine** for the Maycrest Group. Before any work begins, you ensure all memory systems are current and aligned.

## Execution Steps

Run these steps in order every time this command is invoked:

### Step 1: Pull Latest from sloth-memory repo

```bash
cd "C:/Users/Owner/Downloads/Projects/sloth-memory" && git pull origin main 2>&1
```

If the repo doesn't exist or pull fails, note it but continue.

### Step 2: Read Current Memory State

Read these files to understand current state:
1. `C:/Users/Owner/Downloads/Projects/sloth-memory/MEMORY.md` — External memory index
2. `C:/Users/Owner/.claude/projects/C--Users-Owner-Downloads-Projects/memory/MEMORY.md` — Local auto-memory index
3. `C:/Users/Owner/.claude/CLAUDE.md` — Global instructions (current state section)

### Step 3: Scan Active Projects for Changes

For each active project, check git status to detect what's changed since last sync:

```bash
# Maycrest Digital Website
cd "C:/Users/Owner/Downloads/Projects/Maycrest Digital/website-repo" 2>/dev/null && git log --oneline -5 2>/dev/null

# SlothFit
cd "C:/Users/Owner/Downloads/Projects/famfit" 2>/dev/null && git log --oneline -5 2>/dev/null

# Sloth Skill Tree
cd "C:/Users/Owner/Downloads/Projects/sloth-skill-tree" 2>/dev/null && git log --oneline -5 2>/dev/null

# SlothPack (if exists)
cd "C:/Users/Owner/Downloads/Projects/slothpack" 2>/dev/null && git log --oneline -5 2>/dev/null

# TRCA Booking App (if exists)
cd "C:/Users/Owner/Downloads/Projects/trca-booking-app" 2>/dev/null && git log --oneline -5 2>/dev/null
```

### Step 4: Update Memory Files

If any project state has changed since the memory was last written:
1. Update the relevant memory file in `~/.claude/projects/.../memory/`
2. Update the corresponding file in `sloth-memory/projects/`
3. Keep both systems in sync

### Step 5: Push Updates to sloth-memory

If any memory files were updated:

```bash
cd "C:/Users/Owner/Downloads/Projects/sloth-memory" && git add -A && git commit -m "Sloth Update: sync memory $(date +%Y-%m-%d)" && git push origin main 2>&1
```

### Step 6: Display Status Dashboard

```
🦥 SLOTH UPDATE — Memory Sync Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
├── sloth-memory repo: [synced / pull failed / no changes]
├── Local auto-memory: [current / updated N files]
├── Active Projects:
│   ├── Maycrest Digital: [status — last commit, branch]
│   ├── SlothFit: [status — last commit, branch]
│   ├── Sloth Skill Tree: [status — last commit, branch]
│   ├── SlothPack: [status — last commit, branch]
│   └── TRCA: [status — last commit, branch]
├── Memory Changes: [N files updated / no changes]
└── Ready: All systems current
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Rules

1. Always pull before push — never force push sloth-memory
2. If merge conflicts exist in sloth-memory, flag to Corey — don't auto-resolve
3. Only update memory files that actually changed — don't rewrite identical content
4. Include the date in commit messages so history is traceable
5. If a project directory doesn't exist on this machine, skip it silently
6. This command is informational + sync only — it does not start new work
