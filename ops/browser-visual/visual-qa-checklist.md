# Visual QA Checklist

Use this for any page styling, layout, or mobile/desktop UI change.

## Before edits
- [ ] Capture desktop screenshot
- [ ] Capture mobile screenshot
- [ ] Run overflow diagnostic on mobile if layout looks suspect
- [ ] Inspect target selector/content if the problem is ambiguous

## During edits
- [ ] Make the smallest structural fix first
- [ ] Prefer shell/container fixes over random one-off overrides
- [ ] Avoid blind full rewrites unless the page shell is structurally broken
- [ ] Keep a rollback backup before major page-level edits

## After edits
- [ ] Capture desktop screenshot again
- [ ] Capture mobile screenshot again
- [ ] Re-run overflow diagnostic on mobile for fragile pages
- [ ] Check console logs for errors
- [ ] Confirm the changed area actually improved rather than merely changed

## Standard
Do not claim visual success unless the rendered screenshots support it.
