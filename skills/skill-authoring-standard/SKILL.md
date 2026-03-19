---
name: skill-authoring-standard
description: Enterprise skill creation and refactoring for OpenClaw agents. Use when creating new skills from scratch, editing or refactoring existing skills, auditing skill quality against standards, or organizing skill directory structure. Triggers on "create a skill", "author a skill", "tidy up a skill", "improve this skill", "clean up this skill", or "audit skill quality".
---

# Skill Authoring Standard — Enterprise Skill Creation

## Purpose
Create, refine, and audit agent skills that are clear, well-scoped, and production-ready.

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
- Creating new skills from scratch
- Editing, refactoring, or improving existing skills
- Auditing skill quality and completeness
- Organizing skill directory structure

**Do NOT use for:** Running skills (→ use the skill directly), routing to skills (→ `skill-router`), measuring skill quality (→ `quality-scorecard`).

## Skill Anatomy

Every skill MUST have:

### 1. Frontmatter (YAML)
```yaml
---
name: skill-name
description: Clear one-sentence description. Triggers on [list of trigger phrases].
---
```

**Rules:**
- `name`: lowercase, hyphen-separated, matches directory name
- `description`: One sentence covering purpose + trigger phrases

### 2. SKILL.md Structure
```
# Skill Name — Subtitle

## Purpose
One paragraph on what this skill accomplishes.

## When to Use
- Bullet list of trigger scenarios

## Do NOT Use For
- Cross-references to other skills for adjacent tasks

## Do This
[Step-by-step workflow]

## Core Rules
[Key discipline points]


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
**Artifact**: What gets produced
**Evidence**: How to verify it was done correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action
```

### 3. Optional Supporting Files
- `references/` — Reference docs, frameworks, templates
- `scripts/` — Helper scripts, automations
- `templates/` — Reusable templates

## Creation Workflow

1. **Scope** — Define the skill's boundaries (what it does and doesn't do)
2. **Structure** — Write frontmatter + SKILL.md following anatomy
3. **Detail** — Add workflow steps, rules, anti-patterns, and proof standards
4. **Route** — Add "Do NOT Use For" cross-references to adjacent skills
5. **Superpower Layer** — For any meaningful skill, include or reference:
   - spec-first behavior for ambiguous/high-risk tasks
   - plan-first behavior for multi-step tasks
   - parallel dispatch guidance for independent work
   - review-before-completion and verification-before-completion
   - enterprise backup / rollback / retry rules
6. **Test** — Validate trigger accuracy against real prompt examples
7. **Audit** — Score using `quality-scorecard` before publishing

## Quality Standards

| Standard | Requirement |
|----------|-------------|
| Frontmatter | name + description with trigger phrases |
| Purpose | Clear, one paragraph |
| When to Use | 3+ trigger scenarios |
| Do NOT Use | 2+ adjacent skill cross-references |
| Workflow | Step-by-step, numbered |
| Output Contract | Artifact + Evidence + Decision + Next |
| Anti-patterns | 3+ common mistakes |


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
**Artifact**: SKILL.md + optional supporting files
**Evidence**: Quality score ≥80 on quality-scorecard
**Decision**: Skill approved for use
**Next**: Add to routing (STACK-MAP.md) if needed

## Anti-Patterns
- ❌ No "Do NOT Use For" section (scope creep)
- ❌ Vague triggers: "use when helpful" → be specific
- ❌ No output contract (agent doesn't know when it's done)
- ❌ Skipping anti-patterns (agent repeats common mistakes)
- ❌ Making one skill do everything (split into focused skills)

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
