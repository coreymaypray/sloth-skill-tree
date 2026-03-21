---
name: security-audit
description: "The full security sweep — threat modeling, detection review, compliance check, and incident readiness. No stone unturned. Usage: /security-audit [system or application name]"
---

# Full Security Audit

You are running the Maycrest Group's comprehensive security assessment. Four specialists, one mission: find every crack before someone else does. The user has described the system to audit.

## Stage 0: Threat Context

Invoke the `maycrest-automate:threat-intel-analyst` skill. Set the intelligence baseline:
- Industry-specific threat landscape assessment
- Relevant APT groups and their current TTPs
- Trending attack vectors for the target environment
- Known campaigns targeting similar organizations
- Intelligence-driven prioritization for subsequent audit stages

Deliver: **Threat Context Brief** to inform all subsequent audit stages.

## Stage 1: Threat Modeling

Invoke the `maycrest-automate:security-engineer` skill. Map the attack surface:
- System architecture review (components, data flows, trust boundaries)
- STRIDE analysis across all major components
- Attack tree construction for critical assets
- MITRE ATT&CK technique mapping for top threats
- Risk matrix (likelihood x impact) with priority ratings
- Authentication and authorization model review

Deliver: **Threat Model Report** with prioritized risk register.

## Stage 2: Detection & Monitoring Review

Invoke the `maycrest-automate:threat-detection-engineer` skill. Assess visibility:
- Current detection coverage assessment (what can we see, what's blind?)
- Log collection and retention audit
- Alert rule effectiveness (signal-to-noise ratio)
- SIEM/monitoring tool configuration review
- Detection gap analysis mapped to MITRE ATT&CK
- Recommended detection rules for uncovered techniques

Deliver: **Detection Coverage Matrix** with gap analysis.

## Stage 3: Compliance Check

Invoke the `maycrest-automate:compliance-auditor` skill. Check the boxes that matter:
- Regulatory framework identification (GDPR, SOC2, HIPAA, PCI — what applies?)
- Data handling and privacy assessment
- Access control policy review
- Encryption standards audit (at rest, in transit)
- Third-party and vendor risk assessment
- Documentation and evidence gaps
- Data subject rights implementation audit (GDPR/CCPA)
- Remediation roadmap for compliance gaps

Deliver: **Compliance Status Report** with gap-to-remediation mapping.

## Stage 4: Incident Response Readiness

Invoke the `maycrest-automate:incident-response-commander` skill. Test the playbook:
- IR plan existence and completeness review
- Communication chain validation (who gets called, in what order?)
- Escalation procedure assessment
- Backup and recovery capability check
- Tabletop exercise scenario design
- Mean time to detect/respond estimation
- Post-incident review process evaluation

Deliver: **IR Readiness Score** (1-10) with improvement plan.

## Output

### Consolidated Security Report

#### Executive Summary
- Overall security posture rating (Critical / Needs Work / Solid / Hardened)
- Top 5 findings by severity
- Estimated remediation effort

#### Detailed Findings

| # | Finding | Severity | Category | Remediation | Effort |
|---|---------|----------|----------|-------------|--------|
| | | Critical/High/Med/Low | Threat/Detection/Compliance/IR | | Quick/Moderate/Major |

#### Remediation Roadmap
- **Immediate** (this week): Critical and high-severity items
- **Short-term** (30 days): Medium-severity items and quick wins
- **Ongoing**: Process improvements and monitoring enhancements

#### Appendices
- Full threat model
- Detection coverage matrix
- Compliance gap details
- IR exercise scenarios

The Maycrest Group takes security personally. This audit is thorough because the alternative is unacceptable.
