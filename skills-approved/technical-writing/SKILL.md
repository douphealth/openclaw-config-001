---
name: technical-writing
description: Use when writing or restructuring technical documentation such as READMEs, setup guides, API docs, tutorials, handoff docs, SOPs, or implementation notes. Triggers on requests for clearer docs, developer-facing guides, onboarding docs, migration docs, documentation audits, or turning rough engineering notes into usable documentation.
---

# Technical Writing

## Do NOT Use This For
- marketing copy (use conversion-copywriting)
content strategy (use content-strategy-planning)

## Purpose
Turn technical reality into documentation people can actually use. Ship docs that reduce questions, not create them.

## Use this when
- Writing or restructuring READMEs, setup guides, API docs, tutorials, SOPs
- Performing documentation audits or gap analysis
- Converting rough engineering notes into shareable docs
- Creating onboarding or handoff documentation

Do **not** use for: skill authoring (use `skill-authoring-standard`), marketing copy (use `conversion-copywriting`), or one-off chat explanations.

## Do this

### Phase 1: Audience & type
1. Identify the reader and the job they are trying to do.
2. Decide the doc type: tutorial (learning), how-to (task), reference (lookup), or explanation (understanding).
3. Match depth to audience: expert vs. onboarding vs. cross-functional.

**Doc type routing:**
| Reader wants to... | Doc type | Lead with |
|-------------------|----------|-----------|
| Learn a concept | Explanation | Analogy, mental model |
| Complete a task | How-to | Steps, prerequisites |
| Build something step-by-step | Tutorial | Working example, environment setup |
| Look up a fact | Reference | Searchable index, parameter tables |
| Understand a decision | ADR/Decision doc | Context, options evaluated, rationale |

### Phase 2: Structure
4. Lead with outcome: what will the reader be able to do after reading?
5. List prerequisites and assumptions up front.
6. Break content into sections with one job each.
7. Use progressive detail: essential path first, edge cases after.

### Phase 3: Write & validate
8. Make examples concrete and testable where possible.
9. Include working code, commands, or screenshots — not pseudocode.
10. If instructions are version-sensitive, say so prominently.
11. Remove assumptions, filler, and stale implementation details.

### Phase 4: Documentation audit checklist
12. **Completeness**: Does every public API/function have a doc? Every setup step covered?
13. **Accuracy**: Are all commands tested? Do code examples compile/run?
14. **Currency**: Any version references older than 12 months? Any deprecated features still documented?
15. **Navigation**: Can a reader find what they need in <30 seconds? Is there a table of contents?
16. **Onboarding test**: Can a new team member follow this without asking questions?
17. **Searchability**: Are docs findable via search, internal wiki, or sensible naming?

### Template patterns

**README pattern:**
```
Purpose → Quick Start → Prerequisites → Detailed Usage → Configuration → Troubleshooting → Contributing
```

**API doc pattern:**
```
Endpoint → Auth → Parameters → Request example → Response example → Error codes → Rate limits → SDK notes
```

**Runbook pattern:**
```
Alert description → Impact severity → Diagnosis steps → Resolution steps → Escalation path → Post-mortem template
```

**Setup guide pattern:**
```
Prerequisites → Environment setup → Install → Verify installation → Common issues → Next steps
```

**Migration guide pattern:**
```
Why migrate → Breaking changes → Pre-migration checklist → Step-by-step migration → Rollback plan → Post-migration validation
```

## Core rules
- Clarity beats completeness theater.
- Bad docs are a product bug.
- Keep setup paths runnable and realistic.
- Organize for scanability before polish.
- One doc type per document — don't mix tutorial and reference.
- Write for the reader who is tired, distracted, and in a hurry.

## Output contract
Deliver:
1. **Target reader** — who this is for and what they're trying to do
2. **Document type** — tutorial / how-to / reference / explanation
3. **Improved structure** — section outline with one-job-per-section
4. **Revised documentation** — full draft following the structure
5. **Gaps & assumptions** — what still needs confirmation or testing
6. **Audit score** — pass/fail on each of the 6 audit checklist items

## Verification steps
- [ ] All commands/code examples have been tested or flagged as untested
- [ ] Prerequisites are listed before any instructions begin
- [ ] Version sensitivity is called out where applicable
- [ ] A reader from the target audience can follow the doc without external help
- [ ] Table of contents or navigation aid is present for docs >50 lines
- [ ] No untested commands presented as trustworthy

## Resources
Read when needed:
- `references/doc-type-router.md`

## Checks and common mistakes
- Do not mix tutorial, reference, and explanation into one wall of text.
- Do not hide prerequisites halfway down the page.
- Do not include untested commands as if they are trustworthy.
- Do not write for insiders only — test with a fresh pair of eyes.
- Do not skip the "verify" step — readers need to know it worked.
- Do not let perfect be the enemy of shipped — get the core docs right first.

## Output Contract
**Artifact**: Skill-specific deliverable (report, fix, config, or document)
**Evidence**: Proof that the work was completed correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action or monitoring period
