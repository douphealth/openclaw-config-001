# Monitoring Thresholds Template

Standard threshold configurations by site/service type. Customize per asset criticality.

## Uptime Monitoring

| Interval | Criticality | Check frequency | Down threshold | Latency threshold |
|---|---|---|---|---|
| High (revenue site) | Critical | 1 min | >1 min down | >3s response |
| Medium (content site) | Warning | 2 min | >3 min down | >5s response |
| Low (portfolio/legacy) | Info | 5 min | >10 min down | >10s response |

## SSL Certificate

| Days remaining | Severity | Action |
|---|---|---|
| <30 days | Warning | Schedule renewal |
| <14 days | Warning (escalating) | Renew immediately |
| <7 days | Critical | Emergency renewal |
| <3 days | Critical + escalation | Manual intervention |

## DNS Health

| Check | Threshold | Severity |
|---|---|---|
| A record mismatch | Any deviation from expected IP | Critical |
| Nameserver change | Unplanned NS modification | Critical |
| TTL anomaly | TTL <60s or >86400s without reason | Warning |
| Propagation failure | Not propagated within expected window | Warning |

## Ranking Monitoring

| Keyword position | Drop threshold | Severity | Action |
|---|---|---|---|
| Position 1-3 | Drop >2 positions | Critical | Investigate immediately |
| Position 4-10 | Drop >3 positions | Warning | Check SERP changes, competitors |
| Position 11-20 | Drop >5 positions | Info | Monitor trend |
| Position 21+ | Drop >10 positions | Info | Log only |

## Error Rate

| Metric | Warning | Critical |
|---|---|---|
| HTTP 5xx rate | >1% for 5 min | >5% for 3 min |
| HTTP 4xx rate | >5% for 10 min | >15% for 5 min |
| Page load (p95) | >4s | >8s |
| Database query time (p95) | >500ms | >2s |

## Multisite Watchdog

For portfolio monitoring, define per-site criticality:

```yaml
sites:
  - domain: revenue-site.com
    criticality: high
    checks: [uptime, ssl, rankings, error-rate]
    uptime_interval: 1min
  - domain: content-site.com
    criticality: medium
    checks: [uptime, ssl, rankings]
    uptime_interval: 2min
  - domain: legacy-site.com
    criticality: low
    checks: [uptime]
    uptime_interval: 5min
```
