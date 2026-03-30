# SerpApi Usage Notes for Amazon Product Boxes

## Goal
Get one trustworthy Amazon product page and usable image with the fewest possible queries.

## Minimal workflow
1. confirm fit score first
2. lock the exact product type
3. retrieve the key from a safe secret source
4. run one precise Amazon-targeted query
5. retry only if the failure mode is obvious
6. rotate keys only on auth/quota/provider failure

## Secret handling
- Prefer `.secrets/` or environment-backed config over pasted keys.
- If a task provides a key file, treat each line as a rotation candidate.
- Never echo raw keys into logs, docs, or chat.
- Report only the key index used if operational notes are needed.

## Query design
Use:
- exact product type
- one critical qualifier
- `amazon`

Examples:
- `monstera sphagnum moss pole amazon`
- `snake plant potting mix indoor amazon`
- `french bulldog slow feeder bowl amazon`
- `full spectrum clip on grow light amazon`

Avoid:
- vague exploratory shopping searches
- broad comparison/catalog browsing
- repeated synonym loops
- wasting requests before fit is confirmed

## Provider-aware guidance
- Prefer an Amazon-native search path when the provider/account supports it.
- Otherwise use a precise web query meant to surface Amazon product pages.
- Do not jump across multiple engines unless the primary provider path clearly fails.

## Rotation
- Start with the first available key.
- Rotate only for auth, quota, or provider-level failure.
- Do not rotate because the first result was weak; improve the query first.

## Final URL check
Before output:
- confirm it is an Amazon product page
- strip junk params
- enforce `tag=papalex-20` exactly once
- avoid search-result, redirect, or short-link endpoints
