---
name: technical-writing
description: Use when writing or restructuring technical documentation such as READMEs, setup guides, API docs, tutorials, handoff docs, SOPs, migration docs, or implementation notes that must be usable by real readers.
---

# Technical Writing

## Purpose
Turn technical reality into documentation people can actually use so the docs reduce questions instead of creating them.

## Use this when
- writing or restructuring READMEs, setup guides, API docs, tutorials, SOPs, migration docs, or handoff docs
- auditing documentation for clarity, completeness, or usability
- converting rough engineering notes into usable docs
- creating onboarding or operational documentation

## Do NOT use this for
- marketing copy (→ `conversion-copywriting`)
- content strategy work (→ `content-strategy-planning`)
- skill authoring (→ `skill-authoring-standard`)
- one-off chat explanations with no durable documentation artifact

## Do this
1. Identify the target reader and what they need to accomplish.
2. Choose the document type: tutorial, how-to, reference, explanation, decision doc, or runbook.
3. Lead with the outcome and prerequisites.
4. Structure the doc so each section has one clear job.
5. Use tested or clearly flagged examples, commands, and screenshots.
6. Call out version sensitivity, assumptions, and verification steps.
7. Remove filler, stale detail, and insider-only shortcuts.

## Core rules
- One document should mainly serve one document type.
- Clarity beats completeness theater.
- Bad docs are a product bug.
- Organize for scanability before polish.
- Write for a tired reader in a hurry.
- Do not present untested commands as trustworthy.

## Useful patterns
- README: purpose → quick start → prerequisites → usage → configuration → troubleshooting
- API docs: endpoint → auth → params → request → response → errors → limits
- runbook: alert → impact → diagnosis → resolution → escalation → aftermath
- setup guide: prerequisites → install → verify → troubleshoot → next steps
- migration guide: why → breaking changes → prep → migration → rollback → validation

## Resources
Read when needed:
- `references/doc-type-router.md`

## Checks and common mistakes
- mixing tutorial, reference, and explanation into one blob
- hiding prerequisites below the fold
- skipping the verify step
- writing for insiders only
- leaving version-sensitive instructions ambiguous
- producing docs with no clear user outcome

## Output contract
**Artifact:** revised documentation, outline, audit, or handoff doc
**Evidence:** clearer structure, tested or explicitly flagged instructions, and identified gaps/assumptions
**Decision:** doc ready, needs validation, or blocked by missing technical truth
**Next:** publish, test with target reader, or fill missing information
