---
name: editorial-post-enhancement
description: "Enterprise blog post audit & enhancement. Use when upgrading any published or draft blog post for #1 ranking potential: rapid audit for ranking blockers, Hormozi/Ferriss voice rewrite, semantic keyword enrichment, beautiful HTML design, image gallery integration, internal linking, schema markup, SEO/GEO/AEO meta optimization. Triggers on improving a blog post, enriching an article, adding internal links, adding media, improving FAQ design, strengthening SEO/GEO/AEO, closing topic gaps, or polishing into a premium article."
---

# Editorial Post Enhancement — #1 Ranking Content System

## Purpose
Transform ANY blog post into a premium, ranking-dominating asset that's helpful, practical, human-written, visually stunning, and technically perfect for SEO + AI visibility.

## When to Use
- Audit and fix a blog post that's not ranking well
- Rewrite content in Hormozi/Ferriss style (practical, punchy, no fluff)
- Enrich posts with missing semantic keywords and entities
- Add beautiful HTML design elements (tables, tip boxes, comparisons)
- Integrate 2-3 relevant images from media gallery with SEO alt text
- Build high-quality internal links with rich anchor text
- Add comprehensive schema markup (Article, FAQPage, BreadcrumbList, HowTo)
- Optimize meta title/description for SEO + GEO + AEO

**Do NOT use for:** Writing articles from scratch (→ `content-strategy-planning`), conversion page copy (→ `conversion-copywriting`).

## Triage Protocol
Before ANY enhancement:
1. **Fetch post** via REST API with `_fields=id,title,content,meta,yoast_meta,categories,tags,featured_media`
2. **Fetch site posts** for internal linking candidates (batch, `_fields=id,title,slug,categories`)
3. **Fetch media gallery** for image candidates (`/wp-json/wp/v2/media?per_page=100&_fields=id,source_url,alt_text,media_details`)
4. **Identify content type** — page vs post vs CPT
5. **Plan rollback** — save original content before modifying

## Inputs Required (Pre-Flight)
1. **Post ID or URL** — Target post to enhance
2. **Site credentials** — App password or WP-CLI access
3. **Target keyword** — Primary keyword to rank for (if not obvious from content)
4. **Competitor URLs** — Top 3-5 SERP results (for content gap analysis)
5. **Brand voice** — Hormozi/Ferriss style (punchy, practical, direct)

## Phase 1: Rapid Content Audit (2 min)

### Ranking Blocker Checklist
Scan the post and identify ALL blockers:

| Blocker | Check | Fix Priority |
|---------|-------|--------------|
| **No H1 or weak H1** | Must contain primary keyword | CRITICAL |
| **Thin content** | <1500 words = thin for competitive keywords | HIGH |
| **No TL;DR** | Scanners bounce without summary | HIGH |
| **Missing internal links** | Target: 6-10 contextual links | HIGH |
| **No FAQ section** | Missing AEO/AI visibility | HIGH |
| **No schema markup** | AI can't parse structure | HIGH |
| **Weak meta title** | Missing keyword or value prop | HIGH |
| **Weak meta description** | Missing keyword, CTA, or benefit | MEDIUM |
| **No images** | Or images with generic alt text | MEDIUM |
| **Keyword stuffing** | Unnatural repetition hurts readability | MEDIUM |
| **No table of contents** | Long posts need navigation | MEDIUM |
| **No comparison tables** | When discussing options | MEDIUM |
| **Wall of text** | No subheadings for 400+ words | MEDIUM |
| **Missing H2/H3 structure** | Flat hierarchy confuses crawlers | MEDIUM |
| **No expert quotes/stats** | No authority signals | LOW |
| **No video embed** | Missing engagement signal | LOW |

