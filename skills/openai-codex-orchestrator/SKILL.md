---
name: openai-codex-orchestrator
description: Enterprise-grade Codex 5.3 OAuth/API orchestration for OpenClaw. Prevents quota exhaustion with budget guardrails, adaptive rate limiting, cache/dedup, model routing, and resilient fallback execution.
---

# OpenAI Codex Orchestrator (Enterprise)

Use this skill whenever a workflow would call OpenAI/Codex.

## Operating Philosophy
1. Never send unnecessary requests (local-first, cache-first, dedup-first)
2. Never send wasteful requests (prompt compression, structured outputs)
3. Never let one API failure stall execution (retry/fallback/degrade)

## Mandatory Pipeline (every request)
0. `scripts/codex_preflight.py` (single gateway decision: proceed/fallback/defer)
1. `scripts/codex_auth_verify.py` (token validity + access check)
2. `scripts/codex_budget_guard.py` (hour/day/month budgets + reserve logic)
3. `scripts/codex_rate_limiter.py precheck` (proactive pacing)
4. `scripts/codex_cache.py get` (TTL cache check)
5. `scripts/codex_request_planner.py` (model + prompt envelope)
6. Execute request (external caller)
7. `scripts/codex_rate_limiter.py update` (header-driven state update)
8. `scripts/codex_cache.py set` (cache deterministic outputs)
9. `scripts/codex_usage_report.py` (observability/reporting)

## Credentials & Secrets
- Store only in `.secrets/openai-codex.env` (chmod 600)
- Never commit secrets.

Required fields:
- OPENAI_API_KEY (fallback auth)
- OPENAI_ORG_ID (optional)
- OPENAI_PROJECT_ID (optional)
- CODEX_MODEL=codex-5.3
- CODEX_FALLBACK_MODEL=codex-5.3-mini
- CODEX_EMERGENCY_MODEL=gpt-4o-mini
- CODEX_MAX_MONTHLY_SPEND_USD
- CODEX_MAX_DAILY_SPEND_USD
- CODEX_MAX_HOURLY_REQUESTS
- CODEX_MAX_DAILY_REQUESTS
- CODEX_MAX_TOKENS_PER_REQUEST
- CODEX_CACHE_TTL_HOURS

Optional OAuth fields:
- OAUTH_GRANT_TYPE=client_credentials
- OAUTH_TOKEN_ENDPOINT=https://api.openai.com/v1/oauth/token
- OAUTH_REFRESH_STRATEGY=proactive
- OAUTH_REFRESH_BUFFER_SECONDS=300
- OAUTH_MAX_REFRESH_RETRIES=3
- OAUTH_REFRESH_BACKOFF=exponential

## Hard Safety Rules
- Never bypass budget guard for non-P0 tasks.
- Never ignore repeated 429/5xx patterns.
- Never claim optimization without ledger evidence.
- If auth/budget/rate gate fails -> fallback/defer/halt per policy.
- **Single gateway rule:** every AI API call across skills must route through this orchestrator.
- Enforce with `scripts/codex_gateway_enforcer.py`.

## Performance Targets
- Cache hit rate > 40%
- Local bypass rate > 30% where applicable
- Error rate < 2%
- Zero non-P0 budget-exhaust incidents

## References
- `references/architecture-map.md`
- `references/routing-policy.md`
- `references/retry-fallback-policy.md`
- `references/budget-policy.md`
- `references/oauth-policy.md`
- `references/request-optimization-pipeline.md`


## Anti-Patterns (blocked)
See `references/anti-patterns.csv`.

## Script map
- scripts/codex_preflight.py
- scripts/codex_client.py
- scripts/budget_manager.py
- scripts/rate_limiter.py
- scripts/cache_manager.py
- scripts/batch_queue.py
- scripts/model_router.py
- scripts/prompt_optimizer.py
- scripts/daily_report_generator.py
- scripts/alert_manager.py

## Reference map
- references/prompt-templates.md
- references/model-pricing.md
- references/rate-limit-guide.md
- references/oauth-setup-guide.md
- references/tuning-playbook.md
- references/cost-optimization-checklist.md
- references/token-budget-impact-analysis.csv
