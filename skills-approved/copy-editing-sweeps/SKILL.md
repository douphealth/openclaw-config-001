---
name: copy-editing-sweeps
description: Use when improving existing marketing copy through systematic editing passes rather than writing from scratch. Triggers on requests to edit copy, polish a draft, tighten language, remove fluff, improve clarity, strengthen proof, increase specificity, or review conversion copy line by line.
---

# Copy Editing Sweeps

## Do NOT Use This For
- writing new content from scratch (use `conversion-copywriting`)
- full article enhancement with SEO (use `editorial-post-enhancement`)

## Purpose
Improve existing copy without losing its core message by editing in focused, sequential passes.

## Use this when
There is already a draft and the job is to improve it. Not for new positioning or full rewrite from zero (use `conversion-copywriting`). Not for full blog-post upgrade with SEO polish (use `editorial-post-enhancement`).

## Decision Tree

```
Copy needs improvement?
├── Don't understand what it says? → Start with Clarity pass
├── Sounds generic/boring? → So-What + Specificity passes
├── Claims feel unsupported? → Proof pass
├── Doesn't convert? → Emotion + Risk Reduction passes
├── Voice feels off? → Voice & Tone pass
└── Everything needs work? → Full sweep sequence (all 7 passes)
```

## Sweep Sequence (Run in Order)

### Pass 1: Clarity
**Goal**: Remove confusion, overpacked sentences, jargon, and ambiguity.

| Problem | Fix |
|---|---|
| Sentences >25 words | Split or restructure |
| Jargon without definition | Plain language or brief explanation |
| Ambiguous pronouns (it, this, they) | Replace with specific noun |
| Double negatives | Rewrite as positive statement |
| Passive voice (when it obscures who does what) | Active voice with clear subject |

**Test**: Can a smart 15-year-old understand this on first read?

### Pass 2: Voice & Tone Consistency
**Goal**: Keep the tone consistent and on-brand throughout.

| Check | Question |
|---|---|
| Formality level | Does it shift between casual and corporate? |
| Person | Does it switch between "you," "we," "one"? |
| Energy level | Does enthusiasm spike and drop randomly? |
| Brand vocabulary | Are key terms used consistently? |

**Rule**: Don't erase the original voice unless it's actively hurting the piece.

### Pass 3: So-What / Benefit Depth
**Goal**: Connect every claim to consequences for the reader.

| Problem | Fix |
|---|---|
| Feature stated without benefit | Add "which means..." clause |
| Benefit stated without impact | Add "so you can..." or "without..." clause |
| Abstract value claim | Make concrete: "Save time" → "Cut your invoicing from 2 hours to 15 minutes" |

**Formula**: Feature → Benefit → Consequence → Stakes
"We use AES-256 encryption (feature) so your data stays protected (benefit) even if our servers are compromised (consequence) — your client records never leak (stakes)."

### Pass 4: Proof
**Goal**: Support important claims or soften unprovable ones.

| Claim Type | Proof Strategy |
|---|---|
| Performance claim ("increases sales") | Case study, before/after data, testimonial with numbers |
| Capability claim ("we do X") | Portfolio item, process description, credentials |
| Comparison claim ("better than Y") | Third-party review, head-to-head data, independent test |
| Opinion/preference claim | Testimonial, user quote, community signal |

**Softening language** for claims without proof:
- "Works for everyone" → "Used by 2,000+ teams"
- "Best in the industry" → "Rated #1 by [source]"
- "Guaranteed results" → "See results in [timeframe] or get [remedy]"

### Pass 5: Specificity
**Goal**: Replace vague abstractions with concrete detail.

| Vague | Specific |
|---|---|
| "Save time" | "Reclaim 6+ hours per week" |
| "Many customers" | "14,000 businesses" |
| "Fast results" | "Results in under 72 hours" |
| "High quality" | "Hand-reviewed by senior editors" |
| "Affordable" | "Starting at $29/month" |

