---
name: seo-content-pipeline
description: "End-to-end SEO content optimization pipeline. Pulls GSC/Bing data, identifies highest-impact opportunities, generates specific optimization plans, and feeds into editorial-post-enhancement for execution. Use when optimizing content for rankings, fixing indexation issues, boosting organic traffic with data-driven decisions, or running site-wide content improvements."
---

# SEO Content Pipeline — Data-Driven Content Optimization

## Purpose
Connect search data (GSC/Bing) to content actions (editorial enhancement) in one seamless pipeline. No guessing — every optimization is backed by real search data.

**This skill is the CONNECTIVE TISSUE** between `seo-intelligence` (data source) and `editorial-post-enhancement` (execution engine).

## When to Use
- Run a site-wide content optimization pass backed by GSC data
- Find the highest-ROI pages to improve right now
- Generate prioritized optimization plans with specific actions per page
- Feed editorial-post-enhancement with pre-computed keyword context
- Fix declining traffic with data-driven refresh priorities
- Identify content gaps worth filling

**Do NOT use for:** Pulling raw GSC data only (→ `seo-intelligence`), editing a single post (→ `editorial-post-enhancement`), site-wide technical SEO audit (→ `seo-audit-playbook`).

## Pipeline Flow
```
GSC/Bing Data → Opportunity Analysis → Prioritized Plan → Editorial Enhancement → Verify (7-14 days)
```

## Triage Protocol
Before ANY pipeline run:
1. **Identify site** — Which WordPress site? Get URL + credentials.
2. **Check GSC access** — Verify service account has property access (test call via seo-intelligence).
3. **Define scope** — Full site audit or specific section/category?
4. **Set time budget** — How many pages to optimize this sprint?
5. **Check editorial-post-enhancement** — Confirm it has what it needs (post IDs, target keywords).

## Inputs Required (Pre-Flight)
1. **Site URL** — Verified property in GSC/Bing WMT
2. **API credentials** — GSC service account JSON; Bing API key (stored in `.secrets/`)
3. **WordPress credentials** — App password for REST API access
4. **Date range** — Analysis period (default: last 28 days vs previous 28 days for trend)
5. **Page budget** — How many pages to optimize this cycle (default: 10)

---

## Phase 1: Data Collection (via seo-intelligence)

### 1A: Pull GSC Performance Data
Use seo-intelligence to pull ALL of these in one batch:

```python
# Last 28 days — queries
gsc_query_report = {
    "startDate": "2026-02-17",  # 28 days ago
    "endDate": "2026-03-17",    # today
    "dimensions": ["query"],
    "rowLimit": 5000,
    "dimensionFilterGroups": []
}

# Last 28 days — pages
gsc_page_report = {
    "startDate": "2026-02-17",
    "endDate": "2026-03-17",
    "dimensions": ["page"],
    "rowLimit": 5000,
    "dimensionFilterGroups": []
}

# Last 28 days — query + page pairs (for keyword→page mapping)
gsc_query_page_report = {
    "startDate": "2026-02-17",
    "endDate": "2026-03-17",
    "dimensions": ["query", "page"],
    "rowLimit": 25000,
    "dimensionFilterGroups": []
}

# Previous 28 days — pages (for trend comparison)
gsc_page_previous = {
    "startDate": "2026-01-20",
    "endDate": "2026-02-16",
    "dimensions": ["page"],
    "rowLimit": 5000,
    "dimensionFilterGroups": []
}
```

### 1B: Pull Bing WMT Data
Same dimensions, same date range. Use for cross-engine validation.

### 1C: Pull WordPress Post Inventory
```bash
# All published posts with SEO meta
curl -s "https://site.com/wp-json/wp/v2/posts?per_page=100&_fields=id,title,slug,link,yoast_meta,categories,tags,date,modified&status=publish" \
  -u "app_user:app_password"
```

### 1D: Get Indexed Pages List
```bash
# GSC URL Inspection (batch, max 10 parallel)
curl -s -X POST "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"inspectionUrl":"https://site.com/post-slug","siteUrl":"https://site.com"}'
```

### Data Assembly
Merge into a single analysis table:

