---
name: technical-writing
description: Enterprise technical documentation creation and improvement. Use when writing or restructuring READMEs, setup guides, API docs, tutorials, handoff docs, SOPs, implementation notes, or migration guides. Triggers on clearer docs, developer-facing guides, onboarding documentation, documentation audits, or turning rough engineering notes into usable documentation.
---

# Technical Writing — Enterprise Documentation

## Purpose
Turn technical reality into documentation people can actually use. Ship docs that reduce questions, not create them.

## When to Use
- Writing or restructuring READMEs, setup guides, API docs, tutorials, SOPs
- Documentation audits or gap analysis
- Converting rough engineering notes into shareable docs
- Creating onboarding or handoff documentation
- Migration guides or change documentation

**Do NOT use for:** Marketing copy (→ `conversion-copywriting`), content strategy (→ `content-strategy-planning`), skill authoring (→ `skill-authoring-standard`).

## Documentation Framework

### Phase 1: Audience & Type

Route to the correct doc type:

| Reader wants to... | Doc type | Lead with |
|-------------------|----------|-----------|
| Learn a concept | Explanation | Analogy, mental model |
| Complete a task | How-to | Steps, prerequisites |
| Build something step-by-step | Tutorial | Working example, environment setup |
| Look up a fact | Reference | Searchable index, parameter tables |
| Understand a decision | ADR/Decision | Context, options evaluated, rationale |

### Phase 2: Structure
1. Lead with outcome: what will the reader be able to do after reading?
2. List prerequisites and assumptions up front
3. Break content into sections with one job each
4. Use progressive detail: essential path first, edge cases after

### Phase 3: Write & Validate
5. Make examples concrete and testable
6. Include working code, commands, or screenshots — not pseudocode
7. If instructions are version-sensitive, say so prominently
8. Remove assumptions, filler, and stale implementation details

### Phase 4: Audit Checklist
9. **Completeness**: Every public API/function documented? Every setup step covered?
10. **Accuracy**: All commands tested? Do code examples compile/run?
11. **Currency**: Version references <12 months? Deprecated features still documented?
12. **Navigation**: Reader finds what they need in <30 seconds? Table of contents present?
13. **Onboarding test**: New team member can follow without asking questions?
14. **Searchability**: Findable via search, wiki, or sensible naming?

## Templates

**README**: Purpose → Quick Start → Prerequisites → Detailed Usage → Configuration → Troubleshooting → Contributing

**API Doc**: Endpoint → Auth → Parameters → Request example → Response example → Error codes → Rate limits → SDK notes

**Runbook**: Alert description → Impact severity → Diagnosis steps → Resolution steps → Escalation path → Post-mortem template

**Setup Guide**: Prerequisites → Environment setup → Install → Verify installation → Common issues → Next steps

**Migration**: Why migrate → Breaking changes → Pre-migration checklist → Step-by-step migration → Rollback plan → Post-migration validation


## Self-Critique Scorecard (/25)
After every operation, score yourself:

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Functionality** (1-5) | ? | Does it work perfectly and meet all requirements? |
| **Quality** (1-5) | ? | Is it enterprise-grade and production-ready? |
| **Verification** (1-5) | ? | Was it verified via multiple methods? |
| **Speed** (1-5) | ? | Was execution optimal with parallel operations? |
| **Learning** (1-5) | ? | Were new patterns documented and memory updated? |

**Target: 22+/25 before claiming completion**

### Pre-Flight Checklist
- [ ] Credentials verified and target exists
- [ ] Rollback plan identified
- [ ] Success criteria defined
- [ ] Anti-patterns reviewed

### Post-Flight Checklist
- [ ] Verified via API response + live check
- [ ] Quality score logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered
- [ ] No common mistakes made

## Output Contract
**Artifact**: Documentation (README, guide, API doc, runbook, or migration doc)
**Evidence**: Audit checklist pass, code examples tested, target reader can follow
**Decision**: Documentation approved for use
**Next**: Team review, version control integration

## Anti-Patterns
- ❌ Mixing tutorial, reference, and explanation into one wall of text
- ❌ Hiding prerequisites halfway down
- ❌ Untested commands presented as trustworthy
- ❌ Writing for insiders only
- ❌ Skipping the "verify" step
- ❌ Perfect as enemy of shipped — get core docs right first, polish later

## Compatibility
- Targets current WordPress 6.9+ where applicable
- REST API + WP-CLI preferred over browser automation
- Batch operations via `_fields` + `per_page=100` + `concurrent.futures`
- Browser automation only when API/CLI insufficient

## Inputs Required (Pre-Flight)
Before executing any task in this skill:
1. **Target identification** — What site, page, post, or system is being operated on?
2. **Auth verification** — Confirm credentials work (test API call or CLI command)
3. **Current state** — Understand what exists before making changes (GET before POST)
4. **Environment** — Production vs staging (assume production unless stated)
5. **Constraints** — No downtime? Preserve SEO? Preserve data? Budget limits?

## Triage Protocol
Before ANY operation:
1. **Identify** — What type of content/system/problem is this?
2. **Check state** — Query current state via API/CLI before modifying
3. **Verify creds** — Confirm authentication works
4. **Plan rollback** — How to undo if something breaks?
5. **Scope check** — Is this a single item or batch? Scale determines approach.

## Speed Optimizations
- **API calls**: Always use `_fields` parameter (80%+ payload reduction)
- **Pagination**: Use `per_page=100` for list endpoints
- **Parallelism**: Use `concurrent.futures` for independent operations (max 10/site)
- **Caching**: Store results in session — never re-fetch same data
- **Batching**: Group similar operations into single API calls where possible
- **Direct CLI**: Use WP-CLI `wp db query` for complex operations

## Error Recovery (Auto-Learning)
- Track error patterns — after 2 failures, try alternative approach
- Log recurring fixes to `memory/YYYY-MM-DD.md`
- Update references when new patterns discovered
- Rollback plan: Know how to undo before making changes

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

## Output Contract
- **Artifact**: What was created/changed/deleted
- **Evidence**: API response proof + live verification
- **Decision**: Success/failure with reasoning
- **Next**: What follow-up is needed (if any)
