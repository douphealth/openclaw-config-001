---
name: monitoring-ops
description: Monitoring and alerting operations for search rankings, uptime, brand mentions, competitor intelligence, multisite watchdog checks, OctoLens-based monitoring, social listening, and technical health review. Use when a user asks to track keyword movements, watch site availability, monitor brands or competitors, aggregate health across multiple sites, detect technical risk signals, or define actionable alert thresholds.
---

# Monitoring Ops
Track rankings, uptime, mentions, competitive intel, site health.

## WHEN
Rank tracking, uptime, brand mentions, competitor alerts, multisite watchdog, social monitoring, OctoLens, technical health

**Do NOT use this skill for:** SEO auditing or ranking diagnosis (→ `seo-audit-playbook`), tracking implementation or tag debugging (→ `tracking-measurement`).

## OPS
- Rank: keywords by domains to positions to daily delta to alert drop over 3
- OctoLens: GitHub/social/web monitoring, competitive intel, trends, alerts
- Multisite: iterate sites, health check each, aggregate, alert issues
- Technical: response time, SSL expiry, DNS, CDN, error rates
- Social: brand/keyword mentions, sentiment, volume trends, engagement

## ALERTS
Triggers: rank drop over 3, uptime under 99.5%, SSL expiry under 14d, mention spike over 2 sigma. Output: severity plus asset plus action.


## Output Contract
**Artifact**: Monitoring dashboard or alert configuration
**Evidence**: Alert firing test, escalation path verified
**Decision**: Monitoring active
**Next**: Review alert quality after 1 week
