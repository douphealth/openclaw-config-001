---
name: enterprise-trend-blog-automation
description: Build and run fully automated enterprise-grade weekly trend-to-post publishing for WordPress portfolios. Use when discovering high-demand low-competition trending entities, mapping them to each site, generating rank-ready posts, and publishing with strict SEO/AEO/GEO, E-E-A-T, slug-pattern compliance, and verification gates.
---

# Enterprise Trend Blog Automation

Run in strict order: **Trend Discovery -> Opportunity Scoring -> Site Match -> Draft Build -> SEO/AEO/GEO Packaging -> Slug/Metadata Validation -> Publish -> Verify -> Report**.

## 1) Discovery (web-wide trend scan)
- Pull trend candidates from multi-source web signals (SERP, forums, social/news queries).
- Keep only entities/topics with:
  - high immediate demand
  - low-to-medium competition signal
  - strong business relevance to each target site
- Output: ranked shortlist per site.

## 2) Opportunity scoring (mandatory)
Score each candidate on:
- demand velocity
- competition gap
- topical relevance
- monetization/intent fit
- freshness window
Reject weak-fit candidates.

## 3) Site-fit + entity map
For each selected site:
- map candidate to existing topical clusters
- define core/supporting/contextual entities
- define internal-link targets (hub/spoke/money pages)

## 4) Content generation standard
Generate one enterprise-grade post per selected site:
- intent-matched H1
- answer-first block (40-70 words)
- minimum body length target: **>= 3000 words**
- human-sounding, high-agency editorial tone inspired by Alex Hormozi / Tim Ferriss style principles (direct, tactical, outcome-focused) without imitation or fabricated personal claims
- high-utility body with evidence + clear decision support
- FAQ section (entity-rich, unique answers)
- trust footer (method, disclosure where needed, updated date)
- visual/HTML break elements at least every **~200 words** to prevent wall-of-text scanning drop-off
- affiliate product box enrichment: resolve accurate Amazon product URL/title/image via `scripts/amazon_product_resolver.py`

## 5) SEO/AEO/GEO implementation (mandatory)
- title tag (50-65 chars)
- H1 aligned with intent (not a duplicate of title)
- meta description (145-160 chars)
- slug precision with site-specific URL pattern policy
- schema only when visible content supports it
- internal links with rich contextual anchors
- top-3 SERP gap analysis and integration of top **20 missing terms/entities** naturally into relevant sections
- semantic entity coverage across core/supporting/contextual entities with no keyword stuffing
Use: `scripts/serp_gap_top3.py`

## 6) Slug policy enforcement (critical)
Before publish:
- inspect site sitemap + existing URL conventions
- detect whether category-prefixed slug pattern is required
- generate slug matching the dominant existing structure
- never publish a slug that breaks site taxonomy convention
Use: `scripts/slug_pattern_guard.py`

## 7) Quality and risk gates
- run banned-pattern scan
- run readability + visual density checks
- run internal-link quality gate (`scripts/internal_link_quality_gate.py`)
- run post completeness gate (`scripts/post_completeness_gate.py`) with thresholds:
  - min words >=3000
  - visual blocks at least 1 per ~200 words
  - answer-first + FAQ presence required
- require quality score >=85 before publish (target >=90)

## 8) Publish + verify
- run hard blocker first: `scripts/publish_blocker.py`
- if blocker fails: do not publish
- backup target first
- atomic publish/update
- verify source + live render
- verify metadata/canonical/schema visibility
- log report with evidence paths

## 9) Outputs per run
1. trend shortlist report
2. scored opportunities report
3. per-site content brief
4. top-3 SERP gap + top20 missing terms/entities report
5. generated post package (title/H1/meta/slug/body)
6. amazon product-box resolution report (url/title/image + source)
7. publish verification report
8. blockers + next best action
