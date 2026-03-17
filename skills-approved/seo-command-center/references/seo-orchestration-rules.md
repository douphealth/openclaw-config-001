# SEO Orchestration Rules

Routing decision tree and workflow templates for cross-cutting SEO work.

## Decision Tree

```
Is the request about a single page or element?
├─ YES → Route directly to the specialized skill
│   ├─ Content quality → editorial-post-enhancement
│   ├─ Structured data → schema-ops
│   └─ Copy/positioning → conversion-copywriting
└─ NO → Continue ↓

Is the request a diagnosis or execution?
├─ DIAGNOSIS → seo-audit-playbook first
│   ├─ Technical issues found → infrastructure-ops (fix) → auto-verification
│   ├─ Content issues found → content-strategy-planning → editorial-post-enhancement
│   ├─ Cannibalization found → content-strategy-planning (consolidation)
│   ├─ Schema issues found → schema-ops
│   └─ No clear cause → check GSC data, backlinks, algorithm updates
└─ EXECUTION → Continue ↓

What's the primary goal?
├─ More organic traffic → content-strategy-planning → editorial-post-enhancement
├─ Fix rankings drop → seo-audit-playbook → (route by finding)
├─ Launch new site → content-strategy-planning → schema-ops → monitoring-ops
├─ Scale pages → programmatic-seo-blueprints → schema-ops → monitoring-ops
└─ Improve conversions from SEO traffic → revenue-site-execution
```

## Anti-Pattern Patterns (Do NOT)

- **Kitchen sink SEO:** Running every SEO skill on every request. Route to the minimum needed.
- **Content before diagnosis:** Writing new content when the problem is cannibalization or technical.
- **Schema without content:** Adding structured data to thin or duplicate pages.
- **Monitoring without action:** Setting up rank tracking but not defining what rank changes trigger action.
- **Audit without prioritization:** Listing 47 issues without ranking them by impact.

## Handoff Template

When routing between SEO skills, pass this context:

```
## SEO Handoff
**From:** [previous skill]
**To:** [next skill]
**Goal:** [specific objective]
**Key findings so far:** [bullet list]
**Assets in scope:** [site/page list]
**Constraints:** [timeline, resources, technical limits]
**Evidence:** [links to audit results, GSC data, crawl reports]
```

## Workflow Templates

### Template 1: New Site SEO Foundation
1. `content-strategy-planning` — keyword research, page structure, content priorities
2. `editorial-post-enhancement` — produce priority content (top 5-10 pages)
3. `schema-ops` — Organization, WebSite, BreadcrumbList markup
4. `monitoring-ops` — rank tracking on target keywords from launch

### Template 2: Ranking Recovery
1. `seo-audit-playbook` — diagnose cause with evidence
2. Route by finding:
   - Technical → fix + verify
   - Content/cannibalization → consolidate or improve
   - Links → investigate backlink profile
3. `monitoring-ops` — track recovery metrics

### Template 3: Content Scale-Up
1. `content-strategy-planning` — identify content gaps and opportunities
2. `programmatic-seo-blueprints` — if scale warrants template pages
3. `editorial-post-enhancement` — for high-priority manual content
4. `schema-ops` — structured data for new page types
5. `monitoring-ops` — track new keyword rankings

### Template 4: Technical SEO Fix
1. `seo-audit-playbook` — identify technical issues with crawl data
2. `infrastructure-ops` — implement fixes (redirects, speed, server config)
3. `auto-verification` — confirm fixes are live and working
4. `monitoring-ops` — watch for recovery signals
