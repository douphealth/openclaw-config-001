---
name: seo-audit-playbook
description: Enterprise-grade SEO audit and diagnosis system. Use when auditing sites, diagnosing ranking drops, checking for keyword cannibalization, analyzing technical SEO issues, running competitive analysis, or performing comprehensive site health checks. Triggers on SEO audit requests, ranking drops, indexing problems, technical SEO reviews, on-page SEO checks, crawlability concerns, site health checks, title/meta reviews, cannibalization detection, or requests to explain why a site is not ranking.
---

# SEO Audit Playbook — Enterprise Site Diagnosis

Comprehensive SEO audit system with cannibalization detection, technical analysis, and actionable fix prioritization.

## WHEN TO USE

Trigger this skill when the user asks about:
- SEO audits, site health checks, ranking diagnosis
- "Why isn't my site ranking?" or ranking drops
- Technical SEO issues, crawlability problems
- Keyword cannibalization detection and resolution
- Indexing issues, Google Search Console problems
- Core Web Vitals, page speed, mobile optimization
- Competitor SEO analysis
- Site migration SEO validation
- On-page SEO optimization
- Content quality assessment

## DO NOT USE FOR
- Writing or editing content (→ editorial-post-enhancement)
- Implementing schema markup (→ schema-ops)
- Setting up tracking (→ tracking-measurement)
- Content strategy (→ content-strategy-planning)

## AUDIT ORDER (ALWAYS FOLLOW THIS SEQUENCE)

1. **Crawlability & Indexation** — Can Google find and index your pages?
2. **Technical Foundations** — Core Web Vitals, mobile, HTTPS, redirects, canonicals
3. **On-Page Optimization** — Titles, metas, headers, content, schema
4. **Content Quality & Intent Match** — E-E-A-T, depth, freshness, intent
5. **Internal Linking & Authority** — Link architecture, anchor text, orphan pages
6. **Cannibalization Check** — Keyword overlap, competing pages, resolution
7. **Competitive Analysis** — Gap analysis, SERP comparison

## 1. CRAWLABILITY & INDEXATION ANALYSIS

### 1.1 Robots.txt Validation
```python
import urllib.request
import re

def audit_robots_txt(domain):
    """Audit robots.txt for issues."""
    issues = []
    try:
        req = urllib.request.Request(f'https://{domain}/robots.txt', 
                                     headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode()
            
            # Check for blocking important paths
            blocks = re.findall(r'Disallow:\s*(/[^\s]*)', content, re.I)
            critical_paths = ['/', '/wp-content/', '/category/', '/tag/']
            for path in critical_paths:
                if path in blocks:
                    issues.append(f'CRITICAL: Robots.txt blocks {path}')
            
            # Check for sitemap declaration
            if 'Sitemap:' not in content:
                issues.append('WARNING: No Sitemap declaration in robots.txt')
            
            # Check for overly restrictive rules
            if re.search(r'Disallow:\s*/\s*$', content, re.M):
                issues.append('CRITICAL: Robots.txt blocks entire site!')
                
    except Exception as e:
        issues.append(f'ERROR: Cannot fetch robots.txt: {e}')
    
    return issues
```

### 1.2 XML Sitemap Validation
```python
def audit_sitemap(domain):
    """Check sitemap health."""
    issues = []
    try:
        req = urllib.request.Request(f'https://{domain}/sitemap.xml',
                                     headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode()
            
            # Count URLs
            urls = re.findall(r'<loc>(.*?)</loc>', content)
            if len(urls) == 0:
                issues.append('CRITICAL: Sitemap has no URLs')
            elif len(urls) > 50000:
                issues.append(f'WARNING: Sitemap has {len(urls)} URLs (consider splitting)')
            
            # Check for non-canonical URLs
            for url in urls[:100]:  # Sample first 100
                if '?' in url and 'lang=' not in url:
                    issues.append(f'WARNING: Sitemap contains query string URL: {url}')
                    break
                    
    except Exception as e:
        issues.append(f'ERROR: Cannot fetch sitemap: {e}')
    
    return issues
```

### 1.3 Indexation Check (via Google Search Console API)
```python
def check_indexation_gsc(domain, gsc_data):
    """Analyze indexation coverage from GSC data."""
    issues = []
    
    # Check for indexing drops
    # Check for excluded pages
    # Check for errors
    # Check for warnings
    
    return issues
```

## 2. TECHNICAL SEO ANALYSIS

