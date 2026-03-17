---
name: monitoring-ops
description: Use when designing or operating uptime checks, technical health monitors, ranking watchlists, multisite watchdogs, mention monitoring, competitor intelligence, or actionable alert thresholds that should feed reliable operational alerts.
---

# Monitoring Ops

## Purpose
Design and operate monitoring systems that detect meaningful change, surface actionable issues, and feed reliable alerting without drowning the operator in noise.

## Use this when
- tracking site uptime, response health, SSL expiry, DNS, or technical availability
- watching keyword positions or ranking deltas over time
- monitoring brand mentions, competitor signals, or trend spikes
- aggregating health across multiple sites or assets
- defining thresholds, severity logic, or watchdog checks
- setting up OctoLens, UptimeRobot, Pingdom, or custom monitoring

## Do NOT use this for
- one-off SEO diagnosis or ranking explanation (→ `seo-audit-playbook`)
- tag/debug measurement implementation work (→ `tracking-measurement`)
- delivery-routing-only work where the monitor already exists (→ `notification-engine`)
- designing alert escalation chains (→ `notification-engine`)

## Do this

### 1. Define assets to monitor
List every asset (site, domain, service) and its criticality level. Not everything needs the same monitoring intensity.

### 2. Select monitor categories

| Category | What to watch | Example thresholds |
|---|---|---|
| Uptime / availability | HTTP status, latency, failures | Down >1min, repeated 5xx, latency >3s |
| Technical health | SSL expiry, DNS records, CDN, error rate | SSL <14 days, DNS mismatch, CDN failure |
| Search visibility | GSC/Bing clicks, impressions, CTR, page-two opportunities, sitemap/indexation anomalies | Clicks down >20%, CTR <2% on page-one pages, batch indexation drop |
| Rankings | daily/weekly deltas on priority keywords | Drop >3 positions on top-10 keywords |
| Mentions / social | volume spikes, sentiment shifts, competitor events | Spike >2 sigma, unusual negative surge |
| Multisite watchdog | aggregated health across portfolio | Any critical asset degraded |

### 3. Define thresholds and severity
For each monitor, define:
- **Warning threshold:** degraded but not critical (e.g., SSL <30 days, ranking drop 2-3 positions)
- **Critical threshold:** immediate action needed (e.g., site down, SSL <3 days, ranking drop >5 positions)
- **Baseline:** what "normal" looks for this metric

### 4. Set review cadence
- Real-time (uptime, error rates)
- Daily (rankings, traffic anomalies)
- Weekly (trend analysis, mention volume)
- Monthly (SSL expiry horizon, comprehensive health review)

### 5. Prove the alert path
Don't just configure the monitor — fire a test alert and confirm it arrives. Connect to `notification-engine` for escalation design.

### 6. Tune for signal over noise
- If a monitor fires more than 3x/week, the threshold is wrong or the monitor is decorative
- Archive monitors that nobody acts on
- Review monthly: is this monitor still serving a decision?

## Example: Multi-site WordPress portfolio monitoring

**Assets:** 9 WordPress sites, mixed criticality

**Configuration:**
| Site | Criticality | Uptime check | SSL check | Ranking watch | Error rate |
|---|---|---|---|---|---|
| affiliatesite1.com | High | 1 min interval | 30d warning, 7d critical | Top 20 keywords, daily | 5xx > 2% for 5 min |
| affiliatesite2.com | High | 1 min interval | 30d warning, 7d critical | Top 15 keywords, daily | 5xx > 2% for 5 min |
| smallersite.com | Low | 5 min interval | 14d warning, 3d critical | Top 5 keywords, weekly | None |

**Test procedure:**
1. Trigger artificial 503 on staging endpoint → confirm uptime monitor fires within 2 min
2. Confirm alert arrives in notification channel (Telegram)
3. Simulate SSL expiry <7 days → confirm critical alert fires
4. Simulate ranking drop of 4 positions → confirm warning alert fires

## Alert output format
Every meaningful monitor should be able to state:
- **Asset:** which site/service
- **Metric or event:** what changed
- **Threshold crossed:** which boundary
- **Severity:** info / warn / critical
- **Likely action:** what the operator should do

## Resources
- `references/monitoring-thresholds-template.md` — standard threshold configurations by site type
- Workspace `TOOLS.md` — site inventory and infrastructure notes
- Platform docs: UptimeRobot API, Pingdom, Google Search Console API

## Checks and common mistakes
- Monitoring metrics that nobody will act on (decorative monitors)
- Setting thresholds with no severity logic (everything is "alert")
- Noisy monitors that fire too often → operator learns to ignore them
- No proof that alerts actually arrive (configure without testing)
- Mixing SEO diagnosis into monitoring operations (keep them separate)
- Forgetting to update monitors when site inventory changes

## Output contract
**Artifact:** Monitoring plan or watchdog configuration with assets, thresholds, and cadence
**Evidence:** At least one test alert fired and confirmed received; threshold values documented per asset
**Decision:** Monitoring active and tuned, needs alert-routing setup (→ `notification-engine`), or blocked
**Next:** Connect to notification channels, tune thresholds after 1-week baseline, review monthly
