| name | description | version |
|------|-------------|--------|
| wordpress-blog-mastery | The definitive WordPress blog writing system. Covers the complete lifecycle from topic ideation through research, outlining, drafting, revision, SEO integration, visual planning, conversion architecture, internal linking intelligence, and publish-grade verification for every content type. Includes a full HTML/CSS component library for beautiful modern post design. Produces content that reads as expert-written, ranks in search, gets cited by AI, converts readers, and looks stunning on every device. Use when writing any blog post, article, guide, review, comparison, tutorial, or editorial content for a WordPress site. | 4.0 |

# WordPress Blog Mastery v4.0

Enterprise-grade content orchestration engine for SOTA blog post creation, optimization, and lifecycle management. Combines high-fidelity article drafting, semantic-refresh logic, multi-pass editorial gates, internal linking intelligence, and a professional HTML/CSS component library.

## Core Philosophical Pillars

1. **Serves the Reader:** Answers their question better than anything else available.
2. **Demonstrates Expertise:** Through specificity, experience signals, and honest analysis.
3. **Earns Trust:** By being transparent about limitations, methodology, and commercial relationships.
4. **Delivers a Premium Reading Experience:** Through intentional visual design, modern HTML structure, and friction-free navigation.

---

## PART I: INTERNAL LINKING INTELLIGENCE ENGINE

Internal links are not an afterthought; they are the primary mechanism for site structure, authority distribution, and reader retention.

### 1.1 Internal Link Planning - Link Map Construction

Before writing, build the link map for this post:

| Quantity Guideline | Post Length | Internal Links OUT | Internal Links IN |
|--------------------|-------------|--------------------|-------------------|
| Short | < 1,500 words | 4-6 | 2-3 |
| Medium | 1,500 - 3,000 words | 6-10 | 3-5 |
| Long | 3,000 - 5,000 words | 10-15 | 5-8 |
| Epic | > 5,000 words | 15-20 | 8-12 |

**Hard Limits:**
- Never exceed 1 internal link per 150 words (prevents spam signals).
- Never have fewer than 3 internal links on any published post (prevents orphan risk).
- Never link to the same target URL more than twice in one post.
- Never add more than 3 links in a single paragraph.

### 1.2 Semantic Anchor Text Engineering

| Rule | Explanation | Example |
|------|-------------|---------|
| **Descriptive & Contextual** | Anchor must describe the destination AND fit the sentence naturally. | "...our guide to choosing the right [WordPress hosting]..." |
| **No Naked URLs** | Never use raw URLs as anchor text. | [FAIL] "...see https://example.com/hosting" |
| **No Generic Anchors** | Never use "click here", "read more", "this article". | [FAIL] "[Click here] to learn more." |
| **Include Semantic Variants** | Use synonyms and related phrases naturally. | "WordPress caching solutions", "speed optimization plugins" |
| **Optimal Length** | 3-8 words. Under 3 is vague; over 8 dilutes signal. | "[protein powder buying guide]" (4 words) |

### 1.3 Link Placement Intelligence (Scroll Depth Map)

| Placement Zone | Link Type | Rationale |
|----------------|-----------|-----------|
| **Intro (0-15%)** | Hub/Pillar Page | Establishes cluster relationship early; highest crawl priority. |
| **Core Content (15-70%)** | Sibling/Supporting | Contextual relevance; links when subtopics naturally connect. |
| **Mid-Content (40-70%)** | "Learn More" Paths | Deep-dives for engaged readers. |
| **Conclusion (70-90%)** | Next-Step Content | Guides reader to the next logical action. |
| **Related Reading (90-100%)** | Curated 3-5 Links | Final retention opportunity before exit. |

---

## PART II: PERFECT POST STRUCTURE ARCHITECTURE

### 13-Zone Scroll-Depth-Aware Structural Spine

