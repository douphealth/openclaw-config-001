---
name: seo-audit-playbook
description: Enterprise-grade SEO audit and diagnosis system. Use when auditing sites, diagnosing ranking drops, checking for keyword cannibalization, analyzing technical SEO issues, running competitive analysis, or performing comprehensive site health checks. Triggers on SEO audit requests, ranking drops, indexing problems, technical SEO reviews, on-page SEO checks, crawlability concerns, site health checks, title/meta reviews, cannibalization detection, or requests to explain why a site is not ranking.
---

# SEO Audit Playbook

## Purpose
Run a structured SEO diagnosis that finds root causes, prioritizes fixes, and avoids generic advice.

Enterprise SEO audit system with cannibalization detection, technical analysis, and actionable fix prioritization.

## Decision Tree: What Kind of Audit?

```
SEO issue or audit request
│
├── "Why isn't my site ranking?"
│   └── Full audit workflow (Sections 1–7, follow audit order)
│
├── Ranking dropped suddenly
│   ├── Check crawlability first (Section 1)
│   ├── Check Core Web Vitals (Section 2.1)
│   ├── Check for cannibalization (Section 4)
│   └── Check GSC for manual actions or coverage issues
│
├── Pages not indexing
│   └── Crawlability + indexation analysis (Section 1)
│
├── Technical SEO review
│   └── Technical foundations (Section 2)
│
├── On-page optimization check
│   └── On-page analysis (Section 3)
│
├── Cannibalization detection
│   └── Keyword cannibalization analysis (Section 4)
│
├── Competitor analysis
│   └── Competitive analysis framework (Section 6)
│
└── Site migration validation
    └── Run full audit before + after, compare results
```


## Enterprise Protocols (MANDATORY)

Before executing, read `skills/shared/enterprise-protocol.md` and follow:
- Pre-flight health check (site accessible, creds valid, state captured)
- Mandatory backup before any modification
- Retry with exponential backoff (max 3 attempts per API call)
- Progress reporting every 10 operations
- Verification after each modification
- Health checks every 50 items in long operations
- Rollback plan identified before starting

## Superpower Layer

For complex or high-risk work, also follow:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use

- SEO audits, site health checks, ranking diagnosis
- "Why isn't my site ranking?" or ranking drops
- Technical SEO issues, crawlability problems
- Keyword cannibalization detection and resolution
- Indexing issues, Google Search Console problems
- Core Web Vitals, page speed, mobile optimization
- Competitor SEO analysis
- Site migration SEO validation


## Do NOT Use For
- Writing or heavily editing content (use `editorial-post-enhancement`)
- Implementing schema markup as the primary task (use `schema-ops`)
- Setting up analytics/tracking instrumentation (use `tracking-measurement`)
- Content strategy and editorial planning (use `content-strategy-planning`)

## Audit Order (ALWAYS FOLLOW THIS SEQUENCE)

```
1. Crawlability & Indexation      → Can Google find and index pages?
2. Technical Foundations           → CWV, mobile, HTTPS, redirects, canonicals
3. On-Page Optimization            → Titles, metas, headers, content, schema
4. Content Quality & Intent Match  → E-E-A-T, depth, freshness, intent
5. Internal Linking & Authority    → Link architecture, anchor text, orphans
6. Cannibalization Check           → Keyword overlap, competing pages
7. Competitive Analysis            → Gap analysis, SERP comparison
```

## 1. Crawlability & Indexation Analysis

### 1.1 Robots.txt Validation

| Check | Severity | Fix |
|-------|----------|-----|
| Blocks critical paths (`/`, `/wp-content/`, `/category/`) | CRITICAL | Remove blocking Disallow rules |
| No Sitemap declaration | WARNING | Add `Sitemap: https://domain.com/sitemap.xml` |
| Blocks entire site (`Disallow: /`) | CRITICAL | Fix immediately — site is invisible to Google |

### 1.2 XML Sitemap Validation

