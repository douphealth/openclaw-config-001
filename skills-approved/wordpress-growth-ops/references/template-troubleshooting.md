# WordPress Template Troubleshooting

## Template Priority (WordPress Hierarchy)
```
single-{post_type}-{slug}.php → single-{post_type}.php → single.php → singular.php → index.php
page-{slug}.php → page-{id}.php → page.php → singular.php → index.php
archive-{post_type}.php → archive.php → index.php
```

## Detecting Template on Live Page

### Body Class Analysis
```python
# Check body classes for template identification
body_classes = {
    'single-post': "Single post template",
    'single-page': "Single page template",  
    'page-template-elementor_header_footer': "Elementor (header+footer only, NO content area)",
    'page-template-default': "Default page template",
    'page-id-{N}': "This is a PAGE (not a post)",
    'postid-{N}': "This is a POST (not a page)",
    'page-child': "Child page in hierarchy",
    'parent-pageid-{N}': "Parent page ID",
    'wp-singular': "Single content type",
    'wp-page': "Page content type",
    'wp-post': "Post content type"
}
```

### Quick Template Detection Script
```bash
# Get body class from live page
curl -s "https://site.com/page-url/" | grep -o 'class="[^"]*"' | grep 'body' | head -1

# Key signals:
# page-id- → it's a page, NOT a post (even if URL looks like a post)
# postid- → it's a post
# elementor_header_footer → no content area renders
# page-template-default → default template, content SHOULD render
```

## Common Template Issues

### Issue: Page Shows Blank Despite Content in DB
**Diagnosis:**
1. Check body class: `page-id-{N}` vs `postid-{N}`
2. If page-id: the URL is resolving to a PAGE, not a POST
3. Check template: `elementor_header_footer` = no content area
4. Check for slug conflicts

**Fix:** Force-delete conflicting page or change template.

### Issue: Content Renders But Layout is Wrong
**Diagnosis:**
1. Check if Elementor is active (`elementor-location-*` classes)
2. Check if page uses Elementor data (`_elementor_data` meta)
3. Compare `content.raw` vs `content.rendered` — if different, Elementor is overriding

**Fix:** If Elementor data exists, update via Elementor editor, not REST API.

### Issue: Sidebar Showing When It Shouldn't
**Diagnosis:**
1. Check body class for template
2. Default sidebar appears in standard templates

**Fix:** Change template to `elementor_header_footer` to remove sidebar.
```bash
curl -X POST -u "$AUTH" "$SITE/wp-json/wp/v2/posts/{id}" \
  -d '{"template": "elementor_header_footer"}'
```

## Template Values for REST API

| Value | Description | Content Area |
|-------|-------------|--------------|
| `""` (empty) | Default theme template | ✅ Yes |
| `elementor_header_footer` | Elementor H+F only | ❌ No |
| `page.php` | Standard page | ✅ Yes |
| `single.php` | Standard single post | ✅ Yes |

## Elementor-Specific Troubleshooting

### Elementor Content Not Rendering
1. Check `data-elementor-type` on content wrapper
2. Elementor stores content in `_elementor_data` meta, NOT `post_content`
3. Updating `post_content` via REST API has NO effect on Elementor pages
4. Must use Elementor editor or update `_elementor_data` directly (complex JSON)

### Elementor vs WordPress Content
- **WordPress content**: `post_content` field → rendered via `the_content()`
- **Elementor content**: `_elementor_data` meta → rendered via Elementor renderer
- **Both can exist**: Elementor content takes priority if active
