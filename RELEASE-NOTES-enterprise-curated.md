# Enterprise Curated Release Notes

Date: 2026-03-01
Branch: `enterprise-curated`
Base sync commit: `74d8a5d`
Curated commit: `ed05f64`

## What’s included
- Latest OpenClaw enterprise skill stack synced from active workspace
- Master orchestration/autonomy controls and memory automation utilities
- SEO, WordPress, Email, and review quality systems with stronger QA gates

## Curated cleanup
Removed non-essential repository noise from imported third-party skills:
- README/changelog/contributing/test/CI/dev-only artifacts where not required for runtime skill execution
- kept required runtime files (`SKILL.md`, `scripts/`, `references/`, `assets/`)

## Rollout commands
```bash
cd openclaw-config

git checkout main
git pull

git checkout enterprise-curated
git pull

# push from your authenticated environment
git push origin main
git push origin enterprise-curated
```

## Optional: fast deploy branch selection
Use `enterprise-curated` for lean production skill deployments.
Use `main` when you want full-fidelity upstream extras included.
