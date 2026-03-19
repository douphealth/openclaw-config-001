---
name: seo-command-center
description: Unified SEO operations hub for orchestrating audits, keyword research, content optimization, technical SEO, competitor analysis, and schema deployment across specialized skills. Use when a user asks for comprehensive SEO work that spans multiple areas, site-wide audits, or cross-cutting SEO operations. For deep dives into single areas, route to the specialized skills below.
---

# SEO Command Center — Routing Hub

## Purpose
Orchestrate cross-cutting SEO work by routing requests to the right specialist skills in the right order.

Orchestrates cross-cutting SEO work by routing to specialized skills.


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

For complex or high-risk work, also follow:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use

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


## Do NOT Use For
- Single-page SEO tasks (use `seo-audit-playbook` for audits, `schema-ops` for markup)
- Content writing (use `editorial-post-enhancement` or `conversion-copywriting`)
- Tasks that clearly belong to one specialist skill with no orchestration need

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
- Apply `skills/api-efficiency-protocol.md` before routing any multi-skill SEO operation
- Batch page analysis (10-20 per call)
- Pre-crawl data before live crawl
- Template-based reports
- Parallel checks where possible
- Route to one specialist per primary deliverable to reduce overlap and wasted calls

## Anti-Patterns
- ❌ Routing a single-page task to the command center instead of the specialist skill directly — adds unnecessary orchestration overhead
- ❌ Running SEO operations sequentially when they could run in parallel — always check for independent workstreams
- ❌ Skipping the routing table and guessing which skill to use — the table exists for a reason
- ❌ Reporting "SEO complete" without crawling the site — surface-level claims without evidence
- ❌ Mixing opinion with diagnosis in the health score — separate factual findings from strategic recommendations
- ❌ Orphaning tasks with no follow-up plan — every action item needs an owner and a deadline
- ❌ Ignoring cannibalization checks before content recommendations — the #1 way to create new problems

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

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


