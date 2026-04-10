# openclaw-config-001

Production-curated OpenClaw configuration and skill repository.

## Purpose
This repository is the non-secret source of truth for:
- approved OpenClaw skills in `skills-approved/`
- runtime configuration templates
- operations and recovery runbooks
- release bundles and validation scripts
- implementation, upgrade, and memory-operation documentation

## Fast paths
- Validate: `make validate`
- Backup: `make backup`
- Release: `make release`
- Health: `make health`
- Restore dry run: `make restore-dry-run`

## Repo contract
- Secrets are never committed.
- `MANIFEST.yaml` defines the production-approved skill set.
- `skills-approved/` is the curated approval layer.
- `skills-archive/` contains previous versions.
- Every release should generate a checksum.

## Core files
- `RECOVERY.md`
- `SECURITY.md`
- `MANIFEST.yaml`
- `CHANGELOG.md`
- `docs/memory-operations.md`

## Skill Architecture
Approved skills are hardened with enterprise standards:
- **Boundaries**: skills declare what they should NOT be used for
- **Output Contracts**: skills define what done means
- **Concrete Examples**: skills should include before/after or applied scenarios when valuable
- **Cross-references**: skills point to related skills for handoffs
- **Scripts**: some skills extract repeatable logic into scripts
- **References**: some skills include detailed reference patterns and checklists
- **Verification Hooks**: skills should include explicit proof expectations

### Key infrastructure skills
- `skill-router` — master routing guide
- `workflow-macros` — pre-built multi-skill pipelines
- `auto-verification` — catches false completion claims with proof
- `quality-scorecard` — tracks skill quality over time
- `swarm-orchestrator` — director/worker/verifier patterns

## OpenClaw runtime assumptions
- Config path: `~/.openclaw/openclaw.json`
- Install / daemon bootstrap: `openclaw onboard --install-daemon`
- Health checks: `openclaw gateway status`, `openclaw doctor`

## Workspace Configuration
Enterprise-grade config files live in `config/`:
- `AGENTS.md` — root operating instructions
- `SOUL.md` — agent personality and values
- `USER.md` — user profile template
- `TOOLS.md` — infrastructure cheat sheet template
- `IDENTITY.md` — agent identity template
- `MEMORY.md` — long-term memory template
- `HEARTBEAT.md` — periodic check instructions

Quick setup:
- `bash config/scripts/setup-workspace.sh`

See `config/README.md` for full documentation.

## Notes
- Treat `skills-approved/` as the current production-curated surface.
- Keep repo descriptions count-agnostic unless counts are generated automatically.
- Run `make validate` before release or push.

## Version History
- **v3.2** (2026-03-17): Skill hardening pass with concrete examples, verification hooks, and reference files.
- **v3.1** (2026-03-16): Enterprise-grade workspace configuration templates and setup scripts.
- **v3** (2026-03-14): Major upgrade from thin skills to enterprise-grade routing, verification, and workflow layers.
- **v2** (2026-03-06): Initial production curation.
