# plantastichaven.com — Recovery Pack

## Stack
- WordPress + LiteSpeed + Cloudflare + CyberPanel

## Known Failure Modes
- origin HTTPS instability / timeout behavior
- partial REST saves during unstable periods
- duplicate Link Whisper related-post blocks in raw content + render-time duplicates
- duplicated embeds/tables/FAQ blocks after repeated save waves
- full HTML documents embedded in body content on some posts
- embedded article/header/H1 wrappers inside post body

## Safe Recovery Pattern
1. confirm site health
2. back up affected posts
3. diagnose raw duplication vs render-time duplication
4. remove saved raw duplicate blocks first
5. canary repair 1 post
6. verify live render
7. proceed in small waves only

## Stop Conditions
- 3 consecutive transport failures
- live site health check fails twice in a row
- duplicate counts do not fall after canary repair
- repaired post loses canonical/title/meta/H1 integrity

## High-Value Verification Checks
- live page returns 200 quickly
- H1 count = 1
- Related Posts visible count <= 1
- no `<!DOCTYPE html>` / `<html>` / `<body>` embedded inside content
- canonical and title still present

## Backup Location
- `ops/backups/ph-posts/`
- `ops/backups/ph-structural-fixes/`

## Best Skill Chain
`failure-recovery-director` → `content-integrity-cleanup` → `batch-mutation-controller` → `auto-verification`
