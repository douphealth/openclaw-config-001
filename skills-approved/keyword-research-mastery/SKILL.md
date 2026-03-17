---
name: keyword-research-mastery
description: "Enterprise keyword research & opportunity discovery. Use when finding keywords, discovering ranking opportunities, building topic clusters, analyzing search intent, expanding seed keywords, identifying long-tail opportunities, planning content calendars, or researching keywords for GEO/AEO optimization. Integrates with GSC data, Google Autocomplete, SERP analysis, and competitor research. Triggers on keyword research, find keywords, topic ideas, search volume, content opportunities, what should I write about, keyword difficulty, long-tail keywords."
---

# Keyword Research Mastery — Enterprise Opportunity Discovery

## Purpose
Discover, analyze, and prioritize keywords that drive organic traffic, AI visibility, and business growth. Combines GSC data, SERP analysis, intent classification, and competitive intelligence into actionable content plans.

## When to Use
- Starting a new content strategy or campaign
- Expanding into new topics or markets
- Finding keywords for a specific product/service
- Identifying long-tail keyword opportunities from GSC data
- Building topic clusters for topical authority
- Researching keywords for GEO/AEO optimization
- Planning content calendars by priority

**Do NOT use for:** Editing existing posts (→ `editorial-post-enhancement`), technical SEO (→ `seo-audit-playbook`), GSC data pulling only (→ `seo-intelligence`).

## Triage Protocol
1. **Check GSC data first** — We already have real performance data for all sites
2. **Identify seed topics** — What core topics does the site cover?
3. **Check existing rankings** — What's already ranking (even poorly)?
4. **Find gaps** — Where are competitors ranking but we're not?
5. **Prioritize by ROI** — Volume × relevance × ease of ranking

## Inputs Required (Pre-Flight)
1. **Target site** — Which of our 10 sites?
2. **Seed keywords/topics** — Starting points for research
3. **GSC data** — Pull from cache/seo-intel/{domain}.json
4. **Competitor URLs** — Who ranks for our target terms?
5. **Business goals** — Traffic, leads, authority, or revenue?

## Phase 1: GSC Data Mining (Our Secret Weapon)

We have REAL data from GSC for all 10 sites. Mine it first:

### 1A: Find Hidden Gems in GSC
```python
import json

# Load cached GSC data
with open('cache/seo-intel/{domain}.json') as f:
    data = json.load(f)

# Queries with impressions but NO clicks (content exists but not optimized)
no_clicks = [q for q in data['top_queries'] if q['clicks'] == 0 and q['imp'] >= 10]

# Queries at position 5-15 (close to page 1)
page2 = [q for q in data['top_queries'] if 5 <= q['pos'] <= 15 and q['imp'] >= 50]

# Queries with high impressions but low CTR (position ≤10, CTR <2%)
low_ctr = [q for q in data['top_queries'] if q['pos'] <= 10 and q['ctr'] < 0.02 and q['imp'] >= 100]
```

### 1B: Cross-Site Keyword Opportunities
Compare what's working on one site to apply to others:
- plantastichaven.com: "spider plant" variants working → similar patterns on other plant content?
- gearuptofit.com: shoe reviews getting impressions → expand review content?
- efficientgptprompts.com: writing prompts ranking → more prompt categories?

## Phase 2: Keyword Discovery Methods

### Method 1: Google Autocomplete (Free, Real-Time)
```python
import requests

def get_autocomplete_suggestions(seed_keyword, lang='en'):
    """Get Google Autocomplete suggestions for seed keyword."""
    url = "http://suggestqueries.google.com/complete/search"
    params = {'client': 'firefox', 'q': seed_keyword, 'hl': lang}
    resp = requests.get(url, params=params)
    suggestions = resp.json()[1]
    return suggestions

# Expand alphabetically
def alphabet_soup(seed_keyword):
    """Get suggestions for seed + each letter."""
    results = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        suggestions = get_autocomplete_suggestions(f"{seed_keyword} {letter}")
        results.extend(suggestions)
    return list(set(results))
```

