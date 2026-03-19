---
name: task-intake-spec-writer
description: Convert vague, high-stakes, or multi-step requests into a precise execution brief with constraints, success criteria, risks, rollback, and next-step plan. Use when a user request is underspecified or too important to execute ad hoc.
---

# Task Intake Spec Writer

## Purpose
Turn messy requests into execution-grade specs. This skill exists to stop expensive misunderstandings before work begins.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`
- `skills/shared/execution-brief-template.md`
- `skills/shared/scripts/execution_brief.py`

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
- The user asks for a large, vague, emotional, or multi-step task
- The task affects production systems, SEO, money paths, content fleets, or infra
- The correct strategy is not obvious yet
- Multiple skills could apply and wrong routing would be expensive
- You need an execution brief before using swarm/orchestration skills

## Do NOT Use For
- Tiny, obvious one-step tasks
- Fully specified tasks with clear success criteria and low risk
- Pure brainstorming with no execution intent

## Inputs Required
1. Requested outcome
2. Target surface(s): site, system, content set, workflow, infra
3. Constraints: time, downtime, safety, SEO, data preservation, model restrictions
4. Known blockers or recent failures
5. Preferred operating mode (fastest / safest / highest quality / balanced)

## Intake Workflow

### 1. Define the real goal
Convert the request into:
- **Outcome**: what must be true when done?
- **Scope**: what is included / excluded?
- **Constraints**: what cannot be broken or changed?

### 2. Define success criteria
Specify:
- measurable success
- acceptable partial success
- failure conditions
- required evidence

### 3. Identify risk class
Classify as:
- low-risk
- production-sensitive
- infrastructure-unstable
- multi-skill
- batch / scale
- rollback-critical

### 4. Select execution mode
Choose one:
- direct execution
- specialist skill execution
- plan-first execution
- parallel execution director
- failure-recovery mode

### 5. Produce the execution brief
The brief must include:
- objective
- scope
- constraints
- risks
- best strategy
- required skills
- worker split if parallel
- verification standard
- rollback plan

## Output Template

```markdown
## Execution Brief

### Objective
[one-sentence outcome]

### Scope
- Included:
- Excluded:

### Constraints
- 

### Risk Level
[low / medium / high]

### Best Strategy
[direct / specialist / plan-first / parallel / recovery-led]

### Skills to Use
1. 
2. 
3. 

### Execution Plan
1. 
2. 
3. 

### Verification Standard
- 

### Rollback / Recovery
- 
```

## Anti-Patterns
- ❌ turning a vague request into immediate execution
- ❌ assuming urgency removes the need for specification
- ❌ skipping rollback thinking on production work
- ❌ routing directly into mutation-heavy skills without defining success first

## Output Contract
**Artifact**: execution brief
**Evidence**: explicit constraints, success criteria, strategy, and skill selection
**Decision**: how the task should be executed
**Next**: route to the correct specialist / director skill

## Self-Critique Scorecard (/25)
1. **Clarity** (1-5): Did the spec remove ambiguity?
2. **Scope** (1-5): Were boundaries and exclusions clear?
3. **Strategy** (1-5): Was the best execution mode selected?
4. **Risk** (1-5): Were constraints and rollback identified?
5. **Usefulness** (1-5): Could a worker execute from this brief cleanly?

**Target: 22+/25**
