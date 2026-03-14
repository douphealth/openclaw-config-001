---
name: editorial-post-enhancement
description: Enterprise-grade content optimization system for blog posts and editorial content. Use when upgrading published or draft articles for better SEO, E-E-A-T signals, SERP visibility, internal linking, schema markup, conversion optimization, or answer-engine friendliness. Triggers on requests to improve articles, add internal links, strengthen SEO, close topic gaps, optimize titles/slugs/meta, enhance E-E-A-T, or turn drafts into high-performing editorial assets. CRITICAL: Always checks for keyword cannibalization before optimization.
---

# Editorial Post Enhancement — Enterprise Content Optimization

Turn articles into high-performing editorial assets with E-E-A-T, SERP optimization, cannibalization awareness, and conversion design.

## WHEN TO USE

Trigger this skill when the user asks about:
- Improving, optimizing, or enhancing blog posts/articles
- Adding internal links, schema, FAQ sections
- Strengthening SEO, E-E-A-T, or SERP visibility
- Closing topic gaps or adding missing entities
- Optimizing title, slug, meta description
- Improving content quality or depth
- Adding visual elements or conversion CTAs
- "Make this article rank better"

**DO NOT use for:** Net-new content creation (use conversion-copywriting) or content strategy planning (use content-strategy-planning).

## CRITICAL PRE-FLIGHT CHECKS

### 1. Cannibalization Check (ALWAYS FIRST)
```python
def check_article_cannibalization(article_url, article_keyword, site_content):
    """
    Verify this article won't cannibalize another page.
    
    Returns: dict with 'safe_to_optimize', 'conflicts', 'recommendation'
    """
    conflicts = []
    
    for page in site_content:
        if page['url'] == article_url:
            continue
        
        # Same target keyword?
        if page.get('target_keyword', '').lower() == article_keyword.lower():
            conflicts.append({
                'page': page['url'],
                'reason': 'Same target keyword',
                'severity': 'CRITICAL'
            })
        
        # Ranking for same keyword?
        if article_keyword.lower() in [kw.lower() for kw in page.get('ranking_keywords', [])]:
            conflicts.append({
                'page': page['url'],
                'reason': 'Also ranking for target keyword',
                'severity': 'HIGH'
            })
    
    safe = len([c for c in conflicts if c['severity'] == 'CRITICAL']) == 0
    
    return {
        'safe_to_optimize': safe,
        'conflicts': conflicts,
        'recommendation': 'Proceed with optimization' if safe else 'Resolve cannibalization first'
    }
```

### 2. SERP Analysis for Target Keyword
Before optimizing, understand what's ranking:
- Analyze top 10 results
- Identify content patterns
- Determine search intent
- Find content gaps
- Note SERP features

## DO NOT USE FOR
- Writing brand new content (→ conversion-copywriting)
- Content strategy planning (→ content-strategy-planning)
- Site-wide SEO audits (→ seo-audit-playbook)

## CONTENT STANDARDS (MANDATORY)

Every article MUST meet these standards before publishing:

### 1. Answer-First Structure
- Answer the main query directly in the first paragraph (before any fluff)
- Reader should get value within the first 2 sentences
- No "In this article we'll..." preamble — just answer the question

### 2. Writing Style (Hormozi + Ferriss)
- Short sentences. Punchy. Direct.
- No filler words, no corporate speak, no "it's worth noting"
- Active voice always. "Do this" not "This should be done"
- Practical, actionable, specific — not theoretical
- Examples and numbers over vague claims
- Paragraphs: 1-3 sentences max
- Use "you" and "your" — speak directly to the reader
- Opinionated guidance: "Do X. Don't do Y. Here's why."

### 3. Internal Links (6-10 minimum)
- Contextual rich anchor text (not "click here" or "read more")
- Evenly distributed throughout the article (not clustered)
- Link to pillar pages, related guides, and money pages
- Each link should feel natural — the reader should WANT to click it
- Use descriptive anchor text that includes target keyword when natural

### 4. Media Requirements
- 1 relevant YouTube video (embedded, high-quality, matches topic)
- 2+ relevant images from existing WordPress media gallery
- Images must have descriptive alt text with keywords where natural
- Hero image at the top, second image mid-article

### 5. FAQ Section
- 5-7 questions covering real reader questions
- Answer-first format (direct answer, then explanation)
- Visual design: alternating backgrounds, clear separation
- Schema-ready with proper markup

### 6. References Section
- 3-5 authoritative sources (academic, institutional, expert)
- Include URLs when available
- Format: Author/Organization. (Year). Title. Source.

### 7. Semantic Keyword Coverage
- Include all top semantically relevant entities for the topic
- Before writing, analyze existing content for keyword gaps
- Include top 20 missing keywords from top 3 SERP results
- Use natural integration — don't keyword stuff

### 8. Mobile-First Design
- Responsive CSS (test at 375px, 768px, 1024px)
- Touch-friendly elements (buttons, links)
- Readable font sizes (16px minimum)
- No horizontal scrolling
- Fast-loading (optimize images, minimize CSS)

### 9. Visual Design Elements
- Tip boxes (green accent, left border)
- Warning boxes (orange accent, left border)
- Step boxes (numbered, clean layout)
- Comparison tables (responsive, styled headers)
- Variety/product cards (emoji icons, clean layout)
- CTA boxes (gradient backgrounds, clear buttons)
- FAQ section (alternating backgrounds)

### 10. Conversion Elements
- CTA to newsletter/lead magnet
- Disclosure for affiliate content
- Clear next step for reader

## ENHANCEMENT WORKFLOW

### Step 1: SERP & Intent Analysis
```python
def analyze_serp_for_keyword(keyword):
    """Analyze what's ranking for the target keyword."""
    analysis = {
        'keyword': keyword,
        'intent': classify_search_intent(keyword),
        'top_results': [],
        'common_patterns': [],
        'content_gaps': [],
        'serp_features': [],
    }
    
    # Intent classification
    # Informational: how, what, why, guide, tutorial
    # Commercial: best, review, vs, comparison
    # Transactional: buy, price, coupon, deal
    
    return analysis
```

### Step 2: Topic Gap Analysis
```python
def find_topic_gaps(article_html, competitor_html_list, target_keyword):
    """Find topics competitors cover that this article misses."""
    
    # Extract headings and key terms from article
    article_headings = set()
    article_entities = set()
    
    headings = re.findall(r'<h[2-6][^>]*>(.*?)</h[2-6]>', article_html, re.I | re.S)
    for h in headings:
        clean = re.sub(r'<[^>]+>', '', h).strip().lower()
        article_headings.add(clean)
    
    # Extract from competitors
    competitor_headings = set()
    competitor_entities = set()
    
    for comp_html in competitor_html_list:
        comp_headings = re.findall(r'<h[2-6][^>]*>(.*?)</h[2-6]>', comp_html, re.I | re.S)
        for h in comp_headings:
            clean = re.sub(r'<[^>]+>', '', h).strip().lower()
            competitor_headings.add(clean)
    
    # Find gaps
    missing_headings = competitor_headings - article_headings
    
    return {
        'missing_topics': list(missing_headings)[:10],
        'article_covers': len(article_headings),
        'competitors_average': len(competitor_headings) // max(len(competitor_html_list), 1),
    }
```

### Step 3: Content Quality Scoring
```python
def score_content_quality(html, target_keyword):
    """Score content quality 0-100."""
    score = 0
    feedback = []
    
    # Word count (20 points)
    text = re.sub(r'<[^>]+>', ' ', html)
    words = len(text.split())
    if words >= 2000:
        score += 20
    elif words >= 1000:
        score += 15
    elif words >= 500:
        score += 10
    elif words >= 300:
        score += 5
    else:
        feedback.append(f'Content too short: {words} words')
    
    # Keyword in title (10 points)
    title = re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
    if title and target_keyword.lower() in title.group(1).lower():
        score += 10
    else:
        feedback.append('Target keyword not in title')
    
    # Keyword in H1 (10 points)
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
    if h1 and any(target_keyword.lower() in h.lower() for h in h1):
        score += 10
    else:
        feedback.append('Target keyword not in H1')
    
    # Keyword in first 100 words (5 points)
    first_100 = ' '.join(text.split()[:100])
    if target_keyword.lower() in first_100.lower():
        score += 5
    
    # Headers structure (10 points)
    headers = re.findall(r'<h[2-6][^>]*>', html, re.I)
    if len(headers) >= 5:
        score += 10
    elif len(headers) >= 3:
        score += 5
    else:
        feedback.append('Add more headers for structure')
    
    # Internal links (10 points)
    internal_links = re.findall(r'href=["\']https?://[^"\']*(?:yourdomain|site\.com)[^"\']*["\']', html, re.I)
    if len(internal_links) >= 5:
        score += 10
    elif len(internal_links) >= 3:
        score += 5
    else:
        feedback.append('Add more internal links (aim for 5+)')
    
    # Schema markup (10 points)
    if 'application/ld+json' in html:
        score += 10
    else:
        feedback.append('Add JSON-LD schema markup')
    
    # FAQ section (10 points)
    if re.search(r'faq|frequently asked|common questions', html, re.I):
        score += 10
    else:
        feedback.append('Add FAQ section')
    
    # Images with alt text (10 points)
    images = re.findall(r'<img[^>]*>', html, re.I)
    images_with_alt = re.findall(r'<img[^>]*alt=["\'][^"\']+["\'][^>]*>', html, re.I)
    if images and len(images_with_alt) / len(images) >= 0.8:
        score += 10
    elif images_with_alt:
        score += 5
        feedback.append('Add alt text to all images')
    
    # Lists and tables (5 points)
    if re.search(r'<[ou]l[^>]*>', html, re.I) or re.search(r'<table[^>]*>', html, re.I):
        score += 5
    
    return {'score': score, 'feedback': feedback}
```

## ENHANCEMENT CHECKLIST

### Title Optimization
- [ ] Primary keyword in title (preferably near start)
- [ ] Title length 50-60 characters
- [ ] Compelling/power words included
- [ ] Matches search intent
- [ ] Unique (no other page on site has similar title)

### Meta Description
- [ ] Primary keyword included naturally
- [ ] Length 150-160 characters
- [ ] Clear call-to-action or value proposition
- [ ] Matches page content

### Header Structure
- [ ] Single H1 with primary keyword
- [ ] Logical H2/H3 hierarchy
- [ ] Secondary keywords in headers
- [ ] No skipped levels (H2 → H4)

### Content Enhancement
- [ ] Answer-first introduction (direct answer in first paragraph)
- [ ] Key entities and subtopics covered
- [ ] Missing topics from competitor analysis added
- [ ] Practical examples and implementation steps
- [ ] Expert quotes or data citations
- [ ] Updated statistics and references

### E-E-A-T Signals
- [ ] Author bio with credentials
- [ ] First-hand experience demonstrated
- [ ] External citations to authoritative sources
- [ ] Methodology explained
- [ ] Last updated date visible
- [ ] Contact/about information accessible

### Internal Linking
- [ ] 5-8 contextual internal links distributed naturally
- [ ] Links to pillar/cluster pages included
- [ ] Links to money pages where relevant
- [ ] Anchor text varied and descriptive
- [ ] No link clustering at top or bottom

### Schema Markup
```json
{
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "Article Title",
            "datePublished": "2026-03-13",
            "dateModified": "2026-03-13",
            "author": {
                "@type": "Person",
                "name": "Author Name",
                "url": "https://site.com/author/name"
            },
            "publisher": {
                "@type": "Organization",
                "name": "Site Name",
                "logo": {"@type": "ImageObject", "url": "https://site.com/logo.png"}
            }
        }
    ]
}
```

### Visual Enhancement
- Summary/key takeaway boxes
- Comparison tables for product content
- FAQ section with standout styling
- Tip/warning/callout boxes
- Table of contents for 1500+ word articles
- Relevant images with descriptive alt text

## HTML PATTERNS

### FAQ Section
```html
<section class="faq-section">
    <h2>Frequently Asked Questions</h2>
    <div class="faq-item">
        <h3>Question here?</h3>
        <p>Answer here.</p>
    </div>
</section>
```

### Callout Box
```html
<div class="tip-box">
    <strong>💡 Pro Tip:</strong> Your tip here.
</div>
```

### Comparison Table
```html
<table class="comparison-table">
    <thead>
        <tr><th>Feature</th><th>Product A</th><th>Product B</th></tr>
    </thead>
    <tbody>
        <tr><td>Price</td><td>$99</td><td>$149</td></tr>
    </tbody>
</table>
```

## POST-ENHANCEMENT VALIDATION
- [ ] No duplicate H1
- [ ] No broken internal links
- [ ] Schema validates in Google Rich Results Test
- [ ] Mobile rendering correct
- [ ] No cannibalization introduced
- [ ] Page speed not significantly impacted

## Resources
- `references/html-pattern-library.md`
- `references/eeat-checklist.md`
- `references/serp-optimization-guide.md`
- `references/content-quality-scoring.md`
- `references/publish-readiness-checklist.md`

## Critical Rules
- ALWAYS check for cannibalization before optimizing
- ALWAYS analyze SERP intent before making changes
- NEVER duplicate the page title as another H1 in the body
- NEVER clump internal links in one section
- NEVER add visual elements that don't add value
- ALWAYS verify important internal links work


## Output Contract
**Artifact**: Enhanced article with SEO, internal links, media
**Evidence**: Quality score improvement, gap closure
**Decision**: Ready for publish or further iteration
**Next**: Performance monitoring

## Do NOT Use This For
- Tasks better handled by a more specific skill — check skill-router
- One-off quick questions that don't need a skill
- Tasks in a different domain — route to the correct skill first
