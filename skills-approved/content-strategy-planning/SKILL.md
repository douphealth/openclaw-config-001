---
name: content-strategy-planning
description: Enterprise content strategy, topic cluster design, and editorial planning. Use when planning content strategy, building topic clusters, prioritizing editorial topics, designing content calendars, or mapping content gaps to business goals. Triggers on content strategy, topic clustering, editorial calendar planning, pillar content design, or customer question mining.
---

# Content Strategy Planning — Enterprise Editorial Strategy

## Purpose
Design content systems that drive traffic, leads, and authority through structured topic clusters, not random publishing.

## When to Use
- Planning content strategy from scratch or for a new site
- Building topic clusters and pillar content architecture
- Prioritizing editorial topics by business impact
- Designing content calendars and publishing cadences
- Mining customer questions for content opportunities

**Do NOT use for:** Writing articles (→ `editorial-post-enhancement`), SEO auditing (→ `seo-audit-playbook`), conversion copy (→ `conversion-copywriting`).

## Strategy Framework

### Phase 1: Business Goals
1. Primary content goal: traffic, leads, authority, or education?
2. Target audience segments and their awareness levels (TOFU/MOFU/BOFU)
3. Map buyer journey: awareness → consideration → decision
4. Set measurable targets: traffic, leads, rankings, engagement KPIs

### Phase 2: Topic Research
5. **Customer question mining**:
   - Support tickets and sales call transcripts
   - Reddit, Quora, forums in the niche
   - "People also ask" boxes on Google
   - Competitor comment sections
   
6. **Keyword cluster analysis**:
   - Head terms (high volume, high competition)
   - Long-tail variants (lower volume, easier to rank)
   - Question queries (how, what, why, when)
   - Comparison queries (vs, alternatives, best)

7. **Competitor content gap analysis**:
   - What are competitors ranking for that you're not?
   - What are they covering poorly?
   - Where is the content thin or outdated?

### Phase 3: Topic Cluster Design

**Architecture:**
```
[Pillar: Comprehensive Guide 3000+ words]
├── [Cluster: Specific Subtopic 1500+ words]
├── [Cluster: Specific Subtopic 1500+ words]
├── [Cluster: Comparison/How-To 1500+ words]
├── [Cluster: Tool/Resource List 1500+ words]
└── [Cluster: FAQ/Common Mistakes 1500+ words]
```

**Rules:**
- Each pillar has 5-10 cluster articles
- Every cluster links to pillar (rich anchor text)
- Pillar links to every cluster in relevant context
- Cluster articles target specific long-tail keywords
- Pillar covers the topic comprehensively

### Phase 4: Prioritization Matrix

| Keyword Volume | Competition | Business Value | Priority |
|----------------|-------------|----------------|---------|
| High (>1K/mo) | Low | High | 🔴 **P0** — Write first |
| High | Medium | High | 🟡 **P1** — Write second |
| Medium (100-1K) | Low | High | 🟡 **P1** — Write second |
| Medium | Low | Medium | 🟢 **P2** — Write later |
| Low (<100) | Low | High | 🟢 **P2** — Write for conversion |

### Phase 5: Editorial Calendar

Format: Week → Content Type → Topic → Target Keyword → Funnel Stage → Owner → Status

**Publishing cadence:**
- Week 1: Pillar article (comprehensive)
- Week 2-3: Cluster articles (2 per week)
- Week 4: Refresh/update existing content
- Repeat with next cluster

### Phase 6: Measure & Iterate
- Track: page views, time on page, keyword rankings, leads per article
- Double down on winning topics (more cluster content)
- Prune or consolidate underperforming content quarterly
- Refresh top content every 90 days

## Content Quality Standards
- Every article has target keyword + 3-5 secondary keywords
- 5-8 internal links per article minimum
- CTA or next step (newsletter, offer, related reading)
- Author attribution + publication date + update date
- FAQ section with schema markup for AI visibility

### Voice & Style: Hormozi/Ferriss Standard
All content should be written in the Hormozi/Ferriss style:

**Hormozi Principles:**
- Answer first — Lead with the conclusion, not the buildup
- Short paragraphs — 2-3 sentences max, then whitespace
- Direct language — "Here's the thing:" "The real problem is..."
- Practical examples — Real scenarios, not abstract theory
- Numbered steps — "Step 1: Do this. Step 2: Do that."
- Bold claims backed by proof — "This increased conversions 340%. Here's how:"
- Conversational tone — "Look," "Here's what most people miss," "The bottom line:"

**Ferriss Principles:**
- Personal experiments — "I tried X for 30 days. Here's what happened:"
- Data + stories — Combine numbers with real narratives
- Contrarian takes — "Most people think X. The data says Y."
- Frameworks — Give readers a system they can apply TODAY
- Case studies — "Here's how [Person] did [Thing] in [Timeframe]"
- Time-bounded experiments — "Try this for 7 days"

**Practical > Theoretical:**
- Every claim needs a real example
- Every concept needs a concrete application
- Every section ends with "Here's how to do this:"
- NO abstract generalizations without practical follow-up

## SOTA Strategy Upgrade Layer
- Use `../../skills/shared/references/seo-aeo-geo-superpowers.md` so strategy includes both search demand and AI prompt demand.
- For each major topic cluster, specify whether it serves SEO, AEO, GEO, conversion support, authority building, or multiple goals.
- Prioritize clusters not only by traffic potential, but also by citation-worthiness, prompt importance, and business proximity.
- Recommend content formats that match likely winning answer structures: definition, how-to, comparison, FAQ, glossary, review, tool, or entity-led explainer.

## Output Contract
**Artifact**: Content strategy document with topic clusters, calendar, and measurement plan
**Evidence**: Keyword research data, competitor gap analysis, topic cluster map
**Decision**: Editorial calendar approved for publishing
**Next**: Begin writing pillar content, then highest-priority cluster articles

## Performance Optimizations

### Speed Multipliers
- Batch page analysis (10-20 per call)
- Pre-crawl data before live crawl
- Template-based reports
- Parallel checks where possible

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does it work perfectly?
2. **Quality** (1-5): Enterprise-grade?
3. **Verification** (1-5): Verified via API + live + visual?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Pre-flight checks completed
- [ ] Verified via multiple methods
- [ ] Anti-patterns avoided
- [ ] Score logged to memory

## Anti-Patterns
- ❌ Publishing without keyword targeting or search intent analysis
- ❌ Random topic selection with no cluster structure
- ❌ No internal linking strategy (orphan articles)
- ❌ No measurement plan (publish and forget)
- ❌ Writing for algorithms, not humans
- ❌ Ignoring content freshness (never updating old posts)

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
