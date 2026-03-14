---
name: keyword-intelligence-os
description: Enterprise-grade keyword research, entity intelligence, semantic clustering, cannibalization control, and SEO/AEO/GEO optimization workflow for WordPress and content portfolios. Use when users ask to find best keywords, build topical authority maps, optimize pages/posts for rankings, improve AI visibility, add semantically related entities naturally, or run large-scale keyword-to-content execution plans.
---

# Keyword Intelligence OS (Elite)

## Scope Ownership
### Own
- Execute Enterprise-grade keyword research, entity intelligence, semantic clustering, cannibalization control, and SEO/AEO/GEO optimization workflow for WordPress and content portfolios. Use when users ask to find best keywords, build topical authority maps, optimize pages/posts for rankings, improve AI visibility, add semantically related entities naturally, or run large-scale keyword-to-content execution plans.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

Run in phases. Do not skip gates.

## Objective
Increase ranking velocity and conversion-quality traffic by prioritizing:
- weak/displaceable SERPs
- sufficient demand
- strong intent-to-offer fit
- high AI extractability/citation fit

## Phase sequence
0. Mission lock (goal, scope, constraints)  
1. Intent/query architecture  
2. Keyword universe build  
2.5. Velocity scoring (mandatory)  
3. Entity intelligence  
4. Cluster + cannibalization control  
5. On-page integration  
6. SERP/AEO/GEO packaging  
7. Quality gates

## Phase details (concise)
### 0) Mission lock
Define batch objective, URL scope, compliance/tone/claim constraints.

### 1) Intent architecture
Map one dominant intent per target (info/commercial/transactional/navigational), funnel stage, and business objective.

Reference: `references/workflow-keyword-architecture.md`

### 2) Keyword universe
Build 7-layer keyword set (head/mid/long-tail/questions/comparisons/versioned modifiers/demand modifiers).

Reference: `references/keyword-scoring.md`

### 2.5) Velocity scoring (0–100)
- Demand (0–25)
- Competition weakness (0–25)
- Intent fit (0–20)
- SERP displaceability (0–15)
- AI extractability (0–15)

Bands:
- Tier A 75–100 (execute now)
- Tier B 60–74 (batch 2)
- Tier C <60 (backlog)

Use real providers (DataForSEO/GSC/etc.) when available; never claim guaranteed rankings.

### 3) Entity model
Define core/support/context entities and distribute naturally across title/H1/intro/sections/FAQ/schema fields.

Reference: `references/entity-coverage-checklist.md`

### 4) Cluster + cannibalization
Assign one primary family per URL; resolve collisions via merge/reposition/canonical only when needed; enforce intent-matched internal links.

Reference: `references/cannibalization-control.md`

### 5) On-page integration
Natural insertion only; add intent-driven blocks (steps/comparisons/cost/troubleshooting/FAQ/decision-ready sections).

Reference: `references/on-page-integration-rules.md`

### 6) SERP/AEO/GEO packaging
Add answer-first blocks, extractable structures, clear FAQs, valid schema, citation-ready facts.

Reference: `references/serp-aeo-geo-packaging.md`

### 7) Quality gates (all required)
- intent clarity
- entity coverage
- anti-stuffing readability
- trust/no-clickbait tone
- internal-link relevance
- source/live verification
- recorded priority tier
- AI visibility extractability

Reference: `references/quality-gates.md`

## Deliverables per run
1. keyword map (primary/secondary/questions/entities)
2. scored opportunity table (Tier A/B/C)
3. cluster map + internal-link plan
4. URL-level before/after optimization diff
5. unresolved blockers + shortest unblock path

## Deterministic helpers
- `scripts/keyword_entity_brief.py`
- `scripts/semantic_cluster_engine.py`

Example pipeline:
`python3 scripts/semantic_cluster_engine.py --input <keywords.txt> --output <clusters.json>`

## Constraints
- No irrelevant keyword forcing or stuffing.
- No fabricated volume/CPC/ranking certainty.
- No manipulative fear/clickbait copy.
- No auto-scaled internal links without manual review.
- No bulk programmatic publishing without pacing + QA.