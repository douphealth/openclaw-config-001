| name | description | version |
|------|-------------|--------|
| wordpress-visual-assets | SOTA visual content creation and optimization for blog posts. Generates/optimizes featured images, in-article graphics, infographics, comparison charts, and product imagery. Handles image specs, compression, alt-text generation, and visual compliance. Integrates with wordpress-blog-mastery for content enrichment. | 3.0 |

# WordPress Visual Assets

Enterprise-grade visual content production and optimization engine. Handles end-to-end image creation, optimization, alt-text generation, and visual asset integration for blog posts.

## Own

- **Featured image generation & optimization** — AI-powered or template-based SOTA designs (1200x630px, <100KB, SEO-optimized filenames)
- **In-article graphics creation** — Diagrams, process flows, step-by-step visuals, infographics aligned to article content
- **Comparison charts & tables** — Visual comparisons (product vs. product, feature matrices), designed for mobile + desktop
- **Product box design** — SOTA HTML/CSS product showcase cards (for affiliate integration)
- **Image specifications & compression** — WebP + fallback PNG/JPG, responsive srcset, lazy-loading optimization
- **Alt-text generation** — SEO-optimized, accessible alt text (max 125 chars, includes context + keyword if natural)
- **Image filename optimization** — SEO-friendly names (e.g., `how-to-run-faster-400x300.webp` not `IMG_12345.jpg`)
- **Visual consistency** — Brand color palette adherence, typography matching, design system alignment
- **SERP image optimization** — Ensure featured images meet Google's image search guidelines
- **AEO visual compliance** — Images match text content (no generic stock photos unrelated to article)

## Do NOT Own

- **Article content/copywriting** (wordpress-blog-mastery)
- **SEO strategy/keyword targeting** (seo-intelligence)
- **Affiliate link placement** (conversion-optimizer)
- **Animation/video** — Static imagery only; video is separate skill

## Decision Matrix: Which Workflow to Run

| Signal | Workflow | Priority |
|--------|----------|----------|
| New article ready for featured image | Featured Image Generation | P1 |
| Article has 3+ sections needing visuals | In-Article Graphics Generation | P1 |
| Product review/comparison article | Comparison Chart + Product Box | P1 |
| Images exist but need optimization | Image Optimization + Compression | P1 |
| Article published but images missing alt-text | Alt-Text Batch Generation | P1 |
| Visual consistency audit needed | Brand Alignment Check | P2 |
| Images not ranking in Google Image Search | SERP Image Optimization | P2 |

## Workflow 1: Featured Image Generation

**Goal:** Create SOTA, click-worthy featured image (1200x630px, <100KB, optimized for social + SERP display).

**Input:**
```
Article Title: "[TITLE]"
Keyword: "[KEYWORD]"
Article Summary: "[2-3 sentence summary]"
Brand Colors: [HEX codes]
Style Preference: [modern|minimal|data-driven|lifestyle]
```

**Execution:**

1. **Design Phase** → Create mockup matching style preference, brand colors, readability (headline must be legible at 300px width)
2. **Content Phase** → Add headline (10-12 words max), visual elements (icons, photos), brand logo/watermark
3. **Specification Phase:**
   - Dimensions: 1200x630px (1.91:1 ratio for optimal social sharing)
   - Format: WebP (primary) + PNG/JPG fallback
   - File size: <100KB (WebP), <200KB (PNG)
   - Filename: `{slug}-1200x630.webp`
4. **Output:** Image file + metadata JSON:
   ```json
   {
     "filename": "how-to-run-faster-1200x630.webp",
     "dimensions": "1200x630",
     "size_kb": 45,
     "alt_text": "Colorful infographic: 5 science-backed tips to improve running speed",
     "og_title": "[Article Title]",
     "og_description": "[Meta description]"
   }
   ```

## Workflow 2: In-Article Graphics Generation

**Goal:** Create 2-4 custom visuals (diagrams, flows, step-by-step guides) that reinforce article content.

