# SOTA HTML Visual Component Library (WordPress Blog Mastery v4)

Use these components to upgrade readability, retention, conversion, and trust.

## Design Principles
- Mobile-first (works at 375px)
- Lightweight (pure CSS, no JS required)
- Accessible (semantic tags + ARIA)
- Performance-safe (no layout shift)
- WordPress-compatible (Block Editor / Classic / builders)

---
## CSS Foundation (add once)
```css
:root {
  --oc-primary:#2563eb; --oc-primary-light:#dbeafe; --oc-primary-dark:#1e40af;
  --oc-success:#16a34a; --oc-success-light:#dcfce7;
  --oc-warning:#d97706; --oc-warning-light:#fef3c7;
  --oc-danger:#dc2626; --oc-danger-light:#fee2e2;
  --oc-neutral-50:#fafafa; --oc-neutral-100:#f5f5f5; --oc-neutral-200:#e5e5e5;
  --oc-neutral-600:#525252; --oc-neutral-800:#262626; --oc-neutral-900:#171717;
  --oc-space-xs:.25rem; --oc-space-sm:.5rem; --oc-space-md:1rem; --oc-space-lg:1.5rem; --oc-space-xl:2rem;
  --oc-radius-sm:.375rem; --oc-radius-md:.5rem; --oc-radius-lg:.75rem; --oc-radius-xl:1rem;
  --oc-shadow-sm:0 1px 2px rgba(0,0,0,.05); --oc-shadow-md:0 4px 6px -1px rgba(0,0,0,.07);
}
.oc-article{max-width:42rem;margin:0 auto;padding:0 var(--oc-space-md);line-height:1.7;color:var(--oc-neutral-800)}
.oc-article>*+*{margin-top:var(--oc-space-lg)}
.oc-article img{max-width:100%;height:auto;border-radius:var(--oc-radius-md)}
.related-reading{background:var(--oc-neutral-50);border:1px solid var(--oc-neutral-200);padding:var(--oc-space-md);border-radius:var(--oc-radius-md)}
```

---
## Component 1: Hero Zone
```html
<header class="oc-hero" role="banner">
  <div class="oc-hero__meta">Author · Date · Read Time · Updated Date</div>
</header>
```

## Component 2: Answer-First Block
```html
<div class="oc-answer-block" role="region" aria-label="Quick Answer">
  <p><strong>Quick Answer:</strong> Direct 40–70 word answer.</p>
</div>
```

## Component 3: Quick Verdict / Top Picks
```html
<div class="oc-picks" role="region" aria-label="Top Picks Summary">
  <article class="oc-picks__card">🏆 Best Overall ...</article>
</div>
```

## Component 4: Table of Contents
```html
<nav class="oc-toc" aria-label="Table of Contents">
  <details open><summary>📑 Table of Contents</summary><ol><li><a href="#sec1">Section 1</a></li></ol></details>
</nav>
```

## Component 5: Key Takeaway Callout
```html
<aside class="oc-callout oc-callout--key" role="note"><strong>Key Takeaway:</strong> ...</aside>
```

## Component 6: Pros & Cons
```html
<div class="oc-proscons"><section>👍 Pros...</section><section>👎 Cons...</section></div>
```

## Component 7: Comparison Table (Responsive)
```html
<div class="oc-table-wrap" role="region" aria-label="Comparison"><table class="oc-table">...</table></div>
```

## Component 8: Step-by-Step Module
```html
<div class="oc-steps" role="list"><article class="oc-step" role="listitem">...</article></div>
```

## Component 9: FAQ Accordion
```html
<section class="oc-faq" aria-label="Frequently Asked Questions">
  <details><summary>Question?</summary><p>Answer...</p></details>
</section>
```

## Component 10: Verdict Box
```html
<div class="oc-verdict"><h3>Our Verdict</h3><p>Summary + limitations.</p></div>
```

## Component 11: Stat Highlights
```html
<div class="oc-stats" role="region" aria-label="Key Statistics"><div class="oc-stat">...</div></div>
```

