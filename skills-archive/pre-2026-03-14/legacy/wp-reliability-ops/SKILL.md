---
name: wp-reliability-ops
description: Reliability-first WordPress execution for unstable environments. Use when runs are slowed by timeouts, cache/render mismatch, slug-to-live ID mismatch, flaky APIs, or repeated verification failures. Provides deterministic fallback flows to keep velocity high without losing safety.
---

# WP Reliability Ops

## Scope Ownership
### Own
- Execute Reliability-first WordPress execution for unstable environments. Use when runs are slowed by timeouts, cache/render mismatch, slug-to-live ID mismatch, flaky APIs, or repeated verification failures. Provides deterministic fallback flows to keep velocity high without losing safety.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

## Objective
Maintain execution velocity under degraded runtime conditions without losing safety.

## Mandatory flow
1. classify failure: `network | cache | mapping | payload-shape | auth | plugin`
2. resolve identity before write (slug, REST id, frontend postid alignment)
3. parallel reads + sequential atomic writes
4. verify source truth + live truth
5. if raw is correct but live is flaky, mark `degraded` and retry failed URLs only

## Retry policy
- standard: 3 tries, exponential backoff
- degraded critical URLs: 5 tries
- never rerun full batch if subset failed

## Cache variance protocol
- never claim breakage from single-signal canonical miss
- require dual confirmation
- label ambiguous states `monitor-only`

## Completion gate
Report must include:
- failure bucket counts
- exact URLs retried
- residual degraded items
- rollback readiness

## Constraints
- backup before risky edits
- no destructive bulk operations
- no guaranteed-outcome claims