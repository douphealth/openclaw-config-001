# Health Check Workflow

## Quick sequence
1. run `openclaw memory status --agent main --json`
2. confirm enabled backend + provider health
3. confirm indexed files/chunks are non-zero after initial indexing
4. confirm active subjects have entity files
5. inspect recent daily files for repeated blockers or stale contradictions
6. classify problem as technical, structural, or maintenance

## Rule
Do not blame retrieval quality on embeddings alone when the real problem is stale or duplicated memory files.
