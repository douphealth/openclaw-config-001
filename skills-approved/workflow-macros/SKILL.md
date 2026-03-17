---
name: workflow-macros
description: Use when executing common multi-step workflows that chain multiple skills together. Triggers on requests like full content pipeline, SEO fix workflow, launch checklist, email system setup, content refresh, or other repeated multi-step operating patterns with verification gates.
---

# Workflow Macros

## Purpose
Run battle-tested multi-skill pipelines in the correct order with verification gates and explicit step handoffs.

## Use this when
- the user requests a complex task spanning 3+ skills
- a known workflow pattern repeats frequently
- skills must run in a specific order with quality gates between them

## Do NOT use this for
- single-skill tasks
- ad-hoc one-off tasks with no repeatable pattern
- tasks requiring tight interactive back-and-forth in one thread

## Macro operating rules
- Never skip verification gates.
- If a gate fails, stop and fix before proceeding.
- Each step must produce both an **artifact** and **evidence**.
- If branches are independent, consider `swarm-orchestrator` instead of serial execution.
- Pair high-risk execution with `auto-verification` even if local gates already exist.

## Macro 1: Content Pipeline E2E
**Trigger:** "Write and publish a new article about X"
```
Step 1: content-strategy-planning
  Artifact: brief
  Evidence: topic choice, gap logic, cannibalization check
  Gate: brief is usable and scoped

Step 2: conversion-copywriting OR editorial-post-enhancement
  Artifact: content draft or upgraded article
  Evidence: content quality pass
  Gate: content quality pass

Step 3: schema-ops
  Artifact: schema markup
  Evidence: validation result
  Gate: schema validates

Step 4: wordpress-growth-ops
  Artifact: published page/post
  Evidence: live rendered URL
  Gate: page is live and rendering correctly

Step 5: tracking-measurement
  Artifact: tracking verification
  Evidence: event confirmation
  Gate: events firing
```

## Macro 2: SEO Fix Sprint
**Trigger:** "Fix SEO issues on [site/page]"
```
Step 1: seo-audit-playbook
  Artifact: prioritized issue list
  Evidence: audit findings ranked by impact
  Gate: issue list is ranked and actionable

Step 2: schema-ops
  Artifact: improved schema
  Evidence: validation result
  Gate: schema validates

Step 3: editorial-post-enhancement
  Artifact: page/content improvements
  Evidence: before/after changes
  Gate: on-page quality improved

Step 4: test-automation-ops
  Artifact: verification result
  Evidence: test output
  Gate: tests pass
```

## Macro 3: Site Launch
**Trigger:** "Is this site ready to launch?" / "Launch [site]"
```
Step 1: launch-readiness-audit
  Artifact: readiness report
  Evidence: checklist results
  Gate: all critical items pass

Step 2: money-path-verification
  Artifact: money path proof
  Evidence: end-to-end test result
  Gate: primary conversion path works

Step 3: tracking-measurement
  Artifact: tracking verification
  Evidence: event confirmation
  Gate: all critical events fire

Step 4: notification-engine
  Artifact: monitoring/alerts configured
  Evidence: delivery path proof
  Gate: alerts are configured and provable
```

## Macro 4: Email System Setup
**Trigger:** "Set up email marketing for [site]"
```
Step 1: email-marketing-engine
  Artifact: configured platform
  Evidence: connection proof
  Gate: platform connected

Step 2: lifecycle-email-sequences
  Artifact: sequence set
  Evidence: sequence definitions
  Gate: sequences created

Step 3: lead-magnet-delivery-ops
  Artifact: working capture + delivery flow
  Evidence: end-to-end delivery proof
  Gate: delivery works

Step 4: tracking-measurement
  Artifact: tracking verification
  Evidence: test events / provider metrics
  Gate: opens/clicks/conversions tracked where expected
```