### Content Quality Score (0-25)
| Dimension | Points | What to Check |
|-----------|--------|---------------|
| **Keyword targeting** | /5 | Primary in H1, first 100 words, meta title, meta description |
| **Content depth** | /5 | Word count, topic coverage, unique insights vs competitors |
| **Readability** | /5 | Hormozi/Ferriss style: short sentences, practical examples, no fluff |
| **Internal linking** | /5 | 6-10 contextual links with rich anchor text |
| **Technical SEO** | /5 | Schema, meta tags, image alt text, URL structure |
| **Minimum for publishing** | **≥18/25** | |

## Phase 2: Hormozi/Ferriss Voice Rewrite

### The Hormozi Style
Alex Hormozi writes like he's talking to a friend who needs the answer NOW:

**Principles:**
- **Answer first** — Lead with the conclusion, not the buildup
- **Short paragraphs** — 2-3 sentences max, then whitespace
- **Direct language** — "Here's the thing:" "The real problem is..." "Let me be blunt:"
- **Practical examples** — Real scenarios, not abstract theory
- **Numbered steps** — "Step 1: Do this. Step 2: Do that."
- **Bold claims backed by proof** — "This increased conversions 340%. Here's how:"
- **Bullet points** — Dense information in scannable format
- **Conversational tone** — "Look," "Here's what most people miss," "The bottom line:"
- **One idea per paragraph** — Don't cram multiple concepts
- **Power words** — "Guaranteed," "Proven," "Exactly," "Specifically"

### The Ferriss Style
Tim Ferriss writes like a researcher who tested everything so you don't have to:

**Principles:**
- **Personal experiments** — "I tried X for 30 days. Here's what happened:"
- **Data + stories** — Combine numbers with real narratives
- **Contrarian takes** — "Most people think X. The data says Y."
- **Frameworks** — Give readers a system they can apply TODAY
- **Quotes from experts** — "As Dr. Smith told me..."
- **Case studies** — "Here's how [Person] did [Thing] in [Timeframe]"
- **Practical tools** — Specific apps, templates, scripts
- **Time-bounded experiments** — "Try this for 7 days"

### Rewrite Checklist
For EVERY paragraph, ask:
- [ ] Is this practical or theoretical? → Make it practical
- [ ] Can I add a personal/example scenario? → Add it
- [ ] Is this sentence too long? → Break it
- [ ] Am I saying something obvious? → Cut it
- [ ] Does this help the reader DO something? → If no, rewrite or remove

### Example Transformation
**BEFORE (Theoretical):**
> "Internal linking is an important SEO strategy that helps search engines understand your site structure and distribute page authority."

**AFTER (Hormozi/Ferriss):**
> "Here's the thing about internal links — they're free SEO juice you're probably leaving on the table. When I added 8 strategic internal links to a 2,000-word post, organic traffic jumped 47% in 3 weeks. No new content. No backlinks. Just links."

## Phase 3: Semantic Keyword & Entity Enrichment

### Finding Missing Keywords
1. **Extract post topic** from title and H1
2. **Identify semantic cluster** — What related terms MUST appear?
3. **Check competitor content** — What entities/terms do top 5 results include?
4. **Find gaps** — What's missing from YOUR post?

### Entity Types to Include
| Entity Type | Example | Why It Matters |
|-------------|---------|----------------|
| **People** | Industry experts, founders | Authority signals |
| **Companies** | Tools, brands, services | Topical relevance |
| **Concepts** | Technical terms, frameworks | Semantic depth |
| **Data points** | Statistics, percentages, dates | E-E-A-T signals |
| **Locations** | Cities, countries (if relevant) | Local SEO |
| **Products** | Specific tools, models | Commercial relevance |

### Integration Rules
- **Natural placement** — Don't force entities; add where they genuinely help
- **Contextual** — Explain WHY the entity matters to the reader
- **Spread evenly** — Don't cluster all entities in one section
- **Link to authority** — When mentioning a company/tool, link to their site

### Keyword Density Targets
- **Primary keyword**: 1-2% density (natural, not forced)
- **Secondary keywords**: 0.5-1% each
- **Semantic entities**: As many as naturally fit (aim for 15-25 unique entities)

## Phase 4: Beautiful HTML Design Elements

