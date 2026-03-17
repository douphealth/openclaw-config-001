---
name: analytics-reporting
description: Enterprise analytics and business intelligence reporting. Use when analyzing business, marketing, product, or operational data to produce KPI summaries, dashboards, performance reports, cohort insights, or executive-ready recommendations. Triggers on analytics reporting, KPI tracking, dashboard planning, performance summaries, attribution interpretation, trend analysis, or turning raw metrics into decisions.
---

# Analytics Reporting — Enterprise Business Intelligence

## Purpose
Turn messy metrics into decision-ready reporting with clear caveats, clear business meaning, and no fake certainty.

## When to Use
- Analyzing business, marketing, product, or operational data
- Producing KPI summaries, performance reports, or cohort insights
- Planning dashboard structure or reporting cadence
- Interpreting attribution, trends, or funnel data

**Do NOT use for:** Experiment design (→ `experiment-tracking`), broken instrumentation (→ `tracking-measurement`), launch readiness (→ `launch-readiness-audit`).

## Reporting Framework

### Phase 1: Frame the Question
1. Define the business question before touching numbers
2. Identify source, date range, granularity, and quality risks
3. State upfront: what decision does this analysis serve?

### Phase 2: KPI Framework
4. Select 3-5 primary KPIs that connect directly to the business question
5. For each KPI: metric formula, target/benchmark, direction (↑ or ↓ good)
6. Separate leading indicators (predictive) from lagging indicators (outcome)
7. Add 2-3 supporting metrics for context without clutter

**Selection rules:**
- Every KPI maps to a decision — if no one acts on it, drop it
- Mix efficiency metrics (cost per lead, conversion rate) with growth metrics (revenue, pipeline)
- Avoid vanity metrics unless you can explain why they matter in one sentence
- Use ratios and rates over raw totals when comparing segments

### Phase 3: Analyze
8. Validate data quality before writing conclusions
9. Separate descriptive facts from interpretation
10. Highlight trend, driver, and business impact
11. Separate channel performance, branded vs non-branded where relevant
12. State confidence level and major unknowns

**Analysis discipline:**
- Compare against meaningful baseline (prior period, target, cohort average)
- Flag seasonality, one-time events, or data pipeline changes
- Use absolute numbers for magnitude, percentages for direction
- Call out top 1-3 drivers behind each significant change

### Phase 4: Dashboard Design

**Structure:**
```
┌─────────────────────────────────────────────────────────┐
│  HEADLINE: KPI | Value | vs-Period | Sparkline          │
├─────────────────────────────────────────────────────────┤
│  DRIVERS: Breakdown by channel/segment/cohort           │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │  Segment A   │ │  Segment B   │ │  Segment C   │     │
│  │  ▲ 12%       │ │  ▼ 3%        │ │  → 0%        │     │
│  └──────────────┘ └──────────────┘ └──────────────┘     │
├─────────────────────────────────────────────────────────┤
│  DETAIL: Sortable table with raw data for drill-down    │
├─────────────────────────────────────────────────────────┤
│  CTA: One primary action the viewer should take         │
└─────────────────────────────────────────────────────────┘
```

### Phase 5: Report & Recommend
13. End with recommended actions, not just observations
14. Quantify impact of each recommendation where possible

## Output Contract
**Artifact**: Report or dashboard with business question, data scope, KPI summary, findings, interpretation, and recommended actions
**Evidence**: KPI formulas documented, comparison periods consistent, data quality flags
**Decision**: Actions prioritized with expected impact
**Next**: Schedule follow-up analysis

## Performance Optimizations

### Speed Multipliers
- Parallel data fetching from multiple sources
- Pre-compute common metrics for the session
- Template-based reports and dashboards
- Batch API calls for platform operations
- Automated threshold alerts for significant changes

### Self-Critique Scorecard (/25)
1. **Functionality** (1-5): Does it work perfectly?
2. **Quality** (1-5): Enterprise-grade analysis?
3. **Verification** (1-5): Data validated from multiple sources?
4. **Speed** (1-5): Optimal execution?
5. **Learning** (1-5): Patterns documented?

**Target: 22+/25**

### Auto-Check
- [ ] Data quality validated before conclusions
- [ ] Comparison periods consistent
- [ ] Confidence levels stated
- [ ] Actionable recommendations provided
- [ ] Score logged to memory

## Anti-Patterns
- ❌ Directional noise presented as meaningful trend
- ❌ Metrics without connection to decisions
- ❌ Weak attribution presented as certainty
- ❌ Totals without context, comparison period, or trend
- ❌ Executive summaries that say nothing actionable
- ❌ 10 metrics when 4 would make the point
- ❌ Correlation confused with causation

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
