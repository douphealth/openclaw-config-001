---
name: content-strategy-planning
description: Use when planning content strategy, topic clusters, editorial priorities, keyword research, cannibalization prevention, or content systems tied to traffic, leads, authority, affiliate revenue, or product education. Triggers on requests for content ideas, blog strategy, topic planning, content calendars, pillar content, keyword research, content gap analysis, cannibalization checks, affiliate content planning, or deciding what to publish next.
---

# Content Strategy Planning — Enterprise Framework

## Do NOT Use This For
- writing or editing individual articles (use conversion-copywriting or editorial-post-enhancement)
executing SEO technical fixes (use seo-audit-playbook or schema-ops)

## Purpose

Turn business goals, customer language, search demand, and competitive gaps into a prioritized, cannibalization-safe content plan that builds topical authority and drives measurable outcomes.

## Use This When

- Planning what content to create (not drafting the final piece)
- Keyword research, clustering, or SERP analysis
- Building topic cluster architectures
- Checking for keyword cannibalization before publishing
- Analyzing content gaps vs competitors
- Prioritizing editorial backlog
- Planning affiliate content strategy (money pages, comparisons, reviews)
- Auditing existing content inventory for consolidation opportunities

Do **not** use this skill for single-page copywriting; use `conversion-copywriting`.
Do **not** use this skill for upgrading one existing article end-to-end; use `editorial-post-enhancement`.

---

## 1. Keyword Research Methodology

### 1.1 Seed Keyword Expansion

Start with 3–10 seed terms from customer language, product features, and business goals.

**Expansion sources (in priority order):**
1. Customer questions from support, sales calls, reviews
2. Competitor page titles and H2s
3. Google Autocomplete + "People Also Ask"
4. Related searches at bottom of SERPs
5. Forum/Reddit/Quora phrasing patterns

**Expansion technique — modifier matrices:**

Build a grid of seed × modifier to generate keyword candidates:

| Seed | Modifiers |
|------|-----------|
| {product} | best, review, vs, alternative, pricing, setup, tutorial, for {use case} |
| {problem} | how to, fix, troubleshoot, prevent, why |
| {category} | comparison, guide, checklist, template, examples |

**Example for a hosting affiliate site:**
- Seed: "wordpress hosting"
- Expansion: "best wordpress hosting", "wordpress hosting vs cloud hosting", "wordpress hosting for high traffic", "cheap wordpress hosting", "wordpress hosting review", "wordpress hosting pricing", "managed wordpress hosting"

### 1.2 Keyword Clustering

Group keywords that share the same search intent and SERP overlap. One page targets one cluster.

**Clustering rules:**
- If top-5 SERP results overlap ≥60% between two keywords → same cluster
- If modifiers are purely formatting (guide, tutorial, how to) but intent is identical → same cluster
- If commercial vs informational intent differs → separate clusters

**Cluster naming convention:** `{topic}-{intent}` — e.g., "wordpress-hosting-commercial", "wordpress-setup-informational"

See `references/keyword-clustering-methodology.md` for the full algorithm and Python implementation.

### 1.3 Intent Classification

Classify every keyword cluster into one of four intents:

| Intent | SERP Signals | Content Format | Monetization |
|--------|-------------|----------------|-------------|
| **Informational** | Wikipedia, guides, how-tos | Tutorial, guide, explainer | Email capture, internal links to money pages |
| **Commercial Investigation** | Reviews, comparisons, "best" lists | Roundup, vs page, review | Affiliate links, product CTAs |
| **Transactional** | Pricing pages, buy buttons, product pages | Product page, landing page | Direct conversion |
| **Navigational** | Brand site, login pages | Not targetable (brand owns it) | N/A |

**Decision rules:**
- If SERP shows "best X" lists → commercial intent, create roundup
- If SERP shows Wikipedia or in-depth guides → informational, create guide
- If SERP shows product/pricing pages → transactional, create product or comparison page
- If SERP shows brand pages only → skip (navigational, low opportunity)

### 1.4 Volume vs Keyword Difficulty Scoring

