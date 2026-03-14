# Cannibalization Prevention Checklist

## Why This Matters

Keyword cannibalization occurs when multiple pages on your site compete for the same search terms. Google struggles to determine which page to rank, often resulting in:
- Neither page ranking well
- Rankings fluctuating between pages
- Diluted link equity across pages
- Wasted crawl budget

**This is the #1 content strategy mistake and the most preventable SEO problem.**

---

## Pre-Publish Cannibalization Check — Full Workflow

### Phase 1: Site Search Audit (5 minutes)

Before creating any new content, search your own site:

```
Step 1: Google site search queries
─────────────────────────────────────
site:yourdomain.com "primary keyword"
site:yourdomain.com "secondary keyword 1"
site:yourdomain.com "secondary keyword 2"
site:yourdomain.com intitle:"primary keyword"

Step 2: Check URL slugs
─────────────────────────────────────
Do any existing URLs contain the target keyword as a slug?
Example: /best-wordpress-hosting/ vs /wordpress-hosting-guide/

Step 3: Check title tags
─────────────────────────────────────
Do any existing pages have the target keyword in the title?
Look at the search results from Step 1.

Step 4: Check H1 tags
─────────────────────────────────────
Do any existing pages use the target keyword in H1?
If you have CMS access, check directly.
```

### Phase 2: Performance Analysis (10 minutes)

For each existing page found in Phase 1:

```
┌─────────────────────────────────────────────────┐
│  Existing Page Found                            │
├─────────────────────────────────────────────────┤
│  Q1: Is it ranking in positions 1–20?           │
│  ├─ YES → Continue to Q2                        │
│  └─ NO  → Why not? Thin? Wrong intent?         │
│           → Thin content: EXPAND this page      │
│           → Wrong intent: CREATE new page       │
│           → Technical issue: FIX then reassess   │
│                                                 │
│  Q2: Does it satisfy the search intent?         │
│  ├─ YES, fully → EXPAND with new section        │
│  ├─ Partially  → EXPAND + improve intent match  │
│  └─ NO (wrong angle) → CREATE new page          │
│                        + 301 or canonical old    │
│                                                 │
│  Q3: How much traffic does it get?              │
│  ├─ >100/mo organic → PRESERVE, expand carefully│
│  ├─ 10–100/mo       → Candidate for merge       │
│  └─ <10/mo          → Strong merge/redirect     │
│                                                 │
│  Q4: Does it have backlinks?                    │
│  ├─ YES (quality links) → Keep URL, update      │
│  └─ NO                  → No redirect concern   │
│                                                 │
│  Q5: How old is the content?                    │
│  ├─ <12 months    → Update in place             │
│  ├─ 12–24 months  → Update or create new        │
│  └─ >24 months    → Likely needs full rewrite   │
└─────────────────────────────────────────────────┘
```

### Phase 3: Decision Matrix

```
                        Existing page ranks
                        well (pos 1–20)?
                               │
                   ┌───────────┴───────────┐
                  YES                      NO
                   │                       │
          Intent matches?          ┌───────┴───────┐
           │          │          Thin?        Wrong intent?
          YES         NO          │                │
           │          │         EXPAND          CREATE new
        Expand    Create new   existing        page, 301/
        existing  page, set                    noindex old
        page      canonical or
                  differentiate
                  angle clearly

─────────────────────────────────────────────────────────

DECISION: EXPAND existing page
─────────────────────────────────────
- Add new section covering the new keyword angle
- Update meta title to include new keyword if natural
- Add new internal links from supporting content
- Update publish date
- Request re-indexing in Search Console

DECISION: CREATE new page
─────────────────────────────────────
- Ensure URL slug is distinct from existing pages
- Ensure title tag has a unique angle
- Ensure primary keyword differs from existing page targets
- Add internal links from new page to related existing pages
- Consider: does this new page make an existing page redundant?
  → If YES, 301 redirect the old page to the new one

DECISION: CONSOLIDATE
─────────────────────────────────────
- Pick the strongest page (most traffic, most backlinks, best rankings)
- Move all content from weaker pages into the winner
- 301 redirect weaker pages to the winner
- Update internal links to point to the winner
- Submit old URLs for removal in Search Console
```

