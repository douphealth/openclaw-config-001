---
name: skill-authoring-standard
description: Use when creating, editing, reviewing, or refactoring OpenClaw skills, SKILL.md files, bundled references, or skill directory structure. Triggers on requests to create a skill, improve a skill, clean up a skill, audit skill quality, or turn repeated workflows into reusable skills.
---

# Skill Authoring Standard

## Purpose
Create OpenClaw skills that are discoverable, lean, reusable, hard to misuse, and structured for real execution rather than decorative documentation.

## Use this when
- creating a new skill
- refactoring or tightening an existing skill
- cleaning up a bloated `SKILL.md`
- improving trigger clarity, boundaries, or output contracts
- restructuring a skill directory into better references/scripts/assets

## Do NOT use this for
- executing tasks that an existing skill already handles
- creating a skill for a one-off project note or temporary workaround
- preserving bloated external skill content without distillation

## Non-negotiables
- Write skills for repeated workflows, not one-off stories.
- Keep `SKILL.md` concise; move heavy detail into `references/` or `scripts/`.
- Optimize `description` for triggering conditions, not workflow summary.
- Use exact file names and forward-slash paths.
- Prefer one strong example over many weak ones.
- For fragile or compliance-heavy skills, test behavior before declaring the skill good.
- Every meaningful skill should define artifact, evidence, decision, and next.

## Create or refactor a skill only when
All are true:
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

## Preferred body pattern
Use this default shape unless the task strongly suggests a better one:
1. **Purpose**
2. **Use this when**
3. **Do NOT use this for**
4. **Do this**
5. **Resources**
6. **Checks and common mistakes**
7. **Output contract**

## Tightness rules
Choose the instruction tightness deliberately:
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
- long decision trees that do not need to be loaded every time

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
- structured so another agent can succeed without hidden context
- explicit about proof when proof matters

## Refactor checklist
When improving an existing skill, check for:
- vague or bloated description
- weak or missing boundaries
- duplicated instructions
- no clear decision sequence
- no output contract
- no proof or verification guidance where needed
- too much theory in the main file
- references that should be scripts

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
- output contracts that say nothing real
- “done” language without proof expectations

## Final rule
If importing an external skill, distill it first.
Adopt principles, not bloat.

## Output contract
**Artifact:** validated `SKILL.md` file and any supporting structure changes
**Evidence:** clearer trigger logic, stronger boundaries, and improved operating contract
**Decision:** skill approved, rejected, or needs further refactor
**Next:** monitor trigger accuracy and quality after use
