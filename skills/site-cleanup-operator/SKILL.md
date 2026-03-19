---
name: site-cleanup-operator
description: Specialist cleanup skill for structurally broken, duplicated, or over-injected site content. Combines integrity cleanup, batch control, repair waves, and verification. Use for sitewide cleanup campaigns.
---

# Site Cleanup Operator

## Purpose
Run disciplined cleanup campaigns on broken sites without making the mess worse.

## Shared Doctrine References
- `skills/content-integrity-cleanup/SKILL.md`
- `skills/batch-mutation-controller/SKILL.md`
- `skills/repair-wave-runner/SKILL.md`
- `skills/verification-runner/SKILL.md`
- `skills/failure-recovery-director/SKILL.md`
- `ops/site-recovery-packs/plantastichaven.com.md`
- `ops/site-ops-registry.md`

## When to Use
- Sitewide duplicate Related Posts cleanup
- Duplicate FAQ/embed/table/schema cleanup
- Wrapper stripping and render repair
- Cleanup waves on unstable or recently corrupted sites

## Do NOT Use For
- Ordinary content editing
- New publishing work on healthy sites

## Cleanup Sequence
1. classify corruption
2. back up targets
3. run canary cleanup
4. verify live render
5. run wave-based repairs
6. verify each wave
7. stop on instability

## Output Contract
**Artifact**: cleanup execution + wave log
**Evidence**: before/after counts + live verification
**Decision**: fixed / partial / blocked
**Next**: next wave or recovery escalation
