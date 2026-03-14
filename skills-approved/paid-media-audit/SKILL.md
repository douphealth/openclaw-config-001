---
name: paid-media-audit
description: Use when auditing Google Ads, Meta Ads, Microsoft Ads, or paid acquisition programs for wasted spend, tracking problems, structural issues, bidding mistakes, creative gaps, audience problems, or scale readiness. Triggers on requests for ad account audits, CAC problems, wasted spend reviews, campaign diagnostics, account takeovers, or “why is paid underperforming?”.
---

# Paid Media Audit

## Do NOT Use This For
- setting up tracking (use tracking-measurement)
general analytics reporting (use analytics-reporting)

## Purpose
Find the highest-impact paid media problems before more budget gets wasted.

## Use this when
Use this skill when the task is diagnosing or auditing paid acquisition performance.

Do **not** use this skill when the real issue is primarily tracking implementation; pair with `tracking-measurement` when needed.

If the landing page, offer, or checkout path is the suspected bottleneck, pair with `revenue-site-execution`, `money-path-verification`, or `offer-positioning` instead of blaming media by default.

## Do this
1. Define channel, objective, spend level, and conversion target.
2. Check tracking and conversion action quality first.
3. Audit account structure, bidding, budget pressure, audiences, search terms/placements, and creative coverage.
4. Distinguish efficiency problems from scale problems.
5. Prioritize fixes by business impact, not by how easy they are to talk about.
6. Give a clear action order with projected upside where reasonable.

## Core rules
- Do not judge paid performance without checking measurement quality first.
- Separate structural issues from strategy issues from creative issues.
- Flag budget waste, learning resets, and poor optimization signals explicitly.
- Diagnose using recent data, but look for trend shifts and change-history clues when available.
- Avoid fake precision on upside projections.

## Output
Default output should include:
- account context
- highest-severity findings
- evidence
- likely impact
- action plan
- dependencies on tracking, landing pages, or offer quality

## Resources
Read when needed:
- `references/audit-priority-stack.md`
- `references/portfolio-paid-diagnosis.md`


## Output Contract
**Artifact**: Ad account audit report with recommendations
**Evidence**: Waste analysis, ROAS data, audience insights
**Decision**: Action plan prioritized
**Next**: Implement changes and measure
## Checks and common mistakes
- Do not give generic “test more creatives” advice without identifying the actual gap.
- Do not ignore landing page mismatch when diagnosing ad performance.
- Do not confuse lead volume with lead quality.
- Do not call an account healthy just because CTR looks fine.
