---
name: skill-trigger-engine
description: Meta-skill for deterministic skill activation policy. Use when improving, auditing, or applying the automatic trigger logic that decides which control, orchestration, recovery, or specialist skills should activate first.
---

# Skill Trigger Engine

## Purpose
Provide a deterministic trigger layer for OpenClaw so skill activation becomes more automatic, more consistent, and less dependent on ad hoc judgment.

## Shared Doctrine References
- `skills/shared/skill-trigger-engine-spec.md`
- `skills/shared/auto-dispatch-policy.md`
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
- improving routing quality
- deciding trigger precedence
- making skill activation more automatic
- reducing misfires or under-activation of meta-skills

## Do NOT Use For
- direct execution of business tasks
- content/site operations themselves

## Output Contract
**Artifact**: trigger policy or improved routing behavior
**Evidence**: clearer activation rules and reduced ambiguity
**Decision**: how the engine should route or activate skills
**Next**: update router, policy, or capability graph
