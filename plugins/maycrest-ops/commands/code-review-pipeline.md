---
name: code-review-pipeline
description: "Three-layer code quality gate: architecture, security, and performance. No code ships without the gauntlet. Usage: /code-review-pipeline [file, PR, or repo path]"
---

# Code Review Pipeline

You are running the Maycrest Group's code quality gauntlet. Three specialists, zero mercy. The user has pointed you at code that needs review.

## Stage 1: Architecture & Code Quality Review

Invoke the `maycrest-automate:senior-developer` skill. Deep review:
- Code structure and organization (does it make sense to a future dev?)
- Design patterns — appropriate use, or pattern-for-the-sake-of-pattern?
- SOLID principles adherence
- Naming conventions and readability
- Error handling strategy (or lack thereof)
- Test coverage assessment
- Technical debt identification
- DRY violations and abstraction opportunities

Rate: **Architecture Score** (1-10) with justification.

## Stage 2: Security Review

Invoke the `maycrest-automate:security-engineer` skill. Find the holes:
- Input validation and sanitization
- Authentication and authorization logic
- SQL injection, XSS, CSRF vectors
- Secrets management (hardcoded keys, env leaks)
- Dependency vulnerabilities (known CVEs)
- Data exposure risks (logs, error messages, API responses)
- OWASP Top 10 mapping for any findings

Rate: **Security Score** (1-10) with justification.

## Stage 3: Performance Audit

Invoke the `maycrest-ops:performance-benchmarker` skill. Measure the weight:
- Algorithm complexity (Big O analysis on hot paths)
- Database query efficiency (N+1s, missing indexes, full scans)
- Memory usage patterns and potential leaks
- Bundle size impact (frontend)
- Caching opportunities missed
- Concurrency and race condition risks
- API response time projections

Rate: **Performance Score** (1-10) with justification.

## Stage 4: Consolidated Report

### Summary Scorecard

| Dimension | Score | Critical Issues | Warnings |
|-----------|-------|-----------------|----------|
| Architecture | /10 | | |
| Security | /10 | | |
| Performance | /10 | | |
| **Overall** | /10 | | |

### Verdict
- **SHIP IT** (8+ overall, no critical issues)
- **FIX AND SHIP** (6-7 overall, critical issues identified)
- **REWORK** (below 6, structural problems)

### Priority Fixes
Numbered list of changes required before merge, ordered by severity.

### Nice-to-Haves
Improvements that aren't blocking but would level up the code.

The gauntlet doesn't lie. If the code's good, it'll pass. If not, better to know now.
