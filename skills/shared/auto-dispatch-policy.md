# Auto-Dispatch Policy

Decision policy for when OpenClaw should stay local, ask for clarity, parallelize, or switch into recovery mode.

## 1. Ask a clarifying question first when:
- the requested outcome is ambiguous
- the scope is unclear
- the success condition is unknown
- multiple materially different strategies exist
- the user’s constraints are missing and matter to risk

## 2. Stay single-threaded when:
- the task is tiny and obvious
- writes affect one object only
- the environment is unstable
- correctness matters more than speed and no independent subtask exists

## 3. Use parallel workers when:
- subtasks are genuinely independent
- audits can be chunked safely
- research and verification can run in parallel
- multiple sites or multiple URL clusters can be separated cleanly

## 4. Use batch mutation control when:
- >10 items may be modified
- changes are similar across many records
- rollback matters
- site health could degrade under volume

## 5. Enter failure-recovery mode when:
- repeated transport or save failures occur
- state becomes inconsistent across items
- content becomes duplicated or malformed
- infrastructure health degrades during execution
- evidence is contradictory or unstable

## 6. Default escalation order
1. clarify
2. brief
3. specialist skill or director
4. canary / audit / first wave
5. verify
6. continue or recover

## 7. Parallel safety rules
- never dispatch overlapping writes to the same object set
- one worker owns one deliverable
- audit first, mutate second on unstable systems
- if >20% workers fail, stop and diagnose

## 8. Completion rule
Do not claim complete until:
- the requested business outcome is addressed
- the chosen strategy proved appropriate
- evidence exists from live reality, not just save responses
