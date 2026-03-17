# Search Visibility Data Pack

Use this before making SEO, GEO, AEO, or AI-visibility decisions.
If available, pull real site data from both Google Search Console and Bing Webmaster Tools before diagnosing indexation, ranking, CTR, or content gaps.

## Required inputs
For the last 28 days by default (and optionally compare to previous 28 days):
- GSC page data: clicks, impressions, ctr, position
- GSC query data: clicks, impressions, ctr, position
- GSC page×query data for top pages / target sections
- GSC device split for affected pages
- GSC country split when geo SEO matters
- GSC sitemap status
- Bing page/query performance
- Bing indexation/crawl/sitemap signals where available

## Best use cases
- ranking drop diagnosis
- indexation troubleshooting
- content refresh prioritization
- title/meta CTR optimization
- page-two keyword expansion
- geo/device-specific SEO opportunities
- AI visibility support via query/entity coverage

## Priority slices to extract
1. Top pages by impressions
2. Top pages by clicks
3. High-impression, low-CTR pages
4. Queries in average position 4-15
5. Queries/pages losing clicks period-over-period
6. Pages with impressions but weak click conversion
7. Country/device outliers

## Output expectation
Summarize each site with:
- what is losing visibility
- what is almost winning (page 1 / page 2 opportunities)
- what has CTR problems vs ranking problems
- what is Google-only vs Bing-only
- what should be fixed first

## Rule
If GSC/Bing data is available, use it before making indexation or ranking claims.
If not available, explicitly say the diagnosis is lower-confidence.