# Changelog

## v3 (2026-03-14)

### Added (8 new skills)
- `api-integration-builder` — REST/GraphQL API integration patterns
- `auto-verification` — Automatic completion claim verification
- `infrastructure-ops` — Server/DevOps operations
- `monitoring-ops` — Uptime, logs, performance monitoring
- `notification-engine` — Alert routing (Telegram, email, webhooks)
- `quality-scorecard` — Skill quality scoring (0-100)
- `skill-router` — Master task routing guide
- `test-automation-ops` — Site testing and QA automation
- `workflow-macros` — 5 pre-built multi-skill pipelines

### Upgraded (all skills)
- Added `## Do NOT Use This For` boundary sections to all 36 skills
- Added `## Output Contract` sections to all 36 skills
- Added cross-references (→) to 23 skills
- Extracted Python scripts to `scripts/` in 7 skills
- Added detailed patterns to `references/` in 26 skills

### Archived
- 10 v2 skills from `skills-approved/` → `skills-archive/pre-2026-03-14/approved/`
- 64 legacy skills from `skills/` → `skills-archive/pre-2026-03-14/legacy/`

### Quality Standards
- Every skill must have `## Do NOT Use This For` boundary section
- Every skill must have `## Output Contract` section
- MANIFEST.yaml upgraded to v3 with category organization

## v2 (2026-03-06)

### Initial Production Curation
- 10 skills approved for production use
- MANIFEST.yaml v2 with role assignments
- skills-approved/ and skills-archive/ structure
- Makefile with validate, backup, release, health targets