### Phase 4: Keyword Overlap Scoring

Run this check for every new keyword cluster against your existing content:

```python
def full_cannibalization_check(
    new_cluster: dict,
    existing_inventory: list[dict]
) -> dict:
    """
    Comprehensive cannibalization check.
    
    Args:
        new_cluster: {
            "primary_keyword": str,
            "secondary_keywords": list[str],
            "target_url_slug": str
        }
        existing_inventory: [
            {
                "url": str,
                "title": str,
                "slug": str,
                "primary_keyword": str,
                "secondary_keywords": list[str],
                "ranking_position": int or None,
                "monthly_traffic": int,
                "word_count": int,
                "backlink_count": int,
                "last_updated": str
            }
        ]
    
    Returns:
        {
            "risk_level": "NONE" | "LOW" | "MEDIUM" | "HIGH",
            "conflicts": [...],
            "recommendation": str,
            "action": str
        }
    """
    import re
    
    new_primary = new_cluster["primary_keyword"].lower().strip()
    new_secondaries = set(k.lower().strip() for k in new_cluster["secondary_keywords"])
    new_slug = new_cluster.get("target_url_slug", "").lower()
    new_all = {new_primary} | new_secondaries
    
    # Normalize: extract significant words
    def significant_words(text):
        stop = {"the", "a", "an", "for", "in", "on", "at", "to", "of", "and",
                "or", "is", "are", "was", "be", "with", "by", "from"}
        words = set(re.findall(r'\w+', text.lower()))
        return words - stop
    
    new_words = significant_words(new_primary)
    
    conflicts = []
    
    for page in existing_inventory:
        existing_primary = page["primary_keyword"].lower().strip()
        existing_secondaries = set(k.lower().strip() for k in page.get("secondary_keywords", []))
        existing_all = {existing_primary} | existing_secondaries
        existing_slug = page.get("slug", "").lower()
        
        # Check 1: Exact keyword match
        exact_overlap = new_all & existing_all
        
        # Check 2: Significant word overlap
        existing_words = significant_words(existing_primary)
        word_overlap = new_words & existing_words
        word_overlap_ratio = len(word_overlap) / max(len(new_words), 1)
        
        # Check 3: Slug similarity
        slug_overlap = new_slug and existing_slug and (
            new_slug in existing_slug or existing_slug in new_slug
        )
        
        if exact_overlap or word_overlap_ratio > 0.6 or slug_overlap:
            risk_factors = []
            
            if exact_overlap:
                risk_factors.append(f"Exact keyword overlap: {exact_overlap}")
            if word_overlap_ratio > 0.6:
                risk_factors.append(f"Word overlap: {round(word_overlap_ratio*100)}%")
            if slug_overlap:
                risk_factors.append(f"Slug similarity: '{new_slug}' vs '{existing_slug}'")
            
            # Determine action based on existing page performance
            ranking = page.get("ranking_position")
            traffic = page.get("monthly_traffic", 0)
            
            if ranking and ranking <= 20:
                if word_overlap_ratio > 0.8:
                    action = "EXPAND existing page (high overlap + ranking well)"
                    risk = "HIGH"
                else:
                    action = "REVIEW intent — may need to differentiate or expand"
                    risk = "MEDIUM"
            elif traffic > 50:
                action = "EXPAND existing page (has traffic to preserve)"
                risk = "MEDIUM"
            else:
                action = "Low risk — existing page not performing, safe to create new"
                risk = "LOW"
            
            conflicts.append({
                "existing_url": page["url"],
                "existing_title": page["title"],
                "risk_factors": risk_factors,
                "existing_ranking": ranking,
                "existing_traffic": traffic,
                "risk": risk,
                "recommended_action": action
            })
    
    # Overall risk
    if not conflicts:
        overall = {"risk_level": "NONE", "conflicts": [], 
                   "recommendation": "No cannibalization risk detected",
                   "action": "Proceed with new page creation"}
    else:
        highest_risk = "LOW"
        for c in conflicts:
            if c["risk"] == "HIGH":
                highest_risk = "HIGH"
                break
            elif c["risk"] == "MEDIUM":
                highest_risk = "MEDIUM"
        
        actions = [c["recommended_action"] for c in conflicts]
        
        overall = {
            "risk_level": highest_risk,
            "conflicts": conflicts,
            "recommendation": f"Found {len(conflicts)} potential conflict(s)",
            "action": "; ".join(set(actions))
        }
    
    return overall
```

