# openclaw-config-001

Production control plane for the OpenClaw VPS.

## Purpose
This repository is the non-secret source of truth for:
- **36 approved OpenClaw skills** (enterprise-grade)
- Runtime configuration templates
- Operations and recovery runbooks
- Release bundles and validation scripts

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

## Skill Architecture (v3)
All 36 skills follow enterprise standards:
- **Boundaries**: Every skill declares what it should NOT be used for
- **Output Contracts**: Every skill defines what "done" means (artifact, evidence, decision, next)
- **Cross-references**: Skills point to related skills for seamless handoffs
- **Scripts**: 7 skills have extracted Python scripts for repeatable work
- **References**: 26 skills have detailed reference patterns

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

## Version History
- **v3** (2026-03-14): Major upgrade — 10 thin skills → 36 enterprise-grade with boundaries, output contracts, cross-references, workflow macros, quality scoring, auto-verification
- **v2** (2026-03-06): Initial production curation — 10 skills in skills-approved/
