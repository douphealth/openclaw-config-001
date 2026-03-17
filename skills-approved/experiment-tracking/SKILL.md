---
name: experiment-tracking
description: Use when designing, reviewing, or reporting experiments — A/B tests, CRO tests, messaging tests, pricing tests, onboarding tests, or channel experiments. Triggers on requests for hypotheses, success metrics, sample-size discipline, guardrails, experiment logs, test readouts, or go/no-go decisions.
---

# Experiment Tracking

## Purpose
Run experiments like a disciplined operator: clear hypothesis, clean measurement, defensible decision.

## Use this when
- planning or evaluating an experiment (not just reporting existing performance)
- designing A/B tests, split tests, multivariate tests
- reviewing experiment results and making go/no-go decisions
- setting up experiment logs or readout templates
- checking whether tracking can support a proposed test

## Do NOT use this for
- implementing tracking codes (→ `tracking-measurement`)
- analyzing general performance after an experiment ends (→ `analytics-reporting`)
- one-off copy changes without a test hypothesis (→ `copy-editing-sweeps`)

## Do this

### 1. Define the decision
State exactly what decision this experiment informs. If you can't name the decision, don't run the test.

### 2. Write a falsifiable hypothesis
Format: "Changing [X] will [increase/decrease] [metric] by [amount] because [reason]."
If the hypothesis can't be proven wrong, it's not a hypothesis.

### 3. Define metrics
- **Primary metric:** one per experiment. This is what determines the winner.
- **Secondary metrics:** supporting signals (max 3).
- **Guardrails:** metrics that must not degrade (revenue, lead quality, error rate).

### 4. Check tracking readiness
Before launch, confirm:
- Primary metric is tracked with a reliable event/conversion action
- Guardrail metrics are trackable
- Attribution window is defined and consistent
If tracking is broken, route through `tracking-measurement` first.

### 5. Set runtime and thresholds
- Minimum sample size (use a calculator, not intuition)
- Runtime window (don't stop early because "it looks good")
- Decision threshold (e.g., 95% confidence, minimum 5% effect size)
- Stopping rules (what triggers early stop for harm)

### 6. Record and decide
After the test runs:
- Record result, confidence interval, effect size, sample size reached
- State go/no-go with rationale
- Document what you'd test next

## Example: Homepage headline A/B test

**Hypothesis:** Changing the H1 from "Grow Your Business" to "Get 3x More Leads in 90 Days" will increase demo booking rate by 15% because the specific outcome reduces ambiguity.

| Field | Value |
|---|---|
| Primary metric | Demo bookings / visitor |
| Guardrails | Bounce rate must not increase >10%, page load time must not degrade |
| Variants | A: "Grow Your Business" (control) / B: "Get 3x More Leads in 90 Days" |
| Sample size | 4,200 visitors per variant (calculated for 80% power, 5% MDE) |
| Runtime | 14 days minimum |
| Decision threshold | 95% confidence, minimum 15% lift |
| Result | B: 18.2% lift in demo bookings, 97.3% confidence, bounce rate flat |
| Decision | **Go** — implement variant B, monitor for 7 days post-launch |
| Next | Test social proof block below the new headline |

## Core rules
- One primary success metric per experiment.
- Do not launch tests with broken or uncertain instrumentation.
- Do not stop early just because results look exciting.
- Distinguish statistical significance, practical significance, and business significance.
- Preserve a written experiment log so the same mistakes are not repeated.

## Resources
- `references/experiment-readout-standards.md` — readout template and reporting format
- Sample size calculators: Evan Miller, Optimizely, or VWO calculators

## Checks and common mistakes
- Running multiple hidden experiments inside one messy launch
- Declaring winners from underpowered samples (<100 conversions per variant)
- Ignoring adverse side effects on revenue, lead quality, or user experience
- Using "we learned something" as an excuse for bad experimental design
- Confusing correlation in secondary metrics with proof of causation
- Changing multiple variables at once without a multivariate design

## Output contract
**Artifact:** Experiment log entry with hypothesis, metrics, variants, runtime, and result
**Evidence:** Statistical significance (p-value or confidence interval), sample size reached, effect size with direction
**Decision:** Go / no-go / iterate, with explicit rationale tied to primary metric and guardrail status
**Next:** Implement winner, design follow-up test, or investigate guardrail violations