Score each cluster on a 2×2 matrix:

```
          High Volume
               │
    Quick Win  │  Competitive Play
    (Do First) │  (Strategic Investment)
               │
───────────────┼──────────────────────
               │
    Long-tail  │  Low Priority
    Niche      │  (Skip unless needed
               │   for topical authority)
               │
          Low Volume
    Low KD         High KD
```

**Scoring formula:**
```
Priority Score = (Monthly Volume × Commercial Value × Intent Multiplier) / (KD Score × Competition Density)

Intent Multiplier:
- Transactional: 3.0
- Commercial Investigation: 2.5
- Informational: 1.0
- Navigational: 0.0

Commercial Value (1-5 scale):
- Direct revenue keyword (buy, pricing, best X): 5
- Lead gen keyword (vs, comparison, review): 4
- Mid-funnel (how to use, setup, for X use case): 3
- Top-funnel awareness (what is, history): 1
```

---

## 2. Cannibalization Prevention (CRITICAL)

**This is the #1 content strategy mistake.** Publishing a new page that targets the same keyword as an existing page causes both to rank poorly.

### 2.1 Pre-Publish Cannibalization Check — Decision Tree

```
New keyword cluster identified
│
├── Step 1: Search site for existing coverage
│   └── Query: site:{domain} "{primary keyword}"
│   └── Query: site:{domain} "{secondary keywords}"
│   └── Check title tags, H1s, and URL slugs for overlap
│
├── Step 2: Evaluate existing page performance
│   ├── Existing page ranks in top 20?
│   │   ├── YES → Check if it fully satisfies intent
│   │   │   ├── Intent fully satisfied → EXPAND existing page (add new section)
│   │   │   ├── Intent partially satisfied → EXPAND existing page + improve intent match
│   │   │   └── Intent mismatch (wrong angle) → CREATE new page + add canonical or 301 old
│   │   └── NO (not ranking) → Check why
│   │       ├── Thin content → EXPAND existing page
│   │       ├── Wrong intent → CREATE new page, 301 or noindex old
│   │       └── Technical issue → FIX technical, then reassess
│   │
├── Step 3: Check URL overlap
│   ├── URLs contain same primary keyword slug?
│   │   ├── YES → Consolidate or differentiate slugs
│   │   └── NO → Continue
│   │
├── Step 4: Internal link audit
│   ├── Both pages linked with same anchor text?
│   │   ├── YES → Diversify anchors or consolidate
│   │   └── NO → Continue
│   │
└── Decision:
    ├── EXPAND existing page (preferred when existing page has authority)
    ├── CREATE new page (when no existing coverage or clear intent gap)
    └── CONSOLIDATE (when multiple thin pages target same cluster)
```

### 2.2 Existing Content Inventory

Before any content planning session, build a content inventory:

```python
# Content inventory fields required:
inventory = {
    "url": "",
    "title": "",
    "primary_keyword": "",
    "secondary_keywords": [],
    "intent": "",
    "current_rank": None,  # position or None
    "organic_traffic_monthly": 0,
    "word_count": 0,
    "last_updated": "",
    "internal_links_in": 0,
    "backlinks": 0,
    "status": "active"  # active, consolidate, redirect, noindex
}
```

**Consolidation triggers:**
- 2+ pages targeting same primary keyword → merge into one
- Page with <500 words targeting a competitive cluster → expand or fold into stronger page
- Page with 0 traffic after 6+ months → audit for redirect or noindex

### 2.3 Keyword Overlap Check Algorithm

See `references/cannibalization-prevention-checklist.md` for the full pre-publish checklist and overlap detection methodology.

**Quick overlap test (Python):**

