---
name: swarm-orchestrator
description: Use when work should be decomposed across multiple OpenClaw workers, specialist sessions, or verification passes. Triggers on parallel execution, director-worker-verifier setups, high-throughput batches, multi-site operations, or independent deliverables that benefit from orchestration without overlapping scope.
---

# Swarm Orchestrator

## Purpose
Coordinate complex work through a director / worker / verifier model so execution scales without losing quality, proof, or control.

## Use this when
- the task has multiple independent deliverables
- parallel execution would save meaningful time
- specialist roles would materially improve output quality
- verification should be separated from implementation
- a multi-site or high-throughput workflow would overload a single thread

## Do NOT use this for
- simple single-threaded tasks that finish faster directly
- vague tasks that cannot yet be split cleanly
- tightly interactive problems that need constant back-and-forth in one thread
- decomposition done only for appearance rather than speed or quality

## Operating model
- Main session = director
- Worker sessions = execution
- Separate verifier = QA when proof matters

## Decision gate: should this be decomposed?
Decompose only if at least one is true:
- the deliverables are independent
- the task naturally separates into specialist roles
- waiting on one path should not block another path
- verification should be independent from implementation
- the total task is large enough that orchestration beats direct execution

If none are true, do the work directly.

## Do this
1. Define the exact goal and proof gates before launching workers.
2. Split the work into the smallest sensible independent deliverables.
3. Assign one worker per deliverable.
4. Give each worker a narrow scope, explicit artifact, and explicit evidence requirement.
5. Decide verifier coverage before execution starts.
6. Keep the director focused on prioritization, blockers, synthesis, and proof.
7. Do not declare success until required verification passes.

## Required worker contract
Every worker should receive:
- **goal** — one deliverable only
- **scope** — what is in bounds and out of bounds
- **artifact** — what must be produced
- **evidence** — what proof is required
- **constraints** — tools, safety, time, or approval limits
- **handoff** — what the director should do next

Every worker should return:
- artifact
- evidence
- blockers
- confidence / uncertainty
- next action recommendation

## Verification policy
- If proof is possible, assign or perform verification explicitly.
- Prefer a separate verifier when implementation could bias completion claims.
- Use `auto-verification` for final proof on important outcomes.
- Never let workers treat optimistic progress as verified completion.

## Resources
Read these before launching workers when relevant:
- `references/worker-selection.md` for worker choice and spawn patterns
- `references/parallel-dispatch-patterns.md` for independence checks and worker prompt structure
- `references/site-routing.md` when the task touches one of the workspace websites
- `references/output-contracts.md` when worker outputs need a consistent format

## Rules
- One worker = one deliverable.
- Prefer parallel workers only when tasks are truly independent.
- Prefer REST, API, and file methods over browser methods when possible.
- Set explicit quality gates before execution starts; do not improvise them after the fact.
- Use ACP when debugging or code changes are multi-file and iterative.
- Use normal subagents when research, writing, audits, publishing, or QA dominate.
- Use retry loops sparingly; after repeated failure, change method or escalate instead of thrashing.
- Do not let the main thread become a duplicate worker.

## Checks and common mistakes
- Do not spawn workers for overlapping or vaguely worded tasks.
- Do not split work so finely that orchestration overhead exceeds the benefit.
- Do not skip verification just because execution succeeded.
- Do not treat “worker finished” as “task complete”.
- Do not synthesize outputs until blockers and proof status are clear.

## Default director output
Return:
- plan
- workers launched or not launched
- proof gates
- current blockers
- verified outcomes
- next best actions

## Output contract
**Artifact:** orchestration plan with worker assignments
**Evidence:** worker outputs and verification results
**Decision:** all workers completed and verified, or blocked with reason
**Next:** synthesis and next actions
