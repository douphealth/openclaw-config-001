---
name: experiment-tracking
description: Use when designing, reviewing, or reporting experiments such as A/B tests, CRO tests, messaging tests, pricing tests, onboarding tests, or channel experiments. Triggers on requests for hypotheses, success metrics, sample-size discipline, guardrails, experiment logs, test readouts, or go/no-go decisions from experiment results.
---

# Experiment Tracking

## Do NOT Use This For
- implementing tracking codes (use tracking-measurement)
analyzing results after experiment ends (use analytics-reporting)

## Purpose
Run experiments like a disciplined operator: clear hypothesis, clean measurement, defensible decision.

## Use this when
Use this skill when the task is planning or evaluating an experiment rather than merely reporting existing performance.

If measurement is unreliable, route through `tracking-measurement` before trusting any experiment outcome.

## Do this
1. Define the decision the experiment is meant to inform.
2. Write a falsifiable hypothesis.
3. Define primary metric, secondary metrics, and guardrails.
4. Check whether tracking can actually support the test.
5. Set runtime, stopping logic, and decision thresholds before launch.
6. Record result, confidence, effect size, and next action.

## Core rules
- One primary success metric per experiment.
- Do not launch tests with broken or uncertain instrumentation.
- Do not stop early just because results look exciting.
- Distinguish statistical significance, practical significance, and business significance.
- Preserve a written experiment log so the same mistakes are not repeated.

## Output
Default output should include:
- experiment name
- hypothesis
- variants / control
- primary metric and guardrails
- launch requirements
- decision thresholds
- result summary
- next step

## Resources
Read when needed:
- `references/experiment-readout-standards.md`


## Output Contract
**Artifact**: Experiment log with hypothesis, metrics, decision
**Evidence**: Statistical significance, sample size
**Decision**: Go/no-go decision
**Next**: Implement winner or iterate
## Checks and common mistakes
- Do not run multiple hidden experiments inside one messy launch.
- Do not declare winners from underpowered samples.
- Do not ignore adverse side effects on revenue, lead quality, or user experience.
- Do not let “we learned something” become an excuse for bad experimental design.
