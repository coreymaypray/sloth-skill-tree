# Maycrest Group — Sloth Skill Tree

The official plugin library for **Maycrest Group LLC** — powered by **Sloth Flow**.

Organized under the three Maycrest pillars: **Create · Automate · Secure**.

## Structure

```
plugins/
├── maycrest-create/     Creative Services & Content Production (34 specialists)
├── maycrest-automate/   AI Solutions & Business Automation (37 specialists)
├── maycrest-secure/     Cybersecurity & Threat Intelligence (10 specialists)
├── maycrest-ops/        Operations, QA, PM & Business Support (22 specialists)
└── maycrest-command/    Sloth Command + Sloth Dispatch Orchestration (2 specialists)

skills/
├── resume-career-coach/     Resume, cover letter, LinkedIn, interview prep
├── chevelle-restoration/    1972 Chevelle SS restoration knowledge base
└── davinci-resolve-mcp/     DaVinci Resolve Studio automation via MCP
```

**108 plugin specialists + 3 global skills** across 5 plugins.

## Quick Start

| Need | Command |
|------|---------|
| Strategic multi-pillar work | `/sloth [describe your goal]` |
| Quick single-skill routing | `/sloth-dispatch [describe your task]` |
| Direct specialist access | `maycrest-[pillar]:[skill-name]` |

---

## Installation

### Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) (`npm install -g @anthropic-ai/claude-code`)
- Node.js 18+
- Git

### Step 1: Clone

```bash
git clone https://github.com/coreymaypray/sloth-skill-tree.git
```

### Step 2: Register Marketplace

```bash
claude plugin marketplace add /path/to/sloth-skill-tree/plugins
```

### Step 3: Install All Plugins

```bash
for p in maycrest-command maycrest-create maycrest-automate maycrest-secure maycrest-ops; do
  claude plugin install "$p@sloth-skill-tree" --scope user
done
```

### Step 4: Install Global Skills

```bash
mkdir -p ~/.claude/skills
cp -R skills/* ~/.claude/skills/
```

### Step 5: Restart Claude Code

Type `/` to see all commands. Run `/plugins` to verify.

### Updating

```bash
cd sloth-skill-tree && git pull origin main
```

Restart Claude Code. No reinstall needed — the marketplace points to the repo.

---

## Pillar: CREATE (34 specialists)

Creative Services — design, brand, marketing, content, social media, paid media, cultural content.

| Skill | What It Does |
|-------|-------------|
| **article-writer** | Long-form articles, LinkedIn newsletters, thought leadership |
| **hook-writing** | Scroll-stopping hooks, headlines, email subjects, video intros |
| **tweet-to-short** | Convert social posts into TikTok/Reels/Shorts scripts |
| **content-creator** | Editorial calendars, content pillars, cross-platform planning |
| **social-strategist** | Cross-platform social playbooks and campaign coordination |
| **seo-specialist** | Keyword research, technical SEO audits, ranking strategy |
| **growth-hacker** | Funnel optimization, conversion experiments, channel ID |
| **instagram-curator** | Feed aesthetics, caption writing, Reels strategy, hashtags |
| **tiktok-strategist** | Trend identification, video scripting, short-form growth |
| **twitter-engager** | Tweet writing, threads, hot takes, cybersecurity commentary |
| **youtube-strategist** | Content planning, scripting, thumbnails, SEO, growth |
| **reddit-builder** | Subreddit identification, engagement, authentic presence |
| **carousel-engine** | LinkedIn/Instagram carousel content — slides, copy, CTAs |
| **app-store-optimizer** | App Store keyword research, listing copy, screenshot strategy |
| **ui-designer** | Design systems, component libraries, dark mode, Figma-to-code |
| **ux-architect** | Information architecture, navigation, user flows, layouts |
| **ux-researcher** | Usability testing, interviews, personas, journey mapping |
| **brand-guardian** | Brand consistency audits, identity enforcement |
| **visual-storyteller** | Infographics, storyboards, campaign visuals, data viz |
| **whimsy-injector** | Microcopy, Easter eggs, delightful empty states, fun UI |
| **image-prompt-engineer** | AI image prompts for DALL-E, Midjourney, generative tools |
| **inclusive-visuals** | WCAG compliance, color contrast, accessible imagery |
| **canva-infographic-builder** | Canva infographic workflow with Cyber Sloth aesthetic |
| **black-dating-convo** | Culturally-grounded dating and relationship content |
| **creative-strategist** | Ad creative, RSA headlines, A/B test copy variants |
| **paid-media-auditor** | Campaign forensics, wasted spend ID, ROI analysis |
| **paid-social** | Facebook, LinkedIn, TikTok ad setup and optimization |
| **ppc-strategist** | Google Ads architecture, keyword strategy, bid management |
| **programmatic-buyer** | Display/programmatic advertising, retargeting, audiences |
| **search-query-analyst** | Search term analysis, negative keywords, query reports |
| **tracking-specialist** | GTM, GA4, Stripe event tracking, pixel debugging |
| **cultural-intelligence** | Cross-cultural adaptation, localization, inclusive design |
| **create-lead** | Division dispatcher — routes to the right creative specialist |
| **google-flow** | Veo 3.1 AI video production, Scene Builder, dialogue/SFX |