| URL | GSC Clicks | GSC Impr | GSC CTR | GSC Pos | Bing Clicks | WP Title | WP Modified | Indexed? |
|-----|-----------|----------|---------|---------|-------------|----------|-------------|----------|

---

## Phase 2: Opportunity Analysis

### Category A: CTR Killers (Quick Wins — Est. 1-2 hours/page)

**Definition:** Pages with ≥500 impressions but <2% CTR AND position ≤10.
These pages RANK WELL but the title/description isn't compelling enough to click.

**Formula:**
```
CTR_Killer = (impressions >= 500) AND (ctr < 0.02) AND (position <= 10)
```

**Priority score:**
```
priority_A = impressions × (1 - ctr) × (11 - position) / 100
```
Higher = more potential clicks to recover.

**Action:** Rewrite meta title + meta description using editorial-post-enhancement.
**Expected impact:** +20-50% click increase (from 2% CTR → 3-4% CTR).
**Example:**
- URL: `/best-running-shoes-2026/`
- Current: title "Running Shoes Guide", CTR 1.2%, position 6, impressions 4,200
- Potential clicks: 4,200 × (0.04 - 0.012) = **118 additional clicks/month**

### Category B: Ranking Boosters (Medium Effort — Est. 3-4 hours/page)

**Definition:** Queries at position 5-15 with ≥100 impressions per page.
These are SO CLOSE to page 1 — content enrichment can push them over.

**Formula:**
```
Rank_Booster = (position >= 5) AND (position <= 15) AND (impressions >= 100)
```

**Priority score:**
```
priority_B = impressions × (20 - position) × log10(impressions + 1) / 1000
```

**Action:** Content enrichment (add missing subtopics, expand thin sections) + 4-6 internal links from high-authority posts.
**Expected impact:** Move from page 2 → page 1 (3-5x click multiplier).
**Example:**
- URL: `/how-to-start-a-garden/`
- Current: position 11, impressions 890, clicks 23
- If moved to position 7: estimated 23 × 2.5 = **~58 clicks/month**

### Category C: Content Gaps (High Impact — Est. 6-8 hours/page, new content)

**Definition:** Queries with ≥200 impressions where NO page on the site ranks ≤30.
Users search for this; you have zero coverage.

**Formula:**
```
Content_Gap = (query_impressions >= 200) AND (best_position > 30 OR no_page_ranking)
```

**Priority score:**
```
priority_C = impressions × log10(impressions + 1) / 500
```
Factor in business relevance manually (1-3x multiplier based on topic fit).

**Action:** Create new dedicated content, optimized for the gap query.
**Expected impact:** New ranking page, capture 2-5% of impressions = 4-10 clicks/month initially, growing over time.

### Category D: Declining Content (Urgent — Est. 2-3 hours/page)

**Definition:** Pages losing ≥20% clicks month-over-month.
Something went wrong — algorithm update, content staleness, or competitor leapfrogged.

**Formula:**
```
Declining = (current_period_clicks < previous_period_clicks × 0.80)
```

**Priority score:**
```
priority_D = (previous_clicks - current_clicks) × 2
```

**Action:** Content refresh (update stats, add sections, improve structure) + technical check (indexing, Core Web Vitals, mobile).
**Expected impact:** Recover 50-80% of lost traffic.
**Example:**
- URL: `/best-laptops-for-programming/`
- Previous 28d: 340 clicks → Current 28d: 210 clicks (−38%)
- Lost clicks: 130 → priority_D = 260

### Category E: Non-Indexed Pages (Technical — Est. 30 min-1 hour/page)

**Definition:** Published WordPress posts that don't appear in GSC indexed pages list.
The content exists but Google doesn't know about it.

**Formula:**
```
Non_Indexed = (wp_post_url NOT IN gsc_indexed_urls) AND (wp_status == "publish")
```

**Priority score:**
```
priority_E = estimated_search_volume_for_topic × 0.1
```

**Action:** Technical fix (check robots.txt, noindex tags, canonical issues, sitemap) + submit URL for indexing via GSC.
**Expected impact:** Get page indexed → baseline impressions within 7-14 days.

---

## Phase 3: Optimization Plan Generation

Combine all categories into a single prioritized plan, sorted by priority score.

