# Amazon Product Resolution (SerpApi-first, budget-smart)

## Goal
Select the most accurate Amazon product + image for the affiliate product box with minimal API usage.

## Script
- `scripts/amazon_product_resolver.py`

## Smart API policy
1. Query-level cache first (SQLite cache in `state/serp_product_cache.db`).
2. Prefer SerpApi with max 2 calls per uncached query (shopping + search).
3. Fallback to Serper only when SerpApi key is unavailable.
4. Enforce daily call budget.
5. Canonicalize to `/dp/ASIN/` URL.
6. Extract `og:image` + title from product page.

## Env key
- Primary: `SERPAPI_KEY` in `.secrets/serpapi.env` (chmod 600)
- Fallback: `SERPER_API_KEY` in `.secrets/serperapi.env` (optional)

## Output contract
- `product_url`
- `product_title`
- `product_image`
- `source`

## Guardrails
- If budget exceeded, return blocker and skip non-critical product-box enrichment.
- Never hardcode secrets in committed files.
