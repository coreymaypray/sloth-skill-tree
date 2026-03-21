---
name: new-project
description: "Scaffold a new client app with architecture, schema, and infrastructure. Usage: /new-project [name]"
---

# New Project Scaffold

You are setting up a new Maycrest Group client project. The user has provided a project name.

## Step 1: Discovery Questions
Ask the user these questions (skip any they've already answered):
1. What type of app? (booking, business tool, dashboard, marketplace, other)
2. Target platforms? (iOS, Android, both, web)
3. Key features? (list the top 3-5)
4. Authentication method? (email, Apple, Google, all)
5. Payments needed? (one-time, subscription, marketplace/Connect)
6. Estimated user base? (helps with Supabase plan selection)

## Step 2: Architecture Plan
Invoke `maycrest-automate:backend-architect` skill. Create:
- Tech stack confirmation
- Navigation structure (Expo Router file tree)
- Core screens list
- Key components needed

## Step 3: Database Schema
Invoke `maycrest-automate:backend-architect` skill. Design:
- Core tables with columns and types
- RLS policy outline
- Relationships and indexes
- Supabase plan recommendation

## Step 4: Infrastructure Checklist
Invoke `maycrest-automate:devops-automator` skill. Generate:
- Supabase project setup checklist
- Environment variable template
- Third-party service configuration list
- Deployment pipeline outline

## Step 5: SOW Draft
Generate a Statement of Work outline with:
- Project overview
- Scope (in/out)
- Deliverables
- Estimated timeline
- Pricing tier recommendation

Present everything in a clear, organized format that Corey can review and share with the client.
