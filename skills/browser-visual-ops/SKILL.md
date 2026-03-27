---
name: browser-visual-ops
description: Browser automation and visual verification for web pages using Playwright in the workspace. Triggers on screenshot, visual QA, browser automation, inspect DOM, click/type, navigate, console errors, mobile/desktop screenshots, PDF capture, or canvas snapshot requests.
---

# Browser Visual Ops — Playwright Browser Automation

## Purpose
Use a real browser runtime to open pages, inspect DOM, click/type, navigate, capture screenshots/PDFs, check console errors, and produce visual proof artifacts for page changes.

## When to Use
- User asks for screenshots or visual verification
- Need mobile and desktop page QA
- Need to inspect rendered DOM/state after changes
- Need to click/type through a UI flow
- Need console/network/browser-level debugging
- Need PDF or screenshot artifacts

## Do NOT Use For
- Pure REST/API content edits with no visual risk
- Blind design claims without first running this skill
- Site changes where browser setup is unavailable and user only asked for text updates

## Do This
1. Verify target URL is reachable
2. Ensure Playwright runtime exists in `ops/browser-visual/`
3. Use the helper script `ops/browser-visual/browser_ops.js`
4. Capture desktop and mobile screenshots for visual changes
5. Run mobile overflow diagnostics when layout/viewport breakage is suspected
6. Inspect DOM selectors or text before editing when layout risk exists
7. Save artifacts under `ops/browser-visual/artifacts/`
8. Report with artifact paths and any console errors

## Core Rules
- Never claim visual QA without actual artifacts
- For risky visual edits, capture before/after when possible
- Prefer desktop + mobile screenshots together
- Log console errors if found
- Keep one run = one artifact folder with timestamp
- Use safe viewport defaults unless task needs custom sizing
- If screenshots keep showing regressions after 2-3 targeted fixes, escalate to `skills/shared/page-safe-rewrite-protocol.md`

## Self-Correction Loop
After a visual fix pass, ask:
1. Did screenshots actually improve, or did I just change the page?
2. Did source-level assumptions conflict with rendered output?
3. Is the current page still fragile enough to justify a shell rewrite?
4. Did overflow diagnostics point to a shell problem instead of a local element problem?
5. What visual debugging pattern should be reused next time?

## Helper Commands
- Install runtime: `cd ops/browser-visual && npm install && npx playwright install chromium`
- Install Linux deps on host: `cd ops/browser-visual && sudo npx playwright install-deps chromium`
- Screenshot desktop: `node ops/browser-visual/browser_ops.js screenshot --url https://example.com --device desktop`
- Screenshot mobile: `node ops/browser-visual/browser_ops.js screenshot --url https://example.com --device mobile`
- Full-page screenshot if needed: `node ops/browser-visual/browser_ops.js screenshot --url https://example.com --device desktop --fullPage true`
- DOM inspect: `node ops/browser-visual/browser_ops.js inspect --url https://example.com --selector 'h1'`
- Overflow diagnostic: `node ops/browser-visual/browser_ops.js overflow --url https://example.com --device mobile`
- Paired capture helper: `bash ops/browser-visual/capture_pair.sh "https://example.com"`
- Mobile diagnose helper: `bash ops/browser-visual/diagnose_mobile.sh "https://example.com"`
- PDF: `node ops/browser-visual/browser_ops.js pdf --url https://example.com`

## Proven Notes
- Uses Playwright Chromium from `ops/browser-visual/`
- Uses `domcontentloaded` + `load` + settle delay instead of fragile `networkidle`
- Disables animations during capture for more stable screenshots
- Defaults to viewport screenshots because some heavy custom pages time out on full-page capture
- Cloudflare JS challenge can complete successfully during capture on GearUpToFit from this runtime

## Use This Skill For
- pre-change screenshot baseline
- post-change desktop/mobile proof
- catching layout breakage that source inspection misses
- checking article shells, homepage sections, cards, tables, and overflow issues

## Output Contract
**Artifact**: screenshots/PDF/DOM dump in `ops/browser-visual/artifacts/`
**Evidence**: artifact paths + console error summary
**Decision**: pass/fail on visual verification
**Next**: exact page changes if required