### 2.1 Core Web Vitals Assessment
```python
def audit_core_web_vitals(url):
    """Check Core Web Vitals metrics."""
    # Use PageSpeed Insights API
    import json
    api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile'
    try:
        req = urllib.request.Request(api_url)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            cwv = data.get('loadingExperience', {}).get('metrics', {})
            
            issues = []
            
            # LCP (Largest Contentful Paint) - should be < 2.5s
            lcp = cwv.get('LARGEST_CONTENTFUL_PAINT_MS', {}).get('percentile', 0)
            if lcp > 4000:
                issues.append(f'CRITICAL: LCP is {lcp}ms (should be < 2500ms)')
            elif lcp > 2500:
                issues.append(f'WARNING: LCP is {lcp}ms (should be < 2500ms)')
            
            # CLS (Cumulative Layout Shift) - should be < 0.1
            cls = cwv.get('CUMULATIVE_LAYOUT_SHIFT_SCORE', {}).get('percentile', 0)
            if cls > 250:  # GSC reports CLS * 100
                issues.append(f'CRITICAL: CLS is {cls/100} (should be < 0.1)')
            
            # INP (Interaction to Next Paint) - should be < 200ms
            inp = cwv.get('INTERACTION_TO_NEXT_PAINT', {}).get('percentile', 0)
            if inp > 500:
                issues.append(f'CRITICAL: INP is {inp}ms (should be < 200ms)')
            elif inp > 200:
                issues.append(f'WARNING: INP is {inp}ms (should be < 200ms)')
                
            return issues
    except Exception as e:
        return [f'ERROR: Cannot fetch CWV data: {e}']
```

### 2.2 Mobile Optimization Check
```python
def audit_mobile(url):
    """Check mobile optimization."""
    issues = []
    
    # Fetch page and check viewport meta
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode().lower()
        
        if 'viewport' not in html:
            issues.append('CRITICAL: No viewport meta tag')
        
        if 'width=device-width' not in html:
            issues.append('WARNING: Viewport not set to device-width')
    
    return issues
```

### 2.3 HTTPS & Security Check
```python
def audit_https(domain):
    """Check HTTPS implementation."""
    issues = []
    
    # Check HTTP to HTTPS redirect
    try:
        req = urllib.request.Request(f'http://{domain}/', 
                                     headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10, allow_redirects=False) as resp:
            if resp.status not in [301, 308]:
                issues.append(f'CRITICAL: HTTP does not redirect to HTTPS (status: {resp.status})')
            elif 'https' not in resp.headers.get('Location', ''):
                issues.append('CRITICAL: HTTP redirect does not go to HTTPS')
    except:
        pass
    
    return issues
```

### 2.4 Redirect Chain Analysis
```python
def audit_redirects(url):
    """Check for redirect chains and loops."""
    issues = []
    chain = []
    current_url = url
    
    for i in range(10):  # Max 10 redirects
        try:
            req = urllib.request.Request(current_url, 
                                         headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10, allow_redirects=False) as resp:
                if resp.status in [301, 302, 307, 308]:
                    next_url = resp.headers.get('Location', '')
                    chain.append(f'{resp.status}: {current_url} → {next_url}')
                    current_url = next_url
                else:
                    break
        except:
            break
    
    if len(chain) > 2:
        issues.append(f'WARNING: Redirect chain ({len(chain)} hops): {" → ".join(chain)}')
    elif len(chain) > 0:
        pass  # Single redirect is fine
    
    return issues
```

### 2.5 Canonical Tag Validation
```python
def audit_canonicals(url, html):
    """Check canonical tag implementation."""
    issues = []
    
    canonicals = re.findall(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', html, re.I)
    
    if len(canonicals) == 0:
        issues.append('CRITICAL: No canonical tag found')
    elif len(canonicals) > 1:
        issues.append(f'WARNING: Multiple canonical tags found ({len(canonicals)})')
    else:
        canonical = canonicals[0]
        if canonical != url and not url.startswith(canonical):
            issues.append(f'INFO: Canonical points to different URL: {canonical}')
    
    return issues
```

## 3. ON-PAGE SEO ANALYSIS

### 3.1 Title Tag Audit
```python
def audit_title_tag(html):
    """Analyze title tag."""
    issues = []
    
    titles = re.findall(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
    
    if len(titles) == 0:
        issues.append('CRITICAL: No title tag found')
    elif len(titles) > 1:
        issues.append('WARNING: Multiple title tags found')
    else:
        title = titles[0].strip()
        
        if len(title) == 0:
            issues.append('CRITICAL: Title tag is empty')
        elif len(title) < 30:
            issues.append(f'WARNING: Title too short ({len(title)} chars, recommended 50-60)')
        elif len(title) > 60:
            issues.append(f'WARNING: Title too long ({len(title)} chars, may be truncated in SERPs)')
        
        # Check for keyword placement
        # Check for brand name
        # Check for duplicate patterns
    
    return issues
```

### 3.2 Meta Description Audit
```python
def audit_meta_description(html):
    """Analyze meta description."""
    issues = []
    
    metas = re.findall(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.I)
    
    if len(metas) == 0:
        issues.append('WARNING: No meta description found')
    else:
        desc = metas[0].strip()
        
        if len(desc) == 0:
            issues.append('WARNING: Meta description is empty')
        elif len(desc) < 120:
            issues.append(f'INFO: Meta description short ({len(desc)} chars, recommended 150-160)')
        elif len(desc) > 160:
            issues.append(f'INFO: Meta description long ({len(desc)} chars, may be truncated)')
    
    return issues
```

### 3.3 Header Hierarchy Audit
```python
def audit_headers(html):
    """Check header tag hierarchy."""
    issues = []
    
    headers = re.findall(r'<(h[1-6])[^>]*>(.*?)</\1>', html, re.I | re.S)
    
    h1_count = sum(1 for tag, _ in headers if tag.lower() == 'h1')
    
    if h1_count == 0:
        issues.append('CRITICAL: No H1 tag found')
    elif h1_count > 1:
        issues.append(f'WARNING: Multiple H1 tags found ({h1_count})')
    
    # Check hierarchy
    levels = [int(tag[1]) for tag, _ in headers]
    for i in range(1, len(levels)):
        if levels[i] > levels[i-1] + 1:
            issues.append(f'WARNING: Header hierarchy skip: H{levels[i-1]} → H{levels[i]}')
    
    return issues
```

## 4. KEYWORD CANNIBALIZATION DETECTION (CRITICAL)

### 4.1 Detection Methodology
```python
def detect_cannibalization(urls_and_keywords):
    """
    Detect keyword cannibalization across site pages.
    
    Input: List of dicts with 'url', 'title', 'target_keyword', 'ranking_keywords'
    Output: List of cannibalization issues
    
    Cannibalization occurs when:
    1. Multiple pages target the same primary keyword
    2. Multiple pages rank for the same keyword (GSC data)
    3. Pages have similar title/meta patterns
    """
    issues = []
    
    # Method 1: Target keyword overlap
    keyword_to_pages = {}
    for page in urls_and_keywords:
        kw = page.get('target_keyword', '').lower()
        if kw:
            if kw not in keyword_to_pages:
                keyword_to_pages[kw] = []
            keyword_to_pages[kw].append(page['url'])
    
    for kw, pages in keyword_to_pages.items():
        if len(pages) > 1:
            issues.append({
                'type': 'target_keyword_overlap',
                'severity': 'CRITICAL',
                'keyword': kw,
                'pages': pages,
                'fix': 'Choose one primary page, differentiate others, or consolidate'
            })
    
    # Method 2: Ranking keyword overlap (from GSC)
    keyword_rankings = {}
    for page in urls_and_keywords:
        for kw in page.get('ranking_keywords', []):
            kw_lower = kw.lower()
            if kw_lower not in keyword_rankings:
                keyword_rankings[kw_lower] = []
            keyword_rankings[kw_lower].append({
                'url': page['url'],
                'position': page.get('positions', {}).get(kw, 999)
            })
    
    for kw, rankings in keyword_rankings.items():
        if len(rankings) > 1:
            # Multiple pages ranking for same keyword
            sorted_rankings = sorted(rankings, key=lambda x: x['position'])
            issues.append({
                'type': 'ranking_overlap',
                'severity': 'HIGH' if sorted_rankings[0]['position'] < 10 else 'MEDIUM',
                'keyword': kw,
                'pages': [r['url'] for r in sorted_rankings],
                'best_position': sorted_rankings[0]['position'],
                'fix': 'Consolidate content or differentiate intent'
            })
    
    # Method 3: Title similarity detection
    for i, page1 in enumerate(urls_and_keywords):
        for page2 in urls_and_keywords[i+1:]:
            title1 = page1.get('title', '').lower()
            title2 = page2.get('title', '').lower()
            
            # Simple similarity check
            words1 = set(title1.split())
            words2 = set(title2.split())
            overlap = len(words1 & words2) / max(len(words1 | words2), 1)
            
            if overlap > 0.7:
                issues.append({
                    'type': 'title_similarity',
                    'severity': 'HIGH',
                    'pages': [page1['url'], page2['url']],
                    'similarity': f'{overlap:.0%}',
                    'fix': 'Differentiate titles or consolidate pages'
                })
    
    return issues
```

### 4.2 Cannibalization Resolution Decision Tree
```
CANNIBALIZATION DETECTED → What type?

1. TARGET KEYWORD OVERLAP (multiple pages target same keyword)
   → Which page ranks higher? → Make that the primary
   → Can the other page target a different intent? → Differentiate
   → Is the other page valuable? → Add canonical to primary
   → Is the other page low-value? → 301 redirect to primary

2. RANKING OVERLAP (multiple pages rank for same keyword)
   → Are positions close (<5 apart)? → Likely cannibalizing
   → Is one page clearly better? → Consolidate content, redirect
   → Do they serve different intents? → Differentiate titles/H1s
   → Are both ranking poorly? → Merge into one authoritative page

3. TITLE SIMILARITY (pages have similar titles)
   → Rewrite titles to target different angles
   → Differentiate primary keywords
   → Add unique value propositions to each title
```

