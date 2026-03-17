# Portfolio Search Rollout

The search-visibility pipeline is now prepared for the managed WordPress portfolio.

## Portfolio sites
- affiliatemarketingforsuccess.com
- mysticaldigits.com
- gearuptogrow.com
- frenchyfab.com
- plantastichaven.com
- gearuptofit.com
- micegoneguide.com
- efficientgptprompts.com
- outdoormisting.com

## Workspace manifest
The operational manifest lives in:
- `workspace/.secrets/search/sites.json`

A template also exists at:
- `workspace/.secrets/search/sites.template.json`

The manifest intentionally stores:
- site URL
- GSC property URL
- Bing site URL
- bingMode (`import` or `api`)

It does **not** store raw API secrets in repo-tracked files.

## Recommended rollout order
1. Validate `micegoneguide.com` first
2. Validate one more site with the same Bing mode
3. Confirm output packs land under `workspace/ops/search-data/<site-slug>/`
4. Roll out to the remaining sites via manifest mode

## Expected outcome per site
- `gsc/` normalized files
- `bing/` normalized or raw+normalized files
- merged `summary.json`

## Why this matters
This turns the upgraded SEO / WordPress / editorial skills into data-driven operators across the site portfolio instead of one-off optimization helpers.