**Rule**: Numbers, names, dates, and specific nouns beat adjectives every time.

### Pass 6: Emotion & Stakes
**Goal**: Increase felt relevance without melodrama.

| Technique | Example |
|---|---|
| Name the pain they feel now | "You're spending Sunday nights dreading Monday's inbox" |
| Show the cost of inaction | "Every week without this is another week of manual reporting" |
| Contrast before/after states | "From scrambling to publish → from content calendar to autopilot" |
| Use concrete scenarios | "When the client asks for the report at 4 PM..." |

**Caution**: Emotional language that doesn't match the audience's self-image backfires. B2B buyers don't want to feel "desperate." They want to feel "strategic."

### Pass 7: Risk Reduction Near CTA
**Goal**: Reduce hesitation at action points.

| Risk | Reduction |
|---|---|
| "Will this work for me?" | Specific testimonial from similar persona |
| "What if I waste money?" | Guarantee, trial, or case study with ROI |
| "Is this complicated?" | "Set up in 5 minutes" or "No credit card required" |
| "Am I locked in?" | "Cancel anytime" or "No long-term contract" |
| "Can I trust this company?" | Social proof count, recognizable logos, third-party reviews |

**Location**: Risk reducers should appear in the 2-3 paragraphs before the CTA, not buried at the top.

## Quality Scoring Matrix

Rate each dimension 1-5 after the final pass:

| Dimension | 1 (Weak) | 3 (Acceptable) | 5 (Strong) |
|---|---|---|---|
| Clarity | Confusing on first read | Understandable but dense | Crystal clear |
| Voice consistency | Tonal shifts throughout | Mostly consistent | Distinct and steady |
| Benefit depth | Features only | Benefits stated | Consequences with stakes |
| Proof | Unsubstantiated claims | Some evidence | Claims backed by specifics |
| Specificity | Vague generalities | Mix of vague and specific | Concrete throughout |
| Emotion relevance | Flat or melodramatic | Some resonance | Feels personal |
| Risk reduction | None | Basic guarantee | Preempts all major objections |

**Minimum publish score**: 28/35 (average 4/5). Below that, do another targeted pass.

## Before/After Examples

### Clarity
- **Before**: "Our platform leverages advanced AI-driven methodologies to optimize your workflow efficiency."
- **After**: "Our AI finds bottlenecks in your workflow and suggests fixes — most teams save 6 hours a week."

### Specificity
- **Before**: "Trusted by thousands of businesses worldwide."
- **After**: "Trusted by 14,200 businesses across 83 countries — including Shopify, HubSpot, and Stripe."

### Proof
- **Before**: "Our clients see incredible results."
- **After**: "Revenue Cat increased trial-to-paid conversion by 34% in 90 days using our onboarding sequence."

## Output Template

```markdown
## Copy Edit: [Page/Asset Name]
**Sweeps completed**: [list which passes]
**Quality score**: [X/35]

### Top Issues Found
1. [Issue + which pass caught it]
2. [Issue + which pass caught it]
3. [Issue + which pass caught it]

### Key Changes
| Line/Area | Before | After | Why |
|---|---|---|---|
[Top 3-5 changes]

### Revised Copy
[Full revised text]

### Remaining Notes
[Anything the owner should address that's outside editing scope]
```

## Performance Optimizations

