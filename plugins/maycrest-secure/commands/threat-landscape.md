---
name: threat-landscape
description: "Threat intelligence briefing: STRIDE model meets current threat landscape with actionable technical recommendations. Usage: /threat-landscape [system or industry]"
---

# Threat Landscape Briefing

You are running the Cyber Sloth Empire's threat intelligence pipeline. This isn't a generic security checklist — it's a targeted briefing that maps real-world threats to your specific system. The user has described a system or industry to analyze.

## Stage 1: STRIDE Threat Model

Execute the `/threat-model` command workflow. Produce:
- System architecture overview with trust boundaries
- Full STRIDE analysis per component
- MITRE ATT&CK technique mapping for top threats
- Risk matrix with priority ratings
- Initial mitigation recommendations

This is the foundation — what COULD go wrong, structured and categorized.

## Stage 2: Current Threat Landscape Research

Invoke the `maycrest-automate:trend-researcher` skill. Research what IS going wrong:
- Active threat campaigns targeting this type of system/industry
- Emerging attack vectors and techniques (last 6-12 months)
- Notable breaches in the same sector and lessons learned
- Threat actor profiles relevant to this target (nation-state, criminal, hacktivist)
- Supply chain and third-party risks trending upward
- Regulatory and compliance changes on the horizon

Cross-reference findings with the STRIDE model — where do real-world threats overlap with our theoretical risks?

## Stage 3: Technical Recommendations

Invoke the `maycrest-automate:security-engineer` skill. Make it actionable:
- Map each real-world threat to specific technical controls
- Prioritize by: likelihood (from landscape research) x impact (from threat model)
- Provide implementation-level recommendations (not just "use encryption")
- Tool and technology recommendations where applicable
- Detection signatures and monitoring rules for active threats
- Hardening checklist specific to the tech stack

## Output

### Executive Threat Brief

**For:** [System/Organization Name]
**Date:** Current
**Classification:** Internal

#### Threat Summary
- Overall threat level assessment (Low / Elevated / High / Critical)
- Top 3 threats by combined likelihood and impact
- Key changes since last assessment (or baseline if first)

#### Landscape Overview
- Active campaigns and threat actors of concern
- Industry-specific risk factors
- Emerging trends to watch

#### STRIDE-to-Reality Mapping
| STRIDE Category | Theoretical Risk | Active Real-World Threat | Priority |
|-----------------|-----------------|-------------------------|----------|
| | | | P1-P4 |

#### Actionable Recommendations
Prioritized list with:
- What to do (specific technical control)
- Why now (linked to active threat)
- Implementation effort (Quick Win / Sprint / Project)
- Success metric (how you know it's working)

#### Monitoring Priorities
What to watch for, what alerts to create, what logs to review.

Know your enemy, know your system, know your priorities. That's the Cyber Sloth way.
