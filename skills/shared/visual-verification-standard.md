# Visual Verification Standard

Use this standard when page appearance, layout, or UI behavior matters.

## Required workflow
1. Capture baseline desktop screenshot
2. Capture baseline mobile screenshot
3. If mobile/desktop overflow or broken layout is suspected, run overflow diagnostics
4. Make the smallest structural fix first
5. Capture post-change desktop screenshot
6. Capture post-change mobile screenshot
7. Review console errors if present
8. Do not claim success unless rendered output supports the claim

## Principles
- Rendered output beats source assumptions
- Fix containers/shells before stacking one-off overrides
- Heavy custom pages often require viewport screenshots first, not full-page capture
- If a page keeps fighting patches, prefer a controlled shell rebuild over endless micro-fixes
