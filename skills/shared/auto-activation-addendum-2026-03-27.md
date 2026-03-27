# Auto Activation Addendum — 2026-03-27

## Visual task triggers
When user language includes any of the following, strongly prefer activating `browser-visual-ops`:
- screenshot
- mobile view
- desktop view
- visually broken
- looks ugly
- out of bounds
- overflow
- distorted
- fix the UI
- inspect DOM
- visual proof

## Fragile page triggers
When a request involves a known fragile/custom page and visual breakage:
1. backup first
2. baseline screenshots
3. smallest structural fix
4. post-change screenshots
5. escalate to page-safe rewrite if repeated regressions continue

## Claim standard
Do not claim visual success from source inspection alone if browser tooling is available.