1.  **SEO HEAD:** invisible to reader (Title tag, Meta description, Schema markup JSON-LD).
2.  **HERO ZONE (0-5%):** H1 intent-aligned, Byline, Author, Date, Read Time.
3.  **HOOK (5-10%):** 100-150 words. Mirror situation, establish credibility, promise value.
4.  **ANSWER-FIRST BLOCK (10-12%):** 40-70 words. Direct answer to primary query (AI extraction target).
5.  **QUICK VERDICT SUMMARY (12-15%):** Quick Picks table or numbered steps summary.
6.  **TABLE OF CONTENTS (15-17%):** Clickable links (for posts >2,000 words).
7.  **CONTEXT & METHODOLOGY (17-22%):** How we tested/researched.
8.  **CORE CONTENT (22-75%):** The meat. Evidence, examples, visual modules every 500-800 words.
9.  **SYNTHESIS & VERDICT (75-82%):** Clear recommendation, honest limitations.
10. **ACTION SECTION (82-88%):** Specific next steps, decision framework.
11. **FAQ (88-95%):** 6-10 entity-rich questions with unique answers.
12. **RELATED READING (95-97%):** 3-5 curated links with brief descriptions.
13. **TRUST FOOTER (97-100%):** Editorial methodology, affiliate disclosure, author credentials.

---

## PART III: SOTA HTML VISUAL COMPONENT LIBRARY

Transform flat WordPress posts into premium editorial experiences. All components are:
- **Mobile-first** (work perfectly on 375px screens).
- **Lightweight** (Pure CSS/HTML, no heavy frameworks).
- **Accessible** (proper ARIA roles).
- **Dark-mode aware.**

### Component 2: Answer-First Block (The AI Answer Target)
Visually distinct block for featured snippets.
```html
<div class="oc-answer-block" role="region" aria-label="Quick Answer">
  <div class="oc-answer-blockicon" aria-hidden="true"></div>
  <div class="oc-answer-blockcontent">
    <p class="oc-answer-blocklabel">Quick Answer</p>
    <p>[Direct, factual 40-70 word answer here.]</p>
  </div>
</div>
```

### Component 3: Quick Verdict / Top Picks Table
```html
<div class="oc-picks" role="region" aria-label="Top Picks Summary">
  <div class="oc-picksgrid">
    <div class="oc-pickscard oc-pickscard--winner">
      <span class="oc-picksbadge">Best Overall</span>
      <h3>[Product Name]</h3>
      <p class="oc-pickswhy">[Punchy reason why]</p>
      <a href="[URL]" class="oc-pickslink">Read full review</a>
    </div>
    <!-- Additional cards -->
  </div>
</div>
```

---

## PART IV: EXECUTION & QUALITY METRICS

### 7 Core Workflows

1. **Full-Article Draft Mode:** Generate SOTA post (2500–4000 words) with Hormozi/Ferriss style.
2. **Multi-Pass Editorial Gate:** Elevate article to 95+ score through Fact-Check, Structure, and Tone passes.
3. **Semantic Refresh Mode:** Update old (>12 month) articles with new entities and entities.
4. **Evidence Audit + Refresh:** Verify all claims for high-traffic posts.
5. **Graph Update Mode:** Recommend links to prevent orphan content clusters.
6. **Image Embed + Alt-Text Mode:** Integrated visual asset cues.
7. **Conversion Handoff Mode:** Flag affiliate opportunities for conversion optimization.

### Visual Rhythm Rule
Every 400-600 words of body text **must** be broken by a visual component (image, table, list, or callout). **At no point** on a 375px viewport should the reader see more than 3 consecutive paragraphs without a visual break.

---

## Integration with Other Skills

- **seo-intelligence:** Provides keyword data and SERP competitor analysis.
- **wordpress-visual-assets:** Provides image URLs and alt-text.
- **conversion-optimizer:** Handles affiliate link insertion and product box design.
- **automation-ops:** Schedules distribution and publishing.
- **content-architect:** Defines pillar/cluster strategy.

## Automation Scripts (References)
- `qualitygate.py`: Multi-dimensional quality scoring.
- `internallinkmapper.py`: Builds link map from site inventory.
- `anchortextgenerator.py`: Generates 3 semantic candidates per link.
- `mobilevisualdensitychecker.py`: Verifies no 3 consecutive text blocks without visual break.
