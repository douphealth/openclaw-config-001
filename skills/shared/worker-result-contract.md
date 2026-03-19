# Worker Result Contract

Every parallel worker should return results in a structured format so the director can synthesize outputs cleanly.

## Required Fields
```json
{
  "worker": "worker-name-or-id",
  "task_type": "audit|research|implementation|verification|synthesis",
  "target": "what this worker owned",
  "status": "SUCCESS|FAILED|PARTIAL",
  "summary": "one-sentence outcome",
  "evidence": ["key fact 1", "key fact 2"],
  "changes": ["change 1", "change 2"],
  "blockers": ["blocker 1"],
  "metrics": {
    "items_checked": 0,
    "items_changed": 0,
    "errors": 0
  },
  "next_recommendation": "what should happen next"
}
```

## Rules
- `summary` must be concise and factual
- `evidence` should contain decisive facts, not vague claims
- `status=FAILED` must include at least one blocker
- `status=PARTIAL` must explain what completed vs what did not
- `metrics` should be filled whenever batch work occurs

## Short Text Fallback
If strict JSON is impossible, use this text structure:

```text
STATUS: SUCCESS
WORKER: metadata-audit-1
TARGET: 25 URLs from /post-sitemap.xml
SUMMARY: audited 25 URLs and found 9 title/meta/H1 issues
EVIDENCE:
- 4 URLs had 2 H1s
- 3 URLs had missing meta descriptions
- 2 URLs had overlong titles
CHANGES:
- none (audit only)
BLOCKERS:
- none
NEXT: pass findings to implementation wave
```