---

## Post-Publish Monitoring

After publishing new content, monitor for cannibalization:

### Weekly Check (first month)
```
1. Search Console → Performance → Filter by new page's target keyword
   - Are impressions going to the new page or the old page?
   - Are both pages appearing for the same query?

2. Google: site:yourdomain.com "primary keyword"
   - Which page shows up first?
   - Is the right page ranking?

3. Check internal links
   - Are supporting pages linking to the right target?
   - Are anchor texts consistent?
```

### Monthly Check (ongoing)
```
1. Run full keyword overlap check across all published content
2. Check Search Console for URL cannibalization warnings
3. Review pages that lost rankings after new content was published
4. Update internal linking if wrong pages are ranking
```

---

## Consolidation Playbook

When cannibalization is confirmed:

### Option A: Merge Pages
```
1. Identify the stronger page (more traffic, more links, better rankings)
2. Move unique content from weaker page into stronger page
3. Add new sections to cover any gaps
4. Update meta title/description
5. 301 redirect weaker page → stronger page
6. Update all internal links
7. Submit redirect in Search Console
```

### Option B: Differentiate Pages
```
1. Clearly separate intent:
   - Page A: "WordPress Hosting for Beginners" (informational)
   - Page B: "Best WordPress Hosting" (commercial)
2. Update titles, H1s, and content to reflect distinct angles
3. Cross-link between pages with clear anchor text
4. Update internal links from supporting content
```

### Option C: Canonical Tag
```
Use when:
- Both pages serve a purpose (e.g., slight URL variations)
- You want Google to index only one version
- Redirect would harm user experience

Implementation:
<link rel="canonical" href="https://yoursite.com/preferred-url/" />

Note: Canonical is weaker than 301. Use 301 when possible.
```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│           CANNIBALIZATION DECISION FLOWCHART            │
│                                                         │
│  New keyword cluster identified                         │
│       │                                                 │
│       ▼                                                 │
│  Search site: for existing coverage                     │
│       │                                                 │
│       ▼                                                 │
│  ┌─────────────┐     NO                                │
│  │ Any matches?├──────────→ CREATE new page (safe)      │
│  └──────┬──────┘                                        │
│        YES                                              │
│         │                                               │
│         ▼                                               │
│  ┌──────────────────┐  YES   ┌──────────────────┐      │
│  │ Page ranking top ├───────→│ Intent match?    │      │
│  │ 20?              │        │                  │      │
│  └────────┬─────────┘        │ YES → EXPAND     │      │
│          NO                  │ NO  → CREATE     │      │
│           │                  │      + canonical  │      │
│           ▼                  └──────────────────┘      │
│  ┌──────────────┐                                      │
│  │ Has traffic   │  YES → EXPAND existing               │
│  │ or links?     │                                      │
│  └──────┬───────┘                                      │
│        NO                                               │
│         │                                               │
│         ▼                                               │
│  Low risk → CREATE new, consider 301 old               │
└─────────────────────────────────────────────────────────┘
```
