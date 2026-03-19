# Recovery Playbook Pack

Reusable playbooks for unstable systems, partial failures, and corrupted content states.

## Playbook 1 — Unstable Site During Batch Operations

### Trigger
- repeated timeouts
- intermittent 200/000/524 responses
- batch scripts hanging or failing unpredictably

### Response
1. stop active destructive waves
2. switch to read-only audit mode
3. health check target every 30s
4. reduce concurrency to 1-2 workers
5. process only canary items until stability returns

### Stop Conditions
- 3 consecutive transport failures
- site health below acceptable threshold for >2 checks
- inconsistent API state on same object across retries

## Playbook 2 — Duplicate Content / Duplicate Module Cleanup

### Trigger
- repeated “Related Posts” sections
- duplicate embeds, tables, FAQ blocks
- multiple injected modules after repeated save operations

### Response
1. back up all affected records
2. identify raw-content duplication vs render-time injection
3. remove saved duplicate blocks first
4. verify live page after each canary repair
5. batch the cleanup in small waves

### Verification
- count duplicate markers in raw content
- count visible duplicates on live page
- ensure H1 count remains correct
- ensure canonical/title/meta still present

## Playbook 3 — Partial Save / Batch Corruption

### Trigger
- some records updated, others failed
- mixed old/new states
- unclear scope of damage

### Response
1. snapshot affected IDs
2. classify: rollback vs forward-fix
3. canary-repair one item
4. continue in small verified waves
5. maintain before/after log for each record

## Playbook 4 — Broken Render Structure

### Trigger
- full HTML document pasted into body content
- embedded `<article><header><h1>` wrappers inside post body
- multiple H1s / malformed layout / theme conflict

### Response
1. extract body-level content only
2. remove duplicate structural wrappers
3. preserve semantic content and key media
4. verify 1 H1 on live page
5. verify no stray doctype/head/body inside content

## Playbook 5 — Rollback-Led Recovery

### Trigger
- recent changes are clearly net harmful
- clean backups exist
- forward-fix would be slower or riskier

### Response
1. identify last-known-good backup
2. restore 1 canary item
3. verify live
4. restore in controlled waves
5. compare with current state before finalizing
