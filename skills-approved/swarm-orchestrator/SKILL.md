---
name: swarm-orchestrator
description: Use when work should be decomposed across multiple OpenClaw workers, specialist sessions, or verification passes. Triggers on parallel execution, multi-site operations, director-worker-verifier setups, autonomous execution systems, high-throughput batches, or tasks with independent deliverables that benefit from orchestration.
---

# Swarm Orchestrator

## Do NOT Use This For
- simple single-threaded tasks (do them directly)
tasks that need tight interactive back-and-forth

## Purpose
Coordinate complex work through a director/worker/verifier pattern so execution can scale without losing QA.

## Use this when
Use this skill when:
- the task has multiple independent deliverables
- parallel execution would save meaningful time
- specialist roles would improve output quality
- verification should be separated from implementation
- a multi-site or high-throughput workflow would overload a single thread

Do **not** use this skill when:
- a single focused thread can finish the task quickly
- decomposition would add more overhead than value
- the user wants tight interactive back-and-forth on one small problem

## Operating model
- Main session = director
- Worker sessions = execution
- Separate verifier = QA

## Do this
1. Decide whether the task should stay in the main thread or be decomposed.
2. Split decomposed work into the smallest sensible independent deliverables.
3. Assign one worker per deliverable.
4. Choose verifier coverage before declaring success.
5. Keep the director focused on prioritization, blockers, synthesis, and proof.

## Resources
Read these before launching workers when relevant:
- `references/worker-selection.md` for worker choice and spawn patterns
- `references/parallel-dispatch-patterns.md` for independence checks and worker prompt structure
- `references/site-routing.md` when the task touches one of the workspace websites
- `references/output-contracts.md` when worker outputs need a consistent format

## Rules
- One worker = one deliverable.
- Prefer parallel workers when tasks are independent.
- Prefer REST, API, and file methods over browser methods when possible.
- Do not claim done without proof where proof is possible.
- Use ACP when debugging or code changes are multi-file and iterative.
- Use normal subagents when research, writing, audits, publishing, or QA dominate.
- Do not let workers report optimistic progress as if it were verified completion; require concrete evidence in outputs.
- Set explicit quality gates before execution starts; do not improvise them after the fact.
- Use retry loops sparingly and deliberately; after repeated failure, escalate or change method instead of thrashing.


## Output Contract
**Artifact**: Orchestration plan with worker assignments
**Evidence**: Worker outputs, verification results
**Decision**: All workers completed and verified
**Next**: Synthesis and next actions
## Checks and common mistakes
- Do not spawn workers for vague, overlapping tasks.
- Do not skip verification just because execution succeeded.
- Do not let the main thread become a duplicate worker.
- Do not decompose tiny tasks that would finish faster directly.

## Default director output
Return:
- plan
- workers launched or not launched
- current blockers
- verified outcomes
- next best actions
