---
name: using-superpowers
description: Meta-skill that activates on complex, ambiguous, risky, or multi-step tasks to enforce spec-first planning, safe parallel execution, review, and verification-before-completion. Use when a task should not be executed ad hoc.
---

# Using Superpowers — Meta Execution Discipline

## Purpose
Force OpenClaw into a higher-quality operating mode for serious work. This skill exists to stop premature execution, reduce avoidable damage, and ensure complex work gets clarified, planned, dispatched, reviewed, and verified.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`
- `skills/shared/auto-dispatch-policy.md`
- `skills/shared/auto-router-config.json`
- `skills/shared/capability-map.md`
- `skills/shared/skill-capability-graph.json`

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
- The request is ambiguous, high-stakes, or cross-functional
- The task affects production systems, live sites, money paths, or user-facing assets
- The work spans multiple steps, tools, skills, or deliverables
- More than 10 items may be touched
- Parallel workers would materially improve speed or quality
- Prior attempts failed because execution started too fast or without enough structure

## Do NOT Use For
- Tiny, obvious, low-risk one-step tasks
- Purely conversational or brainstorming-only exchanges with no execution need
- Cases where a single specialist skill can safely execute immediately with minimal risk

## Activation Test
If **2 or more** of these are true, activate this skill:
- [ ] unclear scope
- [ ] production risk
- [ ] more than one system/skill involved
- [ ] batch size > 10
- [ ] rollback matters
- [ ] user is asking for “best strategy”, “most efficient”, or “enterprise-grade” execution

## Mandatory Workflow

### 1. Spec First
Before any serious execution, define:
- target outcome in one sentence
- hard constraints
- success criteria
- what will count as failure

### 2. Plan First
Create a short plan with:
- ordered steps
- dependencies
- safe parallelizable work
- rollback/backup points
- verification checkpoints

### 3. Dispatch Intelligently
Use parallel workers only where independence is real.

Safe to parallelize:
- audits
- research
- classification
- diffing
- verification on separate targets
- independent site/post batches

Unsafe to parallelize blindly:
- overlapping writes to same object
- mutations that depend on prior unstable state
- destructive actions without isolation

### 4. Two-Stage Review
Before completion:
1. **Spec review** — did the output solve the requested problem?
2. **Quality review** — is it clean, non-duplicative, efficient, and enterprise-grade?

### 5. Verification Before Completion
Never claim success from logs or save responses alone.
Collect the strongest relevant proof:
- API state
- rendered state
- user-path confirmation
- downstream effect when relevant

## Output Contract
**Artifact**: scoped execution strategy + routed skill plan or properly controlled execution
**Evidence**: explicit plan, checkpoint logic, and proof standard
**Decision**: execute now / ask one clarifying question / split into workers / defer due to instability
**Next**: hand off to specialist skill(s) or orchestrator

## Anti-Patterns
- ❌ jumping directly into production writes on vague requests
- ❌ using one giant script when staged batches are safer
- ❌ parallelizing overlapping writes to the same asset
- ❌ calling work “done” before live verification
- ❌ letting urgency destroy structure

## Self-Critique Scorecard (/25)
1. **Spec** (1-5): Was the actual outcome clarified before action?
2. **Plan** (1-5): Was execution structured and minimal?
3. **Dispatch** (1-5): Was parallelism used intelligently?
4. **Verification** (1-5): Was reality checked before completion?
5. **Control** (1-5): Did this prevent chaos instead of adding overhead?

**Target: 22+/25**
