---
name: editorial-post-enhancement
description: Use when analyzing a blog post to quickly identify top SEO, readability, and conversion issues, then enhance it with missing keywords/entities, internal links, schema, optimized meta, images, and practical examples in the style of Alex Hormozi/Tim Ferriss. Triggers on requests to improve an existing article for rankings, traffic, engagement, or topical authority.
---

# Editorial Post Enhancement

## Purpose
Take a draft or published article and turn it into a high‑performing, human‑written asset that ranks #1, engages readers, and drives conversions—using fast diagnostics, semantic gap filling, practical examples, and enterprise‑grade publishing quality.

## Use this when
- you have an existing blog post or article (draft or live) and need to improve its SEO, readability, or conversion power
- the article is not ranking in the top 3 for its target keyword despite decent effort
- you want to add missing semantically relevant keywords, entities, and LSI terms naturally
- you need to add practical, personal examples in the style of Alex Hormozi or Tim Ferriss
- the article lacks internal links, schema markup, optimized meta title/description, or helpful media
- you suspect thin content, weak E‑E‑A‑T, or poor answer‑first structure
- you need to verify the article does not cannibalize another page before enhancing

## Do NOT use this for
- creating a brand‑new article from scratch (→ `conversion-copywriting`)
- planning a content calendar or keyword research (→ `content-strategy-planning`)
- performing a site‑wide technical SEO audit (→ `seo-audit-playbook`)
- fixing WordPress plugin/theme or server performance (→ `infrastructure-ops` or `wordpress-growth-ops`)
- pure copy‑editing for grammar/tone only (→ `copy-editing-sweeps`)

## Self‑Improvement Protocol

After each enhancement run this critique loop:

1. **Gap capture:** Did the analysis reveal a new missing entity/keyword pattern? Add it to `references/semantic-gap-patterns.md`.
2. **Example quality:** Were the Hormozi/Ferriss‑style examples actually practical and personal? Rate 1‑5 and note improvements.
3. **Link relevance:** Did added internal links use contextual, varied anchor text? Audit a sample.
4. **Schema validity:** Does the generated JSON‑LD pass Google’s Rich Results Test? Log any errors.
5. **Image relevance:** Are added images truly helpful and SEO‑optimized (alt text, filename, size)?
6. **Metric prediction:** Based on the changes, estimate the expected traffic lift (low/medium/high) and note reasoning.
7. **Update playbook:** If any step revealed a better shortcut, update `references/quick‑analysis‑checklist.md`.

## Do this

### Phase 0: Rapid Triage & Extraction (< 90 seconds)

Run these commands to pull the article and core data:

```bash
# If the article is in WordPress:
wp post get <post-id> --field=post_content --format=raw > /tmp/article.html
wp post get <post-id> --field=post_title,post_excerpt --format=json

# If you have a raw HTML file or URL:
curl -s <url> > /tmp/article.html   # or cp /path/to/file.html /tmp/article.html

# Strip to readable text for quick analysis
pandoc /tmp/article.html -t plain -o /tmp/article.txt  # requires pandoc
# or use: html2text /tmp/article.html > /tmp/article.txt
```

**Quick signals (glance at):**
- Word count (< 800 = thin, > 2500 = possibly over‑optimized)
- Heading structure (`grep -c '^#' /tmp/article.txt` or count H2/H3)
- Presence of list/table/media (`grep -ci '<ul\|<ol\|<table\|<img' /tmp/article.html`)
- External links density (`grep -ci 'href="http' /tmp/article.html`)

### Phase 1: Diagnostic – Find the Top 3 Blockers

Use this ordered checklist to spot the biggest ranking/conversion issues fast.

#### 1.1 Answer‑First & Intent Match
- Does the first 100 words answer the query directly? (If targeting “how to fix X”, does step 1 appear in the first 2 sentences?)
- Is the search intent (informational, commercial, transactional) matched by the content’s promise?
- **Fix:** Rewrite the opening to lead with the direct answer or benefit, then elaborate.

