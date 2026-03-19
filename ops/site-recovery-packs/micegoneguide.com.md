# micegoneguide.com — Recovery Pack

## Stack
- WordPress + Cloudflare

## Known Failure Modes
- cache lag after content changes
- raw markdown remnants showing on live pages
- markdown tables rendered as paragraph text instead of HTML tables
- bad YouTube IDs from automation runs

## Safe Recovery Pattern
1. verify REST state first
2. back up affected posts
3. fix raw content structure
4. purge/verify cache-busted and canonical URLs
5. verify live render and media/video presence

## High-Value Verification Checks
- live page and cache-busted page both reflect change
- table renders as actual HTML table
- YouTube embed resolves to a real video
- no raw markdown remnants visible

## Backup Location
- `ops/backups/mgg-posts/`
- `ops/backups/mgg-optimize/`

## Best Skill Chain
`failure-recovery-director` → `content-integrity-cleanup` → `wp-rest-api-mastery` → `auto-verification`
