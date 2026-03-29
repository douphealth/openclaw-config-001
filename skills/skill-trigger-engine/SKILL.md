---
name: skill-trigger-engine
description: Meta-skill for deterministic skill activation policy. Use when improving, auditing, or applying the automatic trigger logic that decides which control, orchestration, recovery, or specialist skills should activate first.
---

# Skill Trigger Engine

## Purpose
Provide a deterministic trigger layer for OpenClaw so skill activation becomes more automatic, more consistent, and less dependent on ad hoc judgment.

This skill should push the system toward earlier activation of orchestration, persistence, verification, and restartable execution patterns when tasks are meaningful enough to benefit from them.

## Shared Doctrine References
- `skills/shared/skill-trigger-engine-spec.md`
- `skills/shared/auto-dispatch-policy.md`
- `skills/shared/capability-map.md`
- `skills/shared/skill-capability-graph.json`
- `skills/shared/worker-ownership-standard.md`
- `skills/shared/execution-queue-standard.md`

## Superpower Layer

For serious work, also follow:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`
- `skills/shared/review-release-gate.md`
- `skills/shared/role-phase-execution-model.md`
- `skills/shared/response-excellence-standard.md`
- `skills/shared/skill-efficiency-standard.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks when safe
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use
- improving routing quality
- deciding trigger precedence
- making skill activation more automatic
- reducing misfires or under-activation of meta-skills

## Do NOT Use For
- direct execution of business tasks
- content/site operations themselves

## Trigger Defaults (High-Leverage)
### Autonomous / long-run / max-performance requests
If the user asks for autonomy, overnight execution, many-hour work, many-day work, maximum performance, enterprise-grade orchestration, or minimal babysitting:
- activate orchestration/persistence skills early
- prefer `using-superpowers` or `skill-router` first if routing is not already obvious
- strongly consider `job-bootstrapper`, `execution-state-ledger`, `parallel-execution-director`, or `swarm-orchestrator`
- require explicit task states, validation gates, stop conditions, and restart-safe outputs
- prefer deterministic pipeline stages and explicit worker ownership over improvised multi-agent chatter
- for meaningful delivery, route toward `premium-review-director`, `premium-qa-orchestrator`, and `premium-release-gate`
- if reusable patterns emerge, route toward `ops/macros/self-improvement-promotion.md`

### Visual / UI / Layout requests
If the user mentions screenshots, mobile view, desktop view, visual breakage, ugly UI, distorted layout, overflow, or DOM inspection:
- activate `browser-visual-ops` early
- prefer the visual fix macro when the task involves a page/post change
- require screenshot evidence before claiming visual success when browser tooling exists

### Fragile custom page requests
If the task involves a fragile custom page, repeated regressions, or a page already patched multiple times:
- require backup first
- baseline screenshots
- overflow diagnostics if mobile is involved
- escalate to page-safe rewrite sooner instead of endless micro-patching

### Serious keyword/page opportunity requests
If the user is choosing or evaluating a keyword/page opportunity:
- require post-keyword competitive blueprint logic
- filter to true keyword-targeting competitor pages
- include overlap-based content requirements
- include backlink overlap opportunities where possible

## Output Contract
**Artifact**: trigger policy or improved routing behavior
**Evidence**: clearer activation rules and reduced ambiguity
**Decision**: how the engine should route or activate skills
**Next**: update router, policy, or capability graph
