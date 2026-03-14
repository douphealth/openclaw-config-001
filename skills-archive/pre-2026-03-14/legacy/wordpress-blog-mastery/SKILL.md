---
name: wordpress-blog-mastery
description: Definitive WordPress blog writing system for enterprise-grade, conversion-safe, AI-visible content. Use when writing, rewriting, improving, or auditing WordPress blog posts of any type (review, comparison, best-of, how-to, explainer, listicle, case study, editorial, news, comprehensive guide). Includes content-type routing, evidence-first research, writing-craft quality gates, internal-linking intelligence, scroll-depth post architecture, and a modern reusable HTML/CSS component library.
---

# WordPress Blog Mastery v4

Execute in order: **Research → Architecture → Draft → Enhance UX → Revise → Publish → Monitor**.

## A) Content-Type Routing (mandatory)
Run `scripts/content_type_router.py` first. Use detected type to select section architecture and evidence density.

## B) Research + Evidence
- Build brief: `scripts/content_brief_generator.py`
- Build evidence slots: `scripts/evidence_bank_builder.py`
- Enforce dated/verified source references.

## C) Internal Linking Intelligence Engine (new)
Run `scripts/internal_linking_intelligence.py` with current post + candidate targets.
It returns:
- link count targets by content type
- recommended placements by section intent
- anchor diversity controls
- anti-over-optimization guardrails
- cluster-aware hub/spoke routing suggestions

Load `references/internal-linking-intelligence.md` when planning links.

## D) Perfect Post Structure Architecture (new)
Run `scripts/post_structure_architect.py` to generate a scroll-depth-aware section plan:
- above-the-fold hook + answer-first
- 25% scroll checkpoint
- 50% retention module
- 75% synthesis + action block
- end-of-post FAQ + trust footer

Load `references/perfect-post-structure.md` for type-specific templates.

## E) SOTA Visual HTML Component Library (new)
Use `assets/html-component-library.md` to apply production-ready components:
- hero/summary/quick-answer modules
- comparison tables + pros/cons cards
- step blocks, checkpoints, callouts, decision trees
- FAQ accordion, trust footer, disclosure blocks
- mobile-safe spacing and typography presets

Rule: components must improve comprehension/decision support, not decoration.

## F) Writing Craft + Readability
- Ban filler patterns: `scripts/banned_pattern_scanner.py`
- Analyze readability: `scripts/readability_analyzer.py`
- Generate hooks: `scripts/hook_template_generator.py`
- Require natural semantic coverage for entities/subtopics tied to intent (no keyword stuffing).

## F.1) Mandatory SERP Gap Analysis for every post
- Compare current draft against top-3 ranking pages for the target query.
- Extract top 20 missing high-value terms/entities.
- Integrate naturally only where they improve usefulness, completeness, and clarity.
- Re-run quality gate after integration.
- Use: `scripts/serp_gap_top3.py` (added to this skill).

## F.2) Mandatory Internal Link Quality for every post
- Add rich contextual internal links with descriptive anchors (3–8 words).
- Place links in high-value sections (early section + core bodies + next steps).
- Ban generic anchors and forced links.
- Validate before publish with `scripts/internal_link_quality_gate.py`.

## G) Quality Gate (publish blocker)
Run `scripts/quality_gate.py`.
Thresholds:
- >=90 publish-ready
- 85–89 revise weak dimensions
- <85 continue revision loop

## H) Publish Checklist
Run `scripts/publish_checklist_validator.py`.
Require canonical/schema/mobile/disclosure/link integrity pass.

## I) References
- `references/content-type-architectures.md`
- `references/internal-linking-intelligence.md`
- `references/perfect-post-structure.md`
- `references/visual-placement-logic.md`
- `references/hook-engineering-playbook.md`
- `references/evidence-integration-patterns.md`
- `references/readability-engineering.md`
- `references/conversion-architecture.md`
- `references/revision-protocol.md`
- `references/quality-scoring-rubric.md`
- `references/banned-patterns.md`
- `references/sota-content-template.md`

## J) Output Contract
For each post, produce:
1) brief JSON
2) evidence bank JSON
3) structure plan JSON
4) internal link plan JSON
5) draft markdown/html
6) quality report JSON
7) publish checklist report JSON
8) 30-day monitoring actions


## K) Pre-Publish Quality Gate (complete)
### Content Quality
- [ ] Quality score >=85/100
- [ ] Zero banned writing patterns
- [ ] All claims grounded or qualified
- [ ] Read-aloud test passed on intro + conclusion
- [ ] Evidence density meets content-type minimum
- [ ] Voice/tone calibrated for niche

### Post Structure
- [ ] Hero zone complete (author/date/read-time/updated)
- [ ] Hook 100-150 words
- [ ] Answer-first block 40-70 words
- [ ] Quick summary block present
- [ ] TOC present when >2,000 words
- [ ] Methodology/context section present
- [ ] Retention hook between major sections
- [ ] FAQ 6-10 unique answers
- [ ] Related reading 3-5 curated links
- [ ] Trust footer complete

### Internal Linking
- [ ] Hub link present early
- [ ] Link count in range by length
- [ ] Anchors descriptive, varied, 3-8 words
- [ ] No generic anchors / exact-match repetition
- [ ] No section >500 words without internal link
- [ ] 2-3 links in top 30% of content
- [ ] Targets return 200
- [ ] Orphan prevention inbound links queued

### Visual Design
- [ ] Visual component every 400-600 words
- [ ] Required components for content type present
- [ ] Mobile 375px no wall-of-text
- [ ] Image alt text + lazy-load below fold
- [ ] Tables mobile-scrollable with decision column
- [ ] No layout shift; dark mode sanity

### SEO/Technical
- [ ] Title/H1/meta/slug/canonical/schema valid
- [ ] No robots conflicts; OG/Twitter set
- [ ] CWV budget remains stable post-components

### Monetization (if applicable)
- [ ] Disclosure near first affiliate link
- [ ] Affiliate rel attrs: sponsored nofollow noopener
- [ ] CTA language contextual/non-manipulative
- [ ] Commercial blocks integrated editorially

## L) Additional references and scripts
References:
- references/internal-linking-playbook.md
- references/semantic-anchor-text-guide.md
- references/post-structure-blueprints.md
- references/html-component-library.md
- references/visual-rhythm-guide.md
- references/mobile-design-checklist.md
- references/dark-mode-testing.md

Scripts:
- scripts/internal_link_mapper.py
- scripts/anchor_text_generator.py
- scripts/anchor_text_auditor.py
- scripts/orphan_page_detector.py
- scripts/visual_component_assembler.py
- scripts/mobile_visual_density_checker.py
- scripts/internal_link_audit.py