**Input:**
```
Article Sections: [List of H2 sections]
Section That Needs Visuals: [e.g., "Step 1: Initial Setup", "The Scientific Evidence"]
Visual Type: [diagram|process-flow|step-guide|timeline|infographic]
Brand Colors & Fonts: [CSS specs]
```

**Execution:**

1. **Content Analysis** → Identify which sections benefit most from visuals (e.g., numbered steps, complex processes)
2. **Design Creation** → Create visuals matching brand style, readable at mobile sizes (min 12px font)
3. **Specifications** → For each image:
   - Filename: `{slug}-{section}-{width}x{height}.webp`
   - Dimensions: 800x600px (min) for optimal article display
   - Format: WebP + PNG fallback
   - File size: <80KB
4. **Output:** Image files + placement guide:
   ```markdown
   ## Placement Guide
   
   **After H2: "Step 1: Initial Setup"**
   - Image: `guide-step-1-800x600.webp`
   - Alt text: "Step 1 flowchart showing initial setup process"
   - Caption: "Initial Setup Process"
   ```

## Workflow 3: Comparison Chart + Product Box

**Goal:** Create visual comparison matrix and/or affiliate product showcase card (for product reviews).

**Input:**
```
Comparison Data:
  Product A: {name, specs, price, rating}
  Product B: {name, specs, price, rating}
  Product C: {name, specs, price, rating}
Features to Compare: [list]
Brand Colors: [HEX codes]
```

**Execution:**

1. **Comparison Chart** → Create table-style visual (3-5 products, 5-8 features):
   - Design: Clean, mobile-responsive grid or table
   - Highlight: "Winner" or "Best for [Use Case]" row
   - Dimensions: 800x600px minimum
   - File size: <75KB (WebP)
2. **Product Box** (if affiliate):
   - 300x250px (min) or 300x400px (vertical)
   - Image placeholder (top 40%), product name (20%), price (20%), CTA button (20%)
   - CTA button: "Check Price on [Retailer]" with affiliate link
   - Filename: `product-{name}-{width}x{height}.webp`
3. **Output:** Comparison image + Product box HTML component (if applicable)

## Workflow 4: Image Optimization + Compression

**Goal:** Convert/optimize existing images to SOTA web formats (WebP + responsive srcset).

**Input:**
```
Image URLs: [list of URLs or local files]
Target Widths: [400, 600, 800, 1000, 1200]
Quality Target: high|medium|balanced
```

**Execution:**

1. **Conversion** → Convert PNG/JPG to WebP (lossless for graphics, lossy for photos at 80-85 quality)
2. **Compression** → Create multiple sizes (400px, 600px, 800px, 1000px, 1200px widths)
3. **Metadata** → Generate responsive HTML:
   ```html
   <picture>
     <source srcset="image-400w.webp 400w, image-600w.webp 600w, ..."
             sizes="(max-width: 600px) 90vw, (max-width: 1200px) 70vw, 800px"
             type="image/webp">
     <source srcset="image-400w.jpg 400w, image-600w.jpg 600w, ..."
             sizes="(max-width: 600px) 90vw, (max-width: 1200px) 70vw, 800px">
     <img src="image-800w.jpg" alt="[SEO ALT TEXT]" loading="lazy">
   </picture>
   ```
4. **Output:** All optimized image sizes + responsive HTML snippet

## Workflow 5: Alt-Text Batch Generation

**Goal:** Generate SEO-optimized, accessible alt text for all images in an article.

**Input:**
```
Article URL: "[URL]"
Article Keyword: "[KEYWORD]"
Image Filenames: [list]
Image Descriptions: [optional: brief context for each image]
```

**Execution:**

1. **Context Analysis** → Review article content, image placement, article keyword
2. **Alt-Text Generation** → For each image:
   - Max 125 characters
   - Include keyword if natural (but never force it)
   - Describe image content + context
   - Examples:
     - Featured image: "Colorful infographic: 5 science-backed tips to improve running speed"
     - Step diagram: "Flowchart showing 3-step setup process for WordPress email configuration"
     - Product photo: "Gold Hoka Speedgoat 5 running shoe, 3/4 view against white background"
3. **Accessibility Check** → Ensure alt text is concise, descriptive, not keyword-stuffed
4. **Output:** CSV or JSON mapping image filenames to alt text:
   ```json
   {
     "featured-1200x630.webp": "Colorful infographic: 5 science-backed tips to improve running speed",
     "step-guide-800x600.webp": "Flowchart showing 3-step WordPress email setup process"
   }
   ```

## Workflow 6: Brand Alignment Check

**Goal:** Audit existing images for color consistency, typography, design system alignment.

**Input:**
```
Brand Guidelines: [color palette, typography, design system]
Article Images: [list of URLs]
```

**Execution:**

1. **Visual Audit** → Check each image for:
   - Color palette compliance (colors match brand or are neutral)
   - Typography (fonts match or are readable)
   - Design consistency (style matches other site visuals)
   - Professionalism (no low-quality stock photos, blurry images, etc.)
2. **Report** → List non-compliant images + recommendations for redesign
3. **Output:** Brand Alignment Report + list of images needing refresh

## Workflow 7: SERP Image Optimization

**Goal:** Optimize featured image and all in-article images for Google Image Search ranking.

**Execution:**

1. **Featured Image Optimization:**
   - Aspect ratio: 1.91:1 (optimal for social + Google Image Search)
   - Dimensions: 1200x630px minimum
   - Quality: High (no compression artifacts visible)
   - Relevance: Image must match article title/keyword
   - SEO filename: Include keyword + dimensions (e.g., `best-running-shoes-comparison-1200x630.webp`)
2. **In-Article Image Optimization:**
   - Filename: Descriptive, keyword-aware (e.g., `nike-zoom-fly-5-side-view-800x600.webp`)
   - Alt text: Descriptive + keyword where natural
   - Dimensions: 800x600px minimum for optimal display
   - Format: WebP + fallback (supports Google's image indexing)
3. **Image Schema Markup** → Add ImageObject schema:
   ```json
   {
     "@context": "https://schema.org",
     "@type": "ImageObject",
     "url": "https://example.com/image.webp",
     "name": "[Image Description]",
     "description": "[Image Alt Text]",
     "caption": "[If applicable]"
   }
   ```
4. **Output:** Optimized images + schema markup snippets

## Quality Metrics

| Metric | Target | How Measured |
|--------|--------|---------------|
| Featured Image Size | <100KB | File size check |
| Featured Image Dimensions | 1200x630px | Pixel verification |
| In-Article Image Size | <80KB | File size check |
| Image Format | WebP primary | File type validation |
| Alt-Text Length | <125 chars | Character count |
| Alt-Text Keyword Inclusion | Natural | Manual review |
| Image Mobile Responsiveness | 100% | Mobile rendering test |
| Brand Color Compliance | 95%+ | Visual audit |
| Page Image Load Time | <2s | Lighthouse/GTmetrix |
| Images Rank in Google Images | High/Medium/Low | Search operator: `site:example.com inurl:image` |

## Integration with Other Skills

1. **wordpress-blog-mastery** ← Receive image placement cues, visual asset briefs
2. **seo-intelligence** ← Receive keyword data for image optimization
3. **conversion-optimizer** ← Design product showcase cards, affiliate boxes
4. **technical-seo-health** ← Receive image load-time, Core Web Vitals recommendations

## Execution Checklist

- [ ] Featured image designed + optimized (<100KB, 1200x630px)
- [ ] All in-article images created/optimized (<80KB, WebP + fallback)
- [ ] Image filenames SEO-optimized (keyword-aware, dimensions included)
- [ ] Alt text generated for all images (max 125 chars, accessible)
- [ ] Brand colors + typography aligned to design system
- [ ] Product box (if applicable) created with CTA button
- [ ] Comparison charts/diagrams visual and mobile-responsive
- [ ] Responsive srcset HTML generated for all images
- [ ] Image schema markup (ImageObject) included
- [ ] Images tested on mobile (responsive design, load time <2s)
- [ ] Ready for integration with wordpress-blog-mastery
