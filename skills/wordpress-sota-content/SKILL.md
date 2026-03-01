---
name: wordpress-sota-content
description: Enterprise-grade WordPress website management and SOTA content operations: technical SEO/indexation health, trust/safety hardening, schema/canonical integrity, editorial quality, publishing workflows, and incident recovery. Use when auditing/fixing WordPress sites, improving rankings and AI visibility, preventing regressions, running safe live changes (backup -> atomic update -> verify -> rollback), and producing high-performance blog content.
---

# WordPress SOTA Content Ops

## Scope Ownership
### Own
- Execute Enterprise-grade WordPress website management and SOTA content operations: technical SEO/indexation health, trust/safety hardening, schema/canonical integrity, editorial quality, publishing workflows, and incident recovery. Use when auditing/fixing WordPress sites, improving rankings and AI visibility, preventing regressions, running safe live changes (backup -> atomic update -> verify -> rollback), and producing high-performance blog content.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

## Operating profiles
- **Safe:** strict micro-batches.
- **Aggressive:** parallel reads/verification, atomic writes.
- **Degraded:** deterministic narrow retries only.

## Mandatory release gate
1. confirm exact scope (site/URLs/post IDs/plugins)
2. backup before risky change
3. atomic update only
4. verify source + live per unit
5. rollback on anomaly
6. treat homepage/templates/head-layer as high blast radius
7. no closure claim without evidence

## Lane routing
- site remediation → `references/wp-management-sota-runbook.md`
- critical incident → `references/wp-incident-response.md`
- content production → `references/wordpress-sota-template.md`
- indexation/canonical/schema cleanup → `references/wp-seo-indexation-checklist.md`

If multiple lanes apply: Incident → Management → SEO cleanup → Content.

## Deterministic audit
Run `scripts/wp_management_audit.py` before and after major work.
Minimum dimensions:
- HTTP health
- canonical integrity
- JSON-LD presence
- meta presence/length sanity
- readability baseline

## S-tier content upgrades
- entity-first optimization
- snippet-first intro (40–70 words + extractable structure)
- semantic cluster alignment (pillar/spoke)
- scheduled refresh logic (age + drift + opportunity)
- schema by template (Article/FAQ baseline, Product/LocalBusiness when valid)

## Publish + verification protocol
1. backup post JSON/content
2. atomic write
3. live verify URL + expected markers
4. verify canonical/schema/head output
5. verify links/media/alt
6. rollback if verification fails
7. log changes, proof, residual risk

## Required output bundle
1. scope + risk summary
2. before/after audit findings
3. changed URLs + diffs
4. verification proof
5. unresolved blockers + shortest unblock path