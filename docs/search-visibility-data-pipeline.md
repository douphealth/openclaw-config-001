# Search Visibility Data Pipeline

This repo now supports a real search-visibility ingestion pattern for:
- Google Search Console
- Bing Webmaster Tools

## Components

### Scripts
Under `skills-approved/api-integration-builder/scripts/`:
- `gsc_pack.py` — live Google Search Console pack fetcher
- `bing_webmaster_pack.py` — Bing API/raw capture + export-ingest normalizer
- `build_search_visibility_pack.py` — merge GSC/Bing summaries into one normalized site pack

### Data layout
Operational packs are intended to be written under:
- `workspace/ops/search-data/<site-slug>/`

With subfolders:
- `gsc/`
- `bing/`
- merged `summary.json`

## Intended use
These packs are consumed by:
- `seo-command-center`
- `seo-audit-playbook`
- `content-strategy-planning`
- `editorial-post-enhancement`
- `wordpress-growth-ops`
- optionally `monitoring-ops`

## Design choices
- GSC is implemented as a real API fetcher because the API surface is stable and well-documented.
- Bing supports both direct API raw capture and export-ingest normalization because Bing method schemas vary and export ingest remains a reliable operational fallback.
- All outputs normalize toward one shared page/query/device/country schema.

## Secrets
Do not commit credentials.
Use `.secrets/` or environment variables only.

Suggested env names:
- `GSC_SERVICE_ACCOUNT_JSON`
- `BING_WEBMASTER_API_KEY`
- `GSC_PROPERTY_URL`
- `BING_SITE_URL`
