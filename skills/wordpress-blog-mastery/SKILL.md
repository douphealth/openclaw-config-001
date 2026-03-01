| name | description | version |
|------|-------------|--------|
| wordpress-blog-mastery | SOTA enterprise-grade blog content creation, optimization, and lifecycle management. Handles full-article generation (H1-H16 hierarchy), semantic refresh logic, multi-step editorial quality gates, automated internal linking, schema markup generation, and visual asset orchestration. Use for all blog content strategy, creation, and optimization workflows. | 4.0 |

# WordPress Blog Mastery

Enterprise-grade content orchestration engine for SOTA blog post creation, optimization, and lifecycle management. Combines high-fidelity article drafting, semantic-refresh logic, multi-pass editorial gates, and automatic schema/imagery coordination.

## Own

- **High-fidelity article drafting (H1-H16 hierarchy)** — Hormozi/Ferriss narrative style, max 12-word first sentences per section, direct benefit-first messaging
- **Contextual internal linking** — Auto-inject 5+ internal links per article using topic-cluster intelligence from sitemap analysis
- **Multi-step editorial quality gates** — Accuracy (fact-check), tone (conversational), structure (scannable), and schema compliance
- **Automated schema markup generation** — JSON-LD ArticleSchema, ReviewSchema (if applicable), FAQSchema, BreadcrumbSchema with dynamic entity linking
- **Metadata generation** — Title, Meta Excerpt, OpenGraph, Twitter Card, schema-ready descriptions
- **Semantic refresh logic** — Update existing posts with new entities, re-optimize structure, inject current data
- **Programmatic page generation** — Auto-create schema-ready formatting, heading hierarchy, section organization
- **Visual asset coordination** — Image placement cues, alt-text generation, featured image specs (if visual assets skill engaged)
- **SEO/AEO/GEO compliance** — Target search intent, AI-answer-engine optimization (featured snippets, People Also Ask), geo-signals
- **Internal linking graph intelligence** — Use existing link graph to recommend contextual links, avoid orphan clusters

## Do NOT Own

- **Imagery/asset production** (wordpress-visual-assets)
- **SEO keyword research/strategy** (seo-intelligence)
- **Technical site health** (technical-seo-health)
- **Social media distribution** (automation-ops)
- **Affiliate link insertion logic** (conversion-optimizer) — blog writer suggests affiliate opportunities but doesn't insert them

## Decision Matrix: Which Workflow to Run

| Signal | Workflow | Priority |
|--------|----------|----------|
| New blog topic + keyword | Full-Article Draft Mode | P1 |
| Article score <85 (quality) | Multi-Pass Editorial Gate | P1 |
| Post >12 months old + new rank data | Semantic Refresh Mode | P1 |
| High-traffic post + outdated info | Evidence Audit + Refresh | P2 |
| New internal link opportunity (from growth) | Graph Update Mode | P1 |
| Visual assets ready for integration | Image Embed + Alt-Text Mode | P2 |
| Affiliate product reviewed in article | Conversion Handoff Mode | P0 (pass to conversion-optimizer) |

## Workflow 1: Full-Article Draft Mode

**Goal:** Generate a single, SOTA blog post (2500–4000 words) that ranks P1 for target keyword and drives conversions.

**Input:**
```
Keyword: "[TARGET_KEYWORD]"
Search Intent: [commercial|informational|transactional]
Target URL Slug: /[slug]/
Author Bio: [NAME, credentials]
Internal Links: [List of 5–8 contextual URLs from sitemap]
Product/Review Data (optional): {
  affiliate_link: "[URL]",
  image_url: "[IMG_URL]",
  product_name: "[NAME]"
}
```

**Execution:**

