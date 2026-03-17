# Image Alt Text & SEO Guide

Create SEO-optimized alt text for blog post images. Goal: help search engines understand the image AND provide value to screen-reader users.

## Alt Text Formula

```
[Descriptive action or subject] + [relevant keyword naturally embedded] + [specific context if helpful]
```

**Good:** "Google Analytics dashboard showing organic traffic growth from 2,000 to 8,500 sessions over 6 months"
**Bad:** "google analytics screenshot" (too generic)
**Bad:** "best SEO tool google analytics organic traffic SEO" (keyword stuffing)
**Bad:** "image1.jpg" (filename, not alt text)

## Alt Text Length
- **Ideal:** 80-125 characters
- **Maximum:** 125 characters (screen readers cut off after ~125)
- **Minimum:** 10 characters (anything shorter is not descriptive)

## Alt Text by Image Type

### Screenshots (UI/Applications)
```
[App name] [screen/panel] showing [what's visible] with [specific detail]

Examples:
"WordPress post editor with Yoast SEO panel open showing meta description field"
"HubSpot automation workflow showing email trigger followed by 3-day delay and conditional branch"
"Google Search Console performance report filtered to blog pages showing 340% click increase"
```

### Charts & Graphs
```
[Chart type] comparing [variables] showing [key finding/number]

Examples:
"Bar chart comparing monthly revenue from organic traffic ($12K) vs paid ($8K) vs social ($3K) in Q4 2025"
"Line graph showing email open rates declining from 32% to 18% over 12 months with annotation for algorithm change"
"Pie chart of traffic sources: 45% organic search, 25% direct, 20% referral, 10% social"
```

### Photos (People/Places)
```
[Who/what] doing [action] in [context]

Examples:
"Alex Hormozi presenting at a business conference with slide showing 100M dollar revenue milestone"
"Developer pair-programming at a standing desk with dual monitors showing React code editor"
"Happy customer signing contract at coffee shop after successful sales consultation"
```

### Diagrams & Infographics
```
[Diagram type] illustrating [concept] with [number of steps/components]

Examples:
"Sales funnel diagram showing 4 stages: awareness (10,000 visitors) → consideration (2,500 leads) → decision (500 proposals) → purchase (100 customers)"
"5-step content creation workflow: research → outline → draft → edit → publish with time estimates"
"SWOT analysis matrix for SaaS startup with key strengths and threats highlighted"
```

### Product Images
```
[Product name] [type of image] showing [key features/context]

Examples:
"ConvertKit email automation builder interface with trigger-based workflow setup"
"Ahrefs keyword explorer showing search volume 12,100, keyword difficulty 45, and SERP features"
"Canva template editor displaying social media post template with drag-and-drop interface"
```

## Image Filename SEO

Before uploading, name files descriptively:

| Before | After |
|--------|-------|
| `IMG_20250317.jpg` | `google-analytics-traffic-growth-q4-2025.jpg` |
| `screenshot.png` | `wordpress-yoast-seo-meta-description-setup.png` |
| `chart1.png` | `email-open-rates-comparison-by-industry-2025.png` |

**Rules:**
- Lowercase with hyphens (never spaces or underscores)
- Include primary keyword when natural
- Keep under 5 words when possible
- Use `.jpg` for photos, `.png` for screenshots/diagrams, `.webp` for both (modern)

## Image Optimization Checklist

- [ ] Filename is descriptive with hyphens (no `image1.jpg`)
- [ ] Alt text is 80-125 chars, includes keyword naturally
- [ ] Width/height attributes set (prevents layout shift / CLS)
- [ ] Images are compressed (use ShortPixel, TinyPNG, or `wp media regenerate`)
- [ ] Lazy loading enabled for below-fold images (`loading="lazy"`)
- [ ] Responsive srcset for mobile (WordPress handles this natively for most themes)
- [ ] At least one image above the fold (improves visual engagement)
- [ ] No decorative images have alt text (use `alt=""` for purely decorative images)

## Finding Images in WordPress Media Library

```bash
# List recent media uploads
wp media list --fields=ID,guid,mime_type --limit=20

# Search media by keyword (if supported)
wp media list --s="keyword" --fields=ID,guid

# Get image metadata
wp post get <attachment-id> --field=post_title,post_excerpt,post_content

# Check image dimensions
wp post meta get <attachment-id> _wp_attachment_metadata --format=json | jq '.width,.height'

# Bulk regenerate thumbnails
wp media regenerate --yes
```

## Adding Images to a Post (WordPress REST API)

```bash
# Upload new image
curl -X POST <site>/wp-json/wp/v2/media \
  -H "Authorization: Basic <base64-auth>" \
  -H "Content-Disposition: attachment; filename=my-image.jpg" \
  -H "Content-Type: image/jpeg" \
  --data-binary @my-image.jpg

# Set alt text on attachment
curl -X POST <site>/wp-json/wp/v2/media/<attachment-id> \
  -H "Authorization: Basic <base64-auth>" \
  -H "Content-Type: application/json" \
  -d '{"alt_text": "Descriptive alt text here"}'

# Add to post content (insert at position)
# Update post content with the new image block
curl -X PUT <site>/wp-json/wp/v2/posts/<post-id> \
  -H "Authorization: Basic <base64-auth>" \
  -H "Content-Type: application/json" \
  -d '{"content": "<existing-content-with-new-image-block>"}'
```

## Alt Text Quality Scorecard

Rate each image's alt text 1-5:

| Score | Criteria |
|-------|----------|
| 5 | Descriptive, keyword naturally included, specific details, 80-125 chars |
| 4 | Descriptive, keyword present, some specifics |
| 3 | Somewhat generic but describes content |
| 2 | Very generic ("chart showing data") or keyword-stuffed |
| 1 | Missing, "image", "screenshot", or filename as alt |

**Target:** All images score 4+ and at least one scores 5.
