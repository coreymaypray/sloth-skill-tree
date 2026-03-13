---
description: "Product discovery done right: market research, user insights, technical feasibility, and a prioritized feature list. Know before you build. Usage: /discovery-sprint [product idea or problem space]"
---

# Discovery Sprint

You are running the Cyber Sloth Empire's product discovery pipeline. Before a single line of code gets written, we figure out what's worth building. Market research, user insights, technical reality, and a prioritized plan — all in one sprint. The user has a product idea or problem space to explore.

## Stage 1: Market Research

Invoke the `cyber-sloth-product:trend-researcher` skill. Understand the landscape:
- Market size and growth trajectory (is this a growing space?)
- Competitive landscape mapping (who's already here, what do they miss?)
- Emerging trends and technology shifts relevant to this space
- Monetization models in this category (how do competitors make money?)
- Timing assessment (too early, too late, or just right?)
- Adjacent market opportunities (what else could this unlock?)

Deliver: **Market Landscape Brief** with opportunity assessment and competitive map.

## Stage 2: User Research

Invoke the `cyber-sloth-design:ux-researcher` skill. Understand the humans:
- Target user persona development (who are we building for, specifically?)
- Problem validation (is this actually a problem people have?)
- Current solution audit (how do people solve this today? what sucks about it?)
- Jobs-to-be-done framework (what job does this product get hired for?)
- Willingness to pay signals (would people actually pay for this?)
- User interview question framework (for live validation if needed)

Deliver: **User Insight Report** with validated personas and problem statements.

## Stage 3: Technical Feasibility

Invoke the `cyber-sloth-engineering:senior-developer` skill. Reality-check the build:
- Technical architecture assessment (can this be built with our stack?)
- Build vs. buy analysis for key components
- Third-party dependency risks (APIs, services we'd rely on)
- Scalability considerations (what breaks at 10x, 100x, 1000x users?)
- Technical risk register (what's the hardest part to build?)
- Estimated development effort by feature (T-shirt sizing: S/M/L/XL)
- MVP scope recommendation (smallest thing that tests the hypothesis)

Deliver: **Technical Feasibility Report** with effort estimates and risk flags.

## Stage 4: Prioritized Feature List

Invoke the `cyber-sloth-product:sprint-prioritizer` skill. Decide what to build first:
- Feature list derived from research (market gaps + user needs + technical reality)
- RICE scoring (Reach x Impact x Confidence / Effort)
- MVP feature set (the minimum to test the core hypothesis)
- V1 feature set (the minimum to charge money)
- V2 feature set (the features that create competitive advantage)
- Feature dependency map
- Go/No-Go recommendation with confidence level

## Output

### Discovery Sprint Report

#### Executive Summary
- Opportunity assessment (Strong / Moderate / Weak / Pass)
- Core insight in one sentence
- Recommended next step

#### Market Opportunity
- Market size and positioning
- Competitive advantages available
- Timing assessment

#### User Validation
- Primary persona and their #1 pain point
- Problem severity and frequency
- Willingness to pay indicator

#### Technical Plan
- Recommended tech stack
- MVP scope and effort estimate
- Key technical risks

#### Prioritized Roadmap

| Phase | Features | Effort | Goal |
|-------|----------|--------|------|
| MVP | | S/M/L | Test hypothesis |
| V1 | | S/M/L | First revenue |
| V2 | | S/M/L | Competitive moat |

#### Go/No-Go Recommendation
Clear recommendation with confidence level and what would change the answer.

The Cyber Sloth Empire builds deliberately. Discovery first, development second. Always.
