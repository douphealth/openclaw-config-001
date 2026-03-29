# Repo Adoption Checklist

Use this before importing ideas, files, scripts, or workflows from external repos.

## Fit Check
- [ ] Does this solve a real problem in this workspace?
- [ ] Does OpenClaw already provide this natively?
- [ ] Is this pattern better than the current local pattern?
- [ ] Can it be adapted locally without dragging in foreign assumptions?

## Quality Check
- [ ] Is the source repo mature enough to trust selectively?
- [ ] Is the imported idea operationally precise rather than just well-marketed?
- [ ] Can the import be verified after implementation?
- [ ] Can it be maintained by future runs without hidden context?

## Placement Check
- [ ] Do I know exactly where this belongs in the workspace?
- [ ] Does it belong in `skills/`, `ops/`, `memory/`, or not at all?
- [ ] Will it duplicate an existing local artifact?

## Execution Check
- [ ] Am I importing only the smallest high-leverage piece?
- [ ] Do I have a rollback path if the adaptation is poor?
- [ ] Have I documented what was borrowed and why?

## Red Flags
- [ ] host-specific plugin mechanics
- [ ] slash-command bloat
- [ ] UI/dashboard-first adoption without operator need
- [ ] duplicate orchestration or memory systems
- [ ] copying structure just because it looks sophisticated
