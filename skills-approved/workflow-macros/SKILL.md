---
name: workflow-macros
description: Use when executing common multi-step workflows that chain multiple skills together. Triggers on requests like "full content pipeline", "SEO fix workflow", "site launch checklist", "email system setup", or "content refresh". Pre-built pipelines that auto-chain skills in the right order with verification gates.
---

# Workflow Macros

## Purpose
Pre-built, battle-tested multi-skill pipelines that execute common workflows end-to-end with verification gates between steps.

## Use this when
- User requests a complex task that spans 3+ skills
- Common workflow patterns that repeat frequently
- Need to ensure skills run in the correct order with quality gates

## Do NOT use this for
- Single-skill tasks (load that skill directly)
- Ad-hoc one-off tasks
- Tasks requiring tight interactive back-and-forth

## Do this

### Macro 1: Content Pipeline E2E
**Trigger**: "Write and publish a new article about X"
```
Step 1: content-strategy-planning
  → Research topic, check cannibalization, define brief
  → GATE: Brief approved? Proceed.
  
Step 2: conversion-copywriting (if landing page) OR editorial-post-enhancement (if blog)
  → Write/enhance the content
  → GATE: Content quality pass?
  
Step 3: schema-ops
  → Add structured data (Article + FAQPage)
  → GATE: Schema validates?
  
Step 4: wordpress-growth-ops
  → Publish with internal links, metadata, media
  → GATE: Page live and rendering correctly?
  
Step 5: tracking-measurement
  → Verify tracking on new page
  → GATE: Events firing?
```

### Macro 2: SEO Fix Sprint
**Trigger**: "Fix SEO issues on [site/page]"
```
Step 1: seo-audit-playbook
  → Run audit, identify issues, prioritize
  → GATE: Issue list ranked by impact?
  
Step 2: schema-ops
  → Fix/improve schema markup
  → GATE: Schema validates?
  
Step 3: editorial-post-enhancement
  → Fix on-page issues, add internal links
  → GATE: Quality improved?
  
Step 4: test-automation-ops
  → Verify fixes don't break anything
  → GATE: All tests pass?
```

### Macro 3: Site Launch
**Trigger**: "Is this site ready to launch?" / "Launch [site]"
```
Step 1: launch-readiness-audit
  → Full pre-launch checklist
  → GATE: All critical items pass?
  
Step 2: money-path-verification
  → Verify primary conversion path end-to-end
  → GATE: Money path works?
  
Step 3: tracking-measurement
  → Verify all tracking is correct
  → GATE: All events firing?
  
Step 4: notification-engine
  → Set up monitoring alerts
  → GATE: Alerts configured?
```

### Macro 4: Email System Setup
**Trigger**: "Set up email marketing for [site]"
```
Step 1: email-marketing-engine
  → Configure platform, lists, sender
  → GATE: Platform connected?
  
Step 2: lifecycle-email-sequences
  → Design welcome + drip sequences
  → GATE: Sequences created?
  
Step 3: lead-magnet-delivery-ops
  → Set up capture + delivery flow
  → GATE: End-to-end delivery works?
  
Step 4: tracking-measurement
  → Verify email tracking
  → GATE: Opens/clicks tracked?
```

### Macro 5: Content Refresh
**Trigger**: "Update/improve existing content"
```
Step 1: seo-audit-playbook
  → Audit current performance, identify gaps
  → GATE: Prioritized gap list?
  
Step 2: editorial-post-enhancement
  → Apply enhancements (SEO, links, media, copy)
  → GATE: Quality improved?
  
Step 3: schema-ops
  → Update/add schema markup
  → GATE: Schema validates?
  
Step 4: wordpress-growth-ops
  → Publish updates
  → GATE: Changes live?
```

## Output Contract
**Artifact**: Completed multi-step workflow with verification at each gate
**Evidence**: Gate results for each step, final verification proof
**Decision**: Workflow completed or blocked at specific gate
**Next**: Monitor results, iterate if needed

## Checks
- Never skip verification gates
- If a gate fails, stop and fix before proceeding
- Document which macro was used and gate results
- Track macro usage — if a pattern repeats 3+ times, create a new macro
