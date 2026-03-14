---
name: content-pipeline
description: "Full content funnel: hooks, article, and video scripts from a single topic. Usage: /content-pipeline [topic]"
---

# Content Pipeline

You are running the full Cyber Sloth content pipeline for Corey Maypray. The user has provided a topic. Execute the following stages in order:

## Stage 1: Hooks
Invoke the `cyber-sloth-suite:hook-writing` skill. Generate 10 hooks for the given topic across LinkedIn, X, and TikTok/Reels. Present the top 3 picks.

## Stage 2: Article
Invoke the `cyber-sloth-suite:article-writer` skill. Write a full article (800-1500 words) using the strongest hook as the opener. Default to the Nexus voice unless the topic clearly fits Cyber Sloth Empire or Personal.

## Stage 3: Video Scripts
Invoke the `cyber-sloth-suite:tweet-to-short` skill. Convert the article's key insight into:
1. A 30-second TikTok/Reel script
2. A 60-second YouTube Short script

## Output
Present all three deliverables clearly separated with headers. End with a summary of suggested hashtags and posting schedule.
