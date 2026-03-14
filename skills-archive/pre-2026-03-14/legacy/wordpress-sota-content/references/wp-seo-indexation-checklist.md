# WordPress SEO/Indexation Checklist

## Crawl/indexation gates
- robots.txt allows intended crawling.
- XML sitemap(s) load and include only intended URL types.
- Search/utility/thin pages are excluded or noindexed.
- Canonical tags exist and self-match where appropriate.

## Head-layer integrity
- Single canonical tag per page.
- No contradictory robots directives.
- Title/meta description present and intent-aligned.
- OpenGraph/Twitter tags not conflicting with canonical intent.

## Structured data
- Core pages include valid JSON-LD.
- Post pages include Article/BlogPosting graph.
- FAQ pages include FAQPage only when visible FAQ exists.

## Internal architecture
- Pillar pages linked from relevant clusters.
- Descriptive anchor text.
- Orphan pages reduced.

## Reindex process
1. Submit sitemap index and key child sitemaps.
2. Request indexing for top-priority changed URLs.
3. Track recrawl and coverage deltas.
4. Re-verify canonical/schema/snippet after recrawl.
