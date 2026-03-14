# skills-approved

Production-curated OpenClaw skill set. Only these skills are active for routing.

## Active skills

| Skill | Role | Status |
|-------|------|--------|
| openai-codex-orchestrator | orchestrator | active |
| blog-master | content-orchestrator | active |
| wordpress | cms-executor | active |
| seo-research-master | research | active |
| technical-seo-checker | audit | active |
| keyword-intelligence-os | keyword-intel | active |
| wp-reliability-ops | reliability | active |
| git-sync | repo-sync | active |
| grounding-compliance-os | compliance | active |
| automation-ops | automation | active |

## Rules
- Only skills listed in MANIFEST.yaml are production-active
- Every skill must have a SKILL.md
- No secrets in any skill file
- Run `make validate` before releasing
- Archive before deleting any skill

## Adding a new skill
1. Add skill folder here with SKILL.md
2. Add entry to MANIFEST.yaml
3. Run `make validate`
4. Commit and push

## Removing a skill
1. Move to skills-archive/ first
2. Remove from MANIFEST.yaml
3. Run `make validate`
4. Commit and push