1. **Intent + Outline Phase** → Analyze search intent, create 12-section outline (intro, 8 core sections, FAQ, verdict, CTA)
2. **Fact-Ground Phase** → Compile authoritative sources, product specs, internal references from sitemap
3. **Draft Phase** → Generate full article in Hormozi/Ferriss style:
   - Opening hook (max 12 words, benefit-first)
   - Each H2/H3 opens with insight, not definition
   - Conversational tone, short paragraphs (2–3 sentences max)
   - Real-world examples (no fake stories)
   - 5+ contextual internal links embedded naturally
4. **Schema + Metadata Phase** → Generate JSON-LD (ArticleSchema, ReviewSchema if applicable, FAQSchema)
5. **Quality Gate Phase** → Check accuracy, tone, structure, schema compliance (see Editorial Gate Checklist below)
6. **Output:** Clean HTML (no citation markers), markdown, + JSON-LD bundle

### Editorial Gate Checklist

- [ ] **Accuracy:** All facts match cited sources (no hallucinations, no "it is said"-type vagueness)
- [ ] **Tone:** Conversational, direct, no corporate fluff. First sentence of each section ≤12 words.
- [ ] **Structure:** 12+ sections, clear hierarchy (H1 → H2 → H3), scannable with bolded key terms
- [ ] **Internal Links:** 5+ links to contextual content from sitemap (never broken URLs)
- [ ] **Schema:** JSON-LD ArticleSchema valid, FAQSchema only if FAQ exists on-page, ReviewSchema only if visible review exists
- [ ] **Visual Slots:** Clear image placeholder comments (e.g., `<!-- IMAGE: Step 1 photo here, alt="..." -->`)
- [ ] **CTA:** Strong, specific call-to-action (e.g., "Try [product] today" not "learn more")
- [ ] **Affiliate Readiness:** Product sections flagged for affiliate conversion-optimizer handoff

## Workflow 2: Multi-Pass Editorial Gate

**Goal:** Elevate any article from good (70+) to SOTA (95+) quality.

**Execution:**

1. **Pass 1 — Fact-Check** → Verify all claims against primary sources, remove vague language
2. **Pass 2 — Structure Audit** → Ensure H1 → H2 → H3 hierarchy, break up long sections, add subheadings
3. **Pass 3 — Tone Alignment** → Rewrite opening sentences, inject Hormozi/Ferriss style, remove corporate language
4. **Pass 4 — Internal Link Injection** → Add 3–5 contextual links from sitemap (use existing link graph to avoid orphans)
5. **Pass 5 — Schema Compliance** → Validate ArticleSchema, FAQSchema (only if FAQ visible), ReviewSchema (only if review visible)
6. **Pass 6 — Visual + CTA** → Add image placeholder comments, strengthen CTA, flag for affiliate conversion
7. **Output Score:** Re-grade article (target: 95+); if <90, loop back to Pass 1

## Workflow 3: Semantic Refresh Mode

**Goal:** Update old (>12 month) articles with new entities, current data, and re-optimized structure.

**Trigger:** Combination of:
- Article age >12 months
- New rank data available (from SEO-intelligence skill)
- New internal link opportunities identified
- New product reviews or case studies available

**Execution:**

1. **Data Audit Phase** → Scan current article for outdated stats, old product versions, broken links
2. **New Entity Injection** → Add new studies, products, case studies published since article creation
3. **Structure Re-Optimization** → Update heading hierarchy if SERP intent has shifted, add new FAQ items
4. **Re-Link Phase** → Inject new internal links from recent content (3+ new links if available)
5. **Schema Update** → Refresh dateModified, add new entities, validate schema compliance
6. **Output:** Updated article with change summary (for editorial review)

## Workflow 4: Evidence Audit + Refresh

**Goal:** For high-traffic posts (>1K monthly), ensure ALL claims are current and source-verified.

**Execution:**

1. **Evidence Scan** → Extract all factual claims from article
2. **Source Verification** → Check if sources still exist, if data is still current (e.g., product pricing, scientific studies)
3. **Fact Update** → Replace outdated stats, specs, or recommendations
4. **Visual Evidence** → Flag if screenshots/images are outdated (e.g., old UI, discontinued products)
5. **Output:** Updated article + evidence report (which claims were updated, which sources are now primary)

## Workflow 5: Graph Update Mode

**Goal:** Leverage internal link graph intelligence to recommend contextual links and prevent orphan content clusters.

**Execution:**

1. **Graph Analysis** → Map topic clusters from sitemap (e.g., "running shoes" → related posts: reviews, training guides, injury prevention)
2. **Link Opportunity Scan** → Identify unlinked posts that contextually match current article
3. **Link Injection** → Add 2–3 new contextual links to related articles (never force irrelevant links)
4. **Bi-Directional Check** → Suggest backlinks from related articles to this post
5. **Output:** Updated article + backlink suggestions for related articles

## Workflow 6: Image Embed + Alt-Text Mode

**Goal:** Integrate visual assets (from wordpress-visual-assets skill) with automated alt-text and SEO-optimized image metadata.

**Input:**
```
Image URLs: [URL1, URL2, ...]
Image Placement Cues: ["After intro", "In Step 2 section", ...]
Product Images: [affiliate product images with alt-text specs]
```

**Execution:**

1. **Placement** → Insert images at optimal locations (after intro, mid-article, before CTA)
2. **Alt-Text Generation** → Create SEO-optimized, descriptive alt text (max 125 chars, includes keyword if natural)
3. **Image Metadata** → Add title, caption, filename optimization
4. **Output:** Updated article with embedded images, alt-text, captions

## Workflow 7: Conversion Handoff Mode

**Goal:** Flag product reviews and affiliate opportunities for conversion-optimizer skill handoff.

**Execution:**

1. **Identify Affiliate Sections** → Mark any product mentions, comparisons, or recommendations
2. **Create Conversion Brief** → For each affiliate opportunity:
   ```
   Product: [NAME]
   Current Text: [EXCERPT]
   Suggested CTA: [e.g., "Check Price on Amazon"]
   Affiliate Link Ready: [YES/NO]
   Visual Asset Needed: [e.g., product box design]
   ```
3. **Output:** Article + Conversion Handoff Brief (pass to conversion-optimizer)

## Quality Metrics

| Metric | Target | How Measured |
|--------|--------|---------------|
| Accuracy Score | 98%+ | Fact-check against primary sources |
| Readability (Flesch-Kincaid) | Grade 8–10 | Auto-calculated via tool |
| Internal Links | 5–8 per article | Count + context relevance |
| Schema Validity | 100% | JSON-LD validator pass |
| CTA Specificity | Yes/No | Manual: Does CTA name product/action? |
| Visual Alignment | Yes/No | Manual: Do images match content intent? |
| SERP Intent Match | High/Medium/Low | Compared to top 5 SERP results |
| Affiliate Handoff Rate | 80%+ | % of product sections flagged for conversion |

## Integration with Other Skills

1. **seo-intelligence** → Provide keyword data, SERP competitor analysis, long-tail keyword variations
2. **wordpress-visual-assets** → Receive image URLs, alt-text specs, placement cues
3. **technical-seo-health** → Receive site health alerts (broken links, indexation issues) to incorporate into refresh logic
4. **conversion-optimizer** → Hand off product/affiliate sections with conversion brief
5. **automation-ops** → Receive "post ready for publishing" signal to schedule distribution
6. **content-architect** → Receive pillar/cluster strategy to align with internal link graph

## Execution Checklist

- [ ] Keyword intent analyzed + outline created
- [ ] 5+ authoritative sources compiled (no hallucinations)
- [ ] Article drafted in Hormozi/Ferriss style
- [ ] Internal links contextualized (5+ per article)
- [ ] JSON-LD schema generated + validated
- [ ] All facts fact-checked (98%+ accuracy)
- [ ] Affiliate sections flagged for conversion handoff
- [ ] Visual asset placeholders added
- [ ] Quality gate passed (95+ score)
- [ ] Ready for wordpress-visual-assets integration
- [ ] Ready for publishing workflow (automation-ops)
