# Search Visibility Alerts

Use GSC + Bing search-visibility packs to drive SEO alerting with signal-over-noise discipline.

## Core principle
Do not alert on every movement.
Alert only when a change implies a real action.

## Required inputs
Use the normalized pack under `ops/search-data/<site-slug>/summary.json` plus supporting CSVs when available.

## Alert classes

### 1. Traffic-loss alerts
Trigger when:
- total clicks down >20% period-over-period on a priority site
- total impressions down >25% period-over-period on a priority site
- top 3 money pages collectively down >20% clicks

Severity:
- **warn** at 15-20%
- **critical** at >20-30% depending on site importance

### 2. CTR-opportunity alerts
Trigger when:
- page has >1000 impressions and CTR <2% with avg position 3-10
- query has >500 impressions and CTR materially below site baseline

Severity:
- **info** for low-priority pages
- **warn** for money pages or top-cluster pages

### 3. Page-two opportunity alerts
Trigger when:
- query or page-query pair has avg position 4-15 and >200 impressions
- query trend rising while page remains stuck on page 2

Severity:
- **info** by default
- **warn** when the page is tied to a monetization path

### 4. Indexation / sitemap alerts
Trigger when:
- sitemap fetch/parse errors appear in GSC/Bing data
- expected page model sees impression collapse across many pages
- a newly published batch fails to gain impressions after the expected settling window

Severity:
- **warn** for isolated anomalies
- **critical** for portfolio-wide or model-wide drops

### 5. Device / geo split alerts
Trigger when:
- mobile CTR materially underperforms desktop on important pages
- a target country loses impressions or CTR while others remain stable

Severity:
- **warn** when tied to priority revenue markets

## Suggested thresholds by site type

### Affiliate / content sites
- clicks down >20% = warn
- impressions down >25% = warn
- CTR <2% with avg position 3-10 = opportunity alert
- 10+ pages in one model losing impressions = investigate indexation/template issue

### Lead-gen / service sites
- clicks down >15% on primary landing pages = warn
- branded/service pages down >20% = critical
- mobile CTR gap >35% vs desktop on money pages = warn

### Programmatic SEO sites
- indexation rate <80% for recent batch = warn
- >20% of a page model with no impressions after launch window = critical review
- page-two query pool shrinking sharply = investigate template or internal linking changes

## Alert payload format
Every alert should state:
- site
- date range compared
- affected page(s) or model(s)
- metric(s) crossed
- likely interpretation
- suggested next skill

Example:
```json
{
  "site": "https://example.com/",
  "severity": "warn",
  "kind": "ctr_opportunity",
  "range": "last_28_days vs previous_28_days",
  "page": "https://example.com/best-crm/",
  "metric": {
    "impressions": 4200,
    "ctr": 0.014,
    "position": 6.8
  },
  "interpretation": "High-impression page with page-one visibility but weak click capture.",
  "route_to": "editorial-post-enhancement"
}
```

## Skill routing from alerts
- **seo-audit-playbook** → ranking/indexation loss, crawl/model anomalies
- **editorial-post-enhancement** → CTR, title/meta, answer-first, page-two opportunities
- **content-strategy-planning** → cluster expansion and partial-ownership opportunities
- **wordpress-growth-ops** → money pages with traffic-entry loss, device splits, rendering/performance suspicion
- **schema-ops** → rich-result or enhancement-driven CTR opportunities

## Anti-patterns
- alerting on tiny-impression rows
- using avg position alone without clicks/impressions context
- comparing mismatched date windows
- spamming one alert per page instead of batching by site/model
- alerting without a recommended next action
