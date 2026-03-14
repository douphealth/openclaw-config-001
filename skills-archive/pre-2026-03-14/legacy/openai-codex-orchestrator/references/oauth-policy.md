# OAuth Policy

## Token lifecycle
- Prefer proactive refresh at 80% token life or 300s before expiry.
- Max refresh retries: 3 with exponential backoff.
- On refresh failure: use valid cached token; fallback to API key; otherwise halt.

## Session startup check
1. load credentials
2. check token expiry/refresh threshold
3. verify access via lightweight models endpoint
4. confirm org/project routing (if configured)
5. capture rate-limit headers if present