**Commands:** `/brand-refresh`, `/brand-voice`, `/content-blitz`, `/content-pipeline`, `/dating-topic`, `/infographic`, `/launch-campaign`, `/marketing`, `/paid-media`, `/repurpose`

---

## Pillar: AUTOMATE (37 specialists)

AI Solutions — full-stack engineering, mobile, AI, spatial, gamedev, product, workflow automation.

| Skill | What It Does |
|-------|-------------|
| **backend-architect** | Supabase schemas, Edge Functions, RLS, API design, multi-tenant |
| **backend-database** | PostgreSQL/Supabase schema design, migrations, RLS policies, query optimization |
| **backend-infrastructure** | Vercel, Apple sign-in, webhooks, Edge Functions, secrets, deployment pipelines |
| **app-dev** | Full Expo + Supabase + Stripe app lifecycle — client apps and TIE Platform |
| **mobile-app-builder** | Expo specialist — push notifications, EAS Build, deep linking, app store submission |
| **senior-developer** | Full-stack code quality, reviews, refactoring, architecture |
| **frontend-developer** | React Native (Expo) and Next.js — components, NativeWind, navigation |
| **rapid-prototyper** | Zero to MVP fast — proof of concepts and validation prototypes |
| **ai-engineer** | Claude API, RAG systems, chatbots, prompt engineering, LLM cost optimization |
| **data-engineer** | Analytics pipelines, aggregation queries, reporting backends |
| **devops-automator** | CI/CD, GitHub Actions, EAS Build, Vercel config, environment management |
| **optimization-architect** | AI cost governance, circuit breakers, LLM routing, token budgets |
| **technical-writer** | READMEs, API docs, tutorials, runbooks, schema documentation |
| **maycrest-web-design** | Maycrest brand web design — UI/UX patterns, landing pages, component specs |
| **visionos-engineer** | Apple Vision Pro — RealityKit, volumetric content, Liquid Glass, spatial widgets |
| **spatial-metal** | Metal GPU rendering, spatial graphics pipelines, Vision Pro renderers |
| **xr-architect** | Spatial UX — 3D interface layouts, HUD design, depth placement |
| **xr-developer** | WebXR — A-Frame, Three.js XR, Babylon.js, hand tracking |
| **xr-cockpit** | Cockpit/control panel interfaces, spatial HUDs, simulator dashboards |
| **terminal-integration** | Terminal emulation in spatial/native apps — SwiftTerm, ANSI, SSH |
| **unity-developer** | Unity C#, ScriptableObjects, MonoBehaviour, performance optimization |
| **unreal-developer** | UE5 Blueprints, C++, GAS, Nanite, Lumen |
| **godot-developer** | Godot 4 GDScript, C#, signal-based architecture |
| **game-designer** | Game mechanics, GDD writing, gameplay loops, balance, progression |
| **game-audio** | FMOD, Wwise, adaptive music, spatial audio, SFX |
| **level-designer** | Spatial storytelling, encounter design, pacing, blockout |
| **narrative-designer** | Branching dialogue, lore, environmental storytelling |
| **technical-artist** | Shaders, VFX, LOD systems, texture compression, particles |
| **behavioral-nudge** | Gamification, engagement loops, push strategy, churn reduction |
| **feedback-synthesizer** | User feedback analysis, review synthesis, signal prioritization |
| **sprint-prioritizer** | ICE/RICE scoring, backlog management, scope cutting |
| **trend-researcher** | Competitive analysis, emerging trends, market intelligence |
| **agents-orchestrator** | Multi-agent pipeline conductor, parallel workflows |
| **data-consolidation** | ETL, data pipeline construction, cross-system consolidation |
| **developer-advocate** | DevRel, DX audits, tutorial writing, onboarding optimization |
| **model-qa** | LLM quality assurance, prompt evaluation, response benchmarking |
| **automate-lead** | Division dispatcher — routes to the right engineering specialist |

**Commands:** `/design`, `/discovery-sprint`, `/engineering`, `/full-stack-build`, `/gamedev`, `/maycrest-page`, `/new-project`, `/performance-sweep`, `/product`, `/rapid-prototype`, `/sow`, `/spatial`, `/specialized`, `/ux-deep-dive`

---

## Pillar: SECURE (10 specialists)

