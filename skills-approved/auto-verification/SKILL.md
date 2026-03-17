---
name: auto-verification
description: Use after any skill completes work to verify the output is real, correct, and complete. Triggers automatically when a skill claims "done", "fixed", "published", "working", or "complete" and proof is possible.
---

# Auto-Verification

## Purpose
Provide a mandatory proof layer that checks whether a claimed outcome is actually real, user-visible, and complete before accepting completion.

## Use this when
- ANY skill claims work is done, fixed, published, working, or complete
- before declaring a fix worked
- before confirming a deployment went live
- before accepting that a configuration change applied
- before reporting success on a user-visible outcome when proof is possible

## Do NOT use this for
- tasks where verification is impossible or inherently subjective
- quick Q&A that has no artifact or outcome to prove
- research/planning tasks that do not claim implementation

## Verification order
Prefer this order when possible:
1. **User-visible outcome** — what the user would actually experience
2. **Functional behavior** — whether the thing works end-to-end
3. **Underlying state** — config, files, API state, logs
4. **Secondary signals** — status codes, timestamps, background logs

Do not stop at a lower layer if a higher layer is testable.

## Do this

### 1. Detect the claim
Identify exactly what was claimed:
- published
- fixed
- configured
- created
- deleted
- connected
- delivered
- validated

### 2. Choose the strongest proof method
| Claim | Verification Method |
|---|---|
| Page published | Fetch/render URL and confirm expected content appears |
| UI fixed | Reproduce the user-visible path and confirm behavior |
| Email sent | Check provider history/logs and delivery evidence |
| API working | Make a real test call and validate the response |
| Tracking fixed | Confirm real-time or test events fire correctly |
| Schema added | Validate the schema output, not just the source file |
| Config changed | Read config and test the behavior it should change |
| File created | Read file and confirm its contents are correct |
| File deleted | Confirm absence at the source of truth |

### 3. Produce a pass/fail report
Use this structure:
```
CLAIM: [what was claimed]
METHOD: [how verified]
RESULT: ✅ PASS / ❌ FAIL / ⚠️ PARTIAL
EVIDENCE: [proof]
GAP: [what remains unproven]
ACTION: [if fail/partial: exact next fix]
```

### 4. Handle failures
If verification fails:
1. report the specific failure
2. attempt an obvious fix if the method is clear and low risk
3. re-verify
4. if still failing after 2 attempts, escalate with exact blocker details

## Failure taxonomy
Classify failures when helpful:
- **false completion** — claim does not match reality
- **partial completion** — some but not all outcomes are real
- **wrong artifact** — something was produced, but not the requested thing
- **state-only success** — internals changed, but user-visible outcome is still broken
- **verification blocked** — proof may exist, but access or tooling prevented confirmation

## Rules
- NEVER accept “done” without proof when proof is possible.
- ALWAYS check the actual output, not just the status code.
- Prefer user-visible proof over internal proof.
- If verification is impossible, say exactly why.
- Track false completion patterns; they indicate skill quality problems.

## Output contract
**Artifact:** verification report with pass/fail/partial result for each claim
**Evidence:** actual proof data such as rendered content, API response, file contents, logs, or functional test result
**Decision:** accept completion or require rework
**Next:** if failed or partial, exact fix instructions
