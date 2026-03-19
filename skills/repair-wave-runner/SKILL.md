---
name: repair-wave-runner
description: Run canary-first, wave-based repair operations with verification gates, execution ledger logging, and stop conditions. Use when cleanup or recovery must proceed in safe controlled waves.
---

# Repair Wave Runner

## Purpose
Execute repairs safely in waves: canary, verify, next wave, verify, continue or stop. This skill exists to prevent repair work from turning a broken system into a worse one.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/recovery-playbook-pack.md`
- `skills/shared/verification-evidence-pack.md`
- `skills/shared/scripts/execution_ledger.py`

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
- sitewide cleanup must be done gradually
- one canary item should prove the repair first
- the site is unstable enough that huge repair runs are risky
- repairs involve duplicate blocks, metadata normalization, wrapper stripping, or partial rollback

## Workflow
1. define target set
2. create/open execution ledger
3. run canary
4. verify canary
5. run wave 1
6. verify wave 1
7. continue with additional waves only while healthy
8. stop on defined failure thresholds

## Output Contract
**Artifact**: wave log + verification checkpoints
**Evidence**: canary proof + per-wave proof
**Decision**: continue / stop / recover / rollback
**Next**: next wave or escalation