## 5. CONTENT QUALITY ASSESSMENT

### 5.1 E-E-A-T Evaluation Checklist
- [ ] Author clearly identified with credentials
- [ ] Author has real experience with the topic
- [ ] Content demonstrates first-hand expertise
- [ ] External citations to authoritative sources
- [ ] Content is regularly updated
- [ ] Clear about methodology/sources
- [ ] Contact/about information available
- [ ] Privacy policy and terms present

### 5.2 Content Depth Scoring
```python
def score_content_depth(html, target_keyword):
    """Score content depth 0-100."""
    score = 50  # Base
    
    # Word count
    text = re.sub(r'<[^>]+>', ' ', html)
    words = len(text.split())
    if words > 2000:
        score += 15
    elif words > 1000:
        score += 10
    elif words < 300:
        score -= 20
    
    # Header structure
    headers = re.findall(r'<h[2-6][^>]*>', html, re.I)
    if len(headers) >= 5:
        score += 10
    elif len(headers) < 2:
        score -= 10
    
    # Images
    images = re.findall(r'<img[^>]*>', html, re.I)
    if len(images) >= 3:
        score += 5
    
    # Internal links
    internal_links = re.findall(r'href=["\']https?://[^"\']*yourdomain[^"\']*["\']', html, re.I)
    if len(internal_links) >= 3:
        score += 10
    
    # Lists (help readability)
    lists = re.findall(r'<[ou]l[^>]*>', html, re.I)
    if len(lists) >= 2:
        score += 5
    
    # Schema markup
    if 'application/ld+json' in html:
        score += 5
    
    return min(100, max(0, score))
```

## 6. COMPETITIVE ANALYSIS FRAMEWORK

### 6.1 SERP Competitor Analysis
```python
def analyze_serp_competitors(keyword, top_results):
    """Analyze top-ranking pages for a keyword."""
    analysis = {
        'keyword': keyword,
        'avg_word_count': 0,
        'common_headers': [],
        'common_entities': [],
        'content_formats': [],
        'avg_title_length': 0,
        'featured_snippet': None,
        'paa_questions': [],
    }
    
    word_counts = []
    title_lengths = []
    
    for result in top_results:
        # Analyze each result
        word_counts.append(result.get('word_count', 0))
        title_lengths.append(len(result.get('title', '')))
    
    analysis['avg_word_count'] = sum(word_counts) / max(len(word_counts), 1)
    analysis['avg_title_length'] = sum(title_lengths) / max(len(title_lengths), 1)
    
    return analysis
```

## OUTPUT TEMPLATE

```
## SEO Audit Report: {domain}
Date: {date}
Auditor: {auditor}

### Executive Summary
- Overall Health Score: X/100
- Critical Issues: X
- High Priority Issues: X
- Medium Priority Issues: X
- Low Priority Issues: X
- Estimated Impact: {description}

### Critical Issues (Fix Immediately)
1. [Issue] - [Evidence] - [Fix]

### High Priority Issues (Fix This Week)
1. [Issue] - [Evidence] - [Fix]

### Medium Priority Issues (Fix This Month)
1. [Issue] - [Evidence] - [Fix]

### Cannibalization Report
- X keyword overlaps detected
- X ranking conflicts
- X title similarities
- Recommended actions: [list]

### Action Plan
Week 1: [Critical fixes]
Week 2-4: [High priority]
Month 2-3: [Medium priority]
Ongoing: [Monitoring]

### Unknowns & Limitations
- [Data not available]
- [Tools not accessible]
```

## Resources
- `references/technical-checklist.md`
- `references/cannibalization-detection.md`
- `references/competitive-analysis-framework.md`

## Critical Rules
- NEVER claim "no schema found" from static fetches alone
- ALWAYS check for keyword cannibalization before recommending new content
- ALWAYS define site type, priority pages, symptoms, and scope
- ALWAYS provide evidence for findings
- DO NOT mix business opinion with technical diagnosis
- DO NOT jump to content advice before checking crawl/index/render issues
- DO NOT report "audit complete" if only surface HTML was inspected


## Output Contract
**Artifact**: SEO audit report with prioritized fixes
**Evidence**: Crawl data, issue evidence, impact ranking
**Decision**: Fix plan approved
**Next**: Implement and re-audit

## Do NOT Use This For
- Tasks better handled by a more specific skill — check skill-router
- One-off quick questions that don't need a skill
- Tasks in a different domain — route to the correct skill first
