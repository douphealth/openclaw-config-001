---
name: wordpress-growth-os
description: Enterprise WordPress growth operations for multi-site portfolios. Use when auditing/fixing/optimizing WordPress sites for monetization, SEO, AEO/GEO, AI visibility, SERP rankings, internal links, affiliate compliance, schema, technical indexability, content quality, and conversion architecture. Triggers on requests like "fix/optimize all sites", "boost traffic/revenue", "audit and implement", "make it SOTA", "increase rankings/authority", and ongoing autonomous-style improvement loops with strict safety gates.
---

# WordPress Growth OS (HQ Mode)

## Scope Ownership
### Own
- Execute Enterprise WordPress growth operations for multi-site portfolios. Use when auditing/fixing/optimizing WordPress sites for monetization, SEO, AEO/GEO, AI visibility, SERP rankings, internal links, affiliate compliance, schema, technical indexability, content quality, and conversion architecture. Triggers on requests like "fix/optimize all sites", "boost traffic/revenue", "audit and implement", "make it SOTA", "increase rankings/authority", and ongoing autonomous-style improvement loops with strict safety gates.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

Execute in strict order unless user overrides:
1) Stabilize → 2) Monetize → 3) Rank → 4) Scale → 5) Verify + Log

## Operating profiles
- **Safe (default):** micro-batches, backup-before-edit, dual verification.
- **Aggressive (Alex-approved):** larger batches with parallel reads; writes still atomic.
- **Degraded:** narrow deterministic retries under cache/timeout variance.

## 1) Stabilize
Run first on every sprint:
- homepage/money-page render health
- canonical/indexability/robots/sitemap/schema fundamentals
- high-blast-radius UI defects

Reference: `references/stabilization-checklist.md`

## 2) Monetize
- refresh offer map by site
- enforce intent tiers (buyer/commercial/informational feeder)
- enforce CTA + affiliate disclosure/link hygiene

Reference: `references/monetization-os.md`

## 3) Rank (SEO + AEO/GEO)
- repair canonical/internal-link clusters
- improve title/meta/intro for intent + CTR
- add answer-first blocks, FAQ/schema where valid
- improve review/comparison decision UX

Reference: `references/seo-aeo-geo-playbook.md`

## 4) Scale safely
- prioritize template/component-level fixes
- batch by reversibility and impact
- use deterministic helpers:
  - `scripts/wp_growth_priority.py`
  - `scripts/wp_affiliate_link_hygiene.py`

## 5) Verify + log
- produce source + live evidence for all changed URLs
- log `status: done|partial|blocked`, `updated_at`, evidence paths
- if blocked: report exact blocker + shortest unblock path

Reference: `references/reporting-standard.md`

## Mandatory quality gates
A. Write safety: backup + scoped diff before edit  
B. Source truth: edit-context/raw verification pass  
C. Live truth: render verification pass (else mark degraded)  
D. Claim safety: no unsupported KPI/ranking claims  
E. Completion safety: never call done with hidden residual risk

## Recovery mode (P0/P1 first)
Trigger when traffic/indexing regression is reported.
1. Build cross-site damage map (no writes): homepage/indexability/noindex/canonical/robots/sitemap/REST.
2. Classify blockers by blast radius (P0/P1/P2).
3. Freeze non-essential growth writes until P0/P1 are closed.
4. Apply atomic remediations with rollback-ready backups.
5. Re-verify source + live and publish evidence.

Recovery artifacts:
- `reports/portfolio-recovery-audit-*.json`
- per-site remediation report with before/after
- explicit `status` + `outcome` fields

## Constraints
- No blind text replacement on semantic-sensitive content.
- No completion claims without verification evidence.
- No irreversible/destructive changes without explicit safety gate.
- No autonomous long-loop execution beyond user-authorized scope.