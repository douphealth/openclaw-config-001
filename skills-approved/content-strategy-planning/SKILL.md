---
name: content-strategy-planning
description: Use when planning content strategy, topic clusters, editorial priorities, keyword research, cannibalization prevention, content gap analysis, or what-to-publish-next decisions tied to traffic, leads, authority, or revenue.
---

# Content Strategy Planning

## Purpose
Turn business goals, customer language, search demand, and competitive gaps into a prioritized, cannibalization-safe content plan that drives real business outcomes — not just page counts.

## Use this when
- planning what content to create, expand, or consolidate
- doing keyword research, clustering, or content gap analysis
- building topic cluster architecture for a site or domain
- checking for cannibalization before publishing new content
- prioritizing an editorial backlog by business value
- planning affiliate, monetization, or lead-gen content systems
- designing internal-linking topology for topical authority

## Do NOT use this for
- writing or editing individual articles (→ `conversion-copywriting` or `editorial-post-enhancement`)
- executing technical SEO fixes (→ `seo-audit-playbook` or `schema-ops`)
- one-off single-page copy improvements (→ `conversion-copywriting`)
- WordPress plugin/server troubleshooting (→ `wordpress-growth-ops` or `infrastructure-ops`)

## Self-Improvement Protocol

After each strategy run:
1. **Cluster accuracy:** Did the cluster map match real SERP overlap? Note misses in `references/cluster-pattern-learnings.md`.
2. **Intent classification:** Were intent labels accurate when pages were published? Track corrections.
3. **Business value prediction:** Did high-priority topics actually perform? Log actual vs predicted.
4. **Cannibalization prediction:** Did new content cause cannibalization despite checks? Add new signal patterns.
5. **Competitive gap quality:** Were identified gaps actually achievable? Note difficulty calibration improvements.
6. **Priority model tuning:** If the top 5 topics by priority didn't perform, adjust the weighting model in `references/priority-model.md`.

## Do this

### Phase 0: Business Context & Goal Lock (< 5 minutes)

Extract the site's current state before planning:

```bash
# Site structure snapshot
wp post list --post_type=post,page --post_status=publish --fields=ID,post_title,post_type --format=csv > /tmp/site-content.csv

# Category/tag topology
wp term list category --fields=name,slug,count --format=json
wp term list post_tag --fields=name,slug,count --format=json

# Existing content count by topic (rough)
wp post list --post_type=post --post_status=publish --s="<topic>" --fields=ID,post_title
```

**Questions to answer before moving forward:**
1. What is the **primary business goal** this content supports? (organic traffic, leads, sales, authority, affiliate revenue)
2. Who is the **target reader** and what problem are they trying to solve?
3. What **conversion action** should the reader take after consuming content?
4. What is the **current topical authority** strength? (new site = 0 clusters; established = focus on gaps)
5. What **resources** are available? (writer count, publishing cadence, budget for research/tools)

### Phase 1: Seed Topic Discovery

Gather raw topic candidates from multiple sources:

#### Source 1: Customer Language Mining
```bash
# From support tickets, sales calls, community posts — manual extraction
# Record: exact phrases customers use to describe their problem
```
- Mine support tickets for recurring questions
- Extract phrases from sales call transcripts
- Review social media comments and community forum threads
- Check review sites (G2, Capterra, Trustpilot) for competitor reviews

**Output:** List of 20-50 customer-language phrases describing problems, goals, and desired outcomes.

#### Source 2: Search Demand + Search Console Truth Set
```bash
# Use available keyword tools or scrape related searches
# Core seed: primary product/service keywords
# Expand: related questions, comparisons, alternatives
# Pull Google Search Console + Bing Webmaster query/page exports when available
```
- Start with 5-10 core seed keywords
- Expand with "how to", "best", "vs", "alternative to", "template", "checklist" modifiers
- Extract People Also Ask questions from SERP
- Pull GSC and Bing Webmaster queries/pages to see what the site already partially owns
- Note search volumes and keyword difficulty

**Output:** 100-300 raw keyword candidates with volume/difficulty data plus real GSC/Bing query-page evidence where available.

#### Source 3: Competitor Content Audit
```bash
# For each top 3-5 competitor:
curl -s "https://www.google.com/search?q=site:competitor.com+<topic>&num=20" | extract titles/URLs
# Or use Screaming Frog / Ahrefs / SEMrush if available
```
- Catalog competitor's top-performing content by estimated traffic
- Identify topics they cover that you don't (content gaps)
- Note their content formats, depth, and unique angles
- Flag topics where their content is thin (opportunity to outperform)

**Output:** Competitor content map with gap analysis.

#### Source 4: Existing Content Audit
```bash
# Identify underperforming content
wp post list --post_type=post --post_status=publish --fields=ID,post_title --format=csv

# Check for thin content (< 500 words or < 1,000 words based on niche)
# Map existing content to topic clusters
# Find pages with high impressions but low clicks (CTR optimization opportunity)
```
- Categorize existing content by topic/intent
- Identify pages to update, expand, consolidate, or prune
- Flag cannibalization risk where 2+ pages target the same cluster

**Output:** Existing content map with update/consolidate/create recommendations.

### Phase 2: Keyword Clustering

Group keywords by shared intent and SERP overlap. See `references/keyword-clustering-methodology.md` for detailed methodology.

#### Quick Clustering Process
1. **Intent sort:** Group all keywords by intent type:
   - Informational: "how to", "what is", "guide", "tutorial"
   - Commercial investigation: "best", "vs", "review", "comparison"
   - Transactional: "buy", "pricing", "discount", "coupon"
   - Navigational: brand-specific searches (skip these)

2. **SERP overlap test:** For each keyword, check if the same pages rank in top 10:
   ```bash
   # Quick overlap check: do the same URLs appear for both keywords?
   # If >40% SERP overlap → same cluster (one page)
   # If <20% SERP overlap → different clusters (separate pages)
   ```

3. **Cluster naming:** Each cluster gets a clear name based on the dominant intent:
   - "Email marketing guide" (informational cluster)
   - "Best email marketing tools" (commercial cluster)
   - "Email marketing setup" (transactional/how-to cluster)

**Output:** 15-40 keyword clusters, each with a primary keyword, 3-10 secondary keywords, and clear intent label.

### Phase 3: Cannibalization Check

**CRITICAL:** Never recommend new content without this step.

```bash
# For each proposed cluster, check existing coverage:
wp post list --post_type=post,page --post_status=publish --s="<primary keyword>" --fields=ID,post_title,post_type

# Check if existing pages target the same keyword:
# - Same H1/title pattern
# - Same target keyword in SEO plugin meta
# - Same topic/angle
```

**Decision tree:**
```
Existing page targets same cluster?
├─ YES, page is ranking well → UPDATE/EXPAND existing page (don't create new)
├─ YES, page is ranking poorly → CONSOLIDATE: update existing or replace with better
├─ YES, multiple pages target same cluster → CONSOLIDATE into one authoritative page
└─ NO existing coverage → SAFE to CREATE new content
```

See `references/cannibalization-prevention-checklist.md` for detailed checks.

### Phase 4: Opportunity Scoring

Score each cluster opportunity. See `references/priority-model.md` for the full scoring model.

**Quick scoring (5 dimensions, 1-5 each):**
| Dimension | Question | Weight |
|-----------|----------|--------|
| Business Value | Does this directly support revenue or leads? | ×3 |
| Search Demand | Is there meaningful search volume? | ×2 |
| Competition | Can we realistically rank (difficulty vs authority)? | ×2 |
| Intent Match | Does the intent align with our conversion path? | ×2 |
| Effort | How much work to create/update this content? | ×1 (inverse) |

**Priority = (Business × 3) + (Demand × 2) + (Competition × 2) + (Intent × 2) + ((6 - Effort) × 1)**

Sort clusters by priority score. Top 5-10 get scheduled first.

### Phase 5: Topic Cluster Architecture

Design the pillar/spoke structure:

**Pillar page:** Comprehensive, definitive guide on the core topic (3,000-5,000+ words)
**Spoke pages:** Specific subtopic articles that link back to the pillar (1,500-2,500 words)

```
Pillar: "Complete Guide to Email Marketing"
├─ Spoke: "Email Marketing Automation Setup"
├─ Spoke: "Best Email Marketing Tools Compared"
├─ Spoke: "Email Segmentation Strategies"
├─ Spoke: "Welcome Email Sequence Templates"
├─ Spoke: "Email Deliverability Checklist"
└─ Spoke: "Email Open Rate Benchmarks"
```

**Internal linking rules for clusters:**
- Every spoke links TO the pillar with contextual anchor text
- Pillar links TO every spoke with descriptive anchors
- Spokes link TO each other where contextually relevant (natural, not forced)
- No more than 1-2 cross-cluster links per spoke

### Phase 6: Format & Execution Planning

Assign content formats to each cluster:

| Intent | Recommended Formats |
|--------|-------------------|
| Informational | Long-form guide, how-to, tutorial, explainer |
| Commercial | Comparison, review, "best of" list, case study |
| Transactional | Landing page, product page, pricing page, demo page |
| FAQ-type | FAQ section (within pillar or standalone) |

**Publishing order:**
1. Pillar pages first (establish topical authority)
2. High-priority spokes next (capture long-tail traffic)
3. Supporting spokes last (fill gaps, internal link opportunities)
4. Update/consolidate existing content in parallel

## Core rules
- Never recommend new content without a cannibalization check.
- Do not confuse interesting topics with commercially useful topics.
- One page should target one cluster — always.
- Expand or consolidate existing pages when that beats creating new ones.
- Every topic recommendation must map to a clear business goal.
- Prioritize by business value first, then demand, then competitive opportunity.
- Design internal-linking topology with every cluster, not as an afterthought.
- Re-evaluate the priority model after each major publishing cycle.

## Output contract
**Artifact:** Content strategy document with cluster map, prioritized topic list, and publishing plan
**Evidence:** Keyword/intent rationale, cannibalization review, opportunity scoring, internal-linking topology
**Decision:** What to publish (new), expand (existing), consolidate (merge), or prune (remove)
**Next:** Create briefs for top-priority clusters, route to `conversion-copywriting` (new) or `editorial-post-enhancement` (update), or schedule the editorial backlog

## Resources
Read when needed:
- `references/keyword-clustering-methodology.md` — detailed clustering methodology with SERP overlap analysis
- `references/cannibalization-prevention-checklist.md` — comprehensive cannibalization detection and prevention
- `references/affiliate-content-strategy.md` — affiliate-specific content strategy patterns
- `references/priority-model.md` — full opportunity scoring model with calibration
- `references/research-inputs.md` — structured inputs for competitive and demand research

## Checks and common mistakes
- Skipping cannibalization review → creates duplicate content, splits authority
- Treating every topic as equal priority → wastes resources on low-value content
- Recommending new pages when an existing page should be expanded → fragments authority
- Skipping intent classification → targets wrong content format
- Planning topics with no clear audience or business path → generates traffic but not revenue
- Building clusters without internal-linking logic → misses topical authority signals
- Ignoring existing thin/underperforming content → missed pruning and consolidation opportunities
- Not checking competitor depth before recommending format → underinvesting or overinvesting
