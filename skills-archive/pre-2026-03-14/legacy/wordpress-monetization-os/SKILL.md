---
name: wordpress-monetization-os
description: Enterprise WordPress monetization operations for affiliate, ads, lead-gen, digital products, CRO, and revenue analytics. Use when auditing or implementing revenue growth on WordPress sites with safe live execution (backup -> atomic update -> verify), compliance controls, and KPI-driven prioritization.
---

# WordPress Monetization OS (Enterprise)

## Scope Ownership
### Own
- Execute Enterprise WordPress monetization operations for affiliate, ads, lead-gen, digital products, CRO, and revenue analytics. Use when auditing or implementing revenue growth on WordPress sites with safe live execution (backup -> atomic update -> verify), compliance controls, and KPI-driven prioritization.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

## Mission
Increase revenue/session safely by prioritizing high-traffic + high-intent + high-EPC opportunities first.

## Mandatory phase order
1. Monetization audit
2. Affiliate architecture
3. Ads architecture
4. Leads/products layer
5. CRO experiments
6. Reporting + alerts
7. Verify + log

## 1) Audit first
- score URLs: traffic × intent × monetization-gap
- classify: buyer / commercial research / informational feeder
- build Top-20 priority queue by expected RPM lift

## 2) Affiliate architecture
- disclosure near top + first affiliate link
- link hygiene (`rel`/sponsored/nofollow/target policies)
- intent-matched modules (comparison, pros/cons, verdict, alternatives)
- link health checks + replacement queue

## 3) Ads architecture
- deploy ad slots only where UX threshold passes
- use RPM placement templates by content length
- block any change that risks CWV regressions

## 4) Leads + products
- trigger lead magnets on high-traffic informational pages
- segmented CTAs by funnel stage
- relevant upsell blocks on commercial pages

## 5) CRO
- run CTA A/B tests and promote winners
- improve offer framing without hype/deception
- keep internal-link architecture human-reviewed

## 6) Reporting + alerts
Track per URL:
- affiliate EPC/CTR/CVR
- RPM and revenue/session
- opt-in rate
- WoW deltas

Alert on:
- >15% revenue drop
- link failures
- disclosure drift

## 7) Mandatory quality gates
- compliance (FTC/disclosure/attributes)
- trust tone (no manipulative claims)
- UX/CWV safety
- source + live verification
- evidence report with changed URLs + KPI delta

## Constraints
- Never fabricate earnings, EPC, CVR, or benchmarks.
- Never deploy irreversible changes without backup.
- Never claim uplift without measured evidence.
- Never use deceptive urgency/scarcity.

## References
- `references/kpi-model.md`
- `references/compliance-checklist.md`
- `references/plugin-stack.md`
- `references/skill-manifest-example.json`