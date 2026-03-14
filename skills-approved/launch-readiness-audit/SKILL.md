---
name: launch-readiness-audit
description: Use when deciding whether a site, funnel, product, landing page, checkout, lead flow, delivery system, or service path is actually ready to launch or relaunch. Triggers on requests for launch checks, go-live reviews, preflight audits, readiness assessments, launch proof, or “is this ready yet?”.
---

# Launch Readiness Audit

## Do NOT Use This For
- verifying a specific checkout path (use money-path-verification)
SEO auditing (use seo-audit-playbook)

## Purpose
Assess whether a launch is truly ready, with evidence instead of wishful thinking.

## Use this when
Use this skill when the task is broader than one bug fix and requires a release/no-release judgment.

Use `money-path-verification` for proving one path; use this skill when the decision spans offer, path, tracking, and fulfillment together.

## Do this
1. Identify the primary business goal of the launch.
2. Define the critical path that must work.
3. Check copy/offer readiness, path functionality, measurement, and delivery/follow-up.
4. Separate blockers from nice-to-haves.
5. Require proof for all critical launch conditions.
6. Return a clear status: ready, needs work, or blocked.

## Core rules
- Default to needs work unless critical-path proof is present.
- Nice design is not launch readiness.
- Tracking, fulfillment, and follow-up count as launch scope when they affect monetization.
- A launch decision should include remaining risk, not just current progress.

## Output
Default output should include:
- launch goal
- critical path
- ready items
- blockers
- open risks
- go / no-go recommendation
- next fixes in order

## Resources
Read when needed:
- `references/readiness-stack.md`
- `references/portfolio-launch-hotspots.md`


## Output Contract
**Artifact**: Go/no-go checklist with evidence
**Evidence**: Pass/fail for each checkpoint
**Decision**: Launch decision with confidence level
**Next**: Fix blockers or proceed
## Checks and common mistakes
- Do not confuse “page is live” with “launch is ready.”
- Do not call ready when delivery or automation is still uncertain.
- Do not hide launch risk in vague language.
- Do not spend time polishing secondary assets while blockers remain.
