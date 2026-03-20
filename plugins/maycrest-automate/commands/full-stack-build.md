---
name: full-stack-build
description: "The whole damn app, soup to nuts. Orchestrates a full-stack build from blank canvas to deployed product. Usage: /full-stack-build [app name or description]"
---

# Full-Stack Build Orchestration

You are running the Cyber Sloth Empire's flagship build pipeline. This is the big one — end-to-end app construction with every division pulling its weight. The user has described what they want built.

## Stage 1: Requirements Gathering

Before we spin up the machine, nail down the specs. Ask the user for anything missing:
1. What does this app do? (core value prop in one sentence)
2. Target platforms? (web, iOS, Android, all of the above)
3. Key features? (top 5, prioritized)
4. Auth requirements? (email, OAuth, SSO)
5. Payment model? (free, subscription, marketplace, one-time)
6. Any integrations? (third-party APIs, existing systems)
7. Timeline and budget constraints?

## Stage 2: Architecture Design

Invoke the `maycrest-automate:backend-architect` skill. Design the system:
- Tech stack selection and justification
- System architecture diagram (components, services, data flow)
- API contract outline (key endpoints, auth strategy)
- Database schema design (tables, relationships, indexes, RLS policies)
- Infrastructure requirements (hosting, CDN, storage, queues)

Present the architecture for user approval before proceeding.

## Stage 3: Frontend Build

Invoke the `maycrest-automate:frontend-developer` skill. Build the UI:
- Component hierarchy and design system setup
- Core screen implementations
- State management architecture
- Responsive layout strategy
- Client-side routing and navigation

## Stage 4: Mobile Build

Invoke the `maycrest-automate:frontend-developer` skill. Build the mobile layer:
- Expo/React Native project scaffold
- Platform-specific adaptations (iOS/Android)
- Native module integration where needed
- Deep linking and push notification setup
- App store asset preparation

## Stage 5: Deployment Pipeline

Invoke the `maycrest-automate:devops-automator` skill. Wire up the infrastructure:
- CI/CD pipeline configuration
- Environment setup (dev, staging, production)
- Monitoring and alerting
- Backup and disaster recovery plan
- SSL, domains, and DNS configuration

## Stage 6: Quality Assurance

Invoke the `maycrest-ops:reality-checker` skill. Run the QA gauntlet:
- Functional testing across all platforms
- Integration test coverage assessment
- Performance baseline check
- Security sanity check
- UX consistency review
- Bug report and priority classification

## Output

Present a comprehensive build summary:
- Architecture overview
- What was built (screens, APIs, infrastructure)
- What's deployed and where
- Known issues and tech debt
- Recommended next steps and iteration priorities

This is the Cyber Sloth Empire operating at full power. Ship it.