## Macro 5: Content Refresh
**Trigger:** "Update/improve existing content"
```
Step 1: seo-audit-playbook
  Artifact: prioritized gap list
  Evidence: audit findings
  Gate: gap list is usable

Step 2: editorial-post-enhancement
  Artifact: improved content
  Evidence: applied enhancements
  Gate: content quality improved

Step 3: schema-ops
  Artifact: updated schema
  Evidence: validation result
  Gate: schema validates

Step 4: wordpress-growth-ops
  Artifact: published update
  Evidence: live page proof
  Gate: changes are live
```

## Macro 6: Offer / Funnel Upgrade
**Trigger:** "Improve this offer", "fix service page conversions", "rework funnel"
```
Step 1: offer-positioning
  Artifact: positioning direction
  Evidence: chosen message angle
  Gate: positioning direction chosen

Step 2: service-funnel-architecture
  Artifact: funnel structure
  Evidence: CTA / page-flow logic
  Gate: funnel logic coherent

Step 3: conversion-copywriting
  Artifact: upgraded copy
  Evidence: revised sections and CTA logic
  Gate: copy quality pass

Step 4: tracking-measurement
  Artifact: tracking verification
  Evidence: event confirmation
  Gate: conversion events firing
```

## Macro 7: Monitoring / Alert Setup
**Trigger:** "monitor this site", "set alerts", "watch for issues"
```
Step 1: monitoring-ops
  Artifact: monitor scope and thresholds
  Evidence: scope definition
  Gate: scope is clear

Step 2: notification-engine
  Artifact: alert routing setup
  Evidence: delivery proof
  Gate: delivery path works

Step 3: test-automation-ops
  Artifact: monitor/alert proof
  Evidence: simulation or verification result
  Gate: alerting proved
```

## Macro 8: Agent-System Hardening
**Trigger:** "improve the agents", "upgrade the skill system", "make the workspace more autonomous/efficient"
```
Step 1: quality-scorecard
  Artifact: baseline score report
  Evidence: scored core skills and bottlenecks
  Gate: baseline established

Step 2: skill-authoring-standard
  Artifact: upgraded core skills
  Evidence: edited SKILL.md files
  Gate: critical skills hardened

Step 3: auto-verification
  Artifact: verification report
  Evidence: file reads confirming updates
  Gate: upgraded files are real and coherent

Step 4: swarm-orchestrator (optional second wave)
  Artifact: next-wave improvement plan
  Evidence: prioritized worker-ready queue
  Gate: parallelizable follow-up work identified
```

## Macro 9: Continuous Improvement / Remediation Loop
**Trigger:** "keep improving the workspace", "continuous improvement", "remediate weak skills", "make the agents better over time"
```
Step 1: quality-scorecard
  Artifact: fresh score report
  Evidence: weak skills and bottlenecks identified
  Gate: remediation targets ranked

Step 2: skill-authoring-standard
  Artifact: refactored weak skills
  Evidence: updated SKILL.md files / structure improvements
  Gate: targets hardened

Step 3: auto-verification
  Artifact: verification report
  Evidence: file reads or behavior checks proving updates are real
  Gate: changes verified

Step 4: quality-scorecard
  Artifact: follow-up score update
  Evidence: before/after comparison
  Gate: measurable improvement confirmed
```

## Resources
- Use `skill-router` first if a request is ambiguous but may collapse to a single target skill.
- Use `swarm-orchestrator` when independent tracks can run in parallel under one macro.
- Use `auto-verification` for final proof when the macro changes real systems or claims concrete completion.
- Use `ops/agent-system/continuous-improvement-cadence.md` for the standing remediation rhythm.
- Use `ops/agent-system/remediation-queue.md` as the active prioritized queue.

## Output contract
**Artifact:** completed multi-step workflow with verification at each gate
**Evidence:** gate results for each step and final proof
**Decision:** workflow completed or blocked at a specific gate
**Next:** monitor results, iterate if needed
