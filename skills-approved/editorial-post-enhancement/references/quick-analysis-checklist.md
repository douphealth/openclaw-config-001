# Quick Analysis Checklist (90-Second Triage)

Flowchart for rapidly identifying the top 3 issues blocking a blog post from ranking #1.

## Start → Extract Content
```
Get raw HTML:
- WP: wp post get <ID> --field=post_content --format=raw
- URL: curl -s <url> > /tmp/article.html
- File: cp /path/to/article.html /tmp/article.html

Convert to text for quick scan:
pandoc /tmp/article.html -t plain -o /tmp/article.txt
# or: html2text /tmp/article.html > /tmp/article.txt
```

## Decision Diamond 1: Word Count & Thin Content
```
Is word count < 800? 
  YES → Flag: THIN CONTENT (needs expansion, examples, entities)
  NO  → Continue
```

## Decision Diamond 2: Answer-First & Intent
```
Does first 100 words directly answer the query?
  NO → Flag: WEAK ANSWER-FIRST (rewrite opening)
  YES → Continue
```

## Decision Diamond 3: Semantic Gaps (Missing Entities/Keywords)
```
Are top 3 SERP pages using entities/concepts absent here?
  YES → Flag: SEMANTIC GAPS (add missing keywords/entities)
  NO  → Continue
```

## Decision Diamond 4: Internal Linking
```
Are there <2 contextual internal links with varied anchors?
  YES → Flag: WEAK INTERNAL LINKING (add 2-3 contextual links)
  NO  → Continue
```

## Decision Diamond 5: Meta Title/Description
```
Is title >60 chars or missing keyword near front?
Is description >150 chars or weak CTA?
  YES → Flag: SUBOPTIMAL META (rewrite title/description)
  NO  → Continue
```

## Decision Diamond 6: Schema Markup
```
Is valid Article/FAQPage/HowTo schema present?
  NO → Flag: MISSING SCHEMA (add appropriate JSON-LD)
  YES → Continue
```

## Decision Diamond 7: Media & Images
```
Are there <2 helpful images with SEO alt text?
  NO → Flag: INSUFFICIENT MEDIA (add 2-3 images, optimize alt)
  YES → Continue
```

## Decision Diamond 8: Readability & Practicality
```
Is language theoretical/jargon-heavy?
Are there zero personal/practical examples?
  YES → Flag: NOT PRACTICAL ENOUGH (add Hormozi/Ferriss examples)
  NO  → Continue
```

## Decision Diamond 9: E-E-A-T & Trust
```
Is author expertise shown?
Are there trust signals (testimonials, data, sources)?
  NO → Flag: WEAK E-E-A-T (add bio, testimonial, sources)
  YES → CONTENT IS OPTIMIZED ✓
```

## Quick Reference Commands

### Content Extraction
```bash
# WordPress post
wp post get 123 --field=post_content --format=raw > /tmp/article.html
wp post get 123 --field=post_title --format=json

# From URL
curl -s "https://example.com/blog/post" > /tmp/article.html

# Extract readable text (install pandoc: winget install pandoc)
pandoc /tmp/article.html -t plain -o /tmp/article.txt
# Alternative: npx html-to-text-cli /tmp/article.html > /tmp/article.txt
```

### Entity/Keyword Gap Scan (Manual but fast)
```bash
# Get top 3 titles from SERP (simplified)
curl -s "https://www.google.com/search?q=<encoded+query>&num=3" | 
  grep -oP '(?<=<h3 class=").+?(?=</h3>)' | head -3

# Or use a SERP API if available
```

### Internal Link Check
```bash
# Count internal links to same domain
curl -s <url> | grep -o '<a href="[^"]*' | 
  grep -i 'yourdomain\.com' | 
  wc -l

# Extract anchor text samples
curl -s <url> | grep -o '<a href="[^"]*yourdomain[^"]*">[^<]*</a>' | 
  sed 's/<a[^>]*>\([^<]*\)<\/a>/\1/' | 
  head -5
```

### Meta Tags
```bash
curl -s <url> | grep -i '<meta name="title"\|<meta name="description"\|<meta property="og:title"\|<meta property="og:description"'
```

### Schema Validation
```bash
# Extract JSON-LD
curl -s <url> | grep -o '<script type="application/ld\+json">.*</script>' | 
  sed 's/<script type="application\/ld\+json">//;s/<\/script>//' | 
  python3 -m json.tool  # or pipe to validator
```

### Image Audit
```bash
# Count images
curl -s <url> | grep -c '<img'

# Sample image tags with alt
curl -s <url> | grep -o '<img[^>]*alt="[^"]*"[^>]*>' | head -3
```

### Readability Quick Check
```
# Flesch Reading Ease (target 60-70 for general audience)
# 90-100 = 5th grade, 60-70 = 8th-9th grade, 0-30 = college graduate
# Install: pip install textstat
python3 -c "import textstat; print(textstat.flesch_reading_ease(open('/tmp/article.txt').read()))"
```

## Red Flags (Instant Priority)

- **Word count < 500** → almost certainly thin content needing major expansion
- **No answer in first 50 words** → users will bounce immediately
- **Zero internal links** → missing topical authority signal
- **Title > 70 characters** → gets cut off in SERP, hurts CTR
- **Description missing keyword** → lost relevance signal
- **No schema** → missing rich result eligibility, AI visibility
- **No images** → walls of text hurt engagement and time-on-page
- **Every sentence > 25 words** → hurts readability, especially on mobile
- **Zero personal examples** → feels theoretical, not actionable
- **No author bio or trust signals** → low E-E-A-T, hurts rankings in YMYL niches

## Going Deeper (If Quick Check Shows Issues)

If 2+ red flags appear, run the full enhancement protocol:
1. Answer-first & intent match
2. Semantic gaps & missing entities  
3. Internal linking (contextual, varied anchors)
4. Optimized meta title & description
5. Schema markup (Article/FAQPage/HowTo)
6. Helpful images + SEO alt text
7. Readability & practical examples (Hormozi/Ferriss style)
8. E-E-A-T & trust signals
