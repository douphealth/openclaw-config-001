---
name: site-audit-director
description: Enterprise meta-skill for running comprehensive site audits across GSC, Bing, crawl, metadata, indexing, schema, and opportunity scoring. Use when a user asks for a full audit or wants a prioritized action queue for a site.
---

# Site Audit Director

## Purpose
Run a serious, multi-layer site audit and synthesize it into one ranked action plan instead of producing scattered diagnostics.

## Strategic Entry Point
Use this as the **primary entrypoint for full-site audits**.
- Use `seo-command-center` after the audit when the goal becomes ongoing SEO operations.
- Use this skill first when the user wants a comprehensive diagnosis and prioritized fix queue.

## Shared Doctrine References
- `skills/shared/enterprise-protocol.md`
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`
- `skills/shared/execution-brief-template.md`
- `skills/shared/worker-result-contract.md`
- `skills/shared/verification-evidence-pack.md`
- `ops/site-ops-registry.md`
- `skills/shared/scripts/site_dossier_generator.py`
- `skills/shared/scripts/synthesize_worker_results.py`

## Superpower Layer

For serious work, also follow:
- `skills/shared/openclaw-superpowers.md`
- `skills/shared/superpower-checklist.md`

Default execution mode:
1. clarify/spec first if ambiguous
2. write a short plan before large execution
3. dispatch parallel workers for independent subtasks when safe
4. review output for spec compliance and quality
5. verify in reality before claiming complete

## When to Use
- Full-site SEO audit requests
- “Audit this site” / “find what’s wrong” / “give me the best next fixes”
- User wants GSC + Bing + technical + on-page + content + opportunity prioritization
- User wants one prioritized queue instead of raw data dumps

## Do NOT Use For
- Single-page SEO review only
- Pure keyword research without site diagnosis
- Pure implementation tasks (route to specialist skills after the audit)

## Audit Layers
Dispatch or run these layers:
1. **Search performance** — GSC + Bing (`seo-intelligence`, `keyword-research-mastery`)
2. **Technical crawlability** — robots, sitemaps, canonicals, status codes (`seo-audit-playbook`)
3. **Snippet quality** — titles, meta descriptions, H1 integrity (`seo-audit-playbook`, `editorial-post-enhancement`)
4. **Indexation / decay** — declining pages, page-2 opportunities, CTR failures (`seo-intelligence`)
5. **Entity / GEO / AI visibility** — FAQ, comparison intent, answerability (`ai-visibility`, `schema-ops`)
6. **Cluster / internal linking** — topical authority, orphan risk, cannibalization (`content-strategy-planning`, `seo-competitor-analysis`)

## Director Workflow

### 1. Intake
Build a short execution brief:
- target site
- audit depth requested
- constraints (read-only vs implement fixes)
- date range for performance review

### 2. Dispatch audit workers
Suggested worker split:
- Worker A: GSC/Bing/search performance
- Worker B: technical/sitemap/robots/canonical checks
- Worker C: metadata/H1/sample content quality
- Worker D: keyword/GEO/opportunity mining
- Worker E: cluster/cannibalization/internal-link interpretation

### 3. Synthesize findings
Rank issues by:
- business impact
- implementation speed
- reversibility
- evidence strength
- whether the issue blocks everything else

### 4. Produce action queue
Required output:
- P0 immediate fixes
- P1 fast wins
- P2 strategic improvements
- exact next move

## Scoring Model
Use a simple weighted priority score:
- **Impact** (1-5)
- **Ease** (1-5)
- **Evidence confidence** (1-5)
- **Urgency** (1-5)
- **Compounding value** (1-5)

Prioritize items with the highest combined score.

## Output Contract
**Artifact**: site audit report + prioritized fix queue
**Evidence**: GSC/Bing/crawl/on-page findings with supporting facts
**Decision**: exact next best move(s)
**Next**: route to implementation skills or batch controller

## Anti-Patterns
- ❌ dumping raw metrics without prioritization
- ❌ mixing indexing problems with snippet problems without distinction
- ❌ calling something “technical SEO” without evidence
- ❌ giving 50 recommendations with no order of attack
- ❌ auditing without a decisive next move

## Self-Critique Scorecard (/25)
1. **Coverage** (1-5): Were all meaningful audit layers included?
2. **Evidence** (1-5): Were findings supported by real data?
3. **Prioritization** (1-5): Is the fix queue actually useful?
4. **Clarity** (1-5): Can execution begin from this report immediately?
5. **Leverage** (1-5): Did this identify the fastest/highest-value path?

**Target: 22+/25**
