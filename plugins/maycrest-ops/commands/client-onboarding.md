---
name: client-onboarding
description: "New client zero-to-sixty: project scaffold, SOW, sprint plan, and executive kickoff summary in one shot. Usage: /client-onboarding [client name] [project type]"
---

# Client Onboarding Pipeline

You are running the Cyber Sloth Empire's new client onboarding sequence. First impressions matter — this pipeline gets a new engagement structured and professional from day one. The user has a new client to onboard.

## Stage 1: Project Scaffold

Execute the `/new-project` command workflow. Set up the foundation:
- Discovery questions (app type, platforms, key features, auth, payments)
- Architecture plan (tech stack, navigation, core screens, components)
- Database schema design (tables, RLS, relationships)
- Infrastructure checklist (Supabase setup, env vars, services)

This gives us the technical blueprint.

## Stage 2: Statement of Work

Execute the `/sow` command workflow. Formalize the engagement:
- Client and project context
- Scope of work with clear boundaries
- Deliverables with acceptance criteria
- Timeline and milestone schedule
- Investment and payment schedule
- Maintenance and support terms
- Legal terms

The SOW is the contract backbone — make it tight.

## Stage 3: Sprint Planning

Invoke the `maycrest-automate:sprint-prioritizer` skill. Plan the execution:
- Break the project scaffold into epics and stories
- Prioritize by: client-visible value first, infrastructure second
- Map the first 3 sprints with clear goals
- Identify the "first deliverable" moment (when the client sees something real)
- Define velocity assumptions and adjust timeline if needed
- Create a dependency chain so nothing blocks unnecessarily

## Stage 4: Executive Kickoff Summary

Invoke the `maycrest-ops:exec-summary` skill. Create the executive brief:
- Project overview (2-3 sentences, no jargon)
- Key deliverables and timeline visualization
- Team and communication structure
- Investment summary
- Next steps and immediate actions
- Risk factors and mitigation approach

This is what the client's decision-maker reads. Make it crisp.

## Output

### New Client Package

| Document | Purpose | Audience |
|----------|---------|----------|
| Project Architecture | Technical blueprint | Dev team |
| Statement of Work | Formal agreement | Client stakeholders |
| Sprint Plan | Execution roadmap | Project team |
| Executive Summary | Kickoff brief | Client leadership |

### Immediate Next Steps
1. Send executive summary for review
2. Schedule kickoff meeting
3. Get SOW signed
4. Begin Sprint 1

The Cyber Sloth Empire onboards clients like we build software — methodical, professional, and slightly faster than they expected.
