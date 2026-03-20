---
name: rapid-prototype
description: "From zero to MVP before your coffee gets cold. Fast prototype with just enough polish to prove the concept. Usage: /rapid-prototype [idea or feature]"
---

# Rapid Prototype Pipeline

You are running the Cyber Sloth Empire's speed build. No overthinking, no gold-plating — just a functional prototype that proves the idea works. The user has described what they want to test.

## Stage 1: Scope the MVP

Before writing a single line of code, ruthlessly cut scope:
1. What's the ONE thing this prototype needs to prove?
2. What's the absolute minimum feature set? (aim for 2-3 features max)
3. Who's seeing this? (internal demo, investor pitch, user test)
4. What can we fake? (mock data, placeholder UI, hardcoded values)
5. Time constraint? (default: build it in one session)

Create a "Build / Skip / Fake" list for every feature mentioned.

## Stage 2: Prototype Build

Invoke the `cyber-sloth-engineering:rapid-prototyper` skill. Build fast:
- Scaffold the project with the leanest stack possible
- Implement core flow (the happy path only)
- Use mock data and placeholder content where it saves time
- Skip auth, skip edge cases, skip error handling (for now)
- Focus on the "aha moment" — the thing that makes people get it

## Stage 3: UI Polish Pass

Invoke the `cyber-sloth-design:ui-designer` skill. Make it presentable:
- Apply consistent spacing, typography, and color
- Add just enough visual hierarchy to be usable
- Polish the hero screen/flow (first impression matters)
- Skip pixel-perfection — aim for "looks intentional, not broken"

## Stage 4: Sanity Check

Invoke the `cyber-sloth-testing:reality-checker` skill. Quick gut check:
- Does the core flow actually work end-to-end?
- Is the value proposition clear within 10 seconds?
- Any embarrassing bugs in the demo path?
- What would kill the demo? Fix only those things.

## Output

Deliver the prototype with:
- Working demo (link or instructions to run)
- What's real vs. what's faked
- Known limitations (the stuff we skipped on purpose)
- "If this validates" next steps — what to build for real
- Time spent vs. time saved by prototyping first

Speed is the feature. Ship it ugly, ship it fast.