## Component 12: Affiliate Disclosure Banner
```html
<aside class="oc-disclosure" role="note"><strong>Disclosure:</strong> Affiliate links may earn commission.</aside>
```

## Component 13: Related Reading Grid
```html
<nav class="oc-related" aria-label="Related Articles"><a class="oc-related__card" href="/guide">...</a></nav>
```

## Component 14: Methodology / Trust Footer
```html
<footer class="oc-trust" role="contentinfo"><h3>Editorial Process</h3><p>Method + update cadence + reviewer.</p></footer>
```

## Component 15: Checklist Block
```html
<div class="oc-checklist" role="list"><label role="listitem"><input type="checkbox">Step</label></div>
```

## Component 16: Expert Quote
```html
<blockquote class="oc-quote"><p>"Quote"</p><footer>— Expert</footer></blockquote>
```

---
## Quick-Reference Matrix
| # | Component | Use When | Content Types |
|---|---|---|---|
| 1 | Hero Zone | Every post | All |
| 2 | Answer-First | Every post | All |
| 3 | Quick Picks | Above-fold summary | Best-of, Comparison |
| 4 | TOC | >2,000 words | Long-form |
| 5 | Key Callout | Insight peaks | All |
| 6 | Pros/Cons | Option evaluation | Review, Best-of |
| 7 | Comparison Table | 3+ options | Comparison, Best-of |
| 8 | Step Module | Sequential tasks | How-to |
| 9 | FAQ Accordion | Bottom Q&A | All |
| 10 | Verdict Box | Final recommendation | Review, Comparison |
| 11 | Stat Highlight | Data emphasis | Data-heavy |
| 12 | Disclosure Banner | Near first affiliate link | Commercial |
| 13 | Related Reading | Pre-footer retention | All |
| 14 | Trust Footer | Bottom of post | All |
| 15 | Checklist | Setup/audit tasks | How-to, Guide |
| 16 | Expert Quote | E-E-A-T support | All |

## Component Assembly Per Content Type (CSV-ready)
| Content Type | Required Components | Optional Components |
|---|---|---|
| Best-Of Roundup | 1,2,3,4,6,7,9,10,12,13,14 | 5,11,16 |
| Head-to-Head Comparison | 1,2,4,6,7,9,10,12,13,14 | 3,5,11 |
| In-Depth Review | 1,2,6,9,10,12,13,14 | 4,5,7,11,16 |
| How-To Guide | 1,2,4,8,9,13,14 | 5,15,16 |
| Explainer/Definition | 1,2,4,9,13,14 | 5,11,16 |
| Comprehensive Guide | 1,2,4,5,9,13,14 | 7,8,11,15,16 |
| Tactical Listicle | 1,2,9,13,14 | 4,5 |
| Case Study | 1,2,11,9,13,14 | 4,5,16 |

## Visual Rhythm Rules
- Insert at least **one visual component every 400–600 words**.
- On mobile (375px), never allow more than **3 consecutive paragraphs** without a visual break (component, image, table, list, or callout).
- If violated, add a component before publish.

### Recommended Visual Cadence
1. Hook (~150 words) -> Component 2 (Answer-First)
2. Context (~200 words) -> Component 3 or 11
3. Section block (~400 words) -> Component 5/7/8
4. Section block (~400 words) -> Component 6/7
5. Section block (~400 words) -> Component 16/5
6. Section block (~400 words) -> Component 7/15
7. Verdict (~200 words) -> Component 10
8. FAQ -> Component 9
9. Close -> Components 13 + 14

## Internal Linking Opportunities by Component
| Component | Link Opportunity |
|---|---|
| Answer-First Block | 1 hub link inside answer text |
| Quick Picks Table | “Read full review” links (in-page + related internal destinations) |
| Callout Box | Natural deep-dive link (“detailed guide to X”) |
| Pros/Cons | Link specific pro/con to relevant comparison content |
| Steps | Link tool/resource mentions to tutorials |
| FAQ | 1 internal link per 2–3 answers |
| Verdict Box | Link alternatives/deeper comparison |
| Related Reading | 3–5 curated contextual internal links |
