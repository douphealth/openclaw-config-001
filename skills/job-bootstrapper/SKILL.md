---
name: job-bootstrapper
description: Create the initial execution brief, ledger, target set, strategy choice, and worker plan for serious tasks. Use when work should start with structure instead of ad hoc execution.
---

# Job Bootstrapper

## Purpose
Start serious work cleanly. This skill creates the skeleton of a job before implementation begins.

## Shared Doctrine References
- `skills/shared/execution-brief-template.md`
- `skills/shared/auto-dispatch-policy.md`
- `skills/shared/capability-map.md`
- `skills/shared/scripts/execution_brief.py`
- `skills/shared/scripts/execution_ledger.py`

## When to Use
- Multi-step tasks
- Risky production work
- Long-running jobs
- Jobs that may need workers, checkpoints, or recovery

## Do NOT Use For
- Tiny one-step tasks
- Purely conversational answers

## Bootstrap Output
- execution brief
- chosen strategy
- initial targets
- worker split (if needed)
- ledger initialized
- first checkpoint written

## Output Contract
**Artifact**: bootstrapped job package
**Evidence**: brief + ledger + strategy
**Decision**: ready for execution / needs clarification
**Next**: hand off to director or specialist skill
