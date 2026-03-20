---
name: seo-intelligence
description: "Enterprise SEO intelligence via Google Search Console + Bing Webmaster Tools APIs. Use when pulling search performance data, diagnosing indexation issues, finding ranking opportunities, analyzing query/page performance, boosting GEO/AEO/AI visibility, optimizing crawl budget, or building data-driven SEO strategies. Triggers on GSC data, Bing WMT analysis, indexation fixes, ranking opportunities, crawl optimization, or AI visibility boost."
---

# SEO Intelligence — GSC + Bing WMT Data-Driven Optimization

## Purpose
Pull real search data from Google Search Console and Bing Webmaster Tools to diagnose issues, find opportunities, and drive organic traffic growth with surgical precision.

## When to Use
- Pull search performance data (queries, pages, CTR, impressions)
- Diagnose indexation issues (coverage errors, excluded pages)
- Find ranking opportunities (high impressions, low CTR)
- Analyze which queries/pages need optimization
- Boost GEO (Generative Engine Optimization) and AEO (Answer Engine Optimization)
- Improve AI visibility (structure content for AI parsing)
- Optimize crawl budget and submission
- Track ranking changes over time

**Do NOT use for:** On-page content editing (→ `editorial-post-enhancement`), WordPress operations (→ `wp-rest-api-mastery`), site-wide SEO audit (→ `seo-audit-playbook`).

## SOTA Intelligence Upgrade Layer
- Pair query/page data with `../../skills/shared/references/seo-aeo-geo-superpowers.md`.
- Turn high-impression queries into prompt clusters, FAQ opportunities, answer-block opportunities, and AI-citation targets.
- For low-CTR or near-page-1 pages, distinguish whether the needed fix is CTR/snippet, content depth, extractability, entity trust, or intent alignment.
- Use `../../skills/shared/references/ai-citation-scorecard.md` when a page needs deeper rewrite prioritization.

## Triage Protocol
Before ANY SEO intelligence task:
1. **Identify data source** — GSC API, Bing WMT API, or both?
2. **Check credentials** — Verify API access works (test call)
3. **Define date range** — Last 7/28/90 days? Custom range?
4. **Set dimensions** — Query? Page? Country? Device?
5. **Plan action** — What will you DO with the data?

## Inputs Required (Pre-Flight)
1. **Site URL** — Verified property in GSC/Bing WMT
2. **API credentials** — GSC service account JSON or OAuth token; Bing API key
3. **Date range** — Analysis period (default: last 28 days)
4. **Dimensions** — What to group by (query, page, country, device)
5. **Row limit** — How many rows to return (default: 1000)

## Phase 1: Google Search Console API

### Setup
```python
# Install: pip install google-api-python-client google-auth
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
credentials = service_account.Credentials.from_service_account_file(
    'path/to/service-account.json', scopes=SCOPES)
service = build('searchconsole', 'v1', credentials=credentials)
```

### Authentication Options
| Method | Best For | Setup |
|--------|----------|-------|
| **Service Account** | Server/automated scripts | Create in GCP Console, download JSON key, add as user in GSC |
| **OAuth2** | Interactive apps | Client ID + Secret, user consent flow |
| **Domain Verification** | Full site access | DNS TXT record or HTML file upload |

### Core API Endpoints

#### Search Analytics (Performance Data)
```python
def get_search_analytics(site_url, start_date, end_date, dimensions=None, row_limit=1000):
    """Pull search performance data from GSC."""
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': dimensions or ['query'],
        'rowLimit': row_limit,
        'dataState': 'final'  # Use 'all' for fresh data (may change)
    }
    response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
    return response.get('rows', [])

# Example: Top queries by clicks
rows = get_search_analytics('https://example.com', '2026-02-01', '2026-03-17', ['query'])
for row in rows:
    print(f"{row['keys'][0]}: clicks={row['clicks']}, impressions={row['impressions']}, ctr={row['ctr']:.2%}, position={row['position']:.1f}")
```

