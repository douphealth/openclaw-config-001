---
name: programmatic-seo-blueprints
description: Design and deploy scalable SEO page systems for affiliate marketing sites. Covers page models (comparison, alternative, location, directory, template, glossary, integration), quality gates, technical implementation, affiliate-specific patterns, monitoring, and Python scripts for page generation at scale. Triggers on programmatic SEO, pages at scale, template pages, comparison pages, alternative pages, directory pages, location pages, integration pages, or requests to build scalable content systems.
---

# Programmatic SEO Blueprints — Enterprise Skill

## Purpose

Design, validate, build, and monitor scalable SEO page systems that create **genuinely differentiated value** across thousands of pages — built specifically for affiliate marketing sites.

This is NOT a license to mass-produce thin doorway pages. Every page must pass quality gates before scaling.

## When to Use Programmatic SEO vs Manual Content

### Use Programmatic SEO When:
- There is a **repeatable search pattern** with variable components (e.g., "[Product] vs [Product]", "Best [Category] in [Location]")
- **Demand exists** across 100+ keyword variants (validated via SERP presence, not just volume tools)
- You have a **structured data source** that enables per-page uniqueness (product specs, pricing, features, user reviews)
- The content differentiation can be **templated** without sacrificing quality
- Your site has enough **domain authority** or topical relevance to compete

### Use Manual Content When:
- Search intent is nuanced, opinionated, or requires original research
- The topic has fewer than 20-30 viable keyword variants
- Expertise, personal experience, or unique perspective is the ranking factor
- SERPs are dominated by deep editorial content from authoritative sources

### Hybrid Approach (Recommended for Affiliate Sites):
- Programmatic for scalable comparison, alternative, and category pages
- Manual editorial content for buyer's guides, in-depth reviews, and "best of" roundups that link to programmatic pages
- Use editorial content to build topical authority, then let programmatic pages capture long-tail

## 1. Strategy Framework

### Page Model Selection

| Page Model | Best For | Min Viable Pages | Affiliate Fit |
|---|---|---|---|
| **Comparison** (`A vs B`) | Software, tools, products with distinct features | 50+ pairs | ★★★★★ |
| **Alternative** (`X alternatives`) | Replacing established products | 30+ products | ★★★★★ |
| **Location** (`Best X in Y`) | Local services, location-dependent offers | 100+ locations | ★★★★☆ |
| **Directory** (`Category list`) | Curated lists of tools/products in a niche | 20+ categories | ★★★★☆ |
| **Template** (`Niche templates`) | Design, dev, productivity resources | 50+ templates | ★★★☆☆ |
| **Glossary** (`Terms & definitions`) | Technical/niche education with tool tie-ins | 100+ terms | ★★★☆☆ |
| **Integration** (`Tool A + Tool B`) | SaaS ecosystems, API-connected tools | 100+ pairs | ★★★★☆ |

### Demand Validation Methodology

**Step 1: Pattern-Level Demand**
```
1. Identify your seed pattern: "best [product] for [use case]"
2. Use Google Autocomplete, People Also Ask, and related searches to find 50+ variants
3. Check SERP composition: Are there programmatic pages already ranking?
   - If yes → proven pattern, but you need differentiation
   - If no → either no demand or an opportunity (check with broader terms)
4. Estimate aggregate demand: Sum of variant search volumes × realistic CTR for your position
```

**Step 2: Per-Page Validation**
```
For each potential page in your set:
1. Does the search query show clear intent (not ambiguous)?
2. Do at least 2 programmatic page types rank on page 1?
3. Can you provide UNIQUE information not available on ranking pages?
4. Is the query commercially relevant (affiliate commission potential)?
```

**Step 3: SERP Analysis Template**
```
For each target SERP, document:
- Top 10 URLs and their page type
- Content depth (word count, tables, images, tools)
- Featured snippets present (type: paragraph, list, table)
- Domain authority range of ranking pages
- Affiliate presence (are competitors monetizing?)
- Gaps you can fill (data, comparison depth, user experience)
```

### Scalability Assessment

```
DATA AVAILABILITY SCORECARD:
[ ] Primary data source identified (product API, scraping, manual research)
[ ] Data covers all required fields for unique page content
[ ] Data can be refreshed/updated automatically
[ ] Data is accurate enough to publish without manual review per page

CONTENT DIFFERENTIATION SCORECARD:
[ ] Each page has at least 3 unique data points vs siblings
[ ] Per-page unique content exceeds 30% of total page content
[ ] Can add user-generated or dynamic elements (reviews, pricing, availability)
[ ] Can add editorial judgment layer (ratings, recommendations)

SCALE SCORECARD:
[ ] Total addressable pages: _____
[ ] Pages with sufficient differentiation: _____
[ ] Data maintenance effort per month: _____ hours
[ ] Content update frequency required: _____
```

### Risk Assessment

| Risk | Threshold | Mitigation |
|---|---|---|
| **Thin content** | <300 words unique content per page | Add unique data tables, expert commentary, dynamic content |
| **Duplicate content** | >70% similarity between any two pages | Enforce uniqueness via quality gate scripts (see references/) |
| **Crawl budget waste** | >10% of crawled pages are noindexed or low-value | Strategic noindex, consolidate thin pages, optimize sitemaps |
| **Keyword cannibalization** | 2+ pages targeting same primary keyword | Canonical tags, clear URL hierarchy, cannibalization detection script |
| **Google penalty (doorway pages)** | Pages exist only for search engines, not users | Pass "human usefulness" test: would a real person bookmark this? |

## 2. Page Model Blueprints

### Blueprint A: Comparison Pages (`[Product A] vs [Product B]`)

**URL Pattern:** `/compare/product-a-vs-product-b/`

**Example:** `/compare/surfshark-vs-nordvpn/`

**Data Requirements:**
- Product names, logos, descriptions
- Pricing tiers (current, with dates)
- Feature list with per-product support status (yes/no/partial)
- Pros and cons (at least 5 each)
- User ratings (aggregated from multiple sources)
- Best-for categories (who is each product best for?)
- Screenshots or UI comparisons

**Content Structure:**
```
1. Quick Verdict (50-100 words — which product wins, for whom)
2. Pricing Comparison Table (all tiers side-by-side)
3. Feature-by-Feature Comparison (matrix table with ✓/✗/◐)
4. Deep-Dive Sections (performance, ease of use, support, integrations)
5. Pros & Cons (balanced, for both products)
6. Who Should Choose [Product A] vs Who Should Choose [Product B]
7. FAQ Section (3-5 questions, schema-marked)
8. Alternatives to Both (links to alternative pages)
9. Related Comparisons (links to other vs pages)
```

**Schema Markup:**
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[Product A] vs [Product B]: Which is Better in 2026?",
  "description": "...",
  "mainEntity": {
    "@type": "FAQPage",
    "mainEntity": [...]
  }
}
```
Also include `Product` schema for each product, and `Review` schema if editorial ratings are present.

**Internal Linking Pattern:**
- Link to each product's individual review/overview page
- Cross-link to other comparison pages involving either product
- Link to relevant "best [category]" directory pages
- Link to "alternatives" pages for each product

### Blueprint B: Alternative Pages (`[Product] Alternatives`)

**URL Pattern:** `/alternatives/product-name/`

**Example:** `/alternatives/surfer-seo/`

**Data Requirements:**
- Target product's core features and pricing
- Each alternative's features, pricing, and differentiators
- Migration difficulty for each alternative
- Specific use cases where the alternative is better

**Content Structure:**
```
1. Why Look for [Product] Alternatives? (pain points, limitations)
2. Quick Comparison Table (all alternatives vs original, key features)
3. #1 Alternative: [Name] — Best for [specific use case]
   (Mini-review: what it is, why it's better, pricing, who it's for)
4. #2 through #N Alternative sections
5. Feature-by-Feature Deep Comparison Table
6. Pricing Comparison
7. Migration Guide (how to switch from [Product])
8. FAQ
```

**Key Differentiation:**
- Include a **"Switch Score"** (how easy is migration, 1-5)
- Include **"Better For" tags** (which alternative beats the original for what)
- Include **pricing savings calculator** (if alternatives are cheaper)

### Blueprint C: Location Pages (`Best [Service] in [Location]`)

**URL Pattern:** `/best/service-in-location/`

**Example:** `/best/web-hosting-in-canada/`

**Data Requirements:**
- Service providers with local presence/availability
- Local pricing (if different by region)
- Local regulations, compliance requirements
- Regional user reviews/ratings
- Local support availability

**Content Structure:**
```
1. Quick Picks (top 3 for this location)
2. Full Comparison Table
3. Location-Specific Considerations (data laws, server locations, payment methods)
4. Individual Provider Sections (pricing in local currency, local support info)
5. Location-Specific FAQ
6. Related Location Pages (neighboring regions)
```

**Key Differentiation:**
- Localized pricing in native currency
- Compliance/regulation notes specific to the location
- Server/infrastructure location data
- Local user review aggregation

### Blueprint D: Directory Pages (`[Category] Tools/Products List`)

**URL Pattern:** `/category/subcategory/`

**Example:** `/tools/seo/`

**Data Requirements:**
- Product name, logo, description, category tags
- Pricing (free/paid/freemium + starting price)
- Key features (top 3-5)
- User rating + review count
- Last updated date

**Content Structure:**
```
1. Category Introduction (what these tools do, who needs them)
2. Filterable/Sortable Table (by price, rating, features, free vs paid)
3. Top Picks (editorial selection, 3-5 tools)
4. Individual Tool Cards (structured data, consistent format)
5. Buying Guide (what to look for in this category)
6. Related Categories (internal links)
```

### Blueprint E: Template Pages (`[Niche] Templates`)

**URL Pattern:** `/templates/niche/template-name/`

**Content Structure:**
```
1. Template Preview (visual/interactive)
2. What's Included
3. How to Use (step-by-step)
4. Customization Options
5. Related Templates
6. Template Bundle Offers (affiliate opportunity)
```

### Blueprint F: Glossary Pages (`[Niche] Terms & Definitions`)

**URL Pattern:** `/glossary/term-slug/`

**Content Structure:**
```
1. Definition (concise, 1-2 sentences)
2. Detailed Explanation (2-3 paragraphs)
3. Example / How It Works
4. Related Terms (internal links)
5. Tools That Implement This (affiliate links)
6. Learn More Resources
```

**Hub Page:** `/glossary/` — alphabetical listing of all terms, grouped by topic

### Blueprint G: Integration Pages (`[Tool A] + [Tool B] Integration`)

**URL Pattern:** `/integrations/tool-a-plus-tool-b/`

**Content Structure:**
```
1. Integration Overview (what connects, what it enables)
2. Setup Guide (step-by-step, with screenshots)
3. Use Cases (what you can do with this integration)
4. Limitations & Workarounds
5. Alternative Integrations
6. Related Integrations (both tools with other partners)
```

## 3. Template Design Methodology

### Unique Value Injection Per Page

Every programmatic page MUST have unique value. Use this hierarchy:

1. **Proprietary data** (your own testing, user data, calculations) — strongest
2. **Derived data** (comparisons, scores, rankings you compute from raw data) — strong
3. **Aggregated data** (compiled from multiple sources with your structure) — moderate
4. **Templated editorial** (expert commentary sections customized per page) — baseline

**Minimum unique content per page:** 40% must be page-specific (not reusable across sibling pages)

### Data Source Mapping

```
PRIMARY SOURCES (per page model):
- Comparison: Product APIs, pricing pages, feature matrices
- Alternative: Core product analysis + alternative feature databases
- Location: Regional databases, currency APIs, compliance registries
- Directory: Product databases with categorization
- Glossary: Expert-written definitions + cross-references
- Integration: API documentation, integration marketplaces

DATA FRESHNESS REQUIREMENTS:
- Pricing data: Updated weekly minimum
- Feature data: Updated monthly
- Review/rating data: Updated monthly
- Compliance/regulation: Updated quarterly
- Static content (definitions, guides): Updated quarterly
```

### Content Differentiation Strategy

For each page model, enforce these uniqueness rules:

```
COMPARISON PAGES:
- Quick verdict must be unique (different winners for different product pairs)
- Feature comparison tables will naturally differ (different products = different features)
- FAQ questions should be pair-specific
- At least 500 words of editorial analysis unique to this comparison

ALTERNATIVE PAGES:
- "Why look for alternatives" section must address product-specific pain points
- Alternative rankings differ per target product
- Migration guides are product-specific

LOCATION PAGES:
- Localized intro paragraphs (unique per location)
- Local compliance/regulation sections
- Pricing in local currency
- Location-specific FAQ

DIRECTORY PAGES:
- Category-specific buying guides
- Editorial picks based on category criteria
- Category-specific feature comparisons
```

### Meta/Title/URL Template Patterns

```
COMPARISON:
  Title: "[Product A] vs [Product B] ([Year]): Which is Better?"
  Meta: "Compare [Product A] and [Product B] on features, pricing, and performance. See which tool is best for your needs with our detailed side-by-side analysis."
  URL: /compare/product-a-vs-product-b/

ALTERNATIVE:
  Title: "[N] Best [Product] Alternatives in [Year] ([Free & Paid])"
  Meta: "Looking for [Product] alternatives? We tested [N] options and ranked them by features, pricing, and ease of use. Find your perfect match."
  URL: /alternatives/product-name/

LOCATION:
  Title: "Best [Service] in [Location] ([Year] Guide)"
  Meta: "Find the best [service] in [location]. Compare top providers on pricing, features, and local support. Updated [Month Year]."
  URL: /best/service-in-location/

DIRECTORY:
  Title: "Best [Category] Tools ([Year] Ranked & Compared)"
  Meta: "Discover the best [category] tools. [N]+ options compared on features, pricing, and user ratings. Find the right tool for your workflow."
  URL: /category/subcategory/

GLOSSARY:
  Title: "What is [Term]? [Niche] Definition & Examples"
  Meta: "[Term] explained: definition, how it works, examples, and tools that use it. Part of our [niche] glossary."
  URL: /glossary/term-slug/

INTEGRATION:
  Title: "[Tool A] + [Tool B] Integration: Setup Guide & Use Cases"
  Meta: "Connect [Tool A] and [Tool B] with our step-by-step integration guide. Learn setup, use cases, and alternatives."
  URL: /integrations/tool-a-plus-tool-b/
```

## 4. Quality Gates

See `references/quality-gates.md` for the full quality gate system including Python scripts.

**Core quality rules:**
- Minimum 300 words of unique content per page
- Maximum 70% similarity between any two sibling pages
- Every page must answer: "Would a human bookmark this?"
- Pages with <200 words of unique content → noindex
- Pages with >85% similarity to another → consolidate or differentiate
- No page published without passing the automated quality check

## 5. Technical Implementation

### URL Structure Design

```
RECOMMENDED STRUCTURE (use subfolders, NOT subdomains):

/compare/{product-a}-vs-{product-b}/          → Comparison pages
/alternatives/{product-name}/                  → Alternative pages
/best/{service}-{preposition}-{location}/      → Location pages
/{category}/                                   → Directory hub pages
/{category}/{subcategory}/                     → Directory sub-pages
/glossary/{term}/                              → Glossary pages
/glossary/                                     → Glossary hub (alphabetical)
/integrations/{tool-a}-plus-{tool-b}/          → Integration pages
/templates/{niche}/                            → Template hub
/templates/{niche}/{template-name}/            → Individual template

RULES:
- Use hyphens, not underscores
- Lowercase only
- Keep URLs under 75 characters when possible
- Include the primary keyword in the URL
- Use consistent slug patterns within each page model
```

### XML Sitemap Strategy

```
SITEMAP ARCHITECTURE:

/sitemap.xml                    → Index of sub-sitemaps
/sitemap-comparisons.xml        → All comparison pages
/sitemap-alternatives.xml       → All alternative pages
/sitemap-locations.xml          → All location pages
/sitemap-directory.xml          → All directory pages
/sitemap-glossary.xml           → All glossary pages
/sitemap-integrations.xml       → All integration pages
/sitemap-static.xml             → Blog posts, about, contact, etc.

RULES:
- Max 50,000 URLs per sitemap file (or 50MB uncompressed)
- Include <lastmod> for every URL (use actual content modification date)
- Split by page model for easier monitoring of indexation rates
- Auto-generate sitemaps when new pages are added
- Submit individual sitemaps in Google Search Console for per-model tracking
- Remove noindexed pages from sitemaps entirely
```

### Crawl Budget Optimization

```
1. ROBOTS.TXT STRATEGY:
   - Block faceted navigation URLs (?sort=, ?filter=, ?page=)
   - Block internal search results
   - Allow all programmatic page models
   - Block staging/dev environments

2. CRAWL PRIORITY:
   - Hub pages (category pages, glossary index) → Priority 0.8
   - High-value comparison/alternative pages → Priority 0.7
   - Long-tail programmatic pages → Priority 0.5
   - Paginated directory pages → Priority 0.3

3. INDEXATION MANAGEMENT:
   - Publish in batches (50-100 pages), monitor indexation rate
   - If indexation rate <80% after 30 days, audit for quality issues
   - Use IndexNow API for instant notification to Bing
   - Monitor crawl stats in Google Search Console weekly
```

### Pagination Handling

```
DIRECTORY PAGES WITH PAGINATION:
- Use rel="next" and rel="prev" (still useful for UX even if Google ignores them)
- Ensure each paginated page has unique title: "Best [Category] Tools - Page [N]"
- Include unique intro content per page (different editorial picks, summaries)
- Implement "Load More" with server-side rendering for SEO
- Paginated URLs: /{category}/page/{n}/ (clean, indexable)

NEVER:
- Use infinite scroll without SSR fallback
- Block paginated pages in robots.txt
- Canonical all paginated pages to page 1
```

### Canonical Tag Strategy

```
EVERY PROGRAMMATIC PAGE:
- Self-referencing canonical tag is mandatory
- Example: <link rel="canonical" href="https://site.com/compare/a-vs-b/" />

FOR SIMILAR/DUPLICATE PAGES:
- If two pages are >85% similar, canonical the lower-value one to the higher-value one
- If a comparison page can be accessed in both orders (a-vs-b and b-vs-a), redirect one to the other
- Always canonical to the preferred URL variant (no trailing slash inconsistency)

CANONICAL URL RULES:
- Always use absolute URLs
- Always include protocol (https://)
- No parameters in canonical URLs
- Consistent trailing slash policy (choose one, stick with it)
```

### Internal Linking Automation

```
LINKING RULES PER PAGE MODEL:

Comparison Pages:
  → Link to both products' individual pages
  → Link to 3-5 related comparison pages (share one product in common)
  → Link to relevant category directory page
  → Link to alternative pages for each product

Alternative Pages:
  → Link to the target product's comparison pages
  → Link to each alternative's comparison pages
  → Link to relevant category directory page
  → Cross-link between alternative pages that share alternatives

Location Pages:
  → Link to neighboring location pages (same service)
  → Link to comparison pages for providers mentioned
  → Link to relevant category directory page

Glossary Pages:
  → Link to related terms (bidirectional)
  → Link to tools/products mentioned in definition
  → Link to relevant category directory page
  → Link from relevant comparison/alternative pages (contextual)

AUTOMATION APPROACH:
- Build a relationship graph of all pages
- Auto-generate "Related Pages" sections based on shared entities
- Manual editorial links in content body (higher value)
- Minimum 5 internal links per programmatic page
```

### Page Speed at Scale

```
REQUIREMENTS:
- Core Web Vitals: LCP <2.5s, FID <100ms, CLS <0.1
- Page weight: <1MB total (including images)
- Time to First Byte: <200ms

IMPLEMENTATION:
- Static site generation (SSG) or ISR for all programmatic pages
- Lazy-load images below the fold
- Compress all images (WebP with JPEG fallback)
- Minimize JavaScript; prefer server-rendered HTML
- Use a CDN for all static assets
- Cache product data locally (don't make API calls per page load)
- Pre-render comparison tables (don't load via JS)
- Defer non-critical CSS/JS
```

## 6. Affiliate-Specific Programmatic Patterns

See `references/affiliate-programmatic-patterns.md` for full templates and Python scripts.

**Key patterns covered:**
- Product comparison matrix pages (feature × product grid)
- `[Product] vs [Product]` with affiliate CTAs
- `Best [Category] for [Use Case]` with ranked recommendations
- `[Product] alternatives` with migration scoring
- `[Product] pricing comparison` across all tiers
- Feature-by-feature comparison tables with verdicts

## 7. Monitoring & Optimization

### Indexation Rate Tracking

```python
# Prefer normalized GSC/Bing search-visibility packs first
# Track indexation per page model using Google Search Console API
# or by checking site:domain.com inurl:/compare/ patterns

INDEXATION THRESHOLDS:
- >90% indexation within 30 days → Healthy, continue publishing
- 70-90% indexation → Audit quality, check for thin content flags
- <70% indexation → Stop publishing, diagnose and fix issues first

MONITORING CADENCE:
- Weekly: Check new page indexation rates
- Monthly: Audit full indexation across all page models
- Quarterly: Review and prune underperforming pages
```

### Ranking Distribution Analysis

```
TRACK THESE METRICS PER PAGE MODEL:
- Pages ranking in positions 1-3
- Pages ranking in positions 4-10
- Pages ranking in positions 11-20
- Pages not ranking (impressions <10/month)
- Average position trend (improving, stable, declining)

ACTION THRESHOLDS:
- If >20% of pages in a model are not ranking → Review template quality
- If average position declining → Check competitor content updates
- If a page drops from top 10 → Immediate audit and refresh
```

### Thin Content Detection

```
Run monthly (see quality-gates.md for script):
1. Crawl all programmatic pages
2. Measure unique word count per page
3. Calculate similarity scores between sibling pages
4. Flag pages with <300 unique words
5. Flag pages with >70% similarity to another page
6. Generate report with action items (improve, consolidate, noindex)
```

### Cannibalization Monitoring

```
Run monthly:
1. Export all ranking keywords from GSC
2. Group keywords by page URL
3. Identify keywords where 2+ of your pages are ranking
4. If both pages ranking 11+ → Consolidate to stronger page
5. If one page ranking 1-10, other 11+ → Canonical weaker to stronger
6. If both pages ranking 1-10 → Differentiate content, split keywords
```

### Performance Metrics Dashboard

```
PER PAGE MODEL, TRACK:
- Total organic sessions
- Organic CTR (from GSC)
- Conversion rate (affiliate clicks / sessions)
- Revenue per page
- Revenue per session

TOP PERFORMING PAGES:
- Identify top 10% pages by revenue
- Study what makes them successful
- Apply learnings to underperforming pages
- Create more pages in that specific sub-pattern

UNDERPERFORMING PAGES:
- Pages with traffic but no conversions → Improve CTAs, add more context
- Pages with impressions but no clicks → Improve titles and meta descriptions
- Pages with no impressions → Audit for technical issues or consolidate
```

### A/B Testing Framework for Templates

```
TESTABLE ELEMENTS (per page model):
1. CTA placement and copy
2. Comparison table layout (horizontal vs vertical)
3. Quick verdict length and placement
4. Number of alternatives/comparisons shown
5. FAQ placement (top vs bottom)
6. Pricing display format

METHODOLOGY:
- Run tests within a page model (compare 50 vs 50 pages)
- Minimum 2-week test duration
- Minimum 1,000 sessions per variant
- Track: CTR, time on page, affiliate click-through rate
- Implement winner across the full model
```

## Workflow: Building a Programmatic Page System

```
PHASE 1: VALIDATE (1-2 weeks)
├── Identify repeatable search pattern
├── Validate demand (SERP analysis, autocomplete research)
├── Assess data availability and differentiation potential
├── Run risk assessment
└── Decision: Go / No-Go

PHASE 2: DESIGN (1-2 weeks)
├── Select page model
├── Design URL structure
├── Build content template
├── Define data schema
├── Design internal linking graph
├── Write 3 pilot pages manually
└── Validate with quality gates

PHASE 3: BUILD (2-4 weeks)
├── Build data pipeline (APIs, scraping, manual research)
├── Build page generator (Python scripts)
├── Build quality gate pipeline
├── Build sitemap generator
├── Build internal linking automation
└── Generate pilot batch (20-50 pages)

PHASE 4: LAUNCH (1 week)
├── Publish pilot batch
├── Submit sitemaps
├── Monitor indexation (wait 2 weeks)
├── Run quality audit on indexed pages
└── Fix any issues

PHASE 5: SCALE (ongoing)
├── Publish in batches of 50-100
├── Monitor indexation rates per batch
├── Run monthly quality audits
├── Run monthly cannibalization checks
├── Optimize underperforming pages
├── Update pricing/features monthly
└── A/B test template improvements
```

## Resources

When working on this skill, read these reference files as needed:
- `references/page-model-templates.md` — Detailed templates, HTML structures, and Python generation scripts for each page model
- `references/quality-gates.md` — Quality gate system with Python scripts for uniqueness detection, thin content identification, and cannibalization monitoring
- `references/affiliate-programmatic-patterns.md` — Affiliate-specific patterns, comparison matrix templates, and monetization-optimized page structures


## Output Contract
**Artifact**: pSEO page template with quality gates
**Evidence**: Template output sample, quality checklist
**Decision**: Template approved for scale
**Next**: Deploy and monitor indexation
## Checks and Common Mistakes

- ❌ Starting with volume ("we can make 10,000 pages!") instead of usefulness
- ❌ Generating pages with no meaningful data differentiation
- ❌ Ignoring crawl budget and indexation management
- ❌ Publishing all pages at once (batch and monitor instead)
- ❌ Neglecting internal linking (pages need link equity)
- ❌ Forgetting data freshness (stale pricing kills trust)
- ❌ Over-templating to the point pages feel robotic
- ❌ No quality gate between generation and publication
- ❌ Ignoring cannibalization until it's a problem
- ❌ Promising rankings because a pattern exists (competition matters)

## Do NOT Use This For
- Tasks better handled by a more specific skill — check skill-router
- One-off quick questions that don't need a skill
- Tasks in a different domain — route to the correct skill first
-off quick questions that don't need a skill
- Tasks in a different domain — route to the correct skill first
