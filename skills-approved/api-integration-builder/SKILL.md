---
name: api-integration-builder
description: Use when connecting external APIs, building webhook handlers, setting up OAuth flows, creating API wrappers, or integrating third-party services into OpenClaw workflows.
---

# API Integration Builder

## Purpose
Rapidly build reliable API integrations for OpenClaw workflows with proper auth, error handling, and rate limiting.

## Use this when
- Connecting to external REST or GraphQL APIs
- Building webhook receivers or handlers
- Setting up OAuth2 flows for third-party services
- Creating API wrappers that other skills can call
- Debugging failed API calls

**Do NOT use this skill for:** WordPress REST API work (→ `wordpress-growth-ops`), email API setup and delivery pipelines (→ `email-marketing-engine`), or general debugging and technical documentation (→ `technical-writing`).

## Do this

### 1. Identify the integration type
| Type | Pattern | When |
|------|---------|------|
| REST | `curl`/`fetch` with JSON | Most CRUD APIs |
| GraphQL | POST with query string | Schema-driven APIs |
| Webhook | HTTP server or OpenClaw hook | Event-driven |
| OAuth2 | Browser flow + token storage | User-authed APIs |

### 2. Authentication setup
- **API key**: Store in `.secrets/<service>.env`, load with `source`, never hardcode.
- **OAuth2**: Use `scripts/check-api.sh` to verify token; refresh if 401.
- **JWT**: Decode with `python3 -c "import jwt; ..."`, check expiry before requests.

### 3. Build the request
For REST (bash):
```bash
curl -s -w "\n%{http_code}" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  "$ENDPOINT"
```

For Python:
```python
import requests
r = requests.get(url, headers={"Authorization": f"Bearer {key}"}, timeout=30)
r.raise_for_status()
```

### 4. Handle errors
- Retry on 429 (rate limit) with `Retry-After` header.
- Retry on 5xx up to 3 times with exponential backoff.
- Log 4xx errors with request body for debugging.
- Never retry 401/403 — fix auth first.

### 5. Rate limiting
- Check `X-RateLimit-Remaining` / `Retry-After` headers.
- For bulk operations, add 100–200ms delay between requests.
- Use `scripts/check-api.sh` to probe rate limits before bulk runs.

### 6. Document the integration
Create a `references/<service>-api.md` with:
- Base URL and version
- Auth method and token location
- Key endpoints used
- Rate limit details
- Error code meanings

## Resources
- `scripts/check-api.sh` — Test endpoint auth, status, rate limits
- `references/` — Per-service API docs you create

## Checks / common mistakes
- Forgetting to source `.env` before curl commands
- Not handling 429 — causes silent data loss
- Hardcoding secrets in SKILL.md or scripts
- Assuming all APIs return JSON — check Content-Type
- Missing timeout on requests — causes hangs

## Output contract
Working integration script or code block + `references/<service>-api.md` documenting the integration.

## Output Contract
**Artifact**: Skill-specific deliverable (report, fix, config, or document)
**Evidence**: Proof that the work was completed correctly
**Decision**: What was decided or recommended
**Next**: Follow-up action or monitoring period