#### URL Inspection
```python
def inspect_url(site_url, inspection_url):
    """Check indexation status of a specific URL."""
    request = {
        'inspectionUrl': inspection_url,
        'siteUrl': site_url
    }
    response = service.urlInspection().index().inspect(body=request).execute()
    result = response.get('inspectionResult', {})
    
    index_status = result.get('indexStatusResult', {})
    return {
        'verdict': index_status.get('verdict'),  # PASS, PARTIAL, FAIL, NEUTRAL
        'coverage': index_status.get('coverageState'),  # Submitted and indexed, etc.
        'robots': index_status.get('robotsTxtState'),
        'indexing': index_status.get('indexingState'),  # INDEXING_ALLOWED, INDEXING_NOT_ALLOWED
        'last_crawl': index_status.get('lastCrawlTime'),
        'canonical': index_status.get('googleCanonical'),
        'user_canonical': index_status.get('userCanonical'),
        'page_fetch': index_status.get('pageFetchState'),
        'sitemap': index_status.get('sitemap'),
        'referring_urls': index_status.get('referringUrls', [])
    }
```

#### Sitemaps
```python
def list_sitemaps(site_url):
    """List all submitted sitemaps."""
    response = service.sitemaps().list(siteUrl=site_url).execute()
    return response.get('sitemap', [])

def submit_sitemap(site_url, sitemap_url):
    """Submit a sitemap for indexing."""
    service.sitemaps().submit(siteUrl=site_url, feedpath=sitemap_url).execute()
```

#### Index Coverage (via Search Analytics by page)
```python
def get_indexed_pages(site_url, start_date, end_date):
    """Get all pages that received impressions (indexed and ranking)."""
    rows = get_search_analytics(site_url, start_date, end_date, ['page'], 25000)
    return [{
        'url': row['keys'][0],
        'clicks': row['clicks'],
        'impressions': row['impressions'],
        'ctr': row['ctr'],
        'position': row['position']
    } for row in rows]
```

### GSC Data Analysis Patterns

#### 1. High Opportunity Queries (High Impressions, Low CTR)
```python
def find_ctr_opportunities(rows, min_impressions=100, max_ctr=0.02):
    """Find queries with high impressions but low CTR — quick wins."""
    opportunities = []
    for row in rows:
        if row['impressions'] >= min_impressions and row['ctr'] <= max_ctr:
            opportunities.append({
                'query': row['keys'][0],
                'impressions': row['impressions'],
                'clicks': row['clicks'],
                'ctr': row['ctr'],
                'position': row['position'],
                'potential_clicks': int(row['impressions'] * 0.05) - row['clicks']  # If CTR improved to 5%
            })
    return sorted(opportunities, key=lambda x: x['potential_clicks'], reverse=True)
```

#### 2. Ranking Opportunities (Position 5-15)
```python
def find_ranking_opportunities(rows, min_pos=5, max_pos=15, min_impressions=50):
    """Find queries ranking on page 2-3 that could reach page 1."""
    return [{
        'query': row['keys'][0],
        'position': row['position'],
        'impressions': row['impressions'],
        'clicks': row['clicks'],
        'page': None  # Need cross-dimension analysis to find the page
    } for row in rows if min_pos <= row['position'] <= max_pos and row['impressions'] >= min_impressions]
```

#### 3. Declining Pages (Traffic Loss Detection)
```python
def find_declining_pages(current_rows, previous_rows):
    """Compare two periods to find pages losing traffic."""
    prev_map = {r['keys'][0]: r for r in previous_rows}
    declining = []
    for row in current_rows:
        page = row['keys'][0]
        if page in prev_map:
            prev = prev_map[page]
            click_change = row['clicks'] - prev['clicks']
            if click_change < -10:  # Lost more than 10 clicks
                declining.append({
                    'page': page,
                    'current_clicks': row['clicks'],
                    'previous_clicks': prev['clicks'],
                    'change': click_change,
                    'change_pct': click_change / max(prev['clicks'], 1) * 100
                })
    return sorted(declining, key=lambda x: x['change'])
```

#### 4. Non-Indexed Pages Discovery
```python
def find_non_indexed_pages(site_url, all_post_urls, start_date, end_date):
    """Find pages in WordPress that aren't indexed (no impressions)."""
    indexed = get_indexed_pages(site_url, start_date, end_date)
    indexed_urls = {p['url'] for p in indexed}
    return [url for url in all_post_urls if url not in indexed_urls]
```

## Phase 2: Bing Webmaster Tools API

### Setup
```python
import requests

BING_API_BASE = 'https://www.bing.com/webmaster/api.svc/json'
API_KEY = 'your-bing-api-key'  # From Bing WMT dashboard

headers = {
    'Content-Type': 'application/json; charset=utf-8'
}

def bing_api(endpoint, params=None):
    """Call Bing Webmaster Tools API."""
    params = params or {}
    params['apikey'] = API_KEY
    response = requests.get(f'{BING_API_BASE}/{endpoint}', params=params, headers=headers)
    return response.json()
```

