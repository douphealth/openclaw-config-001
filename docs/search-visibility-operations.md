# Search Visibility Operations

This document makes the GSC + Bing pipeline operational.

## 1. Put secrets in place

### Google Search Console
Store a service-account JSON at:
- `C:\Users\User\.openclaw\workspace\.secrets\search\google-service-account.json`

Then either:
- set env var `GSC_SERVICE_ACCOUNT_JSON` to that full path
- or pass `--service-account` directly to the runner

Important: the service account must be added as a user on each Search Console property.

### Bing Webmaster
Set env var:
- `BING_WEBMASTER_API_KEY`

Or store the key externally and inject it at runtime.

## 2. Create a site manifest
Copy:
- `workspace/.secrets/search/sites.template.json`

to:
- `workspace/.secrets/search/sites.json`

Fill in each site's:
- `siteUrl`
- `gscProperty`
- `bingSiteUrl`
- `bingMode`
- Bing export paths if using `import`

## 3. Run one site first
### PowerShell wrapper
```powershell
cd C:\Users\User\.openclaw\workspace\repo_openclaw_config_001\scripts
.\run-search-visibility-pack.ps1 -StartDate 2026-02-18 -EndDate 2026-03-17
```

### Direct Python (single site)
```powershell
python C:\Users\User\.openclaw\workspace\skills\api-integration-builder\scripts\run_search_visibility_pack.py `
  --site https://example.com/ `
  --gsc-property https://example.com/ `
  --bing-mode import `
  --bing-queries-file C:\secure\exports\example-queries.csv `
  --bing-pages-file C:\secure\exports\example-pages.csv `
  --start-date 2026-02-18 `
  --end-date 2026-03-17
```

## 4. Expected output
Under:
- `C:\Users\User\.openclaw\workspace\ops\search-data\<site-slug>\`

You should get:
- `gsc\...`
- `bing\...`
- `summary.json`

## 5. How the skills should use it
- `seo-audit-playbook` → real indexation/query/page evidence
- `content-strategy-planning` → topic prioritization from partial ownership and page-2 opportunities
- `editorial-post-enhancement` → title/meta/query/entity optimization from real data
- `wordpress-growth-ops` → traffic-entry and money-page diagnostics from actual search-platform signals

## 6. Operational rollout order
1. Validate one site manually
2. Validate second site with a different Bing mode if needed
3. Add remaining portfolio sites to `sites.json`
4. Run monthly or biweekly
5. Feed summaries into SEO/content optimization work

## 7. Important constraints
- GSC average position is an aggregate signal, not an exact rank
- Do not make CTR decisions on tiny-impression rows
- Bing export schemas may vary; import mode normalizes common column names but may still need site-specific tweaks
- Keep raw exports and credentials out of git
