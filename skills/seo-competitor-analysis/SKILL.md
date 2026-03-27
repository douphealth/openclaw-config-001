---
name: seo-competitor-analysis
description: Enterprise SEO competitor intelligence and analysis. Deep competitor research including keyword gaps, content strategy mapping, backlink analysis, SERP positioning, and competitive threat assessment. Use when analyzing competitors, finding content gaps, benchmarking SEO performance, identifying keyword opportunities, or building competitive strategies.
---

# SEO Competitor Analysis — Enterprise Competitive Intelligence

## Purpose
Identify, analyze, and benchmark SEO competitors to find content gaps, keyword opportunities, and strategic advantages.


## Shared Doctrine References
- `skills/shared/seo-aeo-geo-superpowers.md`
- `skills/shared/seo-aeo-geo-checklist.md`
- `skills/shared/seo-aeo-geo-research-workflow.md`

## Enterprise Protocols (MANDATORY)

Before executing, read `skills/shared/enterprise-protocol.md` and follow:
- Pre-flight health check (site accessible, creds valid, state captured)
- Mandatory backup before any modification
- Retry with exponential backoff (max 3 attempts per API call)
- Progress reporting every 10 operations
- Verification after each modification
- Health checks every 50 items in long operations
- Rollback plan identified before starting
## Superpower Layer

For serious work, also follow:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks when safe
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use
- "Who are my SEO competitors and what are they ranking for?"
- Content gap analysis vs specific competitors
- Keyword opportunity discovery
- Competitor content strategy mapping
- SERP positioning analysis
- Competitive threat assessment
- Backlink profile comparison
- "Why is competitor X outranking us?"


## Do NOT Use For
- General SEO auditing of your own site (use `seo-audit-playbook`)
- Content writing or article upgrades (use `editorial-post-enhancement`)
- Schema implementation (use `schema-ops`)
- Broad SEO orchestration across many specialist domains (use `seo-command-center`)

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

### Phase 2B: Overlap-Based Competitor Filtering (MANDATORY for page-level targeting)
When analyzing a specific keyword/page opportunity:
- keep only competitor pages that clearly target the keyword in both title and URL
- remove pages ranking incidentally without strong exact-topic focus
- build the content-gap set from the remaining true competitors only
- keep only subtopics/secondary keywords where multiple top competitors overlap
- treat that overlap set as the required competitive blueprint, not optional extras

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

### Phase 4B: Backlink Overlap Prioritization
For the filtered competitor pages targeting the same keyword:
- identify referring domains linking to multiple competitor pages
- prioritize domains that linked to 2+ relevant competitor pages
- these are the strongest outreach targets because they already link to this content format/topic
- output backlink opportunities ranked by overlap count first, then by site relevance

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

## Anti-Patterns
- ❌ Analyzing 20+ competitors superficially instead of 3-5 deeply — depth beats breadth for actionable insights
- ❌ Copying competitor content strategy without understanding *why* it works for their audience — context matters
- ❌ Ignoring SERP competitors that aren't business competitors — they're still stealing your clicks
- ❌ Using stale keyword data (>90 days old) for gap analysis — SERPs shift fast, refresh before making decisions
- ❌ Reporting keyword gaps without estimating traffic potential — not all gaps are worth filling
- ❌ Skipping the competitive threat assessment — knowing who's getting stronger matters as much as who's ranking now
- ❌ Confusing correlation with causation in competitor analysis — "they rank #1" ≠ "because they do X"

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
- Apply `skills/api-efficiency-protocol.md` for search, content, and benchmark API pulls
- Batch page analysis (10-20 per call)
- Pre-crawl data before live crawl
- Template-based reports
- Parallel checks where possible
- Analyze 3-5 serious competitors deeply instead of 20 shallowly

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

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