### Authentication
1. Go to Bing Webmaster Tools → Settings → API Access
2. Copy your API key
3. Store in `.secrets/bing-api-key.txt`

### Core API Endpoints

#### Query Stats (Search Performance)
```python
def get_bing_query_stats(site_url, start_date, end_date, row_limit=1000):
    """Get query performance data from Bing."""
    return bing_api('GetQueryStats', {
        'siteUrl': site_url,
        'startDate': start_date,
        'endDate': end_date,
        'rowLimit': row_limit
    })
```

#### Page Stats
```python
def get_bing_page_stats(site_url, start_date, end_date):
    """Get page-level performance data from Bing."""
    return bing_api('GetPageStats', {
        'siteUrl': site_url,
        'startDate': start_date,
        'endDate': end_date,
        'rowLimit': 1000
    })
```

#### Crawl Stats
```python
def get_bing_crawl_stats(site_url, start_date, end_date):
    """Get crawl statistics from Bing."""
    return bing_api('GetCrawlStats', {
        'siteUrl': site_url,
        'startDate': start_date,
        'endDate': end_date
    })
```

#### URL Traffic
```python
def get_bing_url_traffic(site_url, url):
    """Get traffic data for a specific URL."""
    return bing_api('GetUrlTraffic', {
        'siteUrl': site_url,
        'url': url
    })
```

#### Submit URL for Indexing
```python
def submit_bing_url(site_url, url):
    """Submit a URL for Bing indexing."""
    return bing_api('SubmitUrl', {
        'siteUrl': site_url,
        'url': url
    })
```

#### Get Backlinks
```python
def get_bing_backlinks(site_url, row_limit=1000):
    """Get backlink data from Bing."""
    return bing_api('GetBacklinks', {
        'siteUrl': site_url,
        'rowLimit': row_limit
    })
```

## Phase 3: GEO (Generative Engine Optimization)

### What GEO Optimizes For
AI search engines (Perplexity, ChatGPT Search, Google AI Overview, Bing Copilot) need:

| Signal | Implementation |
|--------|---------------|
| **Clear entity relationships** | Person → Company → Product links |
| **Structured facts** | Declarative sentences with data |
| **Citable statements** | "According to [Source], X% of..." |
| **FAQ structure** | Question → Concise answer → Detail |
| **Schema markup** | Article, FAQPage, Organization, Person |

### GEO Checklist (Every Post)
- [ ] Include 3+ citable statistics with sources
- [ ] Use "According to..." pattern for authority
- [ ] Structure content with clear Q&A sections
- [ ] Add Organization + Person schema
- [ ] Include entity relationships (who, what, where)
- [ ] Use Speakable schema for voice optimization
- [ ] Add fact-based summary at top (TL;DR)

### AI Visibility Schema Stack
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "Article", ...},
    {"@type": "FAQPage", ...},
    {"@type": "BreadcrumbList", ...},
    {"@type": "Organization", "name": "...", "sameAs": ["twitter", "linkedin"]},
    {"@type": "Person", "name": "...", "jobTitle": "...", "sameAs": [...]},
    {"@type": "Speakable", "cssSelector": [".ep-tldr", "h2"]}
  ]
}
</script>
```

## Phase 4: AEO (Answer Engine Optimization)

### Answer Box Targeting
- **Format questions as H2/H3**: "How do I fix WordPress indexation?"
- **Answer in first sentence**: Direct, 40-60 word answer
- **Then expand**: Details, examples, steps
- **Use lists**: Google pulls lists for featured snippets
- **Use tables**: Comparison data in table format

### People Also Ask (PAA) Mining
```python
def find_paa_opportunities(query):
    """Extract PAA questions for a target keyword."""
    # Use Google SERP scraping or tools like:
    # - AlsoAsked.com API
    # - SERP API (ValueSerp, SerpAPI)
    # - Manual extraction from SERP
    pass
```

### AEO Content Structure
```
H1: Primary keyword question or topic
  TL;DR: 2-3 sentence answer
  H2: What is [Topic]?
    → Direct answer (40-60 words)
    → Detailed explanation
  H2: How to [Do Thing]?
    → Step-by-step list
    → Code/example if applicable
  H2: [Common Question]?
    → Direct answer
    → Supporting details
  FAQ Section: 5-7 questions with schema
```

## Phase 5: Indexation Optimization Workflow

### Step 1: Pull Current State
```python
# Get all indexed pages from GSC
indexed = get_indexed_pages(site_url, '2026-02-17', '2026-03-17')

