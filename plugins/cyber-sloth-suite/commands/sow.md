---
description: "Generate a Statement of Work for a client engagement. Usage: /sow [client name] [project type]"
---

# SOW Generator

You are generating a Statement of Work for a Cyber Sloth Empire client engagement. The user has provided a client name and project type.

## Step 1: Gather Details
Ask the user for any missing information:
1. Client name and business type
2. Project type (mobile app, web app, security assessment, managed services)
3. Key deliverables
4. Timeline constraints
5. Budget range (if known)

## Step 2: Generate SOW

Invoke `cyber-sloth-suite:cyber-sloth-app-dev` skill for context on pricing and phases.

### SOW Structure:

**1. Project Overview**
- Client name and context
- Project description (2-3 sentences)
- Objectives and success criteria

**2. Scope of Work**
- In scope (numbered list of deliverables)
- Out of scope (explicit exclusions)
- Assumptions and dependencies

**3. Deliverables**
- Itemized list with descriptions
- Acceptance criteria for each

**4. Timeline & Milestones**
- Phase breakdown with dates
- Key milestone checkpoints
- Review/approval gates

**5. Investment**
- Phase-based pricing
- Payment schedule (typically 50/25/25 or milestone-based)
- What's included in each phase

**6. Maintenance & Support**
- Post-launch support period (included)
- Ongoing maintenance options and pricing
- SLA details

**7. Terms**
- IP ownership (client owns deliverables)
- Confidentiality
- Change request process
- Cancellation terms

Format the SOW professionally, ready for Corey to review and send.
