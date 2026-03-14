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
| Competitor gap analysis, SERP analysis | seo-audit-playbook + content-strategy-planning |
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


## Output Contract
**Artifact**: SEO orchestration plan with task assignments
**Evidence**: Specialist routing, priority matrix
**Decision**: Tasks assigned to specialists
**Next**: Track completion

## Do NOT Use This For
- Tasks better handled by a more specific skill — check skill-router
- One-off quick questions that don't need a skill
- Tasks in a different domain — route to the correct skill first