# Get all posts from WordPress
posts = wp_get_all_posts(site_url)  # Via REST API

# Find non-indexed pages
non_indexed = find_non_indexed_pages(site_url, posts, '2026-02-17', '2026-03-17')
```

### Step 2: Diagnose Non-Indexed Pages
For each non-indexed URL:
1. **URL Inspection** — Check coverage state, robots.txt, canonical
2. **Content Quality** — Is content thin (<500 words)?
3. **Internal Links** — Is the page orphaned?
4. **Duplicate Content** — Does another page target same keyword?
5. **Crawl Errors** — Is the page returning errors?

### Step 3: Fix and Submit
1. Fix technical issues (canonicals, robots, redirects)
2. Improve thin content
3. Add internal links from high-authority pages
4. Submit URL to GSC for indexing
5. Submit URL to Bing for indexing
6. Wait 24-48 hours, re-check status

### Step 4: Monitor
```python
# Track indexing progress over time
def monitor_indexing(site_url, urls_to_track):
    """Check indexing status of specific URLs."""
    results = []
    for url in urls_to_track:
        status = inspect_url(site_url, url)
        results.append({
            'url': url,
            'indexed': status['coverage'] == 'Submitted and indexed',
            'issues': status['coverage'] if status['coverage'] != 'Submitted and indexed' else None
        })
    return results
```

## Speed Optimizations

### API Performance
- **GSC API**: Rate limit 1200 requests/day, use batch where possible
- **Bing WMT API**: Rate limit 10,000 requests/day, more generous
- **Parallel calls**: Use `concurrent.futures` for multiple URL inspections
- **Cache results**: Store API responses for 24h (data doesn't change often)
- **Batch date ranges**: Pull 90-day range once vs 30-day range 3x

### Data Caching Strategy
```python
# Cache API responses to avoid redundant calls
import json, os
from datetime import datetime, timedelta

CACHE_DIR = 'cache/seo-intelligence/'
os.makedirs(CACHE_DIR, exist_ok=True)

def cached_api_call(cache_key, api_func, ttl_hours=24):
    """Cache API responses for TTL hours."""
    cache_file = os.path.join(CACHE_DIR, f'{cache_key}.json')
    if os.path.exists(cache_file):
        mtime = datetime.fromtimestamp(os.path.getmtime(cache_file))
        if datetime.now() - mtime < timedelta(hours=ttl_hours):
            with open(cache_file) as f:
                return json.load(f)
    result = api_func()
    with open(cache_file, 'w') as f:
        json.dump(result, f)
    return result
```

## Error Recovery (Auto-Learning)
- **GSC 403**: Re-authenticate or add service account as GSC user
- **Bing 401**: API key expired, regenerate in Bing WMT dashboard
- **Rate limit hit**: Wait and retry, reduce batch size
- **Empty data**: Property not verified or no data in date range
- **Track patterns**: Log errors to memory/YYYY-MM-DD.md

## Self-Critique Scorecard (/25)
1. **Data** (1-5): Was GSC/Bing data pulled and analyzed correctly?
2. **Insights** (1-5): Were actionable opportunities identified?
3. **GEO/AEO** (1-5): Is content optimized for AI search engines?
4. **Indexation** (1-5): Were non-indexed pages diagnosed and fixed?
5. **Monitoring** (1-5): Is tracking in place for ongoing measurement?

**Target: 22+/25**

## Output Contract
- **Artifact**: SEO intelligence report with data, opportunities, and action items
- **Evidence**: GSC/Bing API data with specific queries, pages, and metrics
- **Decision**: Top 3-5 actionable recommendations with expected impact
- **Next**: Implement fixes, submit for indexing, monitor for 7-14 days

## Anti-Patterns
- ❌ Pulling data without a clear action plan
- ❌ Optimizing for keywords with zero search volume
- ❌ Ignoring Bing (30%+ of search market)
- ❌ Not monitoring after fixes (submit and forget)
- ❌ Over-optimizing meta tags (keyword stuffing)
- ❌ Ignoring GEO/AEO (AI search is the future)
- ❌ Not caching API results (wastes rate limit)

## Compatibility
- Google Search Console API v1 (requires service account or OAuth2)
- Bing Webmaster Tools API v2 (requires API key)
- Python 3.8+ with google-api-python-client, requests
- Rate limits: GSC 1200/day, Bing 10000/day
