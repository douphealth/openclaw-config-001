# HTML Pattern Library

Production-ready HTML snippet patterns for editorial post enhancement. Copy, paste, and customize.

---

## 1. Summary / Key Takeaway Box

Use near the top of the article (after intro) or at the end as a TL;DR.

```html
<div class="ee-summary-box" style="background: #f0f7ff; border-left: 4px solid #2563eb; padding: 20px 24px; margin: 24px 0; border-radius: 6px;">
  <h3 style="margin: 0 0 12px; color: #1e40af; font-size: 1.1rem;">📋 Key Takeaways</h3>
  <ul style="margin: 0; padding-left: 20px; color: #334155;">
    <li><strong>Takeaway 1</strong> — Brief explanation that adds value.</li>
    <li><strong>Takeaway 2</strong> — Brief explanation that adds value.</li>
    <li><strong>Takeaway 3</strong> — Brief explanation that adds value.</li>
  </ul>
</div>
```

---

## 2. Pro Tip Callout

Use inline where you have genuinely useful advice.

```html
<div class="ee-tip-box" style="background: #ecfdf5; border-left: 4px solid #10b981; padding: 16px 20px; margin: 20px 0; border-radius: 6px;">
  <strong style="color: #065f46;">💡 Pro Tip:</strong>
  <span style="color: #334155;">Your tip content here. Make it specific, actionable, and non-obvious.</span>
</div>
```

---

## 3. Warning / Caution Callout

Use when there's a common mistake or pitfall.

```html
<div class="ee-warning-box" style="background: #fef3c7; border-left: 4px solid #f59e0b; padding: 16px 20px; margin: 20px 0; border-radius: 6px;">
  <strong style="color: #92400e;">⚠️ Watch Out:</strong>
  <span style="color: #334155;">Warning content here. Be specific about what goes wrong and how to avoid it.</span>
</div>
```

---

## 4. Important Note / Info Callout

Use for context, definitions, or clarifications.

```html
<div class="ee-info-box" style="background: #f5f3ff; border-left: 4px solid #7c3aed; padding: 16px 20px; margin: 20px 0; border-radius: 6px;">
  <strong style="color: #5b21b6;">ℹ️ Good to Know:</strong>
  <span style="color: #334155;">Informational content that provides useful context.</span>
</div>
```

---

## 5. Best Pick / Editor's Choice

For affiliate content — highlight a top recommendation.

```html
<div class="ee-best-pick" style="background: linear-gradient(135deg, #fefce8, #fef9c3); border: 2px solid #eab308; padding: 24px; margin: 28px 0; border-radius: 8px; text-align: center;">
  <h3 style="margin: 0 0 8px; color: #854d0e; font-size: 1.15rem;">🏆 Editor's Pick</h3>
  <p style="margin: 0 0 16px; color: #713f12; font-size: 1.05rem;"><strong>Product/Tool Name</strong></p>
  <p style="margin: 0 0 16px; color: #334155;">One sentence on why this is the pick. Be specific.</p>
  <a href="/your-affiliate-link" style="display: inline-block; background: #2563eb; color: #fff; padding: 12px 28px; border-radius: 6px; text-decoration: none; font-weight: 600;">Check Price →</a>
</div>
```

---

## 6. Comparison Table

For product comparisons, feature breakdowns, or side-by-side analysis.

