| name | description | version |
|------|-------------|--------|
| wordpress-visual-assets | SOTA visual content creation and optimization for blog posts. Generates/optimizes featured images, in-article graphics, infographics, comparison charts, and product imagery. Handles image specs, compression, alt-text generation, and visual compliance. Integrates with wordpress-blog-mastery for content enrichment. | 3.0 |

# WordPress Visual Assets v3.0

Enterprise-grade visual content production and optimization engine. Handles end-to-end image creation, optimization, alt-text generation, and visual asset integration for SOTA blog posts.

## Core Philosophical Pillars

1. **Visual-Narrative Alignment:** Images must reinforce the text, not just decorate it.
2. **Performance-First Design:** Maximum visual impact with minimum file weight (WebP, <100KB).
3. **Accessibility as Standard:** Every image serves readers using assistive technology via descriptive alt-text.
4. **Mobile-First Clarity:** All graphics, tables, and product boxes must be perfectly legible on 375px screens.

---

## PART I: IMAGE PRODUCTION & OPTIMIZATION

### 1.1 Featured Image Generation (The Social/Search Hook)

**Goal:** Create click-worthy featured images (1200x630px, <100KB).

| Spec | Requirement |
|------|-------------|
| **Dimensions** | 1200 x 630 px (1.91:1 ratio). |
| **Format** | WebP primary; PNG/JPG fallback. |
| **File Size** | < 100 KB (WebP) or < 200 KB (PNG). |
| **Filename** | `{slug}-featured-1200x630.webp` |
| **Design** | Headline must be legible at 300px width. |

### 1.2 In-Article Graphics & Visual Rhythm

**Goal:** Break the "wall of text" every 400-600 words with custom visuals.

| Component | Use Case |
|-----------|----------|
| **Diagrams/Flows** | Explaining complex processes or step-by-step logic. |
| **Comparison Charts** | feature-by-feature breakdown of products or options. |
| **Infographics** | Synthesizing data or statistical highlights. |
| **Product Boxes** | High-fidelity HTML/CSS showcase cards for affiliate items. |

### 1.3 Alt-Text & Metadata Engineering

Every image must include:
- **Alt-Text:** 70-125 characters, descriptive, including target keyword naturally.
- **Title Tag:** Contextual description (e.g., "Hoka Speedgoat 5 side profile").
- **Caption:** Where appropriate, providing additional context or attribution.
- **Lazy Loading:** `loading="lazy"` for all images below the fold.

---

## PART II: SOTA HTML/CSS COMPONENT DESIGN

Integrated with `wordpress-blog-mastery` for beautiful, interactive post elements.

### 2.1 Responsive Product Box (SOTA DESIGN)
```html
<div class="oc-product-box">
  <div class="oc-product-badge">Top Pick</div>
  <div class="oc-product-content">
    <div class="oc-product-image">
      <!-- IMAGE: Product photo here -->
    </div>
    <div class="oc-product-info">
      <h3>[Product Name]</h3>
      <p>[Punchy 2-3 sentence benefit-first description]</p>
      <div class="oc-product-meta">
        <span class="oc-product-price">[Price/Tier]</span>
        <a href="[URL]" class="oc-btn oc-btn--primary">Check Price</a>
      </div>
    </div>
  </div>
</div>
```

### 2.2 Enterprise Comparison Matrix
- Minimum 3 options, maximum 5.
- "Best For" row required.
- Mobile-scrollable overflow wrapper.

---

## PART III: EXECUTION & QUALITY METRICS

### 7 Core Workflows

1. **Featured Image Generation:** 1200x630px social/SERP hook creation.
2. **In-Article Graphics Generation:** Diagrams and infographics for visual rhythm.
3. **Comparison Chart + Product Box:** Visual synthesis for review content.
4. **Image Optimization + Compression:** Batch conversion to WebP and size reduction.
5. **Alt-Text Batch Generation:** Contextual SEO-aware accessibility engineering.
6. **Brand Alignment Check:** Audit visuals for color and typography consistency.
7. **SERP Image Optimization:** Ensuring images meet Google's indexing guidelines.

### Quality Metrics

| Metric | Target |
|--------|--------|
| **Featured Image Size** | < 100 KB |
| **In-Article Image Size** | < 80 KB |
| **Alt-Text Completion** | 100% |
| **Format Compliance** | WebP (Primary) |
| **Visual Rhythm** | Component break every 400-600 words. |
| **Mobile Legibility** | 100% (verified at 375px). |

---

## Integration with Other Skills

- **wordpress-blog-mastery:** Receives placement cues and visual asset briefs.
- **seo-intelligence:** Provides keyword data for alt-text and filenames.
- **conversion-optimizer:** Designs product showcase cards and affiliate buttons.
- **technical-seo-health:** Provides image load-time and Core Web Vitals reports.
