---
name: api-integration-builder
description: Enterprise API integration design and implementation. Use when building REST API integrations, setting up webhook listeners, connecting external services to WordPress or backend systems, automating data flows via API, or debugging API authentication and response parsing issues.
---

# API Integration Builder — Enterprise API Development

## Purpose
Build reliable, well-documented API integrations that handle errors gracefully, authenticate securely, and deliver consistent results.

## When to Use
- Building REST API integrations with external services
- Setting up webhook listeners and event handlers
- Connecting services (WordPress ↔ CRM ↔ Email ↔ Analytics)
- Automating data flows via API
- Debugging API authentication or response parsing issues

**Do NOT use for:** WordPress-specific operations (→ `wordpress-growth-ops`), tracking/analytics setup (→ `tracking-measurement`), email marketing (→ `email-marketing-engine`).

## Integration Framework

### Phase 1: Design
1. Define the integration goal: what data moves, where, and when?
2. Map the API surface: endpoints, auth, rate limits, error codes
3. Design the data flow: source → transformation → destination
4. Plan error handling: retries, fallbacks, dead-letter queue

### Phase 2: Authentication Methods

| Method | Use Case | Implementation |
|--------|----------|----------------|
| API Key | Simple header-based auth | `Authorization: Bearer <key>` |
| OAuth 2.0 | Token-based with refresh | Token + refresh flow |
| Basic Auth | Username/password | `base64(user:password)` |
| App Passwords | WordPress-specific | `user:app_password` base64 |
| Bearer Token | JWT or API tokens | `Authorization: Bearer <token>` |

### Phase 3: Implementation Pattern
```
1. Auth setup (header/token/OAuth)
2. Request construction (URL, params, headers, body)
3. Response parsing (JSON, XML, CSV)
4. Error handling (status codes, retry logic)
5. Data transformation (source format → target format)
6. Logging and monitoring
```

### Phase 4: Error Handling

| Error | Code | Action |
|-------|------|--------|
| Bad Request | 400 | Log payload, check format |
| Unauthorized | 401 | Refresh token, check credentials |
| Forbidden | 403 | Check permissions, API plan |
| Not Found | 404 | Verify endpoint URL |
| Rate Limited | 429 | Exponential backoff and retry |
| Server Error | 5xx | Retry with exponential backoff |
| Timeout | - | Increase timeout or reduce payload |

**Retry logic:** Wait 1s → 2s → 4s → 8s → give up. Log each attempt.

### Phase 5: Testing & Documentation
10. Test with valid inputs (happy path)
11. Test with invalid inputs (error handling)
12. Test error recovery (force 4xx/5xx responses)
13. Document: auth setup, endpoints, data schemas, rate limits
14. Add monitoring for API health

## WordPress REST API Patterns
- Auth: `base64(username:app_password)` as Basic Auth
- Content: `POST /wp-json/wp/v2/posts/{id}` with `{"content": "..."}`
- Use `<!-- wp:html -->` blocks to prevent wpautop interference
- Always check response status before parsing JSON


## Self-Critique Scorecard (/25)
After every operation, score yourself:

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Functionality** (1-5) | ? | Does it work perfectly and meet all requirements? |
| **Quality** (1-5) | ? | Is it enterprise-grade and production-ready? |
| **Verification** (1-5) | ? | Was it verified via multiple methods? |
| **Speed** (1-5) | ? | Was execution optimal with parallel operations? |
| **Learning** (1-5) | ? | Were new patterns documented and memory updated? |

**Target: 22+/25 before claiming completion**

### Pre-Flight Checklist
- [ ] Credentials verified and target exists
- [ ] Rollback plan identified
- [ ] Success criteria defined
- [ ] Anti-patterns reviewed

### Post-Flight Checklist
- [ ] Verified via API response + live check
- [ ] Quality score logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered
- [ ] No common mistakes made

## Output Contract
**Artifact**: Working API integration with documented endpoints and error handling
**Evidence**: Successful API call with response verification, error handling tested
**Decision**: Integration active and monitored
**Next**: Monitor for 24-48h, tune rate limits and retry logic

## Anti-Patterns
- ❌ No error handling (assumes 200 OK always)
- ❌ Hardcoded credentials in source code
- ❌ No retry logic for transient errors (429, 5xx)
- ❌ Unbounded data fetches (no pagination)
- ❌ No logging (can't debug when it breaks)
- ❌ Not handling rate limits (causes API bans)

## Compatibility
- Targets current WordPress 6.9+ where applicable
- REST API + WP-CLI preferred over browser automation
- Batch operations via `_fields` + `per_page=100` + `concurrent.futures`
- Browser automation only when API/CLI insufficient

## Inputs Required (Pre-Flight)
Before executing any task in this skill:
1. **Target identification** — What site, page, post, or system is being operated on?
2. **Auth verification** — Confirm credentials work (test API call or CLI command)
3. **Current state** — Understand what exists before making changes (GET before POST)
4. **Environment** — Production vs staging (assume production unless stated)
5. **Constraints** — No downtime? Preserve SEO? Preserve data? Budget limits?

## Triage Protocol
Before ANY operation:
1. **Identify** — What type of content/system/problem is this?
2. **Check state** — Query current state via API/CLI before modifying
3. **Verify creds** — Confirm authentication works
4. **Plan rollback** — How to undo if something breaks?
5. **Scope check** — Is this a single item or batch? Scale determines approach.

## Speed Optimizations
- **API calls**: Always use `_fields` parameter (80%+ payload reduction)
- **Pagination**: Use `per_page=100` for list endpoints
- **Parallelism**: Use `concurrent.futures` for independent operations (max 10/site)
- **Caching**: Store results in session — never re-fetch same data
- **Batching**: Group similar operations into single API calls where possible
- **Direct CLI**: Use WP-CLI `wp db query` for complex operations

## Error Recovery (Auto-Learning)
- Track error patterns — after 2 failures, try alternative approach
- Log recurring fixes to `memory/YYYY-MM-DD.md`
- Update references when new patterns discovered
- Rollback plan: Know how to undo before making changes

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

## Output Contract
- **Artifact**: What was created/changed/deleted
- **Evidence**: API response proof + live verification
- **Decision**: Success/failure with reasoning
- **Next**: What follow-up is needed (if any)