```python
def check_overlap(new_keywords: list[str], existing_content: dict) -> dict:
    """
    Check if new keywords overlap with existing content.
    existing_content: {url: {"primary_keyword": str, "secondary_keywords": list}}
    Returns: {url: {"overlap_keywords": list, "overlap_score": float, "action": str}}
    """
    results = {}
    new_set = set(k.lower().strip() for k in new_keywords)

    for url, data in existing_content.items():
        existing = {data["primary_keyword"].lower().strip()}
        existing.update(k.lower().strip() for k in data.get("secondary_keywords", []))

        overlap = new_set & existing
        if overlap:
            score = len(overlap) / len(new_set)
            if score > 0.5:
                action = "EXPAND existing page instead of creating new"
            elif score > 0.2:
                action = "REVIEW — partial overlap, check intent alignment"
            else:
                action = "LOW RISK — minor overlap, monitor"
            results[url] = {
                "overlap_keywords": list(overlap),
                "overlap_score": round(score, 2),
                "action": action
            }

    return results
```

---

## 3. Topic Cluster Architecture

### 3.1 Pillar Page Structure

Each content pillar has:
- **1 Pillar Page** (2000–5000 words, targets broad head term)
- **5–15 Supporting Pages** (1000–2500 words, target long-tail clusters)
- **Hub-and-spoke linking**: Pillar links to all spokes, each spoke links back to pillar + 2–3 sibling spokes

```
                    ┌──────────────┐
                    │  PILLAR PAGE │
                    │  "WordPress  │
                    │   Hosting"   │
                    └──────┬───────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
     ┌──────▼─────┐ ┌─────▼──────┐ ┌─────▼──────┐
     │ Best WP    │ │ WP Hosting │ │ WP Hosting │
     │ Hosting    │ │ vs Cloud   │ │ for High   │
     │ 2026       │ │ Hosting    │ │ Traffic    │
     └──────┬─────┘ └─────┬──────┘ └─────┬──────┘
            │              │              │
     ┌──────▼─────┐ ┌─────▼──────┐ ┌─────▼──────┐
     │ Bluehost   │ │ WP Hosting │ │ Managed WP │
     │ Review     │ │ Pricing    │ │ Setup      │
     │            │ │ Guide      │ │ Tutorial   │
     └────────────┘ └────────────┘ └────────────┘
```

### 3.2 Topical Authority Signals

Google increasingly rewards sites that demonstrate comprehensive coverage of a topic. Build authority through:

1. **Breadth**: Cover all major subtopics within a pillar
2. **Depth**: Go deeper than competitors on each subtopic
3. **Interconnection**: Strong internal link graph within clusters
4. **Freshness**: Regular updates to evergreen content
5. **Entity coverage**: Mention and explain all related entities, tools, concepts

**Topical authority checklist per pillar:**
- [ ] Pillar page published and ranking
- [ ] ≥5 supporting pages live with internal links to pillar
- [ ] All primary entities mentioned on pillar page
- [ ] FAQ section covers PAA questions for head term
- [ ] Schema markup: Article + FAQPage + BreadcrumbList
- [ ] At least 2 comparison/versus pages in cluster
- [ ] At least 1 tutorial/how-to page in cluster
- [ ] At least 1 review page in cluster (if commercial)

### 3.3 Internal Linking Protocol

**From pillar to spokes:** "For more on [specific subtopic], see our guide to [spoke title]."

**From spoke to pillar:** "This is part of our complete guide to [pillar topic]."

**Between spokes:** "If you're comparing options, see our [related spoke title]."

**Anchor text rules:**
- Pillar → spoke: Use exact-match or close variant of spoke's primary keyword
- Spoke → pillar: Use pillar's primary keyword (natural phrasing)
- Spoke → spoke: Use varied, descriptive anchors (avoid exact-match repetition)

---

## 4. Content Gap Analysis

### 4.1 Competitor Gap Analysis Process

1. Identify 3–5 top-ranking competitors in your niche
2. Export their top organic keywords (via Ahrefs, SEMrush, or manual SERP analysis)
3. Build a keyword universe: union of all competitor keywords
4. Subtract keywords you already rank for (positions 1–20)
5. Remaining = content gaps

**Manual gap analysis (no tools):**

