# WordPress Management SOTA Runbook

## Priority order
1. Critical trust/security/rendering breakage
2. Indexation/canonical/schema blockers
3. Content quality and internal linking
4. CRO/performance enhancements

## Operational cycle
1. Discover target URLs and templates.
2. Run baseline audit (status/canonical/schema/meta).
3. Build fix queue with severity + blast radius.
4. Execute smallest high-impact reversible fix first.
5. Verify live output immediately.
6. Log evidence and residuals.
7. Re-audit to confirm closure.

## Non-negotiables
- Backup before risky changes.
- Atomic updates only.
- Verify each update before moving on.
- Never run broad destructive cleanup without explicit approval.

## Verification checklist
- URL returns expected status.
- Canonical present and self-correct.
- JSON-LD present and parseable.
- Title/meta sane and intent-aligned.
- No source leakage or malformed HTML.
- Internal links resolve as expected.