### Modern CSS System (Add to post)
```html
<style>
/* Content Enhancement System */
.ep-wrap { max-width: 860px; margin: 0 auto; font-family: 'Inter', system-ui, sans-serif; line-height: 1.7; }
.ep-tldr { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 24px; border-radius: 12px; margin: 24px 0; }
.ep-tldr h3 { margin: 0 0 12px; font-size: 1.1rem; }
.ep-tip { background: #f0fdf4; border-left: 4px solid #22c55e; padding: 16px 20px; border-radius: 0 8px 8px 0; margin: 20px 0; }
.ep-warning { background: #fefce8; border-left: 4px solid #eab308; padding: 16px 20px; border-radius: 0 8px 8px 0; margin: 20px 0; }
.ep-step { background: #eff6ff; border-left: 4px solid #3b82f6; padding: 16px 20px; border-radius: 0 8px 8px 0; margin: 20px 0; counter-increment: step; }
.ep-comparison { width: 100%; border-collapse: collapse; margin: 24px 0; }
.ep-comparison th { background: linear-gradient(135deg, #1e293b, #334155); color: white; padding: 12px 16px; text-align: left; text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.85rem; }
.ep-comparison td { padding: 12px 16px; border-bottom: 1px solid #e2e8f0; }
.ep-comparison tr:hover td { background: #f8fafc; }
.ep-faq details { border: 1px solid #e2e8f0; border-radius: 8px; margin: 8px 0; }
.ep-faq summary { padding: 16px; cursor: pointer; font-weight: 600; }
.ep-faq summary:hover { background: #f8fafc; }
.ep-faq .answer { padding: 0 16px 16px; color: #475569; }
.ep-cta { background: linear-gradient(135deg, #f97316, #ea580c); color: white; padding: 20px 24px; border-radius: 12px; text-align: center; margin: 24px 0; }
.ep-cta a { color: white; font-weight: 700; }
.ep-img { border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin: 24px 0; }
@media (max-width: 768px) { .ep-comparison { display: block; overflow-x: auto; } }
</style>
```

### HTML Elements to Use
| Element | When to Use | Example |
|---------|------------|---------|
| `ep-tldr` | Top of post — key takeaways | Summary box with gradient |
| `ep-tip` | Pro tips, best practices | Green left border |
| `ep-warning` | Common mistakes, gotchas | Yellow left border |
| `ep-step` | Step-by-step instructions | Blue left border |
| `ep-comparison` | Comparing options/tools | Styled table |
| `ep-faq` | FAQ section | Collapsible details/summary |
| `ep-cta` | Call to action | Orange gradient box |
| `ep-img` | Content images | Rounded corners + shadow |

### Gutenberg Block Format
Wrap all HTML in `<!-- wp:html -->` blocks to prevent wpautop corruption:
```html
<!-- wp:html -->
<div class="ep-wrap">
  <div class="ep-tldr">
    <h3>TL;DR</h3>
    <p>Key takeaways here...</p>
  </div>
</div>
<!-- /wp:html -->
```

## Phase 5: Image Integration

### Process
1. **Fetch media gallery**: `GET /wp-json/wp/v2/media?per_page=100&_fields=id,source_url,alt_text,title,media_details`
2. **Search for relevance**: Match images to post content by title/alt text
3. **Select 2-3 images**: One featured, 1-2 in-content
4. **Update alt text**: SEO-optimized with keyword + description
5. **Insert into post**: With `ep-img` class for styling

### Alt Text Formula
```
[Primary keyword] + [specific description] + [context]
```
**Example**: "WordPress SEO audit showing internal linking structure in Yoast analysis"

### Image Placement Rules
- **Featured image**: Hero/top of post
- **In-content images**: Every 800-1000 words, after a key point
- **Near keywords**: Place images close to primary keyword mentions
- **Break up text**: Use images to separate long sections

## Phase 6: Internal Linking System