| Check | Severity | Fix |
|-------|----------|-----|
| Sitemap has 0 URLs | CRITICAL | Regenerate or fix sitemap |
| Sitemap has >50K URLs | WARNING | Split into sub-sitemaps |
| Contains non-canonical URLs (with query strings) | WARNING | Remove non-canonical URLs |
| Sitemap unreachable (404/500) | CRITICAL | Fix sitemap endpoint |

### 1.3 Indexation Coverage (GSC)

| Coverage State | Meaning | Action |
|----------------|---------|--------|
| Submitted and indexed | Healthy | Monitor |
| Crawled – currently not indexed | Quality or content issue | Audit content depth/relevance |
| Discovered – currently not indexed | Crawl budget or priority issue | Check internal links, sitemap |
| Excluded by noindex tag | Intentional or mistake | Verify intent |
| Duplicate without canonical | Need canonical tag | Add self-referencing canonical |
| Page with redirect | Old URL still in sitemap | Update sitemap to final URL |

## 2. Technical SEO Analysis

### 2.1 Core Web Vitals

| Metric | Good | Needs Improvement | Poor | Action |
|--------|------|-------------------|------|--------|
| LCP | <2.5s | 2.5–4s | >4s | Optimize images, reduce render-blocking |
| CLS | <0.1 | 0.1–0.25 | >0.25 | Set image dimensions, avoid layout shifts |
| INP | <200ms | 200–500ms | >500ms | Reduce JS execution, defer non-critical |

**Check via:** PageSpeed Insights API, Google Search Console, or Chrome UX Report.

### 2.2 Mobile Optimization

| Check | Severity | Fix |
|-------|----------|-----|
| No viewport meta tag | CRITICAL | Add `<meta name="viewport" content="width=device-width, initial-scale=1">` |
| Viewport not set to device-width | WARNING | Update viewport meta |
| Touch elements too close | WARNING | Minimum 48px tap targets |
| Font size too small | WARNING | Minimum 16px base font |

### 2.3 HTTPS & Security

| Check | Severity | Fix |
|-------|----------|-----|
| HTTP does not redirect to HTTPS | CRITICAL | Set up 301/308 redirect |
| HTTP redirect goes to wrong URL | CRITICAL | Fix redirect target |
| Mixed content (HTTP resources on HTTPS page) | WARNING | Update resource URLs to HTTPS |

### 2.4 Redirect Chains

| Chain Length | Status | Action |
|-------------|--------|--------|
| 0 hops (direct) | Healthy | None |
| 1 hop (single redirect) | Acceptable | None |
| 2 hops | WARNING | Consolidate to single redirect |
| 3+ hops | CRITICAL | Flatten chain — redirect directly to final URL |

### 2.5 Canonical Tag Validation

| Check | Severity | Fix |
|-------|----------|-----|
| No canonical tag | CRITICAL | Add self-referencing canonical |
| Multiple canonical tags | WARNING | Remove extras, keep one |
| Canonical points to different URL | INFO | Verify intent (is this a deliberate canonical?) |
| Canonical uses relative URL | WARNING | Use absolute URL |

## 3. On-Page SEO Analysis

### 3.1 Title Tag Audit

| Check | Severity | Fix |
|-------|----------|-----|
| No title tag | CRITICAL | Add title tag with primary keyword |
| Title empty | CRITICAL | Write descriptive title |
| Title <30 chars | WARNING | Expand to 50–60 chars |
| Title >60 chars | WARNING | Shorten to avoid truncation |
| Primary keyword missing | WARNING | Include primary keyword naturally |

### 3.2 Meta Description Audit

| Check | Severity | Fix |
|-------|----------|-----|
| No meta description | WARNING | Add 150–160 char description with CTA |
| Meta description empty | WARNING | Write compelling description |
| Meta description <120 chars | INFO | Consider expanding |
| Meta description >160 chars | INFO | May be truncated in SERPs |

### 3.3 Header Hierarchy Audit

| Check | Severity | Fix |
|-------|----------|-----|
| No H1 tag | CRITICAL | Add single H1 with primary keyword |
| Multiple H1 tags | WARNING | Keep only one H1, convert others to H2 |
| Header hierarchy skip (H2 → H4) | WARNING | Fix hierarchy (add H3 between) |
| <3 header tags total | WARNING | Add more headers for structure |

## 4. Keyword Cannibalization Detection (CRITICAL)

### Detection Methods

**Method 1 — Target Keyword Overlap:**
```
Multiple pages explicitly target the same primary keyword
→ Severity: CRITICAL
→ Fix: Choose one primary page, differentiate others, or consolidate
```

**Method 2 — Ranking Overlap (from GSC data):**
```
Multiple pages rank for the same keyword
→ Severity: HIGH if best position <10, MEDIUM otherwise
→ Fix: Consolidate content or differentiate intent
```

**Method 3 — Title Similarity:**
```
Pages have >70% word overlap in titles
→ Severity: HIGH
→ Fix: Differentiate titles or consolidate pages
```

### Resolution Decision Tree

```
CANNIBALIZATION DETECTED
│
├── Type 1: Target keyword overlap
│   ├── Which page ranks higher? → Make that the primary
│   ├── Can the other target a different intent? → Differentiate
│   ├── Is the other page valuable? → Add canonical to primary
│   └── Is it low-value? → 301 redirect to primary
│
├── Type 2: Ranking overlap
│   ├── Positions close (<5 apart)? → Likely cannibalizing
│   ├── One page clearly better? → Consolidate, redirect
│   ├── Different intents? → Differentiate titles/H1s
│   └── Both ranking poorly? → Merge into one authoritative page
│
└── Type 3: Title similarity
    ├── Rewrite titles to target different angles
    ├── Differentiate primary keywords
    └── Add unique value propositions
```

## 5. Content Quality Assessment

### E-E-A-T Evaluation

| Signal | Check | Present? |
|--------|-------|----------|
| Author identified with credentials | Author bio visible | [ ] |
| First-hand experience | Demonstrated through testing/screenshots | [ ] |
| External citations | Links to authoritative sources | [ ] |
| Content updated regularly | Last updated date visible | [ ] |
| Methodology explained | How conclusions were reached | [ ] |
| Contact info accessible | About/contact page linked | [ ] |

### Content Depth Scoring (0–100)

| Factor | Points | Criteria |
|--------|--------|----------|
| Word count | 15 | >2000 = 15, >1000 = 10, <300 = −20 |
| Header structure | 10 | ≥5 headers = 10, <2 = −10 |
| Images | 5 | ≥3 images |
| Internal links | 10 | ≥3 contextual internal links |
| Lists/tables | 5 | ≥2 lists |
| Schema markup | 5 | JSON-LD present |
| Base | 50 | Starting score |

## 6. Competitive Analysis Framework

### SERP Competitor Analysis

For target keyword, analyze top 10 results:
1. Average word count of ranking pages
2. Common headers/topics covered
3. Content formats used (list, guide, video, tool)
4. Average title length and pattern
5. Featured snippet presence and type
6. PAA questions
7. Domain authority range
8. Content freshness (publication/update dates)

### Gap Identification

| Gap Type | Signal | Action |
|----------|--------|--------|
| Topic gap | Competitors cover topic, you don't | Add section |
| Depth gap | Competitors go deeper | Expand content |
| Format gap | Competitors use tables/video/tools | Add richer formats |
| Freshness gap | Competitors updated recently | Update your content |
| Entity gap | Competitors mention entities you don't | Add entity coverage |

## 7. Output Template

```
## SEO Audit Report: {domain}
Date: {date}

### Executive Summary
- Overall Health Score: X/100
- Critical Issues: X | High: X | Medium: X | Low: X

### Critical Issues (Fix Immediately)
1. [Issue] — [Evidence] — [Fix]

### High Priority (Fix This Week)
1. [Issue] — [Evidence] — [Fix]

### Medium Priority (Fix This Month)
1. [Issue] — [Evidence] — [Fix]

### Cannibalization Report
- X keyword overlaps detected
- X ranking conflicts
- X title similarities
- Recommended actions: [list]

### Action Plan
Week 1: [Critical fixes]
Week 2–4: [High priority]
Month 2–3: [Medium priority]
Ongoing: [Monitoring]

### Unknowns & Limitations
- [Data not available]
- [Tools not accessible]
```

