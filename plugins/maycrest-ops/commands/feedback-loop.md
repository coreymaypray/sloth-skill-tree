---
name: feedback-loop
description: "Turn messy user feedback into prioritized product changes. Synthesis, research, behavioral design, and sprint planning in one pipeline. Usage: /feedback-loop [feedback source or product area]"
---

# Feedback Loop Pipeline

You are running the Cyber Sloth Empire's feedback-to-action pipeline. Raw user feedback is chaos — this pipeline turns it into structured, prioritized, behaviorally-informed product improvements. The user has feedback to process.

## Stage 1: Feedback Synthesis

Invoke the `cyber-sloth-product:feedback-synthesizer` skill. Make sense of the noise:
- Aggregate and categorize all feedback (bugs, feature requests, UX pain, praise)
- Identify recurring themes and frequency patterns
- Sentiment analysis across feedback sources
- Extract the "jobs to be done" behind feature requests
- Separate signal from noise — what are users actually struggling with?
- Identify contradictory feedback and resolve with data where possible

Deliver: **Feedback Themes Report** with frequency, severity, and sentiment per theme.

## Stage 2: Research Analysis

Invoke the `cyber-sloth-design:ux-researcher` skill. Go deeper:
- Map feedback themes to user journey stages (where does the pain occur?)
- Persona-based analysis (do different user types have different pain points?)
- Competitive comparison (how do competitors handle these same issues?)
- Quantitative validation (do usage metrics support the qualitative feedback?)
- Identify root causes vs. symptoms (users say X, but the real problem is Y)
- Opportunity sizing (how many users affected, what's the retention impact?)

Deliver: **Research Insights Report** with validated findings and opportunity scores.

## Stage 3: Behavioral Intervention Design

Invoke the `cyber-sloth-product:behavioral-nudge` skill. Design smart solutions:
- For each validated pain point, propose behavioral interventions
- Apply nudge theory (defaults, framing, social proof, commitment devices)
- Design low-effort, high-impact UX tweaks before resorting to new features
- Propose A/B test designs for each intervention
- Predict second-order effects (will fixing this break something else?)
- Engagement and retention impact estimation

Deliver: **Intervention Playbook** with proposed changes and expected impact.

## Stage 4: Sprint Prioritization

Invoke the `cyber-sloth-product:sprint-prioritizer` skill. Make it executable:
- Score each intervention: impact x effort x confidence (ICE framework)
- Group into: Quick Wins, Next Sprint, Backlog, Needs More Research
- Map dependencies between changes
- Define success metrics for each change
- Create user stories ready for development
- Recommend sprint allocation (how much capacity to dedicate)

## Output

### Feedback Loop Report

#### Executive Summary
- Total feedback processed
- Key themes identified (top 5)
- Recommended actions (prioritized)

#### Theme-to-Action Pipeline

| Theme | Frequency | Research Insight | Intervention | Priority | Sprint |
|-------|-----------|-----------------|--------------|----------|--------|
| | | | | P1-P4 | Quick Win / Next / Backlog |

#### Quick Wins
Changes that can ship this week with minimal risk.

#### Next Sprint Candidates
Validated improvements ready for development.

#### Needs More Research
Promising signals that need deeper investigation.

Users are telling you what they need. The Cyber Sloth Empire listens — and then ships.
