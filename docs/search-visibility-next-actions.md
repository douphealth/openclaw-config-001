# Search Visibility Next Actions

The implementation is now complete enough to begin live data rollout.

## Immediate next actions
1. Place GSC service-account JSON in `workspace/.secrets/search/`
2. Grant the service account access to all target GSC properties
3. Decide Bing mode per site:
   - `import` if using exported Bing reports initially
   - `api` if using direct Bing API key + method flow
4. Run one-site validation on `micegoneguide.com`
5. Inspect generated `summary.json`
6. Feed the pack into:
   - `seo-audit-playbook`
   - `content-strategy-planning`
   - `editorial-post-enhancement`
   - `wordpress-growth-ops`

## Near-term follow-up
- Add monitoring rules from pack deltas
- Add site-specific Bing import schemas if export formats differ
- Add cron or recurring operational cadence once first live runs are verified

## Constraint
The pipeline is implemented, but live data pulls still require real credentials and/or export files supplied outside git.