## Common Mistakes & Anti-Patterns

| Anti-Pattern | Consequence | Prevention |
|-------------|-------------|-----------|
| Claiming "no schema" from static fetch alone | Schema may be JS-rendered | Check rendered HTML too |
| Skipping cannibalization before recommending content | Creates more competition | ALWAYS check Section 4 first |
| Not defining scope/audience/symptoms | Generic, unfocused audit | Ask clarifying questions first |
| Mixing business opinion with technical diagnosis | Unactionable output | Separate diagnosis from strategy |
| Jumping to content advice before checking crawl/index | Misses root cause | Follow audit order (Sections 1–7) |
| Reporting "audit complete" from surface HTML only | Shallow, misleading | Check rendered pages, GSC data, CWV |

## Anti-Patterns
- ❌ Running an audit without checking for keyword cannibalization first — creates more competition instead of fixing rankings
- ❌ Reporting "no issues" from a static HTML fetch alone — JS-rendered content, dynamic schema, and client-side redirects are invisible to basic fetches
- ❌ Prioritizing content recommendations before verifying crawlability and indexation — misses root causes entirely
- ❌ Treating CWV scores from lab data as production reality — always check CrUX field data for real-user performance
- ❌ Delivering audit findings without prioritized action items — reports that sit unread help nobody
- ❌ Skipping the cannibalization check on sites with 100+ pages — it's the #1 missed issue on content-heavy sites
- ❌ Claiming "audit complete" without verifying fixes actually resolved the issues — always re-crawl after changes

## Verification Steps

1. Confirm crawlability was tested (robots.txt + sitemap)
2. Verify Core Web Vitals were checked (not assumed)
3. Confirm cannibalization analysis was run
4. Check that findings have concrete evidence (URLs, screenshots, data)
5. Verify fix recommendations are specific and actionable
6. Confirm output follows the template format

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

## Output Contract

| Field | Description |
|-------|-------------|
| **Artifact** | SEO audit report with prioritized fixes, categorized by severity |
| **Evidence** | Crawl data, issue screenshots, GSC data, CWV metrics, cannibalization findings |
| **Decision** | Fix plan approved with prioritized action items |
| **Next** | Implement critical/high fixes → re-audit in 2–4 weeks |

## Performance Optimizations

### Speed Multipliers
- Apply `skills/api-efficiency-protocol.md` for CMS, GSC, sitemap, and page-state data pulls
- **Parallel checks**: Run robots.txt + sitemap + GSC + CWV checks simultaneously
- **Batch page analysis**: Analyze 10-20 pages per API call, not individually
- **Template-based reports**: Use audit template as starting point, fill in findings
- **Pre-crawl data**: Use sitemap + existing index data before running live crawl
- **Prioritized checks**: Check most-likely causes first (cannibalization, crawlability, CWV)

## Resources

- `references/technical-checklist.md` — Technical SEO checklist
- `references/cannibalization-detection.md` — Detailed cannibalization methodology
- `references/competitive-analysis-framework.md` — Competitor analysis deep-dive

## Compatibility
- Targets current WordPress 6.9+ where applicable
- REST API + WP-CLI preferred over browser automation
- Batch operations via `_fields` + `per_page=100` + `concurrent.futures`
- Browser automation only when API/CLI insufficient

## Inputs Required (Pre-Flight)
Before executing any task in this skill:
1. **Target identification** — What site, page, post, or system is being operated on?
2. **Auth verification** — Confirm credentials work (test API call or CLI command)
3. **Current state** — Understand what exists before making changes (GET before POST)
4. **Environment** — Production vs staging (assume production unless stated)
5. **Constraints** — No downtime? Preserve SEO? Preserve data? Budget limits?

## Triage Protocol
Before ANY operation:
1. **Identify** — What type of content/system/problem is this?
2. **Check state** — Query current state via API/CLI before modifying
3. **Verify creds** — Confirm authentication works
4. **Plan rollback** — How to undo if something breaks?
5. **Scope check** — Is this a single item or batch? Scale determines approach.