```python
def find_content_gaps(competitor_keywords: dict[str, list], 
                       your_ranking_keywords: set) -> list[dict]:
    """
    competitor_keywords: {"competitor1.com": ["kw1", "kw2", ...], ...}
    your_ranking_keywords: {"kw1", "kw2", ...}
    Returns prioritized gap list.
    """
    all_competitor_kws = set()
    kw_sources = {}  # keyword -> [competitors ranking for it]

    for competitor, keywords in competitor_keywords.items():
        for kw in keywords:
            all_competitor_kws.add(kw.lower().strip())
            kw_sources.setdefault(kw.lower().strip(), []).append(competitor)

    gaps = all_competitor_kws - your_ranking_keywords

    prioritized = []
    for kw in gaps:
        competitor_count = len(kw_sources.get(kw, []))
        prioritized.append({
            "keyword": kw,
            "competitors_ranking": competitor_count,
            "priority": "HIGH" if competitor_count >= 3 else "MEDIUM" if competitor_count == 2 else "LOW"
        })

    return sorted(prioritized, key=lambda x: x["competitors_ranking"], reverse=True)
```

### 4.2 SERP Opportunity Analysis

For each gap keyword, analyze the SERP for opportunity signals:

**High opportunity signals:**
- Top 3 results are thin (<1500 words) or outdated (>18 months)
- No featured snippet (or weak snippet you can beat)
- Results are from low-authority sites (DR <40)
- Multiple results have poor Core Web Vitals
- PAA questions are unanswered by current results

**Low opportunity signals:**
- Top 3 results are all DR 70+ sites with 3000+ word guides
- Featured snippet is locked by Wikipedia/official source
- All results recently updated
- SERP dominated by brand pages (navigational intent)

### 4.3 Missing Entity Analysis

After reviewing top-10 SERP results for your target keyword, identify:

1. **Entities mentioned by competitors but missing from your content:**
   - Tools, software, brands
   - Concepts, terminology, frameworks
   - People, companies, organizations
   - Statistics, data points, studies

2. **Questions answered by competitors but not by you** (from PAA, H2s, FAQ sections)

3. **Subtopics covered by competitors at length but skipped by you**

**Entity gap fill script:**

```python
from collections import Counter

def find_missing_entities(your_entities: list[str], 
                          competitor_entities: dict[str, list[str]]) -> list[dict]:
    """
    your_entities: entities mentioned in your content
    competitor_entities: {"competitor1": [entity1, entity2, ...], ...}
    """
    your_set = set(e.lower().strip() for e in your_entities)
    
    entity_frequency = Counter()
    for competitor, entities in competitor_entities.items():
        for entity in entities:
            entity_frequency[entity.lower().strip()] += 1

    missing = []
    for entity, freq in entity_frequency.most_common():
        if entity not in your_set:
            coverage = freq / len(competitor_entities)
            missing.append({
                "entity": entity,
                "competitors_using": freq,
                "coverage_pct": round(coverage * 100),
                "priority": "HIGH" if coverage >= 0.6 else "MEDIUM" if coverage >= 0.3 else "LOW"
            })

    return missing
```

---

## 5. Content Prioritization Framework

### 5.1 Impact × Effort Scoring

Score every content idea on two axes:

**Impact (1–10):**
- Search volume potential: 1–3 (low/med/high)
- Commercial value: 1–3 (awareness/consideration/conversion)
- Topical authority contribution: 1–2 (supports pillar / standalone)
- Competitive advantage: 1–2 (unique angle or weak competition)

**Effort (1–10):**
- Content complexity: 1–3 (simple list / guide / deep research)
- Production requirements: 1–3 (text only / needs graphics / needs data)
- Expertise required: 1–3 (generalist / specialist / expert interview)
- Update frequency: 1 (evergreen) or 2 (needs regular updates)

```
Priority = Impact Score / Effort Score

Priority Bands:
- ≥2.0 → P0 (Ship immediately)
- 1.0–1.9 → P1 (Next sprint)
- 0.5–0.9 → P2 (Backlog)
- <0.5 → P3 (Skip unless strategic)
```

### 5.2 Business Value Alignment

Map every content idea to a business objective:

