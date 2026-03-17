---
name: seo-command-center
description: Unified SEO operations hub for orchestrating audits, keyword research, content optimization, technical SEO, competitor analysis, and schema deployment across specialized skills. Use when a user asks for comprehensive SEO work that spans multiple areas, site-wide audits, or cross-cutting SEO operations. For deep dives into single areas, route to the specialized skills below.
---

# SEO Command Center — Routing Hub

Orchestrates cross-cutting SEO work by routing to specialized skills.

## WHEN TO USE

Master SEO skill for work that spans multiple areas:
- Comprehensive SEO audits → orchestrates **seo-audit-playbook**
- Keyword research & content planning → orchestrates **content-strategy-planning**
- Content optimization → orchestrates **editorial-post-enhancement**
- Programmatic SEO design → orchestrates **programmatic-seo-blueprints**
- Schema deployment → orchestrates **schema-ops**
- Cross-cutting SEO work that spans multiple skills
- SEO health monitoring and reporting
- Competitor intelligence
- Rank tracking and visibility analysis

**For deep dives into single areas**, use the specialized skill directly instead.

## DO NOT USE FOR
- Single-page SEO tasks (→ seo-audit-playbook for audits, schema-ops for markup)
- Content writing (→ editorial-post-enhancement or conversion-copywriting)

## ROUTING TABLE

| User Request | Route To |
|---|---|
| Full site audit, cannibalization, technical crawl | seo-audit-playbook |
| Keyword research, clustering, content gaps, editorial calendar | content-strategy-planning |
| Article optimization, on-page scoring, headline improvements | editorial-post-enhancement |
| Scaled page generation, template pages, directory pages | programmatic-seo-blueprints |
| JSON-LD markup, rich snippets, schema validation | schema-ops |
| Competitor gap analysis, SERP analysis, keyword gaps | seo-competitor-analysis |
| AI visibility, GEO optimization, Perplexity/ChatGPT presence | ai-visibility |
| Internal linking, orphan pages, link depth | seo-audit-playbook |
| Rank tracking, movement alerts | monitoring-ops |

## ORCHESTRATION RULES

- **ALWAYS check for cannibalization** before content recommendations
- **ALWAYS provide evidence** for findings
- **ALWAYS include actionable fix recommendations**
- **NEVER report "SEO complete"** without crawling the site
- **NEVER mix opinion with diagnosis**

## OUTPUT TEMPLATE

```
## SEO Report: {domain}
Date: {date}

### Health Score: X/100 (Grade: B)
- Technical: X/100
- On-Page: X/100
- Content: X/100
- Authority: X/100
- User Signals: X/100

### Top Issues
1. [Issue] — Impact: [High/Med/Low] — Fix: [command/action]

### Keyword Opportunities
- X new keywords identified
- X cannibalization risks
- Priority content queue: [list]

### Action Plan
Immediate: [critical fixes]
This week: [high priority]
This month: [medium priority]
```


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

## Output Contract
**Artifact**: SEO orchestration plan with task assignments
**Evidence**: Specialist routing, priority matrix
**Decision**: Tasks assigned to specialists
**Next**: Track completion

## Do NOT Use This For
- Tasks better handled by a more specific skill — check skill-router
- One-off quick questions that don't need a skill
- Tasks in a different domain — route to the correct skill first

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
