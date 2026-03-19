---
name: verification-runner
description: Run standardized verification after edits, audits, repairs, and batch operations. Use when completion needs real evidence from API state, live render, metadata integrity, and sampled checks.
---

# Verification Runner

## Purpose
Turn verification into a first-class step instead of an afterthought. This skill exists to collect proof, not vibes.

## Strategic Entry Point
Use this as the **general verification entrypoint**.
- Use `auto-verification` when you want specialized verification workflows/templates.
- Use this skill when you need a standard pass/partial/fail evidence decision after edits, batches, audits, or recovery.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/verification-evidence-pack.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`

## When to Use
- After content edits
- After batch mutations
- After cleanup/recovery work
- After audits that recommend concrete actions
- Before claiming anything is done

## Do NOT Use For
- Pure planning/spec work with no changes yet
- Tiny conversational tasks with no external state

## Verification Modes
1. **WP content edit** — API state + live page + H1/canonical/meta check
2. **Batch mutation** — changed count + sampled live checks + health checks
3. **Render integrity** — duplicate counts + wrapper checks + live render
4. **SEO audit** — data sources + ranked opportunities + exact next move
5. **Recovery** — canary result + post-fix health + before/after proof

## Workflow
1. Identify verification mode
2. Collect strongest available evidence
3. Sample if full verification is too expensive
4. Record failures explicitly
5. Return pass / partial / fail with proof

## Output Contract
**Artifact**: verification summary
**Evidence**: concrete proof items
**Decision**: pass / partial / fail
**Next**: continue / stop / recover / escalate