| Business Goal | Content Types | KPI |
|--------------|--------------|-----|
| Revenue (affiliate/direct) | Reviews, comparisons, "best" lists | Conversions, revenue per page |
| Lead generation | Guides, templates, tools | Email signups, demo requests |
| Brand authority | Original research, thought leadership | Backlinks, mentions, citations |
| SEO traffic | Informational guides, glossaries | Organic sessions, keyword rankings |
| Customer retention | Tutorials, advanced guides, changelog | Engagement, support ticket deflection |

**Rule:** Every content idea must have a clear business goal tag. If you can't identify the goal, don't create it.

### 5.3 Editorial Calendar Cadence

**Minimum viable cadence for building topical authority:**
- 2 pillar-supporting articles per week
- 1 new cluster per month (5–15 supporting articles)
- Quarterly content audit (consolidate, update, prune)
- Monthly cannibalization check on new and existing content

---

## 6. Affiliate Content Strategy

### 6.1 Content Hierarchy for Affiliate Sites

```
Level 1 — Money Pages (direct revenue)
├── "Best [Product] for [Use Case]" (roundup reviews)
├── "[Product A] vs [Product B]" (comparisons)
├── "[Product] Review" (single product deep-dives)
└── "[Product] Pricing" (pricing/comparison pages)

Level 2 — Supporting Pages (authority + internal links)
├── "How to Choose [Product Category]" (buying guides)
├── "[Product Category] Explained" (educational)
├── "[Use Case] with [Product]" (tutorial)
└── "[Product] Alternatives" (alternative pages)

Level 3 — Top-funnel Pages (traffic + email capture)
├── "What is [Concept]?" (definitional)
├── "[Topic] Statistics" (data posts)
├── "[Topic] Mistakes to Avoid" (awareness)
└── "[Topic] Checklist" (lead magnets)
```

### 6.2 Review Methodology

