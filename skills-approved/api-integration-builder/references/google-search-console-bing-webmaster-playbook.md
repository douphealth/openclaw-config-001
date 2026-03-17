# Google Search Console + Bing Webmaster Playbook

Use this playbook when wiring OpenClaw skills to real search-visibility data.
The goal is not "more dashboards" — it's giving SEO/content/WordPress skills trustworthy inputs for indexation, CTR, ranking, query, and page-level decisions.

## Why this matters
Without GSC/Bing data, SEO work drifts into guesswork.
These sources provide the closest thing to ground truth for:
- indexation and sitemap visibility
- queries and pages actually getting impressions/clicks
- CTR opportunities
- device/country splits
- crawl and submission signals
- Bing-specific coverage and discovery signals Google does not show

## Integration modes
Choose the smallest reliable mode that works:

### Mode A — Direct API (best)
Use when credentials are available and stable.
- **Google Search Console API**
  - Endpoint pattern: `POST https://www.googleapis.com/webmaster-tools/v3/sites/{siteUrl}/searchAnalytics/query`
  - Auth: OAuth2 service account or OAuth user flow; service account must be granted property access
- **Bing Webmaster API**
  - Endpoint pattern: `https://ssl.bing.com/webmaster/api.svc/json/{METHOD_NAME}?apikey={API_KEY}`
  - Auth: Bing Webmaster API key (or OAuth where supported)

### Mode B — Export ingest (good fallback)
Use CSV/XLSX/JSON exports from GSC and Bing Webmaster Tools when API auth is not yet ready.
This is still valid because the skills are consuming real platform data.

### Mode C — Hybrid
Use direct API for GSC and export ingest for Bing, or vice versa, until both are fully wired.

## Secret storage rules
Never hardcode credentials.
Store in one of these:
- `C:\Users\User\.openclaw\workspace\.secrets\search\google-service-account.json`
- `C:\Users\User\.openclaw\workspace\.secrets\search\bing-webmaster.json`
- `C:\Users\User\.openclaw\.env` with `${ENV_VAR}` references in config/scripts

Suggested env names:
- `GSC_SERVICE_ACCOUNT_JSON`
- `GSC_PROPERTY_URL`
- `BING_WEBMASTER_API_KEY`
- `BING_SITE_URL`

## Minimum data pack every SEO/content skill should request
For a target site and date range, fetch or ingest:

### From Google Search Console
1. **Query × Page performance**
   - dimensions: `query`, `page`
   - metrics: clicks, impressions, ctr, position
2. **Page performance**
   - dimensions: `page`
   - metrics: clicks, impressions, ctr, position
3. **Query performance**
   - dimensions: `query`
   - metrics: clicks, impressions, ctr, position
4. **Country split** (when geo SEO matters)
   - dimensions: `page`, `country`
5. **Device split**
   - dimensions: `page`, `device`
6. **Fresh/partial data** when recency matters
   - `dataState=all`
7. **Sitemap status**
   - submitted sitemap list and latest status

### From Bing Webmaster Tools
1. **Query performance / keyword stats**
2. **Page/url performance**
3. **Crawl/indexation/site scan signals**
4. **Sitemap submission status**
5. **Inbound link / linking page signals** where relevant
6. **URL submission / discovery signals** when indexation is the problem

## Normalized output schema
Every integration should normalize both sources into one shared structure.
Save in JSON or CSV with these canonical fields:

```json
{
  "source": "gsc|bing",
  "site": "https://example.com/",
  "date_start": "2026-02-16",
  "date_end": "2026-03-16",
  "page": "https://example.com/post/",
  "query": "best crm for startups",
  "country": "usa",
  "device": "mobile",
  "clicks": 120,
  "impressions": 4300,
  "ctr": 0.0279,
  "position": 8.4,
  "notes": "optional provider-specific fields"
}
```

## Search visibility data pack
For each site, prepare a compact data pack under:
- `ops/search-data/<site-slug>/gsc-queries.csv`
- `ops/search-data/<site-slug>/gsc-pages.csv`
- `ops/search-data/<site-slug>/gsc-page-query.csv`
- `ops/search-data/<site-slug>/bing-queries.csv`
- `ops/search-data/<site-slug>/bing-pages.csv`
- `ops/search-data/<site-slug>/sitemaps.json`
- `ops/search-data/<site-slug>/summary.json`

### summary.json should include
```json
{
  "site": "https://example.com/",
  "range": "last_28_days",
  "gsc": {
    "total_clicks": 12034,
    "total_impressions": 420330,
    "avg_ctr": 0.0286,
    "avg_position": 11.2,
    "top_pages_by_clicks": [],
    "top_queries_by_impressions": [],
    "low_ctr_high_impression_pages": [],
    "page2_queries": []
  },
  "bing": {
    "total_clicks": 1890,
    "total_impressions": 64020,
    "top_pages_by_clicks": [],
    "top_queries_by_impressions": [],
    "indexation_signals": [],
    "crawl_issues": []
  }
}
```

## Skill-specific uses

### seo-audit-playbook
Use GSC/Bing to validate:
- real indexation loss
- page-level impression collapse
- query loss after content changes
- CTR underperformance on pages already ranking
- device/country-specific drops

### content-strategy-planning
Use GSC/Bing to find:
- existing pages with page-2 queries worth expanding
- query clusters already partially owned
- low-CTR/high-impression content needing title/meta work
- rising query patterns for new topic creation

### editorial-post-enhancement
Use GSC/Bing to choose:
- which page to optimize first
- which queries/entities are already near page 1
- which query/page pairs need answer-first rewrites or better title/meta

### wordpress-growth-ops
Use GSC/Bing to identify:
- money pages losing impressions due to indexation or performance
- post-update drops tied to rendering/plugin conflicts
- geo/device splits showing UX problems on mobile or specific countries

### monitoring-ops
Use GSC/Bing deltas for alerting:
- clicks down > X%
- impressions down > X%
- CTR down on high-impression pages
- sitemap errors or indexation anomalies

## Decision rules
- Do **not** claim indexation problems from crawl guesses alone when GSC/Bing data exists.
- Do **not** prioritize content rewrites before checking whether impressions already exist.
- Do **not** call a title/meta change successful without comparing CTR before/after in GSC/Bing.
- Do **not** assume Google behavior fully represents Bing behavior.

## Verification checklist
The integration is only "done" when you have proof of at least one real data path:
- authenticated GSC request or imported GSC export successfully parsed
- authenticated Bing request or imported Bing export successfully parsed
- normalized files written to `ops/search-data/<site-slug>/`
- at least one SEO/content skill can consume the summary and produce a better decision

## Common mistakes
- granting GSC service account no property access
- mixing URL-prefix and domain-property formats incorrectly
- forgetting date-range consistency between GSC and Bing pulls
- comparing GSC page data to Bing query data without normalization
- treating avg position as exact rank instead of an aggregate signal
- making CTR decisions on tiny-impression queries
- ignoring Bing because traffic share is smaller
