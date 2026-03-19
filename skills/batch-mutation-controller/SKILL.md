---
name: batch-mutation-controller
description: Enterprise controller for safe wave-based batch changes on WordPress and other mutable systems. Use when many items must be modified with canaries, health checks, verification gates, and stop conditions.
---

# Batch Mutation Controller

## Purpose
Apply changes at scale without turning one mistake into a fleet-wide mess.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`
- `skills/shared/recovery-playbook-pack.md`
- `skills/shared/verification-evidence-pack.md`
- `ops/site-ops-registry.md`
- `skills/shared/scripts/wp-bulk-ops.py`
- `skills/shared/scripts/recovery_canary.py`
- `skills/shared/scripts/execution_ledger.py`
- `skills/shared/scripts/repair_wave_runner.py`

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
- 10+ posts/pages/items need similar changes
- batch cleanup, metadata fixes, schema fixes, excerpt fixes, content repair
- any sitewide mutation where failure must be contained
- unstable systems where giant scripts are dangerous

## Do NOT Use For
- single-record edits
- pure audits with no writes
- overlapping writes to the same records from multiple workers

## Mutation Modes

### Mode A — Canary
Use on first change or after instability.
- 1 item only
- verify API state + live state
- stop if anything unexpected happens

### Mode B — Small Wave
Use after successful canary.
- 3-10 items
- verify sample after wave
- continue only if health remains stable

### Mode C — Controlled Batch
Use once system is clearly stable.
- 10-50 items
- progress reports every 10
- health checks every 25-50
- stop on repeated failures

## Mandatory Flow
1. health check target
2. enumerate affected items
3. back up every item before mutation
4. run canary
5. verify canary
6. run small wave
7. verify wave
8. continue in batches only if healthy
9. final verification sample before completion

## Stop Conditions
Abort or pause when:
- 3 consecutive save failures
- health checks fail twice in a row
- verification mismatch appears on 2+ items
- duplicate or malformed state appears unexpectedly
- rollback need becomes clearer than forward-fix

## Verification Rules
At minimum verify:
- mutation landed in saved state
- live page/system reflects expected result
- no new duplication or structural corruption
- no key metadata or canonical loss

## Output Contract
**Artifact**: mutation wave log + changed items + final verification summary
**Evidence**: before/after + health checks + sampled live proof
**Decision**: continue / stop / rollback / escalate
**Next**: next wave or cleanup/recovery

## Anti-Patterns
- ❌ one giant blind script on unstable systems
- ❌ no canary before scale writes
- ❌ treating save success as proof of correctness
- ❌ continuing through repeated transport failures
- ❌ skipping backups because the change seems “small”

## Self-Critique Scorecard (/25)
1. **Control** (1-5): Were writes safely staged?
2. **Containment** (1-5): Would a mistake have stayed small?
3. **Verification** (1-5): Was each wave actually proven?
4. **Efficiency** (1-5): Was batching fast without being reckless?
5. **Recoverability** (1-5): Could everything be reversed if needed?

**Target: 22+/25**
