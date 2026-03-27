# Page-Safe Rewrite Protocol

Use this when a page is too structurally fragile for more micro-patches.

## Trigger conditions
Escalate from patching to controlled rewrite when one or more are true:
- repeated mobile/desktop breakage persists after 2-3 targeted fixes
- page contains leaked CSS/HTML or brittle monolithic inline styling
- page shell is inconsistent enough that local fixes create new regressions
- screenshots keep contradicting source-level expectations

## Rewrite goal
Preserve content substance while rebuilding the presentation layer cleanly.

## Safe rewrite process
1. Capture full backup of the page/post before changes
2. Capture baseline desktop and mobile screenshots
3. Identify what must be preserved:
   - title/H1
   - core sections
   - affiliate links
   - structured data if valid
   - comparison tables / key product blocks
4. Replace the shell, not the editorial substance, unless content itself is poor
5. Use one coherent container/spacing/card/table system
6. Re-test desktop and mobile screenshots after rewrite
7. Only claim success after rendered output is stable

## Anti-patterns
- endless one-off CSS overrides
- mixing multiple contradictory card systems in one page
- patching around leaked CSS instead of fixing the shell
- claiming “fixed” after source cleanup without screenshot proof