### Output Format (per page):

```markdown
## Optimization #1: /best-running-shoes-2026/
**Category:** A (CTR Killer) | **Priority Score:** 87.3/100

### Current Metrics
- Clicks: 45 | Impressions: 4,200 | CTR: 1.07% | Position: 6.2
- Previous period: 38 clicks (+18% trend)

### Primary Keyword (from GSC)
`best running shoes 2026` — 4,200 impressions, position 6.2

### Secondary Keywords (from related queries)
1. `running shoes review 2026` — 1,200 imp, pos 8.1
2. `top running shoes this year` — 890 imp, pos 9.4
3. `best shoes for marathon` — 650 imp, pos 7.3

### Specific Actions
1. **Meta title:** Change to "10 Best Running Shoes 2026 — Tested & Ranked by a Runner"
   - Include number, year, proof element
2. **Meta description:** "After testing 40+ pairs over 500 miles, here are the 10 best running shoes for 2026. Compare cushioning, weight, and price for road, trail, and racing."
   - Include specificity (40+, 500 miles), comparison angle
3. **H1:** Ensure matches primary keyword naturally
4. **Add FAQ section** (4-5 questions from "People Also Ask" data)

### Internal Link Opportunities
- Link FROM: `/marathon-training-guide/` (DA 45) → anchor: "best running shoes for marathon training"
- Link FROM: `/beginner-running-tips/` (DA 38) → anchor: "best shoes for new runners"

### Expected Impact
- Current: 45 clicks/month at 1.07% CTR
- Target: 130 clicks/month at 3.1% CTR
- **+85 clicks/month (+189%)**

### Handoff to editorial-post-enhancement
```
Target post ID: 1234
Target keyword: best running shoes 2026
Secondary keywords: running shoes review 2026, top running shoes this year
Current CTR: 1.07% (improve to 3%+)
Actions: meta-rewrite, FAQ section, internal links
Competitor URLs: [top 3 SERP results]
```
```

### Priority Score Formula (Unified)

For cross-category comparison:

```
score = (impact_weight × impact_score) + (ease_weight × ease_score) + (urgency_weight × urgency_score)

Where:
  impact_score = estimated_additional_clicks_per_month / 100
  ease_score = (10 - estimated_hours) / 10  × 100
  urgency_score = days_since_last_update / 365 × 50

Default weights: impact=0.5, ease=0.3, urgency=0.2
```

---

## Phase 4: Feed to Editorial Enhancement

For each page in the optimization plan (top 5-10 first), pass this context to `editorial-post-enhancement`:

### Context Package Template

```markdown
### SEO Pipeline Context for Post ID: {id}

**Data Source:** GSC last 28d (2026-02-17 to 2026-03-17)
**Category:** {A/B/C/D/E}
**Priority Score:** {score}/100

**Primary Keyword:** {keyword} ({impressions} imp, pos {position})
**Secondary Keywords:** {kw2}, {kw3}, {kw4}

**Current Performance:**
- Clicks: {clicks} | Impressions: {impressions}
- CTR: {ctr}% → Target: {target_ctr}%
- Position: {position} → Target: {target_position}

**Required Actions:**
1. {action_1}
2. {action_2}
3. {action_3}

**Internal Links to Add:**
- From {source_url}: anchor "{anchor_text}"
- From {source_url}: anchor "{anchor_text}"

**Schema Requirements:**
{based on content type — Article, FAQPage, HowTo, etc.}

**Competitor URLs (for gap analysis):**
{top 3 SERP results for primary keyword}
```

### Integration Workflow

1. **Open editorial-post-enhancement** for each prioritized post
2. **Paste the Context Package** as the input context
3. **Execute** the enhancement (it will handle the content changes)
4. **Log the change** in daily memory with before/after metrics snapshot
5. **Move to next post** in priority order

### Batching Strategy
- **Sprint 1 (Week 1):** Top 5 pages by priority score
- **Sprint 2 (Week 2):** Next 5 pages
- **Verify Sprint 1:** Pull GSC data, compare before/after
- **Continue** until all Category A-D opportunities exhausted

---

## Phase 5: Verification (7-14 days after optimization)

### Verification Protocol