**Trust signals required in every review:**
- Hands-on testing evidence (screenshots, video, personal experience)
- Pros AND cons (balanced assessment)
- Specific use case recommendations ("Best for X, not ideal for Y")
- Pricing transparency (actual costs, hidden fees)
- Alternative recommendations (shows you're not just pushing one product)
- Last updated date (freshness matters for commercial queries)
- Affiliate disclosure (FTC compliance)

**Review depth requirements:**
- Single product review: 1500–3000 words, cover features, pricing, pros/cons, who it's for
- Roundup review: 3000–6000 words, 5–10 products, clear winner categories
- Comparison page: 2000–4000 words, feature-by-feature table, verdict

### 6.3 Comparison Content Framework

**Structure for "[Product A] vs [Product B]":**
1. Quick verdict (TL;DR at top)
2. At-a-glance comparison table
3. Detailed feature comparison (3–5 key features)
4. Pricing comparison
5. Pros and cons of each
6. Who should choose which (use-case based)
7. FAQ section (covers PAA questions)

See `references/affiliate-content-strategy.md` for the complete affiliate content playbook.

---

## 7. SERP Feature Optimization

### 7.1 Featured Snippet Strategy

**Target snippet types by keyword intent:**

| Snippet Type | Best For | Format |
|-------------|----------|--------|
| Paragraph (40–60 words) | "What is", "How does" questions | Concise definition + context |
| Numbered list | "How to", "Steps to" | Ordered steps with H2/H3 |
| Bulleted list | "Best", "Top", "Types of" | Unordered list with brief descriptions |
| Table | "Comparison", "Pricing", "Vs" | HTML table with clear headers |

**Snippet optimization checklist:**
- [ ] Answer the question in the first 40–60 words after the heading
- [ ] Use the exact question as an H2
- [ ] Format answer in the target snippet format (paragraph/list/table)
- [ ] Include the keyword naturally in the answer
- [ ] Follow the snippet paragraph with deeper context (keeps user on page)

### 7.2 People Also Ask (PAA) Capture

1. Search your primary keyword
2. Record all PAA questions (expand each to reveal more)
3. Create H2 sections for each PAA question
4. Answer in 40–60 words (snippet-ready) then expand
5. Use FAQPage schema markup

**PAA harvesting script:**

```python
def organize_paa_for_content(paa_questions: list[str], primary_keyword: str) -> list[dict]:
    """
    Organize PAA questions into content sections.
    """
    sections = []
    for i, question in enumerate(paa_questions):
        # Classify question type
        q_lower = question.lower()
        if q_lower.startswith("what"):
            q_type = "definition"
        elif q_lower.startswith("how"):
            q_type = "process"
        elif q_lower.startswith("why"):
            q_type = "rationale"
        elif q_lower.startswith("is") or q_lower.startswith("are"):
            q_type = "yes_no"
        elif "vs" in q_lower or "difference" in q_lower:
            q_type = "comparison"
        else:
            q_type = "general"

        sections.append({
            "h2": question,
            "type": q_type,
            "snippet_target": True,
            "suggested_word_count": 200 if q_type == "definition" else 300,
            "schema": "FAQPage"
        })

    return sections
```

### 7.3 Image Pack Optimization

- Use descriptive, keyword-rich file names (`best-wordpress-hosting-comparison.webp`)
- Write specific alt text (not just keyword stuffing)
- Compress images (WebP preferred)
- Use original screenshots, charts, and diagrams when possible
- Add image structured data where relevant

---

## 8. Complete Workflow

### Step-by-Step Content Strategy Process

```
1. INVENTORY
   └── Export existing content + rankings
   └── Identify gaps and cannibalization risks

2. RESEARCH
   └── Seed keyword expansion
   └── Competitor keyword analysis
   └── SERP feature audit

3. CLUSTER
   └── Group keywords by intent + SERP overlap
   └── Name clusters
   └── Map clusters to content types

4. ARCHITECTURE
   └── Define pillar pages
   └── Map spoke pages to pillars
   └── Plan internal linking

5. CANNIBALIZATION CHECK
   └── Run overlap detection (see Section 2)
   └── Flag expansion vs new page decisions
   └── Identify consolidation opportunities

6. PRIORITIZE
   └── Score Impact × Effort
   └── Align to business goals
   └── Order by priority score

7. OUTPUT
   └── Prioritized roadmap with rationale
   └── Content briefs for P0 items
   └── Internal linking plan
   └── Timeline + cadence
```

---

## 9. Output Format

Default output should include:
- Strategic goal
- Audience/problem framing
- Content pillars with cluster map
- Cannibalization audit results (existing pages that overlap)
- Prioritized topic list with Impact × Effort scores
- Intent classification for each cluster
- SERP feature opportunities (snippets, PAA, images)
- Entity gap analysis
- Recommended formats and distribution notes
- Internal linking plan
- Affiliate monetization strategy (if applicable)
- Content briefs for P0/P1 items
- Repurposing notes where one idea feeds multiple channels
- Recommended title/slug/meta direction when the output will become a live editorial asset
- UX/content-format notes when the page should use richer visual HTML or standout FAQ styling

---

## 10. Checks and Common Mistakes

- **NEVER publish without a cannibalization check.** This is non-negotiable.
- Do not confuse "interesting" with commercially useful.
- Do not generate topics with no clear audience or search path.
- Do not ignore existing customer language.
- Do not treat every topic as equal priority.
- Do not create new pages when expanding existing pages is the right call.
- Do not skip intent classification — wrong intent = wrong content format.
- Do not optimize for featured snippets at the expense of depth and reader value.
- Do not build topic clusters without proper internal linking.
- Do not forget affiliate disclosures on money pages.
- Do not let content go stale — audit and update quarterly.

---

## Resources

Read when needed:
- `references/keyword-clustering-methodology.md` — Keyword clustering algorithm and Python implementation
- `references/cannibalization-prevention-checklist.md` — Pre-publish cannibalization check workflow
- `references/affiliate-content-strategy.md` — Affiliate-specific content strategy and monetization
- `references/priority-model.md` — Detailed priority scoring model
- `references/research-inputs.md` — Research input gathering methodology


## Output Contract
**Artifact**: Content strategy document with topic clusters and priority ranking
**Evidence**: Keyword data, cluster rationale, cannibalization check
**Decision**: Final content plan approved
**Next**: Implementation in editorial calendar
