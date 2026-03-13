---
description: "Rapid STRIDE + ATT&CK threat model for any system. Usage: /threat-model [system name or description]"
---

# Rapid Threat Model

You are performing a rapid threat model for Corey Maypray. The user has described a system or application to analyze.

## Step 1: System Overview
Create a quick architecture summary:
- Components (frontend, backend, database, APIs, third-party services)
- Data flows (what moves where)
- Trust boundaries (where trust levels change)
- Entry points (user-facing attack surface)

## Step 2: STRIDE Analysis

For each major component, evaluate:

| Threat | Question | Finding |
|--------|----------|---------|
| **S**poofing | Can an attacker impersonate a user or service? | |
| **T**ampering | Can data be modified in transit or at rest? | |
| **R**epudiation | Can actions be denied or logs be tampered? | |
| **I**nformation Disclosure | Can sensitive data leak? | |
| **D**enial of Service | Can the system be made unavailable? | |
| **E**levation of Privilege | Can a user gain unauthorized access? | |

## Step 3: MITRE ATT&CK Mapping
Map the top 5 threats to ATT&CK techniques:
- Technique ID and name
- Tactic category
- Relevance to this system
- Detection opportunity

## Step 4: Risk Matrix

| Threat | Likelihood | Impact | Risk Level | Priority |
|--------|-----------|--------|------------|----------|
| | High/Med/Low | High/Med/Low | Critical/High/Med/Low | P1-P4 |

## Step 5: Recommendations
For each P1 and P2 risk:
- Mitigation strategy
- Implementation effort (Quick Win / Moderate / Major)
- Relevant controls (NIST CSF, CIS, etc.)

## Step 6: Summary
- Total threats identified
- Critical/High findings count
- Top 3 immediate actions
- Recommended follow-up (pentest, security review, architecture change)

Present the complete threat model in a format ready for client delivery or internal review.
