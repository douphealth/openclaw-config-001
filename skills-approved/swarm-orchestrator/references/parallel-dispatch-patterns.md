# Parallel Dispatch Patterns

Use this reference when deciding whether to fan work out across multiple workers.

## Dispatch in parallel when
- there are 2+ independent deliverables
- failures or tasks have different root causes
- workers can operate without shared state
- one fix is unlikely to invalidate the others

## Keep work together when
- tasks are tightly coupled
- one diagnosis likely explains several failures
- workers would edit the same files or fight over the same state
- full-system understanding is required before action

## Worker prompt standard
Each worker should get:
- narrow scope
- concrete goal
- constraints
- expected output format

Good worker prompt components:
- what exact file/system/page they own
- what success looks like
- what they must not change
- what evidence they must return

## Director checks
Before launching workers, ask:
1. Are these really independent?
2. Is one worker enough per deliverable?
3. Can I verify outputs separately?
4. Would sequencing be safer than parallelism?

## Common mistakes
- spawning vague overlapping workers
- parallelizing tasks that share state
- asking one worker to solve an entire messy domain
- skipping verifier review because parallel work feels productive
