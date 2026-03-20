---
name: seo-competitor-analysis
description: Enterprise SEO competitor intelligence and analysis. Deep competitor research including keyword gaps, content strategy mapping, backlink analysis, SERP positioning, and competitive threat assessment. Use when analyzing competitors, finding content gaps, benchmarking SEO performance, identifying keyword opportunities, or building competitive strategies.
---

# SEO Competitor Analysis — Enterprise Competitive Intelligence

## Purpose
Identify, analyze, and benchmark SEO competitors to find content gaps, keyword opportunities, and strategic advantages.

## When to Use
- "Who are my SEO competitors and what are they ranking for?"
- Content gap analysis vs specific competitors
- Keyword opportunity discovery
- Competitor content strategy mapping
- SERP positioning analysis
- Competitive threat assessment
- Backlink profile comparison
- "Why is competitor X outranking us?"

**Do NOT use for:** General SEO auditing (→ `seo-audit-playbook`), content writing (→ `editorial-post-enhancement`), schema markup (→ `schema-ops`).

## Analysis Framework

### Phase 1: Competitor Identification
1. **Direct competitors**: Same products/services, same audience
2. **SERP competitors**: Ranking for your target keywords (may not be business competitors)
3. **Content competitors**: Publishing similar content, attracting same audience

**Discovery method:**
- Search target keywords → note top 10 domains per query
- Check "Related searches" and "People also ask"
- Analyze SERP features (who owns featured snippets, AI overviews?)
- Use `web_search` for keyword-based discovery

### Phase 2: Keyword Gap Analysis
For each competitor:
1. **Keywords they rank for that you don't** (opportunity gap)
2. **Keywords you both rank for** (battleground keywords)
3. **Keywords you rank for that they don't** (your advantage)
4. **Keywords where they outrank you** (improvement targets)

**Prioritization matrix:**
| Search Volume | Your Position | Competitor Position | Priority |
|---------------|---------------|--------------------|---------| 
| High | Not ranking | Top 10 | 🔴 Critical |
| High | 11-20 | Top 5 | 🟡 High |
| Medium | Not ranking | Top 10 | 🟡 High |
| Low | Not ranking | Top 10 | 🟢 Monitor |

### Phase 3: Content Strategy Mapping
Analyze competitor's top content:
- **Content types**: Blog posts, tools, calculators, comparisons, guides
- **Content depth**: Word count, media usage, interactivity
- **Content freshness**: Publication dates, update frequency
- **Internal linking patterns**: How they connect related content
- **SERP features targeted**: FAQ, HowTo, Product, Review schemas

### Phase 4: Technical & Authority Comparison
- **Domain authority**: Relative strength (no direct API, estimate via SERP presence)
- **Content velocity**: How often they publish new content
- **Schema implementation**: What structured data they use
- **Page speed**: Core Web Vitals comparison
- **Internal linking**: Site architecture patterns

### Phase 5: Competitive Threat Assessment
Rate each competitor:
| Factor | Score (1-5) |
|--------|-------------|
| Content quality | |
| Content velocity | |
| Domain authority | |
| Technical SEO | |
| Schema implementation | |
| SERP feature presence | |
| **Overall threat level** | |

## Output: Competitor Analysis Report

```markdown
# SEO Competitor Analysis: [Your Domain]

## Executive Summary
- **Top 3 competitors**: [list]
- **Biggest opportunity**: [key finding]
- **Immediate actions**: [top 3]

## Competitor Profiles
[For each competitor: strengths, weaknesses, key metrics]

## Keyword Gap Analysis
- **Critical gaps** (you're missing): [list]
- **Battleground keywords** (competing): [list]
- **Your advantages**: [list]

## Content Strategy Insights
- **Gaps in their content**: [what they're not covering]
- **Their best-performing content**: [top pages]
- **Content types to replicate**: [formats that work]

## Action Plan
1. **Quick wins** (< 1 week): [specific actions]
2. **Short-term** (1-4 weeks): [specific actions]
3. **Long-term** (1-3 months): [strategic moves]
```

## Tools to Use
- `web_search`: Discover competitors, find ranking keywords
- `web_fetch`: Extract and analyze competitor page content
- `browser`: Complex pages requiring JavaScript

## Workflow
1. Identify 3-5 primary competitors via SERP analysis
2. Analyze each competitor's content strategy
3. Map keyword gaps and opportunities
4. Assess competitive threat levels
5. Generate prioritized action plan
6. Update `ops/sites/{domain}/` with competitor intelligence

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

## SOTA Competitor Upgrade Layer
- Use `../../skills/shared/references/serp-ai-research-protocol.md` to compare not only rankings, but also extractability, FAQ coverage, freshness, entity richness, and citation-worthiness.
- Add AI-answer prompt variants to competitor analysis, not just keyword overlap.
- Capture whether competitors win because of authority, structure, source quality, freshness, or answer-format alignment.
- Flag where competitors are structurally weak for GEO/AEO even if they rank today.

## Output Contract
**Artifact**: Competitor analysis report with gap analysis and action plan
**Evidence**: SERP screenshots, keyword data, content samples
**Decision**: Prioritized competitive strategy
**Next**: Implement quick wins, schedule quarterly re-analysis

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
