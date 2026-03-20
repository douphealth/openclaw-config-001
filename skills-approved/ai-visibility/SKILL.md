---
name: ai-visibility
description: "AI search visibility and Generative Engine Optimization (GEO) for tracking and improving brand presence in AI-generated answers. Use when optimizing for Perplexity, ChatGPT, Google AI Overviews, Gemini, Copilot, or other AI search engines. Triggers on AI visibility, GEO optimization, AI search presence, AI answer citations, Perplexity rankings, ChatGPT mentions, AI snippet optimization, or requests to appear in AI-generated answers."
---

# AI Visibility — Generative Engine Optimization (GEO) + AEO

## Purpose
Track, measure, and improve brand/product visibility in AI-generated search answers across Perplexity, ChatGPT, Google AI Overviews, Gemini, and Copilot.

## When to Use
- "Why doesn't our brand show up in Perplexity/ChatGPT?"
- AI search visibility audits
- GEO optimization for existing content
- AEO (Answer Engine Optimization) for featured snippets
- Structured data for AI comprehension
- Content optimization for AI citation
- Monitoring brand mentions in AI answers
- Competitive AI visibility analysis

**Do NOT use for:** Traditional SEO auditing (→ `seo-audit-playbook`), GSC/Bing data pulling (→ `seo-intelligence`), content writing (→ `editorial-post-enhancement`).

## Triage Protocol
1. **Test current visibility** — Query Perplexity, ChatGPT, Google AI for target keywords
2. **Identify citation sources** — Who IS getting cited? Why?
3. **Gap analysis** — What content/format is missing?
4. **Schema audit** — Check existing structured data
5. **Action plan** — Prioritize by query volume × AI answer frequency

## Inputs Required (Pre-Flight)
1. **Target site URL**
2. **10-20 target queries** to test in AI engines
3. **Competitor list** (who appears in AI answers currently)
4. **Existing schema** (check via schema validator)

## SOTA AEO Analytics Upgrade Layer
- Use `../../skills/shared/references/seo-aeo-geo-superpowers.md` as the shared framework.
- Track visibility over time, not as a one-off sample.
- Measure at minimum: Mention Rate, Citation Rate, Primary Citation Rate, AI Share of Voice, and Tier-1 Prompt Coverage.
- Connect every citation gap back to a concrete content/system fix: new page, refresh, FAQ, definition block, entity reinforcement, or trust upgrade.

## AI Search Landscape (2026)

| Platform | Citation Method | Optimization Focus | Data Source |
|----------|----------------|-------------------|-------------|
| **Perplexity** | Links sources in answers | Clear headings, factual statements, E-E-A-T | Own index |
| **ChatGPT** | Uses Bing index + live browsing | Bing SEO, structured content, freshness | Bing + live |
| **Google AI Overviews** | Pulls from indexed pages | Traditional SEO + FAQ/HowTo schema | Google index |
| **Gemini** | Google index based | Same as AI Overviews + Google entities | Google index |
| **Copilot** | Bing + web sources | Bing SEO, Microsoft ecosystem | Bing index |
| **Claude (web)** | Live web search | Clear, citable content | Real-time search |

## GEO Optimization Framework

### 1. Structured Facts (Critical for AI Parsing)
AI engines need to PARSE your content. Make it easy:

**Use declarative statements:**
```
✅ "WordPress powers 43% of all websites as of 2026."
❌ "WordPress is said to power a significant portion of websites."
```

**Use definition patterns:**
```
✅ "SEO (Search Engine Optimization) is the practice of optimizing 
    web content to rank higher in search engine results pages."
```

**Use entity relationships:**
```
✅ "Alex Hormozi is the founder of Acquisition.com, a holding company 
    that invests in service-based businesses."
```

### 2. Citation-Worthy Content
AI engines cite content that looks authoritative:

| Signal | Implementation |
|--------|---------------|
| **Specific numbers** | "47% increase" not "significant increase" |
| **Dates** | "As of March 2026" not "recently" |
| **Expert quotes** | "According to Google's John Mueller..." |
| **Primary sources** | Link to original research, not summaries |
| **Author credentials** | "Written by [Name], [Credential]" |
| **Publication dates** | Visible "Last updated: [Date]" |

### 3. AI-Friendly Formatting
```
H2: What is [Topic]?
  → Direct definition (1-2 sentences)
  → Key facts (bullet list)
  
H2: How does [Topic] work?
  → Step-by-step explanation
  → Numbered list
  
H2: [Specific Question]?
  → Direct answer (40-60 words)
  → Supporting details

H2: Key Takeaways
  → Bullet list of main points
```