### Method 2: People Also Ask (PAA) Mining
```python
def get_paa_questions(query):
    """Extract PAA questions from Google SERP."""
    import re
    url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=headers)
    # PAA questions are in data-q attributes or specific div patterns
    questions = re.findall(r'data-q="([^"]+)"', resp.text)
    return list(set(questions))
```

### Method 3: Related Searches
Extract "Related searches" from bottom of Google SERP pages.

### Method 4: Competitor Gap Analysis
```python
def find_keyword_gaps(our_queries, competitor_pages):
    """Find queries competitors rank for that we don't."""
    our_kw_set = {q['query'] for q in our_queries}
    competitor_kws = set()
    for page in competitor_pages:
        # Extract keywords from competitor page content/title
        competitor_kws.update(extract_keywords(page))
    return competitor_kws - our_kw_set  # Keywords they have, we don't
```

### Method 5: GSC Query Expansion
```python
def expand_from_gsc(queries, min_impressions=10):
    """Use GSC queries as seeds for further expansion."""
    seeds = [q['query'] for q in queries if q['imp'] >= min_impressions]
    expanded = []
    for seed in seeds[:50]:  # Top 50 seeds
        expanded.extend(get_autocomplete_suggestions(seed))
        expanded.extend(get_paa_questions(seed))
    return list(set(expanded))
```

## Phase 3: Search Intent Classification

### 4 Intent Types + Sub-Categories

| Intent | Signal Words | Best Content Format |
|--------|-------------|-------------------|
| **Informational** | what, how, why, guide, tutorial, tips | Guides, tutorials, explainers |
| **Commercial** | best, top, vs, review, comparison, alternatives | Listicles, comparisons, reviews |
| **Transactional** | buy, price, cost, cheap, deal, discount, near me | Product pages, landing pages |
| **Navigational** | brand name, specific product, login, website | Homepage, specific page |

### Intent → Content Mapping
| Intent | Content Type | Target Length | CTA Type |
|--------|-------------|--------------|----------|
| Informational (Educational) | Definitive guide | 2,000-4,000 words | Newsletter, related content |
| Informational (How-to) | Step-by-step tutorial | 1,500-3,000 words | Tool, template download |
| Commercial (Comparison) | Vs/Alternative article | 1,500-2,500 words | Product recommendation |
| Commercial (Best) | Listicle | 2,000-3,500 words | Affiliate links |
| Transactional | Product/service page | 800-1,500 words | Buy/Sign up/Contact |

### GEO Relevance Score
Rate keyword 1-5 on likelihood to trigger AI answers:
- **5**: Definition/factual queries ("what is X", "X vs Y")
- **4**: How-to/instructional queries ("how to do X")
- **3**: Comparison queries ("best X for Y")
- **2**: Local/service queries ("X near me")
- **1**: Navigational/branded queries

## Phase 4: Keyword Scoring & Prioritization

### Priority Score Matrix

| Factor | Weight | Score 1 | Score 5 |
|--------|--------|---------|---------|
| **Search Volume** | 20% | <100/mo | >10,000/mo |
| **Keyword Difficulty** | 25% | KD >80 (hard) | KD <20 (easy) |
| **Business Relevance** | 30% | Tangential | Core offering |
| **Intent Match** | 15% | Informational only | Transactional/commercial |
| **Trend Direction** | 10% | Declining | Growing |

**Priority Score** = Σ(Weight × Score)

### Priority Categories
| Priority | Score | Action |
|----------|-------|--------|
| **P0 — Must Target** | 4.0-5.0 | Create content immediately |
| **P1 — High Value** | 3.0-3.9 | Queue for next sprint |
| **P2 — Opportunity** | 2.0-2.9 | Plan for future calendar |
| **P3 — Monitor** | 1.0-1.9 | Track but don't prioritize |

### Quick Win Detection
Keywords that are EASY wins (apply all):
- Already ranking position 5-15 → Content enrichment
- GSC shows impressions, 0 clicks → Meta title rewrite
- Low KD (<20) + decent volume (>500) → New content
- Competitor ranks, we don't → Content gap fill

## Phase 5: Topic Cluster Architecture

