---
name: content-integrity-cleanup
description: Diagnose and repair duplicated content blocks, repeated modules, malformed wrappers, duplicate schema/FAQ/embed sections, and structural render corruption in posts and pages. Use when content displays incorrectly or repeated elements appear across pages.
---

# Content Integrity Cleanup

## Purpose
Restore content to a clean, stable, render-safe state when prior edits, plugins, or automation have created duplication, malformed wrappers, or broken display.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`
- `skills/shared/recovery-playbook-pack.md`
- `skills/shared/verification-evidence-pack.md`
- `ops/site-ops-registry.md`
- `skills/shared/scripts/wp-bulk-ops.py`
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
- repeated “Related Posts” sections
- duplicate YouTube embeds, tables, FAQ blocks, schema blocks
- full HTML documents pasted into post content
- embedded article/header/H1 wrappers inside body content
- distorted page rendering after content operations
- plugin-injected blocks duplicated in raw content and live render

## Do NOT Use For
- ordinary SEO copy improvements
- clean content that only needs better wording
- technical site fixes unrelated to content structure

## Common Failure Classes
1. **Raw duplication** — duplicate modules saved into content
2. **Render duplication** — plugin/theme injects a second copy at render time
3. **Structural wrapper corruption** — embedded `<html>`, `<body>`, `<article>`, `<header>`, duplicate H1 wrappers
4. **Schema/module over-injection** — repeated FAQ/JSON-LD/tables/embeds from repeated automation runs
5. **Mixed-state corruption** — some items fixed, some partially broken

## Cleanup Workflow

### 1. Diagnose first
For a representative sample, determine:
- raw content duplicate count
- live render duplicate count
- whether duplication exists in raw, render, or both
- whether structural wrappers are malformed

### 2. Snapshot
Back up all affected records before mutation.

### 3. Fix by class
- **Raw duplicate blocks** → remove from content
- **Render-only duplicate blocks** → disable source plugin/module if possible
- **Embedded full HTML docs** → extract body content only
- **Embedded article/header/H1 wrappers** → strip wrapper, preserve body content
- **Duplicate schema/FAQ/embed sections** → keep best single version only

### 4. Canary repair
Repair 1 affected page first.
Verify:
- 1 H1
- 1 related-posts section max
- no embedded doctype/head/body in content
- expected canonical/title/meta still present

### 5. Wave cleanup
Only after canary succeeds:
- run small wave
- verify live samples
- continue in controlled batches

## Verification Checklist
- [ ] raw content duplicate count reduced as expected
- [ ] live page duplicate count reduced as expected
- [ ] H1 count is correct
- [ ] no broken wrappers remain
- [ ] no canonical/title/meta loss
- [ ] page still renders correctly

## Output Contract
**Artifact**: cleanup report + changed records + before/after counts
**Evidence**: raw duplicate counts + live render checks + sample URLs
**Decision**: fixed / partially fixed / blocked by plugin/render layer
**Next**: next cleanup wave or plugin/theme follow-up

## Anti-Patterns
- ❌ trying to clean duplicates without checking whether they’re in raw content or injected on render
- ❌ deleting whole sections before creating backups
- ❌ applying giant regex mutations across unstable sites without canaries
- ❌ fixing one symptom while leaving duplicate wrapper sources active
- ❌ claiming cleanup from raw state without checking live render

## Self-Critique Scorecard (/25)
1. **Diagnosis** (1-5): Was the duplication source correctly identified?
2. **Precision** (1-5): Were only the bad structures removed?
3. **Verification** (1-5): Was live render checked, not just raw state?
4. **Safety** (1-5): Were backups, canaries, and waves used correctly?
5. **Stability** (1-5): Did the cleanup leave content simpler and safer?

**Target: 22+/25**
