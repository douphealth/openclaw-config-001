---
name: api-integration-builder
description: Use when connecting external APIs, building webhook handlers, setting up OAuth flows, creating API wrappers, or integrating third-party services into OpenClaw workflows with reliable auth, error handling, and verification.
---

# API Integration Builder

## Purpose
Build reliable API integrations for OpenClaw workflows with correct authentication, sane retry behavior, clear documentation, and proof that the integration actually works.

## Use this when
- connecting to external REST or GraphQL APIs
- building webhook receivers or handlers
- setting up OAuth2 or token-based third-party auth
- creating API wrappers or integration helpers
- debugging failed API calls or unreliable integrations

## Do NOT use this for
- ordinary WordPress REST work when WordPress execution is the main task (→ `wordpress-growth-ops`)
- email platform buildout as the main task (→ `email-marketing-engine`)
- generic technical writing without actual integration work (→ `technical-writing`)

## Do this
1. Define the integration goal, source system, destination system, and success condition.
2. Identify the integration type: REST, GraphQL, webhook, OAuth2, polling, or hybrid.
3. Define the auth method and where secrets/tokens will live.
4. Build the smallest working request or handler first.
5. Add error handling, retries, idempotency or deduplication where needed.
6. Verify with a real successful request/event.
7. Document the integration so it can be reused safely.

## Auth and secret rules
- Keep secrets in `.secrets/` or approved secret storage, never hardcoded in `SKILL.md` or checked-in scripts.
- Do not retry 401/403 blindly; fix auth first.
- Check token expiry/refresh behavior before assuming the integration is stable.

## Error-handling rules
- Retry 429 and relevant 5xx responses with backoff.
- Respect `Retry-After` when present.
- Log enough request/response context to debug failures safely.
- Add timeouts; do not allow silent hangs.
- For write operations, think about duplicate submission risk before retrying.

## Verification rule
Good proof includes:
- successful authenticated request
- expected response shape or created side effect
- webhook receipt/handler proof
- documented known limits or assumptions

Do not call an integration done from code alone without at least one real proof path.

## Documentation rule
Create or update a reference when the integration is non-trivial:
- base URL/version
- auth method
- secret/token location
- key endpoints/events used
- rate limits / retry notes
- failure modes / special cases

## Resources
- `scripts/check-api.sh` when present for probing auth/status/rate limits
- `references/google-search-console-bing-webmaster-playbook.md` when wiring SEO/content skills to real search-visibility data
- `references/` for per-service API notes you create or update

## Checks and common mistakes
- hardcoding secrets
- assuming all APIs return JSON
- ignoring rate limits until bulk runs fail
- retrying write operations without idempotency thinking
- building the full wrapper before proving one working request
- forgetting webhook signature validation when relevant

## Output contract
**Artifact:** working integration code, wrapper, handler, or documented request pattern
**Evidence:** successful auth/request proof, response or side-effect proof, and documented limits/assumptions
**Decision:** integration approach selected, working, blocked, or needs follow-up
**Next:** operationalize, monitor, extend endpoints, or hand off implementation details