### Hub-and-Spoke Pattern
```
                    ┌──────────────────┐
               ┌────│ Subtopic Guide   │
               │    └──────────────────┘
               │    ┌──────────────────┐
               ├────│ How-To Tutorial  │
               │    └──────────────────┘
┌───────────┐  │    ┌──────────────────┐
│  PILLAR   │──┼────│ Comparison/Review│
│  3000+    │  │    └──────────────────┘
│  words    │  │    ┌──────────────────┐
│           │──┼────│ FAQ/Mistakes     │
└───────────┘  │    └──────────────────┘
               │    ┌──────────────────┐
               └────│ Tools/Resources  │
                    └──────────────────┘
```

### Cluster Viability Checklist
Before building a cluster:
- [ ] At least 8-12 subtopics identified
- [ ] Combined cluster volume >5,000/month
- [ ] Topic is relevant to business
- [ ] Can provide unique expertise/data
- [ ] Competitors haven't dominated yet

### Internal Linking Rules
- Every cluster → Pillar (descriptive anchor text)
- Pillar → Every cluster (contextual placement)
- Cluster → 2-3 related clusters (natural links)
- NO generic anchors ("click here", "read more")

## Phase 6: Content Calendar Generation

### Output Format
| Priority | Keyword | Volume | KD | Intent | Content Type | Target Site | Status |
|----------|---------|--------|-----|--------|-------------|-------------|--------|
| P0 | keyword 1 | 1,200 | 15 | Commercial | Listicle | site.com | Queue |
| P0 | keyword 2 | 800 | 12 | Informational | Guide | site.com | Queue |
| P1 | keyword 3 | 2,400 | 25 | Commercial | Comparison | site.com | Plan |

### Publishing Cadence
- **Week 1**: P0 pillar content (comprehensive guide)
- **Week 2-3**: P0 cluster articles (2/week)
- **Week 4**: Refresh existing content with new internal links
- **Repeat** with next priority tier

## Phase 7: GEO/AEO Keyword Optimization

### AI-Triggering Keywords
Prioritize keywords that trigger AI answers:
- "What is [topic]" → Definition content with schema
- "[X] vs [Y]" → Comparison with table + schema
- "Best [X] for [Y]" → Listicle with structured data
- "How to [X]" → Step-by-step with HowTo schema
- "[Topic] examples" → Numbered list with clear formatting

### Featured Snippet Targeting
Format content to win snippets:
- **Paragraph**: 40-60 word direct answer after question heading
- **List**: Numbered/bulleted steps or items
- **Table**: Comparison data with clear headers
- **Video**: Embedded with timestamp

## Speed Optimizations
- **Cache GSC data** — Don't re-pull within 24h
- **Batch autocomplete** — Parallel requests for alphabet soup
- **Pre-compute from existing data** — Our 10 sites have GSC data cached
- **Use WP REST API** — Get existing content inventory for gap analysis
- **Parallel competitor analysis** — Fetch multiple competitor pages simultaneously

## Self-Critique Scorecard (/25)
1. **Data** (1-5): Was GSC data used as primary source?
2. **Discovery** (1-5): Were multiple discovery methods used?
3. **Intent** (1-5): Was search intent correctly classified?
4. **Prioritization** (1-5): Were keywords scored and ranked by ROI?
5. **Actionability** (1-5): Is there a clear content calendar with specific targets?

**Target: 22+/25**

## Output Contract
- **Artifact**: Prioritized keyword list with topic clusters and content calendar
- **Evidence**: GSC data + autocomplete + PAA + competitor analysis
- **Decision**: Top 10-20 keywords to target first (P0 + P1)
- **Next**: Create content via editorial-post-enhancement, track rankings via seo-intelligence

## Anti-Patterns
- ❌ Targeting only high-volume keywords (too competitive)
- ❌ Ignoring GSC data (we have REAL data — use it!)
- ❌ Not classifying intent (wrong content format = wasted effort)
- ❌ Keyword stuffing (hurts readability and rankings)
- ❌ Not building topic clusters (orphan content doesn't rank)
- ❌ Ignoring long-tail keywords (easier to rank, higher conversion)
- ❌ Not considering GEO/AEO potential (AI search is the future)