Cybersecurity — security engineering, threat intelligence, incident response, compliance, offensive security.

| Skill | What It Does |
|-------|-------------|
| **security-engineer** | Application security, vulnerability audits, RLS review, OWASP checks |
| **threat-detection-engineer** | SIEM rules, Sigma rules, ATT&CK mapping, alert tuning, threat hunting |
| **threat-intel-analyst** | Threat intelligence collection, indicator analysis, TTP tracking |
| **incident-response-commander** | Incident management, on-call rotations, post-mortems, SLO/SLI |
| **cloud-security-architect** | Cloud security posture, IAM, network segmentation, multi-cloud |
| **forensics-investigator** | Digital forensics, evidence collection, chain of custody, analysis |
| **offensive-security-engineer** | Penetration testing methodology, exploit development, red team ops |
| **compliance-auditor** | SOC 2, GDPR, HIPAA, PCI-DSS, ISO 27001 gap analysis, remediation |
| **legal-compliance** | GDPR reviews, privacy policies, data handling audits, user data rights |
| **secure-lead** | Division dispatcher — routes to the right security specialist |

**Commands:** `/cti-report`, `/incident-forensics`, `/pentest`, `/security-audit`, `/threat-landscape`, `/threat-model`

---

## OPS (22 specialists)

Operations — project management, QA/testing, finance, analytics, studio operations.

| Skill | What It Does |
|-------|-------------|
| **senior-pm** | Project breakdown, task creation, scope, timeline, client coordination |
| **project-shepherd** | Client communication, risk management, status reports, stakeholder updates |
| **jira-steward** | Agile traceability, Jira tickets, branch naming, PR templates |
| **experiment-tracker** | A/B test management, hypothesis design, feature flags, results analysis |
| **studio-operations** | Solo/small-agency ops — capacity planning, tool audits, bandwidth |
| **studio-producer** | Creative/technical production, build coordination, deliverable planning |
| **api-tester** | API validation, Edge Function verification, auth flow testing |
| **test-analyzer** | Test output analysis, Jest interpretation, CI failure investigation |
| **accessibility-auditor** | WCAG 2.2 compliance, screen reader testing, keyboard navigation |
| **performance-benchmarker** | App startup time, render perf, query benchmarks, bundle size |
| **reality-checker** | Deployment readiness certification, release gates, production cert |
| **workflow-optimizer** | CI/CD optimization, pipeline speed, flaky test elimination |
| **tool-evaluator** | Testing framework comparison, library assessment, CI/CD tool recommendations |
| **accounts-payable** | Stripe invoicing, vendor management, contractor payments |
| **finance-tracker** | Stripe revenue monitoring, invoice management, project P&L |
| **analytics-reporter** | Business intelligence, revenue metrics, deployment stats, KPIs |
| **data-analytics** | Supabase data analysis, Stripe reporting, custom dashboards, trend analysis |
| **exec-summary** | Board reports, leadership briefs, client summaries, QBRs |
| **infra-maintainer** | Supabase monitoring, Vercel status, EAS troubleshooting, infra audits |
| **support-responder** | Client/end-user support, ticket resolution, troubleshooting |
| **sloth-commit** | Commits and pushes Claude Code memory to GitHub |
| **report-distribution** | Automated report delivery, scheduled reporting, client distribution |

**Commands:** `/client-delivery`, `/client-onboarding`, `/code-review-pipeline`, `/feedback-loop`, `/project-mgmt`, `/support`, `/testing`

---

## COMMAND (2 specialists)

Sloth Command + Sloth Dispatch. Strategic orchestration across all pillars.

| Skill | What It Does |
|-------|-------------|
| **sloth-command** | Sloth Command — analyzes any task, identifies best divisions and skills, builds phased execution plans |
| **chief-of-staff** | Sloth Dispatch — quick single-skill routing, lightweight task dispatch |

**Commands:** `/sloth`, `/sloth-dispatch`

---

## Global Skills (3)

Standalone skills not tied to any pillar.

| Skill | What It Does |
|-------|-------------|
| **resume-career-coach** | Resume, cover letter, LinkedIn, interview prep (8 reference docs) |
| **chevelle-restoration** | 1972 Chevelle SS restoration knowledge base |
| **davinci-resolve-mcp** | DaVinci Resolve Studio automation via MCP server |

---

## Tech Stack

These skills are optimized for:
- **Mobile**: Expo (React Native) + NativeWind + Expo Router
- **Backend**: Supabase (Postgres, Auth, Edge Functions, Realtime, Storage)
- **Payments**: Stripe / Stripe Connect
- **Hosting**: Vercel
- **AI**: Claude Code, Anthropic SDK

But most skills are framework-agnostic and work across any stack.

---

**Maycrest Group LLC** · Indianapolis, IN · Create · Automate · Secure