### Link Requirements
| Metric | Target | Minimum |
|--------|--------|---------|
| Internal links | 8-12 | 6 |
| Unique posts linked | 6-10 | 4 |
| Rich anchor text | 100% | 80% |
| Distribution | Throughout | Not clustered |

### Anchor Text Rules
**DO:**
- Use descriptive phrases: "our complete guide to WordPress SEO optimization"
- Use keyword variations: "how to improve site speed"
- Use natural phrases: "as we covered in our content audit checklist"

**DON'T:**
- Generic: "click here," "read more," "this article"
- URL as anchor: "https://..."
- Single word: "guide," "post," "article"

### Finding Link Candidates
```
GET /wp-json/wp/v2/posts?per_page=100&_fields=id,title,slug,categories&search={topic}
```
- Match by category overlap
- Match by keyword in title
- Match by semantic similarity to current post
- Prioritize high-authority pages (homepage, pillar content)

## Phase 7: Schema Markup (AI Visibility Boost)

### Required Schemas (Every Post)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Post Title Here",
      "description": "Meta description",
      "datePublished": "2026-01-01",
      "dateModified": "2026-03-17",
      "author": { "@type": "Person", "name": "Author Name" },
      "publisher": { "@type": "Organization", "name": "Site Name", "logo": { "@type": "ImageObject", "url": "logo-url" } },
      "image": "featured-image-url",
      "mainEntityOfPage": { "@type": "WebPage", "@id": "post-url" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Question text?",
          "acceptedAnswer": { "@type": "Answer", "text": "Answer text." }
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "site-url" },
        { "@type": "ListItem", "position": 2, "name": "Category", "item": "category-url" },
        { "@type": "ListItem", "position": 3, "name": "Post Title" }
      ]
    }
  ]
}
</script>
```

### Optional Schemas (When Applicable)
| Schema Type | When to Use |
|-------------|-------------|
| `HowTo` | Step-by-step tutorials |
| `Product` | Product reviews/comparisons |
| `Review` | Reviewing a tool/service |
| `VideoObject` | Embedded video content |
| `Speakable` | Voice assistant optimization |
| `ItemList` | Listicles ("Top 10...") |

### Schema Placement
- Append to post content as `<script type="application/ld+json">`
- AFTER the HTML content, BEFORE the closing `<!-- /wp:html -->`
- One `<script>` block per schema type (or use @graph for multiple)

## Phase 8: SEO/GEO/AEO Meta Optimization

### Meta Title Formula
```
[Primary Keyword] — [Specific Benefit/Hook] ([Year])
```
**Examples:**
- "WordPress SEO Audit — Find & Fix Ranking Blockers in 15 Min (2026)"
- "Internal Linking Strategy — How We Boosted Traffic 47% in 3 Weeks"

**Rules:**
- 50-60 characters max
- Primary keyword in first 30 characters
- Include year if time-sensitive
- NO keyword stuffing
- Compelling but honest (no clickbait)

### Meta Description Formula
```
[Problem/Question]. [Solution/Benefit]. [CTA/Bonus].
```
**Examples:**
- "Struggling to rank? Learn the exact WordPress SEO audit process that found 12 ranking blockers in 15 minutes. Free checklist included."

**Rules:**
- 150-160 characters max
- Primary keyword in first 80 characters
- Include a clear benefit
- End with CTA or bonus
- Natural language, not keyword soup

### GEO (Generative Engine Optimization)
- Include clear, declarative statements AI can cite
- Use "According to..." patterns with data
- Include FAQ section with direct answers
- Structure content with clear headings AI can parse
- Add speakable schema for voice assistants

### AEO (Answer Engine Optimization)
- Answer common questions directly in first sentence
- Use question-format H2/H3 headings
- Provide concise answers (40-60 words) then expand
- Include FAQ section with 5-7 questions
- Use structured data to help engines understand content

## Speed Optimizations

### Parallel Operations
```
1. PARALLEL: Fetch post + categories + media + related posts
2. PARALLEL: SERP analysis + content audit + image search
3. SEQUENTIAL: Rewrite content with Hormozi/Ferriss style
4. PARALLEL: Generate schema + build FAQ + find internal links
5. SEQUENTIAL: Assemble final post with all enhancements
6. PARALLEL: Update post + verify live + check body class
```

### API Speed
- Always use `_fields` parameter (80% payload reduction)
- Use `per_page=100` for batch fetches
- Cache post/category maps in session
- Use `concurrent.futures` for parallel API calls (max 10/site)

## Error Recovery (Auto-Learning)
- Track error patterns — after 2 failures, try alternative approach
- Log recurring fixes to `memory/YYYY-MM-DD.md`
- Update references when new patterns discovered
- Rollback plan: Save original content before modifying

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Audit** (1-5): Were all ranking blockers identified and fixed?
2. **Voice** (1-5): Does the content read like Hormozi/Ferriss — practical, punchy, no fluff?
3. **SEO** (1-5): Meta title/description optimized? Schema markup present? Internal links solid?
4. **Visual** (1-5): Beautiful HTML elements? Images with alt text? Mobile-friendly?
5. **AEO/GEO** (1-5): FAQ section? Structured facts? AI-visibility optimized?

**Target: 22+/25**

## Output Contract
- **Artifact**: Enhanced post with Hormozi/Ferriss voice, semantic keywords, beautiful HTML, images, internal links, schema, optimized meta
- **Evidence**: Quality score ≥22/25, all ranking blockers fixed, live verification
- **Decision**: Post approved for publishing/re-publishing
- **Next**: Monitor rankings for 2-4 weeks, track traffic changes

## Anti-Patterns
- ❌ Keyword stuffing (hurts readability, triggers spam filters)
- ❌ All internal links clumped in one section
- ❌ Generic FAQ that doesn't answer real questions
- ❌ Stock images with zero informational value
- ❌ Ignoring mobile experience (check tables overflow, images scale)
- ❌ Removing the article's voice and personality
- ❌ Theoretical content with no practical examples
- ❌ Missing schema markup (AI can't parse your content)
- ❌ Weak meta title/description (kills CTR)
- ❌ No images or images with generic alt text

## Compatibility
- Targets current WordPress 6.9+ where applicable
- REST API + WP-CLI preferred over browser automation
- Batch operations via `_fields` + `per_page=100` + `concurrent.futures`
- Browser automation only when API/CLI insufficient

## Inputs Required (Pre-Flight)
Before executing any task in this skill:
1. **Target identification** — What site, page, post, or system is being operated on?
2. **Auth verification** — Confirm credentials work (test API call or CLI command)
3. **Current state** — Understand what exists before making changes (GET before POST)
4. **Environment** — Production vs staging (assume production unless stated)
5. **Constraints** — No downtime? Preserve SEO? Preserve data? Budget limits?

## Triage Protocol
Before ANY operation:
1. **Identify** — What type of content/system/problem is this?
2. **Check state** — Query current state via API/CLI before modifying
3. **Verify creds** — Confirm authentication works
4. **Plan rollback** — How to undo if something breaks?
5. **Scope check** — Is this a single item or batch? Scale determines approach.

## Speed Optimizations
- **API calls**: Always use `_fields` parameter (80%+ payload reduction)
- **Pagination**: Use `per_page=100` for list endpoints
- **Parallelism**: Use `concurrent.futures` for independent operations (max 10/site)
- **Caching**: Store results in session — never re-fetch same data
- **Batching**: Group similar operations into single API calls where possible
- **Direct CLI**: Use WP-CLI `wp db query` for complex operations

## Error Recovery (Auto-Learning)
- Track error patterns — after 2 failures, try alternative approach
- Log recurring fixes to `memory/YYYY-MM-DD.md`
- Update references when new patterns discovered
- Rollback plan: Know how to undo before making changes

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

## Output Contract
- **Artifact**: What was created/changed/deleted
- **Evidence**: API response proof + live verification
- **Decision**: Success/failure with reasoning
- **Next**: What follow-up is needed (if any)
