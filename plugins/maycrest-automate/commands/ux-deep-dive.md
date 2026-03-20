---
name: ux-deep-dive
description: "Comprehensive UX quality audit: research, architecture, accessibility, and inclusive design. Every user matters. Usage: /ux-deep-dive [product or feature]"
---

# UX Deep Dive

You are running the Cyber Sloth Empire's comprehensive UX audit. Four specialists examine the experience from every angle — because a product is only as good as how it feels to use. The user has a product or feature to evaluate.

## Stage 1: User Research

Invoke the `maycrest-create:ux-researcher` skill. Understand the humans:
- User persona validation (do our assumptions match reality?)
- Journey mapping for primary user flows
- Pain point identification and severity mapping
- Task completion analysis (where do users struggle or bail?)
- Competitive UX benchmarking (what do users expect from this category?)
- Heuristic evaluation against Nielsen's 10 usability heuristics
- Recommended research activities if live user input is needed

Deliver: **User Research Report** with findings, severity ratings, and persona insights.

## Stage 2: Information Architecture Review

Invoke the `maycrest-create:ux-architect` skill. Evaluate the structure:
- Navigation model assessment (is it intuitive or are users getting lost?)
- Content hierarchy audit (is important stuff findable?)
- User flow analysis (do flows match mental models?)
- Labeling and taxonomy review (do words make sense to users?)
- Search and discovery patterns (can users find what they don't know to look for?)
- Cross-device IA consistency (does structure survive mobile?)
- Sitemap/flow diagram with pain points annotated

Deliver: **IA Assessment** with structural recommendations.

## Stage 3: Accessibility Audit

Invoke the `maycrest-ops:accessibility-auditor` skill. Check compliance:
- WCAG 2.1 AA compliance audit (minimum standard)
- Screen reader compatibility testing
- Keyboard navigation completeness
- Color contrast and visual accessibility
- Touch target sizing (mobile)
- Focus management and skip navigation
- ARIA implementation review
- Alt text and media accessibility
- Cognitive accessibility considerations (reading level, complexity)

Deliver: **Accessibility Report** with WCAG violations, severity, and remediation steps.

## Stage 4: Inclusive Design Review

Invoke the `maycrest-create:inclusive-visuals` skill. Broaden the lens:
- Representation audit (do visuals reflect diverse users?)
- Language inclusivity check (gendered language, cultural assumptions)
- Internationalization readiness (RTL, date formats, cultural norms)
- Age-appropriate design considerations
- Socioeconomic accessibility (does it work on slow connections, old devices?)
- Dark pattern audit (are we accidentally manipulating users?)
- Cultural sensitivity review

Deliver: **Inclusive Design Assessment** with specific recommendations.

## Output

### Consolidated UX Report

#### UX Health Score

| Dimension | Score (1-10) | Critical Issues | Opportunities |
|-----------|-------------|-----------------|---------------|
| Usability | | | |
| Information Architecture | | | |
| Accessibility | | | |
| Inclusive Design | | | |
| **Overall UX** | | | |

#### Top 10 Findings
Prioritized by impact on users, with severity and effort ratings.

#### Quick Wins
UX improvements that can ship fast with high user impact.

#### Structural Recommendations
Bigger changes that require design/development investment.

#### Accessibility Compliance Status
- Current WCAG level achieved
- Gaps to AA compliance
- Remediation priority and timeline

#### Inclusive Design Roadmap
Specific steps to make the product work for everyone.

The Cyber Sloth Empire builds for every user, not just the ones who look like us. This audit ensures we're walking that talk.