1. **Pull fresh GSC data** — Same date range length, shifted forward
2. **Compare metrics per page:**

```markdown
## Verification: /best-running-shoes-2026/
**Optimized on:** 2026-03-17
**Verified on:** 2026-03-31 (14 days)

| Metric | Before | After | Change | Target | Met? |
|--------|--------|-------|--------|--------|------|
| Clicks | 45/mo | 72/mo | +60% | +189% | ⏳ |
| CTR | 1.07% | 1.89% | +77% | 3.1% | ⏳ |
| Position | 6.2 | 5.8 | -0.4 | <5 | ⏳ |

**Notes:** CTR trending up, position slightly improved. Full impact expected at 28d mark.
```

3. **Update memory** with patterns:
   - "Meta title rewrites average +40% CTR on Category A pages"
   - "FAQ sections correlated with +0.3 position improvement"

4. **Feed findings back** into future pipeline runs (improve prioritization formulas)

### Success Criteria
- **Category A (CTR):** CTR increase ≥30% within 14 days
- **Category B (Position):** Position improvement ≥2 within 14 days
- **Category C (New content):** Indexed and appearing for target query within 21 days
- **Category D (Declining):** Click trend reverses (positive month-over-month) within 21 days
- **Category E (Indexing):** Page indexed within 7 days of submission

---

## Speed Optimizations

1. **Single-pull architecture** — Pull ALL GSC data once into memory, analyze locally. Zero repeated API calls.
2. **24h result cache** — Store raw GSC pulls in `ops/cache/gsc/{site}/{date}.json`. Reuse if <24h old.
3. **Batch URL inspection** — Max 10 concurrent via `concurrent.futures.ThreadPoolExecutor(max_workers=10)`
4. **Pre-compute internal links** — Pull full WordPress post inventory upfront, score by relevance + authority before pipeline starts.
5. **Parallel category analysis** — Categories A-E are independent; compute all 5 simultaneously.
6. **Incremental runs** — Track which pages were already optimized; skip unless metrics changed >10%.

---

## Self-Critique Scorecard (/25)

Score the pipeline run before claiming completion:

| # | Criterion | Score (1-5) | Notes |
|---|-----------|-------------|-------|
| 1 | **Data Quality** — Was GSC data accurately collected and interpreted? | _/5 | Check date ranges, ensure no gaps |
| 2 | **Prioritization** — Were opportunities correctly ranked by impact? | _/5 | Cross-check priority scores against actual potential |
| 3 | **Actionability** — Were specific, executable actions generated? | _/5 | Each page needs concrete steps, not vague "improve content" |
| 4 | **Integration** — Did editorial-post-enhancement receive complete context? | _/5 | Verify context package had all required fields |
| 5 | **Verification** — Was before/after measurement planned? | _/5 | Calendar reminder set, baseline metrics saved |

**Target:** 22+/25
**Score <20?** → Re-run the weak phases before proceeding.

---

## Output Contract

| Output | Description | Format |
|--------|-------------|--------|
| **Artifact** | Prioritized optimization plan with specific actions per page | Markdown table + detail blocks |
| **Evidence** | GSC data, opportunity categorization, priority score calculations | Raw data + analysis formulas |
| **Decision** | Top 5-10 pages to optimize this sprint | Ordered list with scores |
| **Context** | Pre-computed packages for editorial-post-enhancement | Template per page |
| **Next** | Execute via editorial-post-enhancement, verify in 7-14 days | Calendar reminder + verification protocol |

---

## Quick Reference — Category Cheat Sheet

| Category | Trigger | Action | Effort | Impact | Speed |
|----------|---------|--------|--------|--------|-------|
| A: CTR Killer | ≥500 imp, <2% CTR, pos ≤10 | Meta rewrite | Low | Medium | Fast |
| B: Rank Booster | pos 5-15, ≥100 imp | Enrich + links | Medium | High | Medium |
| C: Content Gap | ≥200 imp, no page ranking | New content | High | High | Slow |
| D: Declining | −20% clicks MoM | Refresh + check | Medium | Medium | Medium |
| E: Non-Indexed | WP post not in GSC index | Technical fix | Low | Medium | Fast |