#### 1.2 Semantic Gaps (Missing Keywords/Entities)
- Run a quick SERP scan: `curl -s "https://www.google.com/search?q=<target+keyword>&num=10" | grep -oP '(?<=<h3>).+?(?=</h3>)'` to get competing titles.
- Extract entities/noun phrases from top 3 pages (use a simple tool or manually note recurring concepts).
- Compare to your article: which entities/concepts are missing?
- **Common gaps:** brand names, specific metrics, tool names, process steps, real‑world numbers, case studies, frequently asked sub‑questions.
- **Fix:** Insert the missing entities naturally into relevant sections; add a “Key takeaways” box with bullet‑point facts if needed.

#### 1.3 Internal Linking & Topical Authority
- Does the article link to at least 2‑3 other relevant posts on your site using varied, descriptive anchor text?
- Are the links placed contextually (within a sentence that explains why the link is useful)?
- **Fix:** Add 2‑3 contextual internal links to cornerstone or related posts. Use anchors like “see how we reduced churn by 40%” instead of “click here”.

#### 1.4 Meta Title & Description (SEO + CTR)
- Is the title ≤ 60 characters, includes the target keyword near the front, and promises a benefit or number?
- Is the description ≤ 150 characters, includes a secondary keyword or long‑tail variant, and has a clear CTA (“Learn how”, “Get the checklist”)?
- **Fix:** Rewrite title and description using the formula: `[Number] + [Adjective] + [Keyword] + [Benefit] | [Brand]`.

#### 1.5 Schema Markup & AI Visibility
- Does the article have valid `Article`, `FAQPage`, or `HowTo` schema (JSON‑LD) in the `<head>`?
- Are critical properties filled: `author`, `datePublished`, `image`, `description`, `keywords` (if applicable)?
- **Fix:** Add the most appropriate schema type. For most informational posts use `Article` with `author` (Person or Organization), `publisher`, `datePublished`, `dateModified`, `image`, and `keywords`.

#### 1.6 Media & Visual Engagement
- Does the article have at least one helpful image above the fold and 2‑3 more throughout?
- Are images optimized (proper dimensions, compressed, lazy‑loaded)?
- Is alt text descriptive and includes a keyword when natural?
- **Fix:** 
  - Search the media library for images matching the post’s topic; download and insert.
  - If none exist, create a simple diagram/table using Markdown→HTML or note to create a custom graphic.
  - Set alt text to describe the image + include a keyword if relevant (e.g., “screenshot showing HubSpot workflow for lead scoring”).
  - Add width/height attributes to prevent layout shift.

#### 1.7 Readability & Practicality (Hormozi/Ferriss Style)
- Is the language conversational, short‑sentence, and free of jargon?
- Does every major claim have a concrete example, personal story, or data point?
- Is the tone “us helping you” rather than “here is a lecture”?
- **Fix:** 
  - Replace vague statements with specific numbers or anecdotes (“Increasing conversions by 23%” → “When we changed the CTA color from blue to orange, our free‑trial sign‑ups jumped from 120 to 148 in one week”).
  - Break long sentences (>20 words) into two.
  - Add a “What this means for you” box after complex sections.
  - Use bold sparingly to highlight key takeaways.

#### 1.8 E‑E‑A‑T & Trust Signals
- Is the author’s expertise shown (credentials, real‑world results)?
- Are there trust elements: testimonials, case studies, data sources, transparent methodology?
- **Fix:** 
  - Add an author bio with specific achievements (“John has helped 200+ SaaS founders reduce CAC by 30%”).
  - Embed a short testimonial or case study snippet.
  - Link to reputable sources for any statistics cited.

### Phase 2: Apply Fixes (One Layer at a Time)

Follow the order above, but only move to the next layer after verifying the current fix:

1. Answer‑first & intent
2. Semantic gaps (keywords/entities)
3. Internal linking
4. Meta title/description
5. Schema markup
6. Media & images
7. Readability/practicality
8. E‑E‑A‑T/trust

After each change, run a quick self‑critique:
- Did I verify the change works in the rendered HTML (not just the source)?
- Did I keep the article’s original voice unless it was harmful?
- Did I add value, not just fluff?

### Phase 3: Final Validation

```bash
# 1. Schema test
curl -s <url> | grep -o '<script type="application/ld\+json">.*</script>' | head -1 | \
  python3 -m json.tool  # or pipe to Google’s Rich Results Test API

# 2. Meta tags
curl -s <url> | grep -i '<meta name="description"\|<meta property="og:title"'

# 3. Image audit
curl -s <url> | grep -i '<img' | head -5

# 4. Internal link sample
curl -s <url> | grep -i '<a href' | grep -i '<your-domain>' | head -3

# 5. Quick readability score (optional)
# Install: pip install textstat
# python3 -c "import textstat; print(textstat.flesch_reading_ease(open('/tmp/article.txt').read()))"
```

**Decision criteria:**
- ✅ Schema valid (no errors)
- ✅ Meta title/description present and within limits
- ✅ At least 2‑3 helpful images with SEO‑optimized alt text
- ✅ At least 2‑3 contextual internal links
- ✅ Answer appears in first 1‑2 sentences
- ✅ Readability score ≥ 60 (good for general audience)
- ✅ No keyword stuffing (keyword density < 2% for primary term)

If any ❌ → fix that item before declaring done.

## Operating rules
- Start with the article’s **goal** (rank, traffic, leads, sales) and tailor enhancements to that.
- Always extract the raw content first — never guess what’s live.
- Fix semantic gaps before adding fluff; missing entities hurt rankings more than missing images.
- Use fresh, personal examples — never invent data or fake stories.
- Keep enhancements proportional: a 1000‑word post needs ~3‑5 major upgrades, not a 20‑point checklist.
- Validate schema and meta tags with live URL, not just source.
- Prefer updating the existing post over creating a duplicate unless splitting intent.
- Document every non‑obvious change in `memory/YYYY-MM-DD.md` for pattern learning.

## Default enhancement order
1. Answer‑first & intent match
2. Semantic gaps & missing entities
3. Internal linking (contextual, varied anchors)
4. Optimized meta title & description
5. Schema markup (Article/FAQPage/HowTo)
6. Helpful images + SEO alt text
7. Readability & practical examples (Hormozi/Ferriss style)
8. E‑E‑A‑T & trust signals

## Build vs buyer rule
- **Internal assets:** enhancement notes, change logs, diagnostic screenshots, internal‑link map.
- **Buyer assets:** the final enhanced article, images, schema, meta tags — everything the visitor sees.

Never ship internal diagnostics as if they were reader value.

## Resources
Read when needed:
- `references/quick‑analysis‑checklist.md` — 90‑second triage flowchart
- `references/semantic‑gap‑patterns.md` — learned missing entities/keywords by topic
- `references/practical‑examples‑library.md` — Hormozi/Ferriss‑style templates
- `references/image‑alt‑text‑guide.md` — SEO‑friendly alt text formulas
- `references/schema‑templates.md` — ready‑to‑paste JSON‑LD for Article, FAQPage, HowTo
- `references/meta‑title‑formulas.md` — CTR‑optimized title templates
- `references/internal‑link‑anchor‑guide.md` — contextual anchor text formulas

## Checks and common mistakes
- Do not add schema without testing it (invalid JSON‑LD can hurt rich‑result eligibility).
- Do not stuff keywords — use synonyms and natural language.
- Do not ignore cannibalization — run `seo-audit-playbook` first if unsure.
- Do not make every sentence sound like a sales pitch; keep educational tone.
- Do not forget mobile rendering — images that are huge on desktop break layout on phones.
- Do not add internal links with exact‑match anchor text every time (looks manipulative).
- Do not forget to update the `modified` date in WordPress after enhancing.
- Do not over‑optimize meta title — if it reads like spam, CTR will drop.
- Do not add images without checking copyright — use your own media library or royalty‑free sources.

## Output contract
**Artifact:** Enhanced blog post (HTML or WordPress update) with improved SEO, readability, and conversion elements.
**Evidence:** 
- Schema validation pass (Google Rich Results Test or equivalent)
- Meta title/description within length limits and include keyword + benefit
- At least 2‑3 contextual internal links with varied, descriptive anchors
- At least 2‑3 helpful images with SEO‑optimized alt text (filename, alt, dimensions)
- Answer to target query appears in first 1‑2 sentences
- Readability score ≥ 60 (Flesch) or equivalent
- No keyword stuffing (primary term < 2% density)
- Added at least one practical, personal example in the style of Hormozi/Ferriss
**Decision:** Ready to publish/update, needs more work (specify which layer), or blocked by cannibalization/intent mismatch (route to `seo-audit-playbook` or `offer-positioning`).
**Next:** Publish/update, monitor rankings/CTA clicks for 48 h, run self‑improvement protocol, or escalate to a more specific execution skill.
