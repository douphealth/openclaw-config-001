# Macro — Memory Health Check

## Use When
- Semantic memory was recently enabled or changed
- Recall quality feels weak
- Daily/entity memory may be drifting
- Fast pass/fail view of memory system quality needed

## Goal
Detect technical and content-layer memory problems before they degrade recall.

## Sequence
1. Run `openclaw memory status --agent main --json`
2. Check memory search is enabled, provider healthy, files/chunks non-zero
3. Check session memory included when expected
4. Inspect memory structure for stale or missing entity files
5. Look for duplicate/stale truths in recent daily notes
6. Decide fix: technical (index/config), structural (entity files), or maintenance (review/consolidation)

## Pass/Fail Checklist
- [ ] Semantic memory enabled
- [ ] Embedding backend healthy
- [ ] Indexed files/chunks present
- [ ] Session memory present when expected
- [ ] Entity memory present for active subjects
- [ ] No obvious daily-note duplication drift
- [ ] Long-term memory not acting like a dump

## Output Format
- **Overall status**: healthy / degraded / blocked
- **Technical findings**: _what's wrong with the system_
- **Structure findings**: _what's missing in entity files_
- **Drift findings**: _what's duplicated or stale_
- **Recommended fix**: _specific next action_
