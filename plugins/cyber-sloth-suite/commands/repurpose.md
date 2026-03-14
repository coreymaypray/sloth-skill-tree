---
name: repurpose
description: "Generate hooks, video scripts, and platform captions from existing content. Usage: /repurpose [text or paste content]"
---

# Content Repurpose Engine

You are repurposing existing content for Corey Maypray across multiple platforms. The user has provided source text (a tweet, LinkedIn post, article excerpt, or thread).

## Step 1: Extract Core Insight
Identify the single strongest idea in the source content. State it in one sentence.

## Step 2: Hooks (5 variations)
Invoke `cyber-sloth-suite:hook-writing` skill. Generate 5 hooks optimized for:
- LinkedIn (x2)
- X/Twitter (x2)
- TikTok/Reels (x1)

## Step 3: Video Scripts
Invoke `cyber-sloth-suite:tweet-to-short` skill. Create:
- 15-second quick hit (TikTok/Reel)
- 30-second standard (TikTok/Reel)
- 60-second deep dive (YouTube Short)

## Step 4: Platform Captions
Write ready-to-post captions for:
- **LinkedIn**: Professional, insight-driven, 150-300 words, with hashtags
- **X/Twitter**: Punchy, under 280 chars, with thread option if needed
- **Instagram**: Conversational, emoji-light, with hashtag block
- **TikTok**: Hook-first caption, trending hashtags

## Output
Present each deliverable under clear headers. End with a content calendar suggestion (which platform to post on which day).
