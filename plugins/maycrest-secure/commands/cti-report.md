---
name: cti-report
description: "Threat intelligence briefing — threat landscape assessment with detection recommendations. Usage: /cti-report [industry, organization, or threat scenario]"
---

# Threat Intelligence Briefing

You are running the Cyber Sloth Empire's threat intelligence pipeline. Two analysts, one objective: know the threat before it knows you. The user has described the industry, organization, or threat scenario.

## Stage 1: Threat Landscape Assessment

Invoke the `maycrest-automate:threat-intel-analyst` skill. Map the threat landscape:
- Industry-specific threat environment analysis
- Relevant APT group profiling (motivation, capability, targeting history)
- Trending TTPs observed in the wild
- Indicator packages (IOCs, infrastructure patterns, malware families)
- Geopolitical and economic factors influencing threat activity
- MITRE ATT&CK technique mapping for identified actors

Deliver: **Threat Intelligence Report** with actor profiles and ATT&CK mapping.

## Stage 2: Detection Recommendations

Invoke the `maycrest-automate:threat-detection-engineer` skill. Close the visibility gaps:
- Detection gap analysis against the identified TTPs
- Sigma rule development for highest-priority techniques
- Log source requirements for effective detection
- MITRE ATT&CK coverage mapping (current vs. recommended)
- Alert tuning recommendations to reduce false positives
- Monitoring priority matrix based on threat likelihood and impact

Deliver: **Detection Recommendations** with Sigma rules and coverage mapping.

## Output

### Consolidated Threat Intelligence Briefing

#### Executive Summary
- Threat level assessment (Critical / Elevated / Moderate / Low)
- Top 3 threats by relevance and likelihood
- Key intelligence gaps

#### Threat Landscape
- Industry risk profile
- Active campaigns and recent incidents in sector
- Emerging threat trends

#### Actor Profiles

| Actor | Type | Motivation | Target Sectors | Key TTPs | Confidence |
|-------|------|------------|----------------|----------|------------|
| | APT/Criminal/Hacktivist | Espionage/Financial/Disruption | | | High/Medium/Low |

#### Recommended Detections
- Sigma rules for priority TTPs
- Log source and telemetry requirements
- Coverage gap remediation plan

#### Monitoring Priorities
- **Immediate Watch**: Active campaigns targeting your sector
- **Elevated Monitoring**: Trending TTPs with high relevance
- **Baseline Awareness**: Emerging threats to track over time

The Cyber Sloth Empire watches the watchers. Intelligence-driven defense means knowing the threat before writing the first rule.
