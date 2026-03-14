---
name: analytics-reporting
description: Use when analyzing business, marketing, product, or operational data to produce KPI summaries, dashboards, performance reports, cohort insights, or executive-ready recommendations. Triggers on requests for analytics reporting, KPI tracking, dashboard planning, performance summaries, attribution interpretation, trend analysis, or turning raw metrics into decisions.
---

# Analytics Reporting

## Purpose
Turn messy metrics into decision-ready reporting with clear caveats, clear business meaning, and no fake certainty.

## Use this when
- Analyzing business, marketing, product, or operational data
- Producing KPI summaries, performance reports, or cohort insights
- Planning dashboard structure or reporting cadence
- Interpreting attribution, trends, or funnel data

Do **not** use for: experiment design (use `experiment-tracking`), broken instrumentation (use `tracking-measurement`), or launch readiness (use `launch-readiness-audit`).

## Do this

### Phase 1: Frame the question
1. Define the business question before touching the numbers.
2. Identify the source, date range, granularity, and obvious quality risks.
3. State upfront: what decision does this analysis serve?

### Phase 2: KPI framework
4. Select 3–5 primary KPIs that connect directly to the business question.
5. For each KPI, define: metric formula, target/benchmark, direction (↑ good or ↓ good).
6. Separate leading indicators (predictive) from lagging indicators (outcome).
7. Add 2–3 supporting metrics that provide context without clutter.

**KPI selection rules:**
- Every KPI must map to a decision — if no one acts on it, drop it.
- Mix efficiency metrics (cost per lead, conversion rate) with growth metrics (revenue, pipeline).
- Avoid vanity metrics unless you can explain why they matter in one sentence.
- Use ratios and rates over raw totals when comparing across segments.

### Phase 3: Analyze
8. Validate data quality before writing conclusions.
9. Separate descriptive facts from interpretation.
10. Highlight trend, driver, and likely business impact.
11. Separate channel performance, branded vs non-branded where relevant.
12. State confidence level and major unknowns.

**Analysis discipline:**
- Compare against a meaningful baseline (prior period, target, cohort average).
- Flag seasonality, one-time events, or data pipeline changes that could distort trends.
- Use absolute numbers for magnitude and percentages for direction.
- Call out the top 1–3 drivers behind each significant change.

### Phase 4: Dashboard design (if applicable)
13. Top row: headline KPIs with sparklines and vs-period deltas.
14. Middle: driver breakdowns (by channel, segment, cohort).
15. Bottom: raw data or detailed table for drill-down.
16. One primary CTA per dashboard view — what should the viewer do next?

**Dashboard structure:**
```
┌─────────────────────────────────────────────────────────┐
│  HEADLINE ROW: KPI | Value | vs-Period | Sparkline      │
├─────────────────────────────────────────────────────────┤
│  DRIVER ROW: Breakdown by channel/segment/cohort        │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │  Segment A   │ │  Segment B   │ │  Segment C   │     │
│  │  ▲ 12%       │ │  ▼ 3%        │ │  → 0%        │     │
│  └──────────────┘ └──────────────┘ └──────────────┘     │
├─────────────────────────────────────────────────────────┤
│  DETAIL: Sortable table with raw data for drill-down    │
├─────────────────────────────────────────────────────────┤
│  CTA: "Review Segment B decline" or "Export report"     │
└─────────────────────────────────────────────────────────┘
```

### Phase 5: Report
17. End with recommended actions, not just observations.
18. Quantify impact of each recommendation where possible.

## Core rules
- Do not present directional noise as a meaningful trend.
- Every key metric should connect to a decision, not just a chart.
- If attribution is weak or incomplete, say so plainly.
- Do not report totals without context, comparison period, or trend.
- Do not produce executive summaries that say nothing actionable.

## Output contract
Deliver reports in this structure:
1. **Business question** — one sentence
2. **Data scope** — sources, date range, granularity, caveats
3. **KPI summary table** — metric, current value, target, trend, verdict
4. **Key findings** — 3–5 bullet insights with business impact
5. **Interpretation** — what the data means, confidence level
6. **Recommended actions** — prioritized, with expected impact
7. **Unknowns** — what's missing, what needs better data

## Verification steps
- [ ] KPI formulas are documented and match source definitions
- [ ] Comparison periods are consistent across metrics
- [ ] Data quality issues are flagged before conclusions
- [ ] Each recommendation has a quantified or reasoned justification
- [ ] Confidence level is stated for major claims
- [ ] Someone unfamiliar with the data can follow the report

## Resources
Read when needed:
- `references/reporting-quality-bars.md`
- `references/portfolio-kpi-priorities.md`

## Checks and common mistakes
- Do not bury caveats after bold conclusions — lead with them.
- Do not confuse correlation with causation.
- Do not report vanity metrics when the business question needs efficiency metrics.
- Do not use 10 metrics when 4 would make the point.
- Do not skip the "so what?" — every finding needs a business implication.
- Do not present month-over-month without considering seasonality.

## Output Contract
**Artifact**: Skill-specific deliverable (report, fix, config, or document)
**Evidence**: Proof that the work was completed correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action or monitoring period
