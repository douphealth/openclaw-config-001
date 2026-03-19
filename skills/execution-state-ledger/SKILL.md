---
name: execution-state-ledger
description: Persist structured state for long-running or interruption-prone jobs, including execution briefs, worker outputs, checkpoints, failures, recovery status, and completion proof. Use when work spans time, batches, retries, or unstable systems.
---

# Execution State Ledger

## Purpose
Prevent long-running work from becoming fuzzy, lossy, or unrecoverable. This skill creates and maintains a structured ledger of what was planned, what ran, what failed, what was verified, and what remains.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/execution-brief-template.md`
- `skills/shared/worker-result-contract.md`
- `skills/shared/verification-evidence-pack.md`
- `ops/site-ops-registry.md`
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
- Long-running jobs
- Multi-batch operations
- Interruption-prone systems
- Any task where state continuity matters across time
- Work with multiple workers, retries, recovery waves, or checkpoints

## Ledger Contents
For each job, persist:
- execution brief
- targets
- checkpoints
- worker outputs
- failures and error classes
- recovery actions
- completion evidence
- next pending step

## Storage Location
Default:
- `ops/execution-ledger/{job-id}.json`
- optional human summary: `ops/execution-ledger/{job-id}.md`

## Workflow
1. open or create ledger before serious execution
2. write execution brief
3. append checkpoints as work progresses
4. append worker results in structured form
5. record failures immediately
6. record verification evidence before completion
7. set final status: complete / partial / blocked / rolled back

## Output Contract
**Artifact**: structured execution ledger
**Evidence**: complete checkpoint trail and proof log
**Decision**: current state of the job at any moment
**Next**: exact next step or blocker

## Anti-Patterns
- ❌ relying on memory for long-running jobs
- ❌ worker outputs scattered across logs only
- ❌ no durable checkpoint after partial success
- ❌ no persistent record of what was verified vs assumed

## Self-Critique Scorecard (/25)
1. **Continuity** (1-5): Could someone resume from this ledger cleanly?
2. **Completeness** (1-5): Are key states/checkpoints recorded?
3. **Clarity** (1-5): Is status obvious at a glance?
4. **Evidence** (1-5): Are proof artifacts attached to milestones?
5. **Recovery Value** (1-5): Would this materially help after failure/interruption?

**Target: 22+/25**
