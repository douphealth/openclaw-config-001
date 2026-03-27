# Workspace Optimization Notes — 2026-03-27

## Improvements Added
- Added `browser-visual-ops` skill for real browser automation and screenshot-based visual verification
- Added local Playwright helper under `ops/browser-visual/`
- Tuned browser helper for this environment:
  - use `domcontentloaded` + `load` + settle delay
  - disable animations during capture
  - viewport screenshots by default
  - full-page only when explicitly needed
- Updated `skill-router` so visual/browser/screenshot tasks route to `browser-visual-ops`
- Updated `TOOLS.md` with the proven visual verification workflow
- Updated `AGENTS.md` so UI/layout work requires visual verification when tooling exists

## Lessons Learned
- Source-level checks are not enough for fragile custom pages
- Screenshot evidence must override optimistic HTML assumptions
- Cloudflare challenge can still allow Playwright-based capture in this environment
- Heavy custom pages often fail under `networkidle`; safer load strategy is required
- Mobile overflow bugs usually require shell-level constraints, not just card-level tweaks

## Recommended Next Workspace Upgrades
1. Add a small wrapper command for paired desktop+mobile capture in one call ✅
2. Add a DOM width/overflow diagnostic mode to the browser helper ✅
3. Add a backup script + scheduled job for critical workspace files ✅ script created, cron-ready README added, schedule still pending actual installation
4. Add a visual QA checklist reference for page-change tasks ✅
5. Add a post-edit screenshot diff workflow if image diff tooling is installed later
6. Add workflow-level visual-fix macro ✅
7. Add page-safe rewrite protocol ✅
8. Add activation-layer visual trigger addendum ✅
9. Add money-page optimization standard ✅
10. Upgrade orchestration rules to require post-keyword competitive blueprints ✅
11. Add unified page-operations standard ✅
