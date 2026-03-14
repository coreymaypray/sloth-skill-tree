---
name: performance-sweep
description: "System optimization from benchmarks to infrastructure tuning to monitoring. Find the bottlenecks, fix them, prove it. Usage: /performance-sweep [system or application]"
---

# Performance Sweep

You are running the Cyber Sloth Empire's performance optimization pipeline. Three stages: measure, optimize, monitor. No guessing, no premature optimization — data drives every decision. The user has a system to speed up.

## Stage 1: Performance Benchmarking

Invoke the `cyber-sloth-testing:performance-benchmarker` skill. Measure everything:
- Response time profiling (P50, P95, P99 for key endpoints/screens)
- Database query performance audit (slow queries, missing indexes, N+1 patterns)
- Frontend performance metrics (LCP, FID, CLS, TTI, bundle size)
- Memory usage patterns and potential leaks
- CPU utilization under load
- Network waterfall analysis (what loads, in what order, how big)
- Throughput capacity testing (requests/second before degradation)
- Identify the top 5 bottlenecks by impact

Deliver: **Performance Baseline Report** with current metrics and bottleneck ranking.

## Stage 2: Infrastructure Optimization

Invoke the `cyber-sloth-engineering:devops-automator` skill. Fix the plumbing:
- Caching strategy implementation (CDN, application cache, database cache)
- Database optimization (query rewriting, index tuning, connection pooling)
- Asset optimization (compression, lazy loading, code splitting)
- Server/serverless configuration tuning
- Network optimization (HTTP/2, preloading, edge deployment)
- Auto-scaling configuration (if applicable)
- Cost-performance tradeoff analysis (are we overpaying for resources?)

For each optimization: expected improvement, implementation effort, and risk level.

## Stage 3: Monitoring Implementation

Invoke the `cyber-sloth-support:infra-maintainer` skill. Build visibility:
- Performance monitoring dashboard design
- Alert thresholds for key metrics (when should someone wake up?)
- Automated performance regression detection
- Log aggregation and query performance tracking
- Uptime monitoring and status page setup
- Capacity planning projections (when will we need to scale?)
- Runbook for common performance incidents

## Output

### Performance Sweep Report

#### Before/After Scorecard

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| P95 Response Time | | | |
| LCP | | | |
| Database Query Avg | | | |
| Bundle Size | | | |
| Memory Usage | | | |
| Throughput (rps) | | | |

#### Optimizations Applied
Numbered list of every change made, with measured impact.

#### Monitoring Setup
- Dashboard link/configuration
- Alert rules configured
- Escalation procedures

#### Remaining Opportunities
Optimizations identified but not yet applied, prioritized by impact.

#### Maintenance Schedule
Recommended cadence for performance reviews going forward.

The Cyber Sloth Empire moves slow on purpose — our systems don't have that luxury. Make it fast.
