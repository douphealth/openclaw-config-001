# Core Web Vitals Quick Reference

## Targets
| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| LCP | < 2.5s | 2.5-4s | > 4s |
| INP | < 200ms | 200-500ms | > 500ms |
| CLS | < 0.1 | 0.1-0.25 | > 0.25 |
| TTFB | < 800ms | 800-1800ms | > 1800ms |

## LCP Fixes
- Preload hero image: `<link rel="preload" as="image" href="...">`
- Use `fetchpriority="high"` on LCP image
- Inline critical CSS
- Server-side render above-fold content

## CLS Fixes
- Set width/height on all images and videos
- Reserve space for ads/embeds
- Use `font-display: swap` or `optional`
- Avoid dynamic content injection above the fold

## INP Fixes
- Defer non-critical JavaScript
- Break long tasks (>50ms)
- Use `requestIdleCallback` for non-urgent work
- Optimize event handlers
