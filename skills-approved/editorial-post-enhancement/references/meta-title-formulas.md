# Meta Title & Description Formulas

CTR-optimized title and description templates. Keep titles ≤60 chars, descriptions ≤155 chars. Primary keyword in first 3-4 words.

## Title Formulas by Intent

### Informational (how-to, guide, tutorial)
- [Number] [Adjective] Ways to [Achieve Result] + [Keyword] | [Brand]
- How to [Keyword] in [Timeframe]: [Benefit] (Step-by-Step)
- [Keyword] Guide: [Number] [Steps/Strategies] That Actually Work
- The [Adjective] Guide to [Keyword] (No Fluff, Just Results)

### Commercial (best of, comparison, review)
- Best [Keyword] for [Use Case] in [Year]: [Number] Tested
- [Product] vs [Product]: [Keyword] Comparison (Honest Review)
- [Product] Review: [Honest Assessment] + [Better Alternative]
- [Number] [Adjective] [Keyword] Compared: Which Wins?

### Listicle / Resource
- [Number] [Keyword] You Need to Know ([Year] Update)
- [Keyword] Tips: [Number] [Adjective] Ways to [Result]
- [Number] Surprising [Keyword] Facts That [Benefit/Change]

### Question-Based
- What Is [Keyword]? [Simple Explanation] + [Why It Matters]
- Is [Keyword] Worth It? [Honest Answer] + [What I'd Do Instead]
- Why Does [Keyword] [Problem]? [Cause] + [Fix]

## Description Formulas

### Standard
- [Primary keyword] → [benefit]. Learn [secondary keyword] with [number] [proven/practical] [steps/tips/examples]. [CTA].

### Problem-Solution
- Struggling with [problem]? Discover how to [solution] using [keyword]. [Number] [proven/practical] [methods] that [specific result]. [CTA].

### Comparison
- [Product A] vs [Product B] for [use case]? We tested both. [Key difference]. See which is better for [specific audience]. [CTA].

### List/Resource
- [Number] [adjective] [keyword] [tips/strategies/tools] for [year]. [Primary benefit]. [Secondary benefit]. [CTA].

## Length Guidelines

| Element | Ideal | Max | Notes |
|---------|-------|-----|-------|
| Title | 50-55 | 60 | Full display in SERP |
| Title + brand | 50-60 | 65 | " \| Brand" appended |
| Meta description | 140-150 | 155 | Full display in SERP |
| OG title | 40-60 | 65 | Social sharing preview |
| OG description | 100-130 | 140 | Social sharing preview |

## Character Counter Snippet
```bash
# Check title length
echo -n "Your Title Here" | wc -c

# Check from live page
curl -s <url> | grep -oP '(?<=<title>).+?(?=</title>)' | tr -d '\n' | wc -c

# Description length
curl -s <url> | grep -oP 'name="description" content="\K[^"]+' | wc -c
```

## Common Mistakes
- ❌ Primary keyword >5 words in (gets cut off in SERP)
- ❌ Duplicate titles across pages (cannibalization signal)
- ❌ All caps or excessive punctuation (!!!???)
- ❌ Missing brand differentiation on important pages
- ❌ Description just repeats title (wasted character budget)
- ❌ No CTA in description ("Learn how", "Get the guide", "See the full list")
- ❌ Keyword stuffing: "Best SEO SEO Tips SEO Guide SEO"
- ❌ Too vague: "Improve your business" (for whom? how?)
