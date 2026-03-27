# Browser Visual Ops

Local Playwright-based browser verification helper for OpenClaw workspace tasks.

## Purpose
Use this for:
- desktop/mobile screenshots
- DOM inspection
- visual verification after page changes
- catching layout bugs that raw HTML inspection misses

## Commands
From `/home/openclaw/.openclaw/workspace/ops/browser-visual`:

### Desktop screenshot
```bash
node browser_ops.js screenshot --url https://example.com/ --device desktop
```

### Mobile screenshot
```bash
node browser_ops.js screenshot --url https://example.com/ --device mobile
```

### Full-page screenshot
```bash
node browser_ops.js screenshot --url https://example.com/ --device desktop --fullPage true
```

### DOM inspect
```bash
node browser_ops.js inspect --url https://example.com/ --selector 'h1'
```

### Overflow diagnostic
```bash
node browser_ops.js overflow --url https://example.com/ --device mobile
```

### PDF
```bash
node browser_ops.js pdf --url https://example.com/
```

## Artifact location
Artifacts are written under:
`ops/browser-visual/artifacts/<timestamp>/`

## Environment Notes
- tuned to avoid fragile `networkidle`
- uses animation suppression for more stable captures
- viewport screenshots are the safe default for heavy custom pages
- if Chromium system libraries are missing on a new host, run:
```bash
sudo npx playwright install-deps chromium
```

## Standard for visual work
For page styling/mobile issues:
1. capture baseline screenshots
2. edit surgically
3. capture desktop + mobile after changes
4. trust screenshots over source assumptions
