---
name: skill-authoring-standard
description: Use when creating, editing, reviewing, or refactoring OpenClaw skills, SKILL.md files, bundled references, or skill directory structure. Triggers on requests to create a skill, improve a skill, clean up a skill, audit skill quality, or turn repeated workflows into reusable skills.
---

# Skill Authoring Standard

## DO NOT USE FOR
- Executing tasks that existing skills handle (use those skills instead)
- Creating skills for one-off tasks (use ad-hoc instructions)

## Purpose
Create OpenClaw skills that are discoverable, lean, reusable, and tested enough to trust.

## Non-negotiables
- Write skills for repeated workflows, not one-off stories.
- Keep `SKILL.md` concise; move heavy detail into `references/` or `scripts/`.
- Optimize `description` for triggering conditions, not workflow summary.
- Use exact file names and forward-slash paths.
- Prefer one strong example over many weak ones.
- For fragile or compliance-heavy skills, test behavior before declaring the skill good.

## When to create a skill
Create a skill when all are true:
- the workflow repeats
- the right approach is not obvious every time
- a future agent would benefit from saved judgment, reference, or tooling

Do **not** create a skill for:
- one-off project notes
- trivial reminders
- things better enforced by code, validation, or scripts

## Standard structure
```text
skill-name/
  SKILL.md
  references/    # optional, load only when needed
  scripts/       # optional, deterministic helpers
  assets/        # optional, output resources/templates
```

## Metadata rules
Frontmatter has only:
- `name`
- `description`

### Name
- lowercase letters, digits, hyphens
- short, clear, action-oriented
- prefer verb-led or strongly descriptive names

### Description
Write for **selection**.
- say when to use the skill
- include concrete triggers, symptoms, contexts, file types, tools, or failure patterns
- use third-person style
- avoid vague labels like “helper” or “utils”
- do **not** summarize the whole workflow if that summary might replace reading the body

Good pattern:
- `Use when ...`

## Body pattern
Use this default shape unless the task strongly suggests a better one:

1. **Purpose** — one short paragraph
2. **Use this when** — triggers and boundaries
3. **Do this** — numbered workflow or decision rules
4. **Resources** — which `references/` or `scripts/` to use and when
5. **Checks / common mistakes** — what usually goes wrong

## Degrees of freedom
Choose the tightness of instructions deliberately.

- **High freedom**: heuristics, review, analysis, writing
- **Medium freedom**: preferred pattern with room for adaptation
- **Low freedom**: exact scripts or exact sequences for fragile operations

Use low freedom when mistakes are expensive.

## Progressive disclosure
Keep `SKILL.md` short enough to scan fast.
Move large materials into `references/` when they are:
- API docs
- schemas
- detailed examples
- variant-specific instructions

Keep references one level deep from `SKILL.md`.
If a reference file is long, add a table of contents.

## Script rule
If the same helper code keeps getting rewritten, make it a script.
Prefer executable scripts for deterministic tasks.
Document whether a file should be:
- executed
- read as reference
- copied as a template

## Quality bar
A good skill should be:
- easy to trigger
- easy to scan
- hard to misuse
- small enough to justify its token cost
- structured so another agent can succeed without extra hidden context

## Testing standard
For reference-heavy or low-risk skills, do a light reality check.
For discipline, compliance, or fragile workflow skills, use the testing reference:
- `references/testing-skills.md`

For stack-level routing and overlap checks, also use:
- `/home/openclaw/.openclaw/workspace/skills/VALIDATION-SCENARIOS.md`
- `/home/openclaw/.openclaw/workspace/skills/VALIDATION-CHECKLIST.md`

## Anti-patterns
- bloated theory in `SKILL.md`
- repeating the same instructions in multiple files
- vague descriptions
- multiple mediocre examples when one good example would do
- deeply nested references
- project-specific narratives pretending to be reusable skills

## Final rule
If importing an external skill, distill it first.
Adopt principles, not bloat.


## Output Contract
**Artifact**: Validated SKILL.md file
**Evidence**: Passes quality checklist, trigger clarity
**Decision**: Skill approved for use
**Next**: Monitor trigger accuracy

## Do NOT Use This For
- Tasks better handled by a more specific skill — check skill-router
- One-off quick questions that don't need a skill
- Tasks in a different domain — route to the correct skill first
