# Keyword Clustering Methodology

## Overview

Keyword clustering groups keywords that should be targeted by the same page. Two keywords belong in the same cluster when they share search intent and have significant SERP overlap.

## When to Cluster

- After initial keyword research produces a raw keyword list
- Before creating any content brief
- When auditing existing content for consolidation

## Clustering Algorithm

### Method 1: SERP Overlap Clustering (Most Accurate)

For each pair of keywords, check if the same pages rank in the top 10 results.

```
SERP Overlap Score = (Shared URLs in Top 10) / 10

Thresholds:
- ≥0.6 (6+ shared URLs) → SAME CLUSTER
- 0.3–0.5 (3–5 shared URLs) → REVIEW (check intent manually)
- <0.3 → DIFFERENT CLUSTERS
```

**Implementation:**

```python
def cluster_by_serp_overlap(keyword_serps: dict[str, list[str]], threshold: float = 0.6) -> dict[str, list[str]]:
    """
    Cluster keywords by SERP overlap.
    
    Args:
        keyword_serps: {keyword: [url1, url2, ..., url10]} - top 10 SERP URLs per keyword
        threshold: minimum overlap ratio to merge (default 0.6)
    
    Returns:
        {cluster_name: [keyword1, keyword2, ...]}
    """
    keywords = list(keyword_serps.keys())
    n = len(keywords)
    
    # Build overlap matrix
    overlap = {}
    for i in range(n):
        for j in range(i + 1, n):
            kw_a, kw_b = keywords[i], keywords[j]
            urls_a = set(keyword_serps[kw_a])
            urls_b = set(keyword_serps[kw_b])
            shared = len(urls_a & urls_b)
            score = shared / 10
            overlap[(kw_a, kw_b)] = score
    
    # Union-Find clustering
    parent = {kw: kw for kw in keywords}
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    
    for (kw_a, kw_b), score in overlap.items():
        if score >= threshold:
            union(kw_a, kw_b)
    
    # Build clusters
    clusters = {}
    for kw in keywords:
        root = find(kw)
        clusters.setdefault(root, []).append(kw)
    
    return clusters
```

### Method 2: Semantic Similarity Clustering (No SERP Data Needed)

When SERP data is unavailable, use word overlap and modifier analysis.

```python
def cluster_by_semantic_similarity(keywords: list[str], threshold: float = 0.5) -> dict[str, list[str]]:
    """
    Cluster keywords by word overlap and intent modifiers.
    Pure Python, no external dependencies.
    """
    import re
    from collections import Counter
    
    # Normalize keywords
    def normalize(kw):
        return set(re.findall(r'\w+', kw.lower()))
    
    # Intent modifiers that signal different clusters
    informational_modifiers = {"how", "what", "why", "when", "where", "guide", "tutorial", "learn"}
    commercial_modifiers = {"best", "top", "review", "reviews", "vs", "versus", "comparison", "alternative"}
    transactional_modifiers = {"buy", "price", "pricing", "cost", "cheap", "discount", "deal", "coupon"}
    
    def get_intent(kw):
        words = normalize(kw)
        if words & transactional_modifiers:
            return "transactional"
        elif words & commercial_modifiers:
            return "commercial"
        elif words & informational_modifiers:
            return "informational"
        return "unknown"
    
    def word_overlap(kw1, kw2):
        w1, w2 = normalize(kw1), normalize(kw2)
        if not w1 or not w2:
            return 0
        shared = len(w1 & w2)
        total = len(w1 | w2)
        return shared / total
    
    # Cluster
    clusters = []
    used = set()
    
    for i, kw in enumerate(keywords):
        if kw in used:
            continue
        
        cluster = [kw]
        used.add(kw)
        intent_i = get_intent(kw)
        
        for j, other in enumerate(keywords):
            if other in used:
                continue
            intent_j = get_intent(other)
            
            # Must share intent
            if intent_i != intent_j and intent_i != "unknown" and intent_j != "unknown":
                continue
            
            # Must have sufficient word overlap
            if word_overlap(kw, other) >= threshold:
                cluster.append(other)
                used.add(other)
        
        clusters.append(cluster)
    
    # Name clusters by most common words
    result = {}
    for cluster in clusters:
        # Pick the highest-volume or first keyword as cluster name
        name = cluster[0]
        result[name] = cluster
    
    return result
```

### Method 3: Modifier-Based Clustering (Fast Heuristic)

Group keywords by their base term + intent modifier pattern.

```python
def cluster_by_modifier(keywords: list[str]) -> dict[str, list[str]]:
    """
    Fast heuristic clustering based on base term extraction.
    Best for initial grouping before manual refinement.
    """
    import re
    
    # Common stop words to strip from base term extraction
    stop_words = {
        "the", "a", "an", "for", "in", "on", "at", "to", "of", "and", "or",
        "is", "are", "was", "were", "be", "been", "with", "by", "from", "that",
        "this", "it", "as", "can", "do", "does", "will", "would", "should",
        "best", "top", "how", "what", "why", "when", "where", "which", "who",
        "review", "reviews", "vs", "versus", "comparison", "alternative", "free",
        "cheap", "pricing", "price", "cost", "buy", "guide", "tutorial"
    }
    
    def extract_base(kw):
        words = re.findall(r'\w+', kw.lower())
        base = [w for w in words if w not in stop_words]
        return " ".join(base[:3])  # Use first 3 significant words as base
    
    clusters = {}
    for kw in keywords:
        base = extract_base(kw)
        clusters.setdefault(base, []).append(kw)
    
    return clusters
```

## Choosing the Right Method

| Method | Accuracy | Data Needed | Speed | Best For |
|--------|----------|-------------|-------|----------|
| SERP Overlap | Highest | Top-10 URLs per keyword | Slow | Final clustering |
| Semantic Similarity | High | Keywords only | Medium | No SERP data available |
| Modifier-Based | Medium | Keywords only | Fast | Initial grouping |

## Cluster Refinement Rules

After automated clustering, apply these manual checks:

1. **Split clusters with mixed intent:** If a cluster contains both "how to install X" and "best X for beginners," split them.
2. **Merge orphan clusters:** If two clusters are tiny (1–2 keywords each) and clearly related, merge them.
3. **Check volume distribution:** A cluster with one high-volume keyword and many low-volume ones is fine — the high-volume keyword is the primary target.
4. **Validate with SERP spot-check:** Manually search 2–3 keywords from each cluster. If results look very different, the cluster may need splitting.

## Output Format

```json
{
  "clusters": [
    {
      "name": "wordpress-hosting-commercial",
      "primary_keyword": "best wordpress hosting",
      "secondary_keywords": ["wordpress hosting review", "top wordpress hosting"],
      "intent": "commercial_investigation",
      "total_volume": 12500,
      "avg_kd": 45,
      "content_type": "roundup_review",
      "priority_score": 8.5
    }
  ]
}
```

## Anti-Cannibalization Rule

**Every cluster = one page. No exceptions.**

If you find yourself assigning two pages to the same cluster, you have a cannibalization problem. Either:
- Merge into one comprehensive page, or
- Split the cluster by clearly differentiating intent (e.g., "beginners" vs "advanced")
