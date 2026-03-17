---
name: experiment-tracking
description: Enterprise experiment design, tracking, and analysis. Use when designing A/B tests, CRO experiments, messaging tests, pricing tests, onboarding tests, or channel experiments. Triggers on hypothesis frameworks, sample size calculators, statistical significance checks, experiment logging, or go/no-go decisions from experiment results.
---

# Experiment Tracking — Enterprise A/B Testing

## Purpose
Design and evaluate experiments with statistical rigor, clear decision criteria, and no premature conclusions.

## When to Use
- Designing A/B, CRO, or messaging experiments
- Calculating sample sizes or test duration
- Checking if results are statistically significant
- Logging experiment results and learnings
- Making go/no-go decisions from test data

**Do NOT use for:** Paid media optimization (→ `paid-media-audit`), analytics reporting (→ `analytics-reporting`), tracking setup (→ `tracking-measurement`).

## Experiment Framework

### Phase 1: Hypothesis
Format: "We believe [change] will [effect] for [audience] because [reason]. We'll measure this by [metric]."

| Component | Example |
|-----------|---------|
| Change | Adding social proof above the CTA |
| Effect | Increase sign-up rate by 10% |
| Audience | First-time visitors from organic traffic |
| Reason | Social proof reduces perceived risk |
| Metric | Sign-up conversion rate |

### Phase 2: Design
1. **Single variable** — test one thing at a time
2. **Control** — keep a version with no changes
3. **Variant** — apply only the change being tested
4. **Duration** — minimum 2 full business cycles (usually 2-4 weeks)
5. **Traffic split** — typically 50/50, can use 80/20 for risk-averse tests

### Phase 3: Sample Size Calculator

Quick heuristic:
| Baseline Conversion | Min Sample (per variant) | Min Detectable Lift |
|--------------------|-------------------------|---------------------|
| 1-5% | 5,000+ | 10-20% relative |
| 5-10% | 2,500+ | 10-15% relative |
| 10%+ | 1,000+ | 5-10% relative |

**Formal calculation**: Use a proper calculator (Google "sample size calculator A/B test") for confidence level 95%, power 80%.

### Phase 4: Evaluate
1. Check statistical significance (p-value < 0.05)
2. Check practical significance (is the lift meaningful?)
3. Examine segment breakdowns — did it work differently for different groups?
4. Look for secondary effects (did one metric improve but another decline?)
5. Document any external factors (holidays, campaigns, outages)

### Phase 5: Decision Matrix

| Significance | Practical Impact | Decision |
|-------------|------------------|----------|
| p < 0.05 | Lift > target | ✅ **Ship** |
| p < 0.05 | Lift < target | ⚠️ **Monitor** — meaningful but small |
| p > 0.05 | Clear winner trend | 🔄 **Extend** — need more data |
| p > 0.05 | No trend | ❌ **Kill** — no difference |

### Phase 6: Log & Learn
Log every experiment: hypothesis, variant, results, significance, decision, and learning. Build institutional knowledge from experiment history.

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

## Output Contract
**Artifact**: Experiment report with hypothesis, results, significance, decision, and next steps
**Evidence**: Statistical significance calculated, sample size adequate, segments analyzed
**Decision**: Ship, monitor, extend, or kill
**Next**: Log to experiment database, design follow-up if needed

## Anti-Patterns
- ❌ Stopping early when results "look good"
- ❌ Testing multiple variables simultaneously
- ❌ Ignoring segment differences
- ❌ Treating statistical significance as practical significance
- ❌ Not logging experiments (losing institutional knowledge)

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