```html
<div class="ee-comparison-table" style="overflow-x: auto; margin: 28px 0;">
  <table style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
    <thead>
      <tr style="background: #1e293b; color: #fff;">
        <th style="padding: 14px 16px; text-align: left;">Feature</th>
        <th style="padding: 14px 16px; text-align: center;">Option A</th>
        <th style="padding: 14px 16px; text-align: center;">Option B</th>
        <th style="padding: 14px 16px; text-align: center;">Option C</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background: #f8fafc;">
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0;"><strong>Price</strong></td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0; text-align: center;">$49</td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0; text-align: center;">$79</td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0; text-align: center;">$29</td>
      </tr>
      <tr>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0;"><strong>Key Feature</strong></td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0; text-align: center;">✅</td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0; text-align: center;">✅</td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0; text-align: center;">❌</td>
      </tr>
      <tr style="background: #f8fafc;">
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0;"><strong>Best For</strong></td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0; text-align: center;">Beginners</td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0; text-align: center;">Pros</td>
        <td style="padding: 12px 16px; border-bottom: 1px solid #e2e8f0; text-align: center;">Budget</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## 7. FAQ Section (Schema-Ready)

Place near the bottom of the article, before the conclusion.

```html
<div class="ee-faq-section" style="margin: 32px 0; padding: 0;">
  <h2 style="margin-bottom: 20px; color: #1e293b;">Frequently Asked Questions</h2>

  <div class="ee-faq-item" style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 10px; color: #334155; font-size: 1.05rem;">❓ Question phrased as users would search it?</h3>
    <p style="margin: 0; color: #475569; line-height: 1.7;">Direct, comprehensive answer. Start with the answer, then add context. Keep it 2-4 sentences.</p>
  </div>

  <div class="ee-faq-item" style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 10px; color: #334155; font-size: 1.05rem;">❓ Another common question?</h3>
    <p style="margin: 0; color: #475569; line-height: 1.7;">Answer here.</p>
  </div>
</div>
```

**Matching FAQ Schema (add to page head or via plugin):**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question phrased as users would search it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Direct, comprehensive answer. Start with the answer, then add context."
      }
    }
  ]
}
</script>
```

---

## 8. Step-by-Step / How-To Block

For guides and tutorials.

```html
<div class="ee-howto-block" style="margin: 28px 0;">
  <div class="ee-step" style="display: flex; gap: 16px; margin-bottom: 20px; align-items: flex-start;">
    <div style="background: #2563eb; color: #fff; min-width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1rem;">1</div>
    <div>
      <h4 style="margin: 0 0 6px; color: #1e293b;">Step Title</h4>
      <p style="margin: 0; color: #475569; line-height: 1.7;">Description of what to do in this step. Be specific and actionable.</p>
    </div>
  </div>
  <div class="ee-step" style="display: flex; gap: 16px; margin-bottom: 20px; align-items: flex-start;">
    <div style="background: #2563eb; color: #fff; min-width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1rem;">2</div>
    <div>
      <h4 style="margin: 0 0 6px; color: #1e293b;">Step Title</h4>
      <p style="margin: 0; color: #475569; line-height: 1.7;">Description of what to do in this step.</p>
    </div>
  </div>
</div>
```

---

## 9. Pros & Cons Block

For product reviews and comparisons.

```html
<div class="ee-pros-cons" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 24px 0;">
  <div style="background: #ecfdf5; border-radius: 8px; padding: 20px;">
    <h4 style="margin: 0 0 12px; color: #065f46;">✅ Pros</h4>
    <ul style="margin: 0; padding-left: 18px; color: #334155;">
      <li>Specific, verifiable pro</li>
      <li>Another real advantage</li>
      <li>Third genuine benefit</li>
    </ul>
  </div>
  <div style="background: #fef2f2; border-radius: 8px; padding: 20px;">
    <h4 style="margin: 0 0 12px; color: #991b1b;">❌ Cons</h4>
    <ul style="margin: 0; padding-left: 18px; color: #334155;">
      <li>Honest limitation</li>
      <li>Another real drawback</li>
      <li>Third genuine con</li>
    </ul>
  </div>
</div>
```

---

## 10. Table of Contents (Sticky / Jump Links)

For long-form content (2,000+ words).

```html
<nav class="ee-toc" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px 24px; margin: 24px 0;">
  <h3 style="margin: 0 0 12px; color: #1e293b; font-size: 1rem;">📑 In This Article</h3>
  <ol style="margin: 0; padding-left: 20px; color: #475569; line-height: 2;">
    <li><a href="#section-1" style="color: #2563eb; text-decoration: none;">Section One Title</a></li>
    <li><a href="#section-2" style="color: #2563eb; text-decoration: none;">Section Two Title</a></li>
    <li><a href="#section-3" style="color: #2563eb; text-decoration: none;">Section Three Title</a></li>
  </ol>
</nav>
```

---

## 11. Disclosure / Affiliate Notice

Required for FTC compliance on affiliate content. Place prominently.

```html
<div class="ee-disclosure" style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 6px; padding: 14px 18px; margin: 20px 0; font-size: 0.9rem; color: #92400e;">
  <strong>FTC Disclosure:</strong> This article contains affiliate links. If you purchase through our links, we may earn a commission at no extra cost to you. We only recommend products we've thoroughly researched and believe provide genuine value. <a href="/disclosure" style="color: #92400e;">Learn more about our review process →</a>
</div>
```