### 4. Schema & Structured Data Stack

**Priority order for AI visibility:**

1. **FAQPage** (highest impact for AI)
2. **HowTo** (process content)
3. **Article** (with author, dates, publisher)
4. **Organization** (with sameAs links)
5. **Person** (author schema)
6. **Speakable** (voice optimization)
7. **BreadcrumbList** (site structure)
8. **Product** (if applicable)
9. **Review** (if applicable)

**Complete AI Visibility Schema:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Title",
      "datePublished": "2026-01-01",
      "dateModified": "2026-03-17",
      "author": {"@type": "Person", "name": "Author", "jobTitle": "Expert"},
      "publisher": {"@type": "Organization", "name": "Site", "logo": {"@type": "ImageObject", "url": "logo"}},
      "mainEntityOfPage": {"@type": "WebPage", "@id": "url"}
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "Q?", "acceptedAnswer": {"@type": "Answer", "text": "A."}}
      ]
    },
    {
      "@type": "SpeakableSpecification",
      "cssSelector": [".ep-tldr", "h2", ".faq-section"]
    }
  ]
}
</script>
```

### 5. AEO (Answer Engine Optimization)

**Answer Box Targeting:**
- Format questions as H2/H3: "How do I fix WordPress indexation?"
- Answer in first sentence: Direct, 40-60 word answer
- Then expand: Details, examples, steps
- Use lists: Google pulls lists for featured snippets
- Use tables: Comparison data in table format

**People Also Ask (PAA) Integration:**
- Search target keyword in Google
- Note all PAA questions
- Create H2/H3 headings matching PAA questions
- Answer each directly in first sentence
- Add to FAQ schema

**Featured Snippet Format:**
```
Paragraph snippet: 40-60 word direct answer
List snippet: Ordered/unordered list with steps
Table snippet: Comparison table with clear headers
Video snippet: Embedded video with timestamp
```

## Phase 6: Freshness Signals
- Update publication dates
- Add "Last updated: [date]" visible on page
- Regular content refreshes (quarterly minimum)
- Use `dateModified` in schema markup

## AI Visibility Audit Process

### Step 1: Query Testing (Manual + Automated)
Test each target query in:
1. Perplexity.ai — Note sources cited
2. ChatGPT with browsing — Note sources cited
3. Google (check AI Overview) — Note sources cited
4. Bing Copilot — Note sources cited

### Step 2: Citation Analysis
For each query:
- Which competitors appear?
- What content format do they use?
- What schema do they have?
- What makes them citable?

### Step 3: Gap Analysis
- Queries where brand doesn't appear
- Content formats missing
- Schema gaps
- Freshness issues

### Step 4: Optimization
- Update content for AI parseability
- Add missing schema
- Improve factual density
- Add expert citations

### Step 5: Re-Testing
- Wait 2-4 weeks
- Re-test all queries
- Document improvements
- Iterate

## Connection to GSC Data
Use `seo-intelligence` to pull:
- **High-impression queries** = Test these in AI engines
- **Position 1-3 queries** = Should already appear in AI answers
- **Declining pages** = May have lost AI citation freshness
- **Non-indexed pages** = Won't appear in any AI answer

## Monitoring
- Weekly query testing across AI platforms
- Track competitor AI citations
- Monitor AI answer accuracy (brand/product mentions)
- Alert on brand disappearing from key AI answers


## Self-Critique Scorecard (/25)
After every operation, score yourself:

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Functionality** (1-5) | ? | Does it work perfectly and meet all requirements? |
| **Quality** (1-5) | ? | Is it enterprise-grade and production-ready? |
| **Verification** (1-5) | ? | Was it verified via multiple methods? |
| **Speed** (1-5) | ? | Was execution optimal with parallel operations? |
| **Learning** (1-5) | ? | Were new patterns documented and memory updated? |

**Target: 22+/25 before claiming completion**

### Pre-Flight Checklist
- [ ] Credentials verified and target exists
- [ ] Rollback plan identified
- [ ] Success criteria defined
- [ ] Anti-patterns reviewed

### Post-Flight Checklist
- [ ] Verified via API response + live check
- [ ] Quality score logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered
- [ ] No common mistakes made

## Output Contract
**Artifact**: AI visibility audit report, GEO optimization recommendations
**Evidence**: Screenshots of AI answers, citation counts, before/after comparison
**Decision**: Content optimized for AI visibility
**Next**: Re-test in 2-4 weeks, iterate

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
