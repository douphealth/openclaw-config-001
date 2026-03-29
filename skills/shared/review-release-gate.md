# Review / Release Gate

Use this for meaningful user-facing, production-facing, or high-value work.

## Review Gate
Two-stage review is required before claiming completion:

### 1. Spec Review
- Did the output solve the requested problem?
- Is the scope correct?
- Did the work avoid surprise expansion?

### 2. Quality Review
- Is the output clean, minimal, maintainable, and premium quality?
- Are there obvious regressions, contradictions, or half-finished edges?
- Is the implementation better than a naive baseline?

## Verification Gate
At least one strong proof type is required, and preferably more than one for important work:
- file/state proof
- config proof
- API proof
- browser/render proof
- execution log proof
- downstream behavior proof

## Release Gate
For public-facing or production-impacting work, do not call it complete until:
- implementation is done
- verification is done
- important docs/state were updated if needed
- rollback/recovery posture is known
- next risk or follow-up is surfaced clearly

## Result Labels
- `ready_for_review`
- `review_changes_requested`
- `ready_for_verification`
- `verification_failed`
- `ready_for_release`
- `released`
- `released_with_followups`

## Anti-Patterns
- saying "done" after implementation only
- treating log output as sufficient proof
- skipping review because the change was small but user-facing
- releasing without noting residual risk