---

## 12. Author Bio Box

For E-E-A-T signals. Place after the article body, before FAQ.

```html
<div class="ee-author-box" style="display: flex; gap: 16px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 28px 0; align-items: flex-start;">
  <img src="/path/to/author-photo.jpg" alt="Author Name" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover;" loading="lazy" />
  <div>
    <p style="margin: 0 0 4px; font-weight: 700; color: #1e293b;">Written by Author Name</p>
    <p style="margin: 0 0 8px; font-size: 0.85rem; color: #64748b;">Role / Credential · Updated: March 2026</p>
    <p style="margin: 0; color: #475569; line-height: 1.6; font-size: 0.95rem;">Brief bio establishing expertise. Include relevant credentials, years of experience, and why they're qualified to write about this topic.</p>
  </div>
</div>
```

---

## 13. Bad vs Good Contrast Block

For teaching concepts with concrete examples.

```html
<div class="ee-bad-good" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 24px 0;">
  <div style="background: #fef2f2; border-radius: 8px; padding: 20px;">
    <h4 style="margin: 0 0 12px; color: #991b1b;">❌ Don't Do This</h4>
    <p style="margin: 0; color: #475569; line-height: 1.7;">Concrete example of what NOT to do, with explanation of why it fails.</p>
  </div>
  <div style="background: #ecfdf5; border-radius: 8px; padding: 20px;">
    <h4 style="margin: 0 0 12px; color: #065f46;">✅ Do This Instead</h4>
    <p style="margin: 0; color: #475569; line-height: 1.7;">Concrete example of the correct approach, with explanation of why it works.</p>
  </div>
</div>
```

---

## 14. Last Updated / Freshness Banner

Signals content freshness for both users and crawlers.

```html
<div class="ee-freshness" style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 12px 18px; margin: 16px 0; font-size: 0.9rem; color: #166534;">
  🔄 <strong>Last Updated:</strong> March 2026 — This guide has been fully revised with current pricing, features, and recommendations.
</div>
```

---

## 15. Content Upgrade / Lead Magnet CTA

Inline email capture block.

```html
<div class="ee-lead-cta" style="background: linear-gradient(135deg, #eff6ff, #dbeafe); border: 2px solid #93c5fd; border-radius: 8px; padding: 24px; margin: 28px 0; text-align: center;">
  <h3 style="margin: 0 0 8px; color: #1e40af;">📥 Free Download</h3>
  <p style="margin: 0 0 16px; color: #334155;">Get our [Specific Lead Magnet Name] — a [format] that helps you [specific benefit].</p>
  <form style="display: flex; gap: 8px; max-width: 420px; margin: 0 auto;">
    <input type="email" placeholder="Enter your email" style="flex: 1; padding: 10px 14px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 0.95rem;" />
    <button type="submit" style="background: #2563eb; color: #fff; padding: 10px 20px; border: none; border-radius: 6px; font-weight: 600; cursor: pointer;">Get It Free</button>
  </form>
  <p style="margin: 8px 0 0; font-size: 0.8rem; color: #64748b;">No spam. Unsubscribe anytime.</p>
</div>
```

---

## 16. Image Figure with Caption

For optimized images with proper semantics.

```html
<figure style="margin: 24px 0; text-align: center;">
  <img src="/path/to/image.webp" alt="Descriptive alt text with keyword naturally included" style="max-width: 100%; height: auto; border-radius: 8px;" loading="lazy" width="800" height="450" />
  <figcaption style="margin-top: 8px; font-size: 0.9rem; color: #64748b; font-style: italic;">Descriptive caption that adds context beyond the alt text.</figcaption>
</figure>
```

---

## Usage Rules

1. **Don't stack multiple callouts in sequence** — space them out with regular content between.
2. **Use max 1-2 callout types per 1,000 words** — visual variety without visual noise.
3. **Comparison tables** — keep to 3-5 columns max for mobile readability.
4. **Every visual element must earn its place** — if it doesn't add comprehension, cut it.
5. **Mobile-first** — test every pattern at 375px width.
6. **Accessibility** — ensure sufficient color contrast, semantic HTML, and alt text.
