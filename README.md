# Cyber Sloth Empire — Claude Code Skills Library

A portable collection of 120+ Claude Code skills, commands, and plugins built by [Corey Maypray](https://github.com/coreymaypray) for the **Cyber Sloth Empire** / **Maycrest** ecosystem.

## What's Inside

| Division | Skills | Focus |
|----------|--------|-------|
| **cyber-sloth-suite** | 9 skills, 23 commands | Core orchestrator — content, security, client delivery |
| **cyber-sloth-engineering** | 13 skills | Security, backend, frontend, DevOps, AI, mobile |
| **cyber-sloth-design** | 8 skills | UX/UI, brand, visual storytelling, inclusive design |
| **cyber-sloth-marketing** | 11 skills | SEO, social, TikTok, YouTube, Reddit, growth |
| **cyber-sloth-specialized** | 9 skills | Compliance, analytics, developer advocacy, AI agents |
| **cyber-sloth-gamedev** | 8 skills | Unity, Unreal, Godot, narrative, audio, level design |
| **cyber-sloth-testing** | 8 skills | API testing, accessibility, performance, QA |
| **cyber-sloth-paid-media** | 7 skills | PPC, programmatic, paid social, tracking |
| **cyber-sloth-spatial** | 6 skills | VisionOS, XR, Metal, spatial computing |
| **cyber-sloth-project-mgmt** | 6 skills | PM, Jira, studio ops, sprint planning |
| **cyber-sloth-support** | 6 skills | Finance, legal, infrastructure, exec summaries |
| **cyber-sloth-product** | 4 skills | Sprint prioritization, feedback, behavioral nudge |
| **resume-career-coach** | 1 skill + 8 refs | Resume, cover letter, LinkedIn, interview prep |

**Total: 96 plugin skills + 23 commands + 1 global skill + 8 reference docs**

## Repository Structure

```
claude-skills-library/
├── plugins/                          # Local Claude Code plugins
│   ├── cyber-sloth-suite/            # Core orchestrator
│   │   ├── .claude-plugin/plugin.json
│   │   ├── commands/                 # 23 slash commands
│   │   ├── skills/                   # 9 core skills
│   │   ├── hooks/                    # Session startup hooks
│   │   └── references/               # Voice personas, agent registry
│   ├── cyber-sloth-engineering/      # Engineering division
│   │   ├── .claude-plugin/plugin.json
│   │   └── skills/
│   ├── cyber-sloth-design/           # Design division
│   ├── cyber-sloth-marketing/        # Marketing division
│   ├── cyber-sloth-testing/          # QA & testing division
│   ├── cyber-sloth-gamedev/          # Game dev division
│   ├── cyber-sloth-spatial/          # XR/VisionOS division
│   ├── cyber-sloth-paid-media/       # Paid media division
│   ├── cyber-sloth-product/          # Product division
│   ├── cyber-sloth-project-mgmt/     # Project management division
│   ├── cyber-sloth-support/          # Support & ops division
│   └── cyber-sloth-specialized/      # Specialized skills
├── skills/                           # Global skills (not plugin-scoped)
│   └── resume-career-coach/
│       ├── SKILL.md
│       └── references/               # 8 reference docs
├── install.sh                        # One-command installer
└── README.md
```

## Installation

### Quick Install (symlink to your Claude config)

```bash
git clone https://github.com/coreymaypray/claude-skills-library.git
cd claude-skills-library
chmod +x install.sh
./install.sh
```

### Manual Install

Copy plugins to your Claude Code local plugins directory:

```bash
# Copy all plugin divisions
cp -R plugins/* ~/.claude/plugins/local/

# Copy global skills
cp -R skills/* ~/.claude/skills/

# Enable plugins in Claude Code settings
# Open ~/.claude/settings.json and add each plugin to the enabledPlugins array
```

### Enable Plugins

After copying, enable plugins in `~/.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "cyber-sloth-suite@local": { "version": "local" },
    "cyber-sloth-engineering@local": { "version": "local" },
    "cyber-sloth-design@local": { "version": "local" },
    "cyber-sloth-marketing@local": { "version": "local" },
    "cyber-sloth-testing@local": { "version": "local" },
    "cyber-sloth-gamedev@local": { "version": "local" },
    "cyber-sloth-spatial@local": { "version": "local" },
    "cyber-sloth-paid-media@local": { "version": "local" },
    "cyber-sloth-product@local": { "version": "local" },
    "cyber-sloth-project-mgmt@local": { "version": "local" },
    "cyber-sloth-support@local": { "version": "local" },
    "cyber-sloth-specialized@local": { "version": "local" }
  }
}
```

## Usage

Skills are invoked via the `Skill` tool in Claude Code or as slash commands:

```
/threat-model [system name]
/security-audit [target]
/content-pipeline [topic]
/sow [client name] [project type]
/maycrest-page [page name]
```

Skills auto-trigger based on context (e.g., the `backend-database` skill activates when working with Supabase schemas).

## Customization

- **Voice personas**: Edit `plugins/cyber-sloth-suite/references/voice-personas.md`
- **Session context**: Edit `plugins/cyber-sloth-suite/hooks/session-start/profile-context.md`
- **Agent registry**: Edit `plugins/cyber-sloth-suite/references/agent-registry.md`

## Tech Stack Context

These skills are optimized for:
- **Mobile**: Expo (React Native) + NativeWind + Expo Router
- **Backend**: Supabase (Postgres, Auth, Edge Functions, Realtime, Storage)
- **Payments**: Stripe / Stripe Connect
- **Hosting**: Vercel
- **AI**: Claude Code, Anthropic SDK

But most skills are framework-agnostic and work across any stack.

## License

Private — Cyber Sloth Empire / Maycrest
