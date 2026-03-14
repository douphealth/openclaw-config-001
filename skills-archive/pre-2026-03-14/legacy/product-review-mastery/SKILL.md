---
name: product-review-mastery
description: Enterprise-grade workflow for writing high-conversion, trust-safe, SEO/AEO-optimized product review blog posts on WordPress. Use when drafting, rewriting, or improving any product review, buyer guide, or review-style comparison. Includes review architecture, evidence methodology, affiliate-compliant product boxes with image specs, visual component system, scoring rubric, and publish verification scripts.
---

# Product Review Mastery

Execute in order: **Research → Review Blueprint → Draft → Visual Product Boxes → Compliance/SEO → QA → Publish**.

## 1) Research & Evidence
- Build review brief: `scripts/review_brief_builder.py`
- Build evidence registry: `scripts/evidence_registry.py`
- Require verifiable claims, date all stats, and label uncertainty where needed.

## 2) Review Architecture (mandatory)
Use `references/review-structure.md` for the canonical sequence:
1. Hook (problem + context)
2. Answer-first verdict block
3. Quick specs + score snapshot
4. Who this is for / not for
5. Testing methodology
6. Deep-dive analysis (performance, usability, value, support)
7. Pros & cons
8. Alternatives
9. Final verdict + confidence level
10. FAQ
11. Trust footer + disclosures

## 3) Product Box System (required for monetized reviews)
Use `assets/product-box-library.md` components:
- Hero product box (image + score + CTA)
- Comparison cards
- Pros/cons cards
- “Best for” badges
- Disclosure-safe CTA box

Generate compliant CTA attrs with `scripts/affiliate_link_validator.py`.

## 4) Writing Quality Rules
- Specific > generic
- Active voice > passive
- Claim + evidence + practical implication
- Honest limitations required (no hype-only reviews)
- Expand every review to be deeply helpful and complete: buyer-fit, trade-offs, testing context, alternatives, and action steps must be explicit.
- Ban filler patterns via `scripts/review_banned_patterns.py`

## 4.1) Semantic Coverage Requirement (mandatory)
Run `scripts/semantic_keyword_planner.py` for every review and naturally incorporate semantically related entities.
- Cover core entity, buyer-intent entities, performance entities, comparison entities, and limitation entities.
- Use natural language variants; do **not** force repetitive exact-match anchors/phrases.
- Quality objective: comprehensive topical coverage with human readability, not keyword stuffing.
- Reference: `references/semantic-keyword-integration.md`

## 5) SEO / AEO / GEO for Reviews
- Title intent: product + review angle + year when relevant
- Answer-first block: 40–70 words
- Review snippets optimized for extraction
- FAQ answers 40–80 words, unique, entity-rich
- Schema alignment only with visible content

## 5.1) Mandatory SERP Gap Analysis (Top-3)
Before finalizing every review:
- run `scripts/serp_gap_top3.py` with top-3 SERP competitor text + current draft
- identify top missing opportunities (up to 20 terms/entities)
- integrate them naturally where they improve clarity and buyer value
- never force terms or degrade readability
- re-run quality gate after integration

Reference: `references/serp-gap-playbook.md`

## 5.2) Mandatory Internal Link Quality
Every generated review must include contextual internal links with rich anchors:
- include at least one cluster/hub link early
- add contextual depth links per major section where naturally relevant
- no generic anchors (click here/read more)
- target anchor length: 3–8 words
- enforce link density/quality via `scripts/internal_link_quality_gate.py`

Reference: `references/internal-link-rich-anchors.md`

## 6) Visual + UX Requirements
- Mobile-first layout integrity
- Comparison/score blocks above fold
- Visual break every 400–600 words
- Product image has descriptive alt text and meaningful caption

Use `scripts/review_visual_density_checker.py` pre-publish.

## 7) Quality Gate (publish blocker)
Run `scripts/review_quality_gate.py` and publish only when >= 85/100.
- >=90: enterprise publish-ready
- 85–89: revise weak dimensions
- <85: rework

## 8) Final Validation
- `scripts/review_publish_validator.py` for technical/editorial checks
- Ensure disclosure near first affiliate link
- Ensure affiliate links use: `target="_blank" rel="sponsored nofollow noopener"`

## 9) Output Contract
Per review, output:
1) brief JSON
2) evidence JSON
3) semantic keyword plan JSON
4) review draft (markdown/html)
5) product box html pack
6) QA report JSON
7) publish validator JSON
