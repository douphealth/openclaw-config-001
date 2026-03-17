---
name: seo-audit-playbook
description: Use when auditing a site or page for ranking problems, indexing issues, technical SEO risk, keyword cannibalization, on-page weaknesses, or competitor gaps that require a prioritized diagnosis with evidence.
---

# SEO Audit Playbook

## Purpose
Diagnose SEO problems in a structured order so technical blockers, content issues, cannibalization, and competitive gaps are identified with evidence and prioritized by likely impact.

## Use this when
- auditing a site or page for SEO health
- diagnosing ranking drops or “why isn’t this ranking?”
- checking crawlability, indexation, canonicals, mobile, or on-page fundamentals
- detecting keyword cannibalization
- running SERP/competitor gap analysis
- preparing a prioritized SEO fix plan

## Do NOT use this for
- writing or editing content (→ `editorial-post-enhancement`)
- implementing schema markup (→ `schema-ops`)
- setting up tracking (→ `tracking-measurement`)
- broad content planning (→ `content-strategy-planning`)
- monitoring rankings over time as the main task (→ `monitoring-ops`)

## Audit order
Always work in this sequence:
1. crawlability and indexation
2. technical foundations
3. on-page optimization
4. content quality and intent match
5. internal linking and authority
6. cannibalization check
7. competitor / SERP gap analysis

Do not jump to content advice before checking whether the page can be found, indexed, rendered, and understood.

## Do this
1. Define scope: site, page set, priority pages, symptoms, and available data.
2. Check crawlability and indexation first.
3. Check technical foundations such as mobile, canonicals, redirects, HTTPS, and render risk.
4. Audit titles, metas, headers, content depth, and key on-page signals.
5. Check internal linking and obvious authority/supporting-structure issues.
6. Check for keyword cannibalization before recommending new content.
7. Compare against the SERP or relevant competitors when useful.
8. Return a prioritized fix list with evidence and impact level.

## Evidence standard
Good findings should include one or more of:
- fetched page evidence
- crawl evidence
- rendered evidence when JS matters
- sitemap/robots evidence
- ranking/GSC data when available
- side-by-side page or SERP comparison

Weak findings:
- opinion-only diagnosis
- “audit complete” after only surface HTML inspection
- assumptions about schema or JS-rendered content without verification

## Priority buckets
Use:
- **Critical** — blocks indexation, crawl, canonical integrity, or primary ranking viability
- **High** — materially harms ranking potential or causes cannibalization/confusion
- **Medium** — worthwhile improvements with moderate impact
- **Low** — polish or nice-to-have improvements

## Cannibalization rules
Always check for:
- multiple pages targeting the same primary keyword
- multiple pages competing for the same intent
- near-duplicate titles/H1 patterns
- weak differentiation where consolidation would be better

## Resources
Read when needed:
- `references/technical-checklist.md`
- `references/cannibalization-detection.md`
- `references/competitive-analysis-framework.md`
- `..\seo-command-center\references\search-visibility-data-pack.md` — required GSC/Bing data slices before indexation/ranking conclusions

Use `schema-ops` validation tooling when schema findings need proof.

## Checks and common mistakes
- Do not report “no schema” from static fetch alone when JS may inject it.
- Do not recommend new content before checking cannibalization.
- Do not mix business opinion with technical diagnosis.
- Do not report an audit as complete if key technical layers were skipped.
- For affiliate/review pages, explicitly check whether expected Product/Review schema is present and valid.

## Output contract
**Artifact:** SEO audit report with prioritized fixes
**Evidence:** issue evidence, supporting crawl/fetch/render data, and impact rationale
**Decision:** top fixes to implement first
**Next:** implement, re-audit, or route follow-on work to the correct execution skill
