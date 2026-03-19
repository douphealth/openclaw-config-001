---
name: failure-recovery-director
description: Diagnose and recover from unstable infrastructure, partial batch failures, broken execution state, duplicated content, failed automations, and rollback-critical incidents. Use when work has already gone wrong or systems are unstable.
---

# Failure Recovery Director

## Purpose
Take control after things break. This skill is for recovery-led operations: stabilizing systems, classifying failure modes, containing further damage, restoring trust, and choosing the safest next move.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`
- `skills/shared/auto-dispatch-policy.md`
- `skills/shared/recovery-playbook-pack.md`
- `skills/shared/verification-evidence-pack.md`
- `ops/site-ops-registry.md`
- `ops/site-recovery-packs/plantastichaven.com.md`
- `ops/site-recovery-packs/micegoneguide.com.md`
- `skills/shared/scripts/recovery_canary.py`
- `skills/shared/scripts/execution_ledger.py`
- `skills/shared/wordpress/rollback-recovery-protocol.md`

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
- Batch work partially failed and state is inconsistent
- Infrastructure is unstable or timing out during operations
- Content has become duplicated, broken, or malformed
- A site is intermittently up/down during execution
- You need to stop further damage before continuing
- Recovery, rollback, cleanup, or triage is more important than speed

## Do NOT Use For
- Clean new work on stable systems
- Tiny isolated issues with obvious fixes
- Pure audits where nothing has failed yet

## Failure Classification
Classify first:
1. **Infra failure** — timeouts, 5xx, broken TLS, rate limiting, load spikes
2. **State corruption** — duplicate blocks, malformed HTML, partial writes, mixed templates
3. **Workflow failure** — wrong plan, wrong skill, missing backup, poor sequencing
4. **Verification failure** — unclear whether changes actually landed
5. **Tooling failure** — scripts/workers hanging, model/tool mismatch, concurrency misuse

## Recovery Workflow

### 1. Contain
- stop active destructive or unstable processes
- reduce concurrency
- avoid more writes until the failure class is known

### 2. Stabilize
- confirm target health
- determine whether the system is safe enough for reads only, limited writes, or no writes
- if unstable, prefer audit and backup over mutation

### 3. Snapshot
- capture current state
- capture affected object list
- create or confirm rollback artifacts

### 4. Choose recovery mode
- **rollback** if latest changes are net harmful and a clean backup exists
- **forward-fix** if corruption is limited and easily repairable
- **freeze + audit** if infrastructure is unstable or root cause is unclear

### 5. Repair in waves
- canary repair (1 item)
- verify live
- small wave
- verify again
- continue only if health remains stable

### 6. Postmortem
Document:
- what failed
- why it failed
- how it was detected
- what rule/protocol should prevent recurrence

## Recovery Output Template

```markdown
## Recovery Plan

### Failure Class
[infrastructure / state corruption / workflow / verification / tooling]

### Current Risk
[low / medium / high]

### Containment Actions
- 

### Recovery Mode
[rollback / forward-fix / freeze+audit]

### Repair Plan
1. 
2. 
3. 

### Verification Standard
- 

### Postmortem Note
- 
```

## Anti-Patterns
- ❌ continuing the same batch script after repeated unknown failures
- ❌ trying to “fix everything at once” on unstable infrastructure
- ❌ writing over corrupted content before snapshotting it
- ❌ claiming recovery because one page loaded once
- ❌ treating infra instability like an ordinary content bug

## Output Contract
**Artifact**: recovery plan and/or controlled repair execution
**Evidence**: before/after state, health checks, verification samples
**Decision**: rollback / forward-fix / stop / escalate
**Next**: stable execution path or manual intervention requirement

## Self-Critique Scorecard (/25)
1. **Containment** (1-5): Did I stop further damage quickly?
2. **Diagnosis** (1-5): Was the failure class correctly identified?
3. **Control** (1-5): Was recovery paced and evidence-based?
4. **Verification** (1-5): Was recovery actually proven?
5. **Prevention** (1-5): Did I document how to avoid recurrence?

**Target: 22+/25**
