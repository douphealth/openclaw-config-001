---
name: parallel-execution-director
description: Enterprise task decomposition and parallel worker orchestration for independent subtasks, audits, batch operations, and multi-surface execution. Use when speed, scale, and accuracy all matter and work can be safely split.
---

# Parallel Execution Director

## Purpose
Decompose serious work into independent deliverables, dispatch the right workers in parallel, and synthesize results without losing control, quality, or rollback safety.

## Strategic Entry Point
Use this as the **primary entrypoint** for serious parallel work.
- Use `using-superpowers` before this when the task is still ambiguous or risky.
- Use this skill to design and direct the parallel plan.
- Use `swarm-orchestrator` as the lower-level worker execution substrate/templates layer.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`
- `skills/shared/auto-dispatch-policy.md`
- `skills/shared/capability-map.md`
- `skills/shared/skill-capability-graph.json`
- `skills/shared/worker-result-contract.md`
- `skills/shared/scripts/synthesize_worker_results.py`
- `skills/swarm-orchestrator/SKILL.md`

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
- A task contains multiple independent deliverables
- There are many URLs/posts/sites/items to audit or process
- Research, implementation, and verification can run concurrently
- You need speed without sacrificing evidence and quality
- One worker can own one clear deliverable

## Do NOT Use For
- Tiny tasks with no meaningful decomposition
- Overlapping writes to the same object where race conditions are likely
- Situations where infrastructure is so unstable that concurrency will amplify failure
- Work where the main challenge is ambiguity, not throughput (use `using-superpowers` first)

## Director Workflow

### 1. Decompose
Break the request into units with:
- a single owner
- a single deliverable
- a clear success condition
- minimal dependency on other units

Good unit examples:
- “Audit 25 URLs for metadata issues”
- “Check GSC/Bing data and return opportunities”
- “Verify top 10 pages for duplicate H1s”
- “Fix 5 structurally broken posts”

Bad unit examples:
- “Improve the whole site”
- “Do SEO and also fix everything else”
- “Touch the same 20 posts from 3 workers at once”

### 2. Classify Each Unit
Label each as one of:
- audit
- research
- implementation
- verification
- synthesis

### 3. Choose Dispatch Pattern

#### Pattern A — Audit Swarm
Use when many assets need inspection.
- 1 worker per chunk
- no writes
- merge results into one prioritized report

#### Pattern B — Research + Execution Split
Use when implementation depends on evidence.
- worker group 1 = research/audit
- main/director synthesizes
- worker group 2 = implementation
- final worker or main session verifies

#### Pattern C — Batch Write Waves
Use when many independent records need similar safe changes.
- canary wave (1-3 items)
- first batch
- health check
- next batch
- final verification sample

#### Pattern D — Multi-Site Split
Use one worker per site, then synthesize centrally.

### 4. Worker Contract
Each worker must return:
- what it checked/changed
- evidence
- pass/fail
- blockers
- next recommendation

Format:
- `SUCCESS: [summary]`
- `FAILED: [reason]`
- `EVIDENCE: [key facts]`

### 5. Checkpoints
Require checkpoints when:
- production writes begin
- >20 items are touched
- failure rate exceeds 10%
- site health degrades
- evidence is conflicting

### 6. Synthesis
The director must:
- deduplicate findings
- rank by impact and urgency
- detect contradictions between workers
- decide go / hold / rollback / escalate

## Worker Count Guide
| Workload | Recommended workers |
|---|---|
| 2-5 units | 2-3 |
| 6-15 units | 4-6 |
| 16-40 units | 6-8 |
| 40+ units | 8-10 max, only if infra stable |

## Stability Rules
- If site/system health is unstable, reduce concurrency immediately
- If >20% workers fail, stop and diagnose
- If writes fail due to transport issues, fall back to smaller waves
- Never let one failing worker silently stall the whole program

## Output Contract
**Artifact**: worker plan + synthesized result
**Evidence**: worker outputs + verification summary
**Decision**: continue / batch next wave / stop / rollback / escalate
**Next**: exact next wave or specialist routing

## Anti-Patterns
- ❌ dispatching vague workers with fuzzy ownership
- ❌ parallelizing overlapping writes to the same record set
- ❌ no synthesis pass after worker completion
- ❌ letting a batch continue through repeated unknown failures
- ❌ treating concurrency as a substitute for thinking

## Self-Critique Scorecard (/25)
1. **Decomposition** (1-5): Were units truly independent and well-scoped?
2. **Dispatch** (1-5): Was worker usage efficient and justified?
3. **Control** (1-5): Were failure rates and checkpoints handled well?
4. **Synthesis** (1-5): Were outputs merged into one coherent truth?
5. **Verification** (1-5): Was the final state actually proven?

**Target: 22+/25**
