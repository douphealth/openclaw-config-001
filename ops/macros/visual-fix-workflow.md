# Visual Fix Workflow Macro

Use this macro for page styling, layout breakage, mobile overflow, desktop inconsistencies, and visual QA tasks.

## Steps
1. Capture baseline desktop screenshot
2. Capture baseline mobile screenshot
3. Run mobile overflow diagnostic if layout is broken or exceeds viewport
4. Inspect target selector/content if the broken area is ambiguous
5. Make the smallest structural fix first
6. Re-capture desktop screenshot
7. Re-capture mobile screenshot
8. Compare rendered output before claiming success
9. If the page remains structurally unstable after 2-3 targeted fixes, escalate to a controlled shell rewrite

## Commands
```bash
bash /home/openclaw/.openclaw/workspace/ops/browser-visual/capture_pair.sh "https://example.com/"
```

```bash
bash /home/openclaw/.openclaw/workspace/ops/browser-visual/diagnose_mobile.sh "https://example.com/"
```

## Rules
- Do not trust source-only assumptions when screenshots disagree
- Prefer shell/container fixes before one-off element overrides
- Use full-page screenshots only when truly needed
- Keep backups before major article/page shell changes