### Speed Multipliers
- Use proven copy frameworks as starting point (don't start from blank)
- Generate 5 headline options simultaneously, pick best 2-3
- Pull customer language from existing reviews/testimonials
- Template-based copy structures for each page type
- Parallel research (audience, competitors, proof points)

### Self-Critique Scorecard (/25)
1. **Clarity** (1-5): Could a stranger understand in 10 seconds?
2. **Specificity** (1-5): Numbers/examples over vague claims?
3. **Persuasion** (1-5): Does it move toward the CTA?
4. **Proof** (1-5): Social proof near CTAs? Objections addressed?
5. **Polish** (1-5): No filler or corporate sludge?

**Target: 22+/25**

### Auto-Check
- [ ] No generic claims without specifics
- [ ] No feature dumps without outcomes
- [ ] CTA is obvious and action-oriented
- [ ] Proof elements placed near conversions
- [ ] Score logged to memory

## SOTA Editing Upgrade Layer
- When editing search-facing or revenue-facing pages, preserve and strengthen extractability: direct answers, scannable headings, specific proof, and quotable lines.
- Remove fluff that weakens both conversion and citation-worthiness.
- If a page is intended to rank or be cited, prefer edits that improve factual density, trust, and answer clarity — not just style.
- Use `../../skills/shared/references/ai-citation-scorecard.md` when the copy is part of a GEO/AEO-critical asset.

## Output Contract
**Artifact**: Edited copy with tracked changes and improvement rationale
**Evidence**: Before/after examples, quality score, pass-by-pass notes
**Decision**: Editorial approval with quality threshold met
**Next**: Publish, further review, or A/B test revised vs. original

## Checks and Common Mistakes
- Do not rewrite just to sound different.
- Do not erase the original voice unless it is actively hurting the piece.
- Do not strengthen claims beyond available proof.
- Do not edit only for grammar if persuasion is the real issue.
- Do not stop after the first decent pass; weak clarity and weak proof often survive superficial edits.
- Do not add specificity that isn't true — fabricated numbers are worse than vague claims.

## Resources
Read when needed:
- `references/plain-english.md`
- `references/quick-pass-checklist.md`

## Compatibility
- Targets current WordPress 6.9+ where applicable
- REST API + WP-CLI preferred over browser automation
- Batch operations via `_fields` + `per_page=100` + `concurrent.futures`
- Browser automation only when API/CLI insufficient

## Inputs Required (Pre-Flight)
Before executing any task in this skill:
1. **Target identification** — What site, page, post, or system is being operated on?
2. **Auth verification** — Confirm credentials work (test API call or CLI command)
3. **Current state** — Understand what exists before making changes (GET before POST)
4. **Environment** — Production vs staging (assume production unless stated)
5. **Constraints** — No downtime? Preserve SEO? Preserve data? Budget limits?

## Triage Protocol
Before ANY operation:
1. **Identify** — What type of content/system/problem is this?
2. **Check state** — Query current state via API/CLI before modifying
3. **Verify creds** — Confirm authentication works
4. **Plan rollback** — How to undo if something breaks?
5. **Scope check** — Is this a single item or batch? Scale determines approach.

## Speed Optimizations
- **API calls**: Always use `_fields` parameter (80%+ payload reduction)
- **Pagination**: Use `per_page=100` for list endpoints
- **Parallelism**: Use `concurrent.futures` for independent operations (max 10/site)
- **Caching**: Store results in session — never re-fetch same data
- **Batching**: Group similar operations into single API calls where possible
- **Direct CLI**: Use WP-CLI `wp db query` for complex operations

## Error Recovery (Auto-Learning)
- Track error patterns — after 2 failures, try alternative approach
- Log recurring fixes to `memory/YYYY-MM-DD.md`
- Update references when new patterns discovered
- Rollback plan: Know how to undo before making changes

## Self-Critique Scorecard (/25)
Before claiming complete, score yourself:
1. **Triage** (1-5): Was current state fully understood before changes?
2. **Execution** (1-5): Was the operation clean, efficient, correct?
3. **Verification** (1-5): Was the result verified via API/live check?
4. **Rollback** (1-5): Can changes be undone if issues found?
5. **Learning** (1-5): Were new patterns documented for future use?

**Target: 22+/25**

## Output Contract
- **Artifact**: What was created/changed/deleted
- **Evidence**: API response proof + live verification
- **Decision**: Success/failure with reasoning
- **Next**: What follow-up is needed (if any)
