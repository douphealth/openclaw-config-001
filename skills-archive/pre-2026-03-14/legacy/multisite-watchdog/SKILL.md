---
name: multisite-watchdog
description: Multi-site regression monitoring for WordPress portfolios. Use when setting or running recurring checks for canonical drift, robots/indexation drift, missing answer blocks, affiliate disclosure regressions, duplicate URLs, and endpoint health.
---

# Multi-site Watchdog

## Scope Ownership
### Own
- Execute Multi-site regression monitoring for WordPress portfolios. Use when setting or running recurring checks for canonical drift, robots/indexation drift, missing answer blocks, affiliate disclosure regressions, duplicate URLs, and endpoint health.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

## Check matrix (per site)
- endpoint health: `/`, `/robots.txt`, `/sitemap_index.xml`, `/wp-json/`
- canonical presence consistency
- answer-block coverage on recent content
- disclosure presence on affiliate pages
- duplicate URL collisions
- sensational-title drift

## Severity model
- `critical`: site unavailable, indexation break, destructive canonical
- `degraded`: cache/render variance or partial mismatch
- `monitor`: non-blocking anomaly

## Output standard
Return:
- pass/fail by check
- severity
- affected URLs
- immediate action recommendation

## Execution rule
Retry failed URLs before declaring regression to reduce false positives.