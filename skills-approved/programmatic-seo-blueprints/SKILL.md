---
name: programmatic-seo-blueprints
description: Design and deploy scalable SEO page systems for affiliate marketing sites. Covers page models (comparison, alternative, location, directory, template, glossary, integration), quality gates, technical implementation, affiliate-specific patterns, monitoring, and Python scripts for page generation at scale. Triggers on programmatic SEO, pages at scale, template pages, comparison pages, alternative pages, directory pages, location pages, integration pages, or requests to build scalable content systems.
---

# Programmatic SEO Blueprints

Enterprise system for designing, validating, building, and monitoring scalable SEO page systems that create genuinely differentiated value across thousands of pages — built for affiliate marketing sites.

> **NOT a license for thin doorway pages.** Every page must pass quality gates before scaling.

## Decision Tree: Programmatic vs Manual?

```
Content need identified
│
├── Is there a repeatable search pattern with variable components?
│   ├── YES (100+ keyword variants) → Programmatic (this skill)
│   ├── YES (20-30 variants) → Hybrid (programmatic + editorial)
│   └── NO → Manual content (conversion-copywriting)
│
├── Do you have structured data enabling per-page uniqueness?
│   ├── YES → Programmatic viable
│   └── NO → Gather data first, then decide
│
├── Is search intent nuanced/opinionated/requiring original research?
│   ├── YES → Manual content
│   └── NO → Programmatic viable
│
└── Are SERPs dominated by deep editorial from authority sites?
    ├── YES → Hybrid approach (editorial builds authority, programmatic captures long-tail)
    └── NO → Programmatic viable
```

## Page Model Selection Matrix

| Page Model | URL Pattern | Min Viable Pages | Affiliate Fit | Unique Value Source |
|-----------|-------------|-----------------|---------------|-------------------|
| **Comparison** (`A vs B`) | `/compare/a-vs-b/` | 50+ pairs | ★★★★★ | Feature matrices, pricing, verdicts |
| **Alternative** (`X alternatives`) | `/alternatives/x/` | 30+ products | ★★★★★ | Migration scores, "better for" tags |
| **Location** (`Best X in Y`) | `/best/x-in-y/` | 100+ locations | ★★★★☆ | Local pricing, compliance, currency |
| **Directory** (`Category list`) | `/category/subcategory/` | 20+ categories | ★★★★☆ | Editorial picks, buying guides |
| **Template** (`Niche templates`) | `/templates/niche/name/` | 50+ templates | ★★★☆☆ | Preview, customization, bundles |
| **Glossary** (`Terms & definitions`) | `/glossary/term/` | 100+ terms | ★★★☆☆ | Expert definitions, tool tie-ins |
| **Integration** (`Tool A + Tool B`) | `/integrations/a-plus-b/` | 100+ pairs | ★★★★☆ | Setup guides, use cases |

## Operational Procedures

### 1. Demand Validation (Before Building Anything)

**Phase 1 — Pattern-Level Demand:**
1. Identify seed pattern: "best [product] for [use case]"
2. Use Google Autocomplete, PAA, related searches to find 50+ variants
3. Check SERP composition: are programmatic pages already ranking?
4. Estimate aggregate demand: variant volumes × realistic CTR

**Phase 2 — Per-Page Validation:**
| Check | Pass Criteria |
|-------|--------------|
| Clear search intent | Query is unambiguous |
| Programmatic pages rank | ≥2 on page 1 |
| Unique data available | Info not on ranking pages |
| Commercial relevance | Affiliate commission potential exists |

**Phase 3 — Scalability Scorecard:**
```
[ ] Primary data source identified (API, scraping, manual)
[ ] Data covers all required fields for unique content
[ ] Data can be refreshed automatically
[ ] Data is accurate enough to publish without per-page review
[ ] Each page has ≥3 unique data points vs siblings
[ ] Per-page unique content exceeds 30% of total
[ ] Total addressable pages: _____
[ ] Pages with sufficient differentiation: _____
```

### 2. Blueprint Implementation

**Blueprint A: Comparison Pages**
```
Content Structure:
1. Quick Verdict (50–100 words — which wins, for whom)
2. Pricing Comparison Table (all tiers side-by-side)
3. Feature-by-Feature Matrix (✓/✗/◐)
4. Deep-Dive Sections (performance, UX, support, integrations)
5. Pros & Cons (≥5 each, balanced)
6. Who Should Choose A vs Who Should Choose B
7. FAQ Section (3–5 questions, FAQPage schema)
8. Alternatives to Both (links to alternative pages)
9. Related Comparisons (cross-links)

Data Requirements:
- Names, logos, descriptions, pricing tiers (with dates)
- Feature list with per-product support status
- User ratings (aggregated), best-for categories
```

**Blueprint B: Alternative Pages**
```
Content Structure:
1. Why Look for [Product] Alternatives? (pain points)
2. Quick Comparison Table (all alternatives vs original)
3. #1 Alternative — Best for [specific use case] (mini-review)
4. #2 through #N Alternative sections
5. Feature Deep Comparison Table
6. Pricing Comparison
7. Migration Guide (how to switch)
8. FAQ

Key Differentiators:
- "Switch Score" (migration difficulty, 1–5)
- "Better For" tags (which alternative beats original at what)
- Pricing savings calculator
```

**Blueprint C: Location Pages**
```
Content Structure:
1. Quick Picks (top 3 for this location)
2. Full Comparison Table
3. Location-Specific Considerations (data laws, servers, payments)
4. Individual Provider Sections (local currency, local support)
5. Location-Specific FAQ
6. Related Location Pages (neighboring regions)

Key Differentiators:
- Localized pricing in native currency
- Compliance/regulation notes specific to location
- Server/infrastructure location data
```

**Blueprint D–G: Directory, Template, Glossary, Integration**
— See `references/page-model-templates.md` for full structures.

### 3. Quality Gates (MANDATORY Before Publication)

| Gate | Rule | Failure Action |
|------|------|----------------|
| Minimum unique content | ≥300 words unique per page | Don't publish |
| Similarity threshold | ≤70% similarity between siblings | Consolidate or differentiate |
| Human usefulness test | "Would a real person bookmark this?" | Don't publish if no |
| Thin content | <200 unique words | `noindex` |
| Near-duplicate | >85% similarity to another page | Consolidate or differentiate |

### 4. Technical Implementation

**URL Structure (use subfolders, NOT subdomains):**
```
/compare/{a}-vs-{b}/              → Comparison pages
/alternatives/{product}/           → Alternative pages
/best/{service}-in-{location}/    → Location pages
/{category}/                        → Directory hubs
/{category}/{subcategory}/         → Directory sub-pages
/glossary/{term}/                  → Glossary pages
/integrations/{a}-plus-{b}/       → Integration pages
```

**Rules:** hyphens only, lowercase, ≤75 chars, primary keyword in URL, consistent patterns.

**Sitemap Architecture:**
```
/sitemap.xml                   → Index of sub-sitemaps
/sitemap-comparisons.xml       → All comparison pages
/sitemap-alternatives.xml      → All alternative pages
/sitemap-locations.xml         → All location pages
/sitemap-directory.xml         → All directory pages
/sitemap-glossary.xml          → All glossary pages
/sitemap-integrations.xml      → All integration pages
/sitemap-static.xml            → Blog, about, contact
```

**Rules:** Max 50K URLs per sitemap, include `<lastmod>`, split by model, auto-generate, remove noindexed pages.

**Canonical Strategy:**
- Self-referencing canonical on every page (mandatory)
- If >85% similar, canonical lower-value to higher-value
- A-vs-B and B-vs-A → redirect one to the other
- Absolute URLs, HTTPS, no parameters

**Internal Linking Rules:**
| From | Link To | Anchor Text |
|------|---------|-------------|
| Comparison page | Both product pages + 3–5 related comparisons + category directory | Exact-match or descriptive |
| Alternative page | Target product comparisons + each alternative's comparisons + category | Varied, descriptive |
| Location page | Neighboring locations + provider comparisons + category | Location-specific |
| Glossary page | Related terms (bidirectional) + tools mentioned + category | Term names |

**Page Speed Requirements:**
- LCP <2.5s, FID <100ms, CLS <0.1
- Page weight <1MB total
- TTFB <200ms
- SSG or ISR for all programmatic pages
- Lazy-load images, WebP compression, CDN for assets

### 5. Monitoring & Optimization

**Indexation Tracking:**
| Indexation Rate (30 days) | Action |
|--------------------------|--------|
| >90% | Healthy — continue publishing |
| 70–90% | Audit quality, check thin content flags |
| <70% | Stop publishing, diagnose and fix |

**Ranking Distribution:**
| Metric | Threshold | Action |
|--------|-----------|--------|
| >20% pages not ranking | Review template quality |
| Average position declining | Check competitor updates |
| Page drops from top 10 | Immediate audit and refresh |

**Monthly Maintenance:**
- Thin content detection (crawl + similarity check)
- Cannibalization monitoring (GSC keyword overlap)
- Pricing/feature data refresh
- Performance metrics review (CTR, conversion rate, revenue/page)

### 6. Complete Build Workflow

```
PHASE 1: VALIDATE (1–2 weeks)
├── Identify repeatable search pattern
├── Validate demand (SERP, autocomplete)
├── Assess data availability
├── Run scalability scorecard
└── GO / NO-GO decision

PHASE 2: DESIGN (1–2 weeks)
├── Select page model
├── Design URL structure
├── Build content template
├── Define data schema
├── Design internal linking graph
├── Write 3 pilot pages manually
└── Validate with quality gates

PHASE 3: BUILD (2–4 weeks)
├── Build data pipeline (APIs, scraping, research)
├── Build page generator (Python)
├── Build quality gate pipeline
├── Build sitemap generator
├── Build internal linking automation
└── Generate pilot batch (20–50 pages)

PHASE 4: LAUNCH (1 week)
├── Publish pilot batch
├── Submit sitemaps
├── Monitor indexation (wait 2 weeks)
├── Run quality audit on indexed pages
└── Fix any issues found

PHASE 5: SCALE (ongoing)
├── Publish in batches of 50–100
├── Monitor indexation per batch
├── Monthly quality + cannibalization audits
├── Optimize underperformers
├── A/B test template improvements
└── Update pricing/features monthly
```

## Common Mistakes & Anti-Patterns

| Anti-Pattern | Consequence | Prevention |
|-------------|-------------|-----------|
| Starting with volume ("10,000 pages!") | Thin content, Google penalty | Start with usefulness, pass quality gates |
| No meaningful data differentiation | Pages are near-duplicates | ≥3 unique data points per page |
| Ignoring crawl budget | Slow indexation, waste | Strategic noindex, sitemap split |
| Publishing all at once | Can't diagnose batch issues | Publish 50–100, monitor, then next batch |
| Neglecting internal linking | No link equity to pages | Auto-generate linking graph |
| Stale pricing/features | Loss of trust, poor rankings | Monthly refresh cadence |
| Over-templating | Pages feel robotic | Editorial judgment layer on top |
| No quality gate before publish | Google sees thin/duplicate content | Automated checks, mandatory |
| Ignoring cannibalization | Competing pages rank poorly | Monthly overlap monitoring |

## Output Contract

| Field | Description |
|-------|-------------|
| **Artifact** | pSEO page template with quality gates, URL structure, and internal linking graph |
| **Evidence** | Template output sample, quality checklist passed, pilot batch validation |
| **Decision** | Template approved for scale or requires iteration |
| **Next** | Deploy pilot batch → monitor indexation → scale in batches |

## Verification Steps

1. Validate pilot pages pass all quality gates
2. Check that each pilot page has ≥40% unique content
3. Verify URL structure follows naming conventions
4. Confirm internal links are correct and functional
5. Submit pilot sitemap and monitor indexation for 2 weeks
6. Run thin content detection on pilot batch
7. Check for cannibalization between pilot pages and existing content

## Resources

- `references/page-model-templates.md` — Detailed HTML structures and Python generation scripts
- `references/quality-gates.md` — Quality gate system with Python scripts
- `references/affiliate-programmatic-patterns.md` — Affiliate-specific patterns and monetization structures

## Self-Critique Scorecard (/25)
After every operation, score yourself:
1. **Functionality** (1-5): Does it work perfectly and meet all requirements?
2. **Quality** (1-5): Is it enterprise-grade and production-ready?
3. **Verification** (1-5): Was it verified via multiple methods (API + live + visual)?
4. **Speed** (1-5): Was execution optimal with parallel operations where possible?
5. **Learning** (1-5): Were new patterns documented and memory updated?

**Target: 22+/25 before claiming completion**

### Quality Checklist
- [ ] Pre-flight checks completed (credentials, target exists, rollback plan)
- [ ] Operation verified via API response + live page check
- [ ] Anti-patterns checked (no common mistakes)
- [ ] Scorecard completed and logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered

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

## Speed Optimizations
- **API calls**: Always use `_fields` parameter (80%+ payload reduction)
- **Pagination**: Use `per_page=100` for list endpoints
- **Parallelism**: Use `concurrent.futures` for independent operations (max 10/site)
- **Caching**: Store results in session — never re-fetch same data
- **Batching**: Group similar operations into single API calls where possible
- **Direct CLI**: Use WP-CLI `wp db query` for complex operations

## Error Recovery (Auto-Learning)
- Track error patterns — after 2 failures, try alternative approach
- Log recurring fixes to `memory/YYYY-MM-DD.md`
- Update references when new patterns discovered
- Rollback plan: Know how to undo before making changes

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

## Output Contract
- **Artifact**: What was created/changed/deleted
- **Evidence**: API response proof + live verification
- **Decision**: Success/failure with reasoning
- **Next**: What follow-up is needed (if any)
