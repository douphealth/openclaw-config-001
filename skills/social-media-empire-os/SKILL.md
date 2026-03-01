---
name: social-media-empire-os
description: Enterprise-grade autonomous social media pipeline for OpenClaw. Monitors RSS, extracts high-value keyword-entities, validates demand/competition, generates platform-native content + creative briefs, and prepares/schedules publishing payloads for Publer/Canva with strict quality, budget, and safety controls.
---

# Social Media Empire OS

Run chain: **Ingest -> Select -> Validate -> Generate -> Design -> Schedule -> Verify -> Report**.

## 0) Secrets + config gate (mandatory)
Use `.secrets/social-media-empire.env` (chmod 600) with:
- PUBLER_API_KEY
- CANVA_CLIENT_ID
- CANVA_CLIENT_SECRET
- BLOG_RSS_URLS (comma-separated)
- BRAND_NAME
- BRAND_WEBSITE
- SOCIAL_MAX_DAILY_POSTS
- SOCIAL_API_DAILY_BUDGET_CALLS

Run: `scripts/social_pipeline_config_check.py`

## 1) RSS ingestion
- Pull all configured feeds
- dedup against state file
- trigger only new posts

Scripts:
- `scripts/social_rss_dedupe.py`

## 2) Keyword/entity selection
- extract candidates from content
- score by demand, competition, viral potential, semantic relevance, evergreen
- keep winner + top 5 runners-up

Script:
- `scripts/social_keyword_score.py`

## 3) Live validation
- demand query checks
- social saturation checks
- trending checks
- top-3 SERP gap extraction + top20 missing terms/entities integration for stronger hooks/captions

## 4) Platform-native generation
Generate separate packs for:
- Facebook
- Instagram carousel
- Google Business Profile
- Pinterest

Script:
- `scripts/social_post_pack_generator.py`

## 5) Visual system (Canva-ready)
- platform-specific dimensions and text overlay rules
- image prompt quality and accessibility constraints

Reference:
- `references/platform-specs.md`

## 6) Publish payload + guard
- prepare Publer-compatible payload object
- validate required fields/limits before publish

Script:
- `scripts/social_publish_guard.py`

## 7) Scheduling strategy
- stagger posts (never all at same time)
- platform-optimal windows
- enforce daily caps and reserve headroom

## 8) Quality bar
- human tone, no robotic filler
- no fabricated claims/statistics
- contextual, rich keyword/entity use (natural, non-spam)
- final pass gate required before publishing

## 9) Output contract
1. new posts detected
2. winner keyword + runners-up + validation notes
3. platform content bundle
4. canva creative brief bundle
5. publer payload bundle
6. publish guard report
