---
name: auto-verification
description: Use after any skill completes its work to verify the output is real, correct, and complete. Triggers automatically when a skill claims "done", "fixed", "published", "working", or "complete". Catches fake completion, partial work, and unverified claims.
---

# Auto-Verification

## Purpose
Automatic verification layer that proves skill outputs are real before accepting completion claims.

## Use this when
- ANY skill claims work is "done" or "complete"
- Before declaring a fix worked
- Before confirming a deployment went live
- Before accepting that a configuration change applied

## Do NOT use this for
- Tasks where verification is impossible (research, planning)
- Quick Q&A that doesn't need proof

## Do this

### 1. Claim Detection
When a skill or worker claims completion, identify what needs verification:
- "Published" → Check page is live and renders
- "Fixed" → Verify fix actually applied
- "Configured" → Test the configuration works
- "Created" → Verify artifact exists and is correct
- "Deleted" → Confirm it's actually gone

### 2. Verification Methods
| Claim | Verification Method |
|-------|-------------------|
| Page published | Fetch URL, check content renders |
| Email sent | Check email history/logs |
| API working | Make test call, verify response |
| Tracking fixed | Check real-time events fire |
| Schema added | Validate with schema validator |
| Config changed | Read config, confirm values |
| File created | Read file, confirm contents |

### 3. Pass/Fail Report
```
CLAIM: [what was claimed]
METHOD: [how verified]
RESULT: ✅ PASS / ❌ FAIL
EVIDENCE: [proof]
ACTION: [if fail: what to fix]
```

### 4. Auto-Retry Logic
If verification fails:
1. Report the specific failure
2. Attempt to fix if fix is obvious
3. Re-verify
4. If still failing after 2 attempts, escalate to user

## Output Contract
**Artifact**: Verification report with pass/fail for each claim
**Evidence**: Actual data proving the claim (URL content, API response, file contents)
**Decision**: Accept completion or require rework
**Next**: If failed, specific fix instructions

## Rules
- NEVER accept "done" without proof when proof is possible
- ALWAYS check the actual output, not just the status code
- If verification is impossible, note it explicitly
- Track false completion claims — they indicate skill quality issues
