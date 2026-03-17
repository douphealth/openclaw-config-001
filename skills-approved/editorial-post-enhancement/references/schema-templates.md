# Schema Markup Templates (JSON-LD)

Ready-to-paste JSON-LD schemas for blog posts and articles. Validate at: https://search.google.com/test/rich-results

## Article Schema (Standard Blog Post)

Use for: informational blog posts, guides, how-tos, listicles.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your SEO-Optimized Title Here (max 110 chars)",
  "description": "Meta description of the article",
  "image": {
    "@type": "ImageObject",
    "url": "https://yoursite.com/wp-content/uploads/featured-image.jpg",
    "width": 1200,
    "height": 630
  },
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://yoursite.com/author/name",
    "jobTitle": "Job Title",
    "sameAs": [
      "https://twitter.com/authorhandle",
      "https://linkedin.com/in/authorprofile"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "name": "Site Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://yoursite.com/logo.png",
      "width": 600,
      "height": 60
    }
  },
  "datePublished": "2026-01-15T08:00:00+02:00",
  "dateModified": "2026-03-17T10:00:00+02:00",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://yoursite.com/blog/post-slug"
  },
  "keywords": ["primary keyword", "secondary keyword", "related entity"],
  "articleSection": "Category Name",
  "wordCount": 2500,
  "inLanguage": "en"
}
</script>
```

## BlogPosting Schema (WordPress Native)

WordPress uses BlogPosting for blog content. Same structure as Article but with `@type: BlogPosting`.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Your Title Here",
  "description": "Your description",
  "image": "https://yoursite.com/featured-image.jpg",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Site Name",
    "logo": "https://yoursite.com/logo.png"
  },
  "datePublished": "2026-01-15",
  "dateModified": "2026-03-17",
  "mainEntityOfPage": "https://yoursite.com/blog/post-slug"
}
</script>
```

## FAQPage Schema

Add when the article contains an FAQ section. Each question/answer pair becomes a `mainEntity` item.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the best way to improve blog SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Focus on three areas: (1) answer the user's query in the first 100 words, (2) add semantically relevant entities and keywords naturally, and (3) build contextual internal links to strengthen topical authority."
      }
    },
    {
      "@type": "Question",
      "name": "How often should I update blog posts for SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Review high-traffic posts quarterly. Update statistics, add new examples, refresh internal links, and check for broken external references. Posts ranking positions 4-10 often benefit most from updates."
      }
    }
  ]
}
</script>
```

## HowTo Schema

Add for step-by-step tutorial/guide articles with clear sequential steps.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Optimize a Blog Post for SEO",
  "description": "Step-by-step guide to improving your blog post rankings",
  "totalTime": "PT30M",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Identify the target keyword and search intent",
      "text": "Research what users are searching for and match your content to the dominant intent (informational, commercial, or transactional).",
      "url": "https://yoursite.com/blog/optimize-post#step-1"
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "Add missing semantic entities and keywords",
      "text": "Compare your article against the top 3 SERP results and add any missing entities, related terms, or subtopics naturally into the content.",
      "url": "https://yoursite.com/blog/optimize-post#step-2"
    },
    {
      "@type": "HowToStep",
      "position": 3,
      "name": "Optimize internal linking and schema markup",
      "text": "Add 2-3 contextual internal links with varied anchor text and implement Article or FAQPage schema markup.",
      "url": "https://yoursite.com/blog/optimize-post#step-3"
    }
  ]
}
</script>
```

## Stacked Schema (Article + FAQPage)

Best practice: combine Article with FAQPage for articles that have both content and FAQs. WordPress inserts multiple `<script>` blocks.

```html
<!-- Article Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Improve Blog Rankings in 2026",
  ...
}
</script>

<!-- FAQPage Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [...]
}
</script>
```

## BreadcrumbList Schema (Optional but Recommended)

Helps Google display breadcrumb navigation in SERPs.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://yoursite.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://yoursite.com/blog/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Article Title",
      "item": "https://yoursite.com/blog/article-slug"
    }
  ]
}
</script>
```

## Adding Schema to WordPress Posts

### Via Yoast SEO (auto-creates Article schema)
```bash
# Yoast auto-generates schema. To customize:
wp post meta get <post-id> _yoast_wpseo_schema_page_type
wp post meta update <post-id> _yoast_wpseo_schema_page_type Article
```

### Via WP REST API
```bash
# Store schema as post meta
wp post meta update <post-id> _custom_schema_json '<script type="application/ld+json">...</script>'

# Then add to post head via theme or plugin
```

### Via wp_head hook (functions.php)
```php
// In your theme's functions.php or a custom plugin:
add_action('wp_head', function() {
  if (is_single()) {
    $schema = get_post_meta(get_the_ID(), '_custom_schema_json', true);
    if ($schema) {
      echo '<script type="application/ld+json">' . $schema . '</script>';
    }
  }
});
```

## Validation & Testing
```bash
# Extract current schema from a page
curl -s <url> | grep -o '<script type="application/ld\+json">.*</script>'

# Validate with Google Rich Results Test
# URL: https://search.google.com/test/rich-results
# Or via API:
curl -s "https://search.google.com/test/rich-results?url=<encoded-url>" | head -20
```

## Common Schema Mistakes
- ❌ Invalid JSON (trailing commas, missing quotes, unescaped characters)
- ❌ Missing required properties (headline, author, datePublished, publisher)
- ❌ Wrong date format (must be ISO 8601: `YYYY-MM-DDTHH:MM:SS+TZ`)
- ❌ image URL is relative (must be absolute: `https://...`)
- ❌ author is Organization when it should be Person (for personal blogs)
- ❌ Multiple Article schemas on one page (use stacked approach instead)
- ❌ FAQPage schema without matching FAQ content on the page
- ❌ `@id` duplicates across pages (each page needs unique `@id`)
- ❌ Schema doesn't match visible content (Google penalizes mismatches)
