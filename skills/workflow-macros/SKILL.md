---
name: workflow-macros
description: Use when executing common multi-step workflows that chain multiple skills together. Triggers on requests like "full content pipeline", "SEO fix workflow", "site launch checklist", "email system setup", or "content refresh". Pre-built pipelines that auto-chain skills in the right order with verification gates.
---

# Workflow Macros

## Purpose
Pre-built, battle-tested multi-skill pipelines that execute common workflows end-to-end with verification gates between steps.

## Superpower Layer

For serious work, also follow:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks when safe
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use
- User requests a complex task that spans 3+ skills
- Common workflow patterns that repeat frequently
- Need to ensure skills run in the correct order with quality gates

## Do NOT Use For
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

### Macro 6: Visual Fix / Fragile Page Repair
**Trigger**: "fix mobile view", "looks broken", "take screenshots", "visual QA", "desktop/mobile issue", "page is visually broken"
```
Step 1: browser-visual-ops
  → Capture baseline desktop + mobile screenshots
  → Run overflow diagnostic if needed
  → GATE: Problem area identified clearly?

Step 2: target execution skill (usually wordpress-growth-ops or direct WP/API edit)
  → Make the smallest structural fix first
  → GATE: Change applied successfully?

Step 3: browser-visual-ops
  → Re-capture desktop + mobile screenshots
  → GATE: Rendered output improved?

Step 4: verification-runner
  → Confirm no regression / final proof set exists
  → GATE: Verified enough to claim success?

Escalation rule:
- If 2-3 targeted visual fixes fail, switch to `skills/shared/page-safe-rewrite-protocol.md`
```


## Self-Critique Scorecard (/25)
After every operation, score yourself:

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Functionality** (1-5) | ? | Does it work perfectly and meet all requirements? |
| **Quality** (1-5) | ? | Is it enterprise-grade and production-ready? |
| **Verification** (1-5) | ? | Was it verified via multiple methods? |
| **Speed** (1-5) | ? | Was execution optimal with parallel operations? |
| **Learning** (1-5) | ? | Were new patterns documented and memory updated? |

**Target: 22+/25 before claiming completion**

### Pre-Flight Checklist
- [ ] Credentials verified and target exists
- [ ] Rollback plan identified
- [ ] Success criteria defined
- [ ] Anti-patterns reviewed

### Post-Flight Checklist
- [ ] Verified via API response + live check
- [ ] Quality score logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered
- [ ] No common mistakes made

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

## Anti-Patterns
- ❌ Loading three skills at once with no gate logic
- ❌ Continuing the macro after a failed checkpoint
- ❌ Using a macro when a single specific skill is enough
- ❌ Letting one worker own multiple unrelated deliverables
- ❌ Repeating the same failed workflow instead of escalating to a safer one

## Self-Correction Loop
After a macro run, ask:
1. Did the gates stop the workflow at the right moment?
2. Should the workflow have escalated sooner to verification or rewrite logic?
3. Did this task expose a missing reusable macro or standard?
4. Which step caused the most friction and should be optimized next?
5. Should this workflow be split into a faster default path and a safer fragile path?

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
- Apply `skills/api-efficiency-protocol.md` across the macro when API-capable skills are chained
- Reuse validated macro sequences instead of designing the workflow from scratch each time
- Stop the workflow at the first failed gate instead of pushing bad state downstream
- Load one skill at a time in sequence, only advancing after the gate passes

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
