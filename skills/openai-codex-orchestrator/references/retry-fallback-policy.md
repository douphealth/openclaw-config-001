# Retry/Fallback Policy

Transient errors (429/5xx):
- attempt1: immediate
- attempt2: +1.5s
- attempt3: +3.0s
Then fallback model or local heuristic.
