---
name: technical-seo-checker
description: Use when the user asks for technical SEO audits, crawl/indexing diagnostics, Core Web Vitals checks, page-speed analysis, mobile issues, or why search engines cannot properly crawl/index the site. Audit technical blockers and provide prioritized remediation steps.
---

# Technical SEO Checker

## Objective
Find and prioritize technical constraints that limit crawlability, indexability, and performance.

## Scope Boundaries
- Include: crawl/index diagnostics, CWV/performance, mobile readiness, canonical/sitemap/robots checks.
- Exclude: full content rewriting, backlink strategy execution.

## Workflow
1. **Establish audit scope**: domain/subfolder, templates, critical URLs, target market.
2. **Check crawl controls**: robots.txt, meta robots, canonicals, hreflang, XML sitemaps.
3. **Check indexation signals**: status codes, duplicate/parameter URLs, soft 404 patterns.
4. **Review architecture health**: redirect chains, orphan pages, internal crawl depth.
5. **Review performance**: CWV (LCP/INP/CLS), render-blocking assets, heavy scripts/media.
6. **Review mobile/security**: responsive behavior, HTTPS integrity, mixed content issues.
7. **Review structured data health**: parse errors and eligibility blockers.
8. **Prioritize fixes** by impact, effort, and blast radius.

## Quality Gates
- Every finding must include evidence and a concrete fix path.
- Separate critical index blockers from optimization improvements.
- Avoid tool-only conclusions without cross-checking page behavior.

## Output Artifacts
Return:
1. Technical issue register (severity, evidence, recommended fix).
2. Priority implementation plan (P0/P1/P2).
3. Verification plan for post-fix recrawl/recheck.
4. Explicit risks/blockers requiring stakeholder decisions.
