# openclaw-config-001

Production control plane for the OpenClaw VPS.

## Purpose
This repository is the non-secret source of truth for:
- **36 approved OpenClaw skills** (enterprise-grade)
- Runtime configuration templates
- Operations and recovery runbooks
- Release bundles and validation scripts
- Approved frontend premium delivery cluster documentation (`docs/frontend-cluster.md`)

## Fast paths
- Validate: `make validate`
- Backup: `make backup`
- Release: `make release`
- Health: `make health`
- Restore dry run: `make restore-dry-run`

## Repo contract
- Secrets are never committed.
- `MANIFEST.yaml` defines the production-approved skill set.
- `skills-approved/` is the curated approval layer (36 skills).
- `skills-archive/` contains previous versions.
- Every release generates a checksum.

## Core files
- `RECOVERY.md`
- `SECURITY.md`
- `MANIFEST.yaml`
- `CHANGELOG.md`
- `docs/memory-operations.md`

## Skill Architecture (v3.2)
All 36 skills hardened with enterprise standards:
- **Boundaries**: Every skill declares what it should NOT be used for
- **Output Contracts**: Every skill defines what "done" means (artifact, evidence, decision, next)
- **Concrete Examples**: Every skill includes real-world before/after scenarios
- **Cross-references**: Skills point to related skills for seamless handoffs
- **Scripts**: 7 skills have extracted Python scripts for repeatable work
- **References**: 30 skills have detailed reference patterns, checklists, and templates
- **Verification Hooks**: All skills include explicit proof expectations

### Key Infrastructure Skills
- `skill-router` — Master routing guide (any task → optimal skill)
- `workflow-macros` — 5 pre-built multi-skill pipelines
- `auto-verification` — Catches false "done" claims with proof
- `quality-scorecard` — Tracks skill quality over time
- `swarm-orchestrator` — Director/worker/verifier multi-agent patterns

## OpenClaw runtime assumptions
- Config path: `~/.openclaw/openclaw.json`
- Install / daemon bootstrap: `openclaw onboard --install-daemon`
- Health checks: `openclaw gateway status`, `openclaw doctor`



## Workspace Configuration

Enterprise-grade config files in `config/`:
- `AGENTS.md` — Root operating instructions (269 lines)
- `SOUL.md` — Agent personality and values
- `USER.md` — User profile template
- `TOOLS.md` — Infrastructure cheat sheet template
- `IDENTITY.md` — Agent identity template
- `MEMORY.md` — Long-term memory template
- `HEARTBEAT.md` — Periodic check instructions

Quick setup: `bash config/scripts/setup-workspace.sh`

See `config/README.md` for full documentation.
## Version History
- **v3.2** (2026-03-17): Skill hardening pass — added concrete examples, verification hooks, and reference files to all 36 skills. Enabled memory search. Net -830 lines with higher quality. 6 new reference files added.
- **v3.1** (2026-03-16): Enterprise-grade workspace configuration — config templates, setup scripts
- **v3** (2026-03-14): Major upgrade — 10 thin skills → 36 enterprise-grade with boundaries, output contracts, cross-references, workflow macros, quality scoring, auto-verification
- **v2** (2026-03-06): Initial production curation — 10 skills in skills-approved/
h boundaries, output contracts, cross-references, workflow macros, quality scoring, auto-verification
- **v2** (2026-03-06): Initial production curation — 10 skills in skills-approved/
