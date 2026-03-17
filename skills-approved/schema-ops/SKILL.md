---
name: schema-ops
description: Enterprise-grade JSON-LD structured data operations for affiliate marketing sites. Generate, validate, deploy, and optimize schema markup for Product, Review, FAQ, HowTo, Article, ItemList, SoftwareApplication, BreadcrumbList, Organization, Person, and AggregateRating. Use when a user asks for rich snippet markup, schema validation, JSON-LD generation, rich result optimization, affiliate schema deployment, or stacked schema design for any page type.
---

# Schema Ops — Affiliate Schema Mastery

Enterprise-grade structured data system for affiliate marketing sites. Generate, validate, deploy, and optimize JSON-LD markup that wins rich results.

## WHEN TO USE

Trigger this skill when the user asks about:
- Schema markup, JSON-LD, structured data, rich snippets
- Product schema, review schema, FAQ schema, HowTo schema
- Star ratings in SERPs, FAQ rich results, product rich results
- Schema validation, Google Rich Results Test, schema errors
- "Best of" list schema, comparison schema, software review schema
- WordPress schema implementation, schema plugins
- Schema stacking (multiple schemas per page)
- Breadcrumb markup, author markup, organization markup
- Any rich result optimization

**Do NOT use this skill for:** General SEO auditing or site diagnosis (→ `seo-audit-playbook`), content strategy or keyword research (→ `content-strategy-planning`).

## DECISION TREE: WHICH SCHEMA TYPE TO USE

| Page Type | Primary Schema | Secondary Schemas |
|-----------|---------------|-------------------|
| Product Review | Review → Product | BreadcrumbList, Person (author), Organization |
| "Best X" Roundup | ItemList → Product (per item) | BreadcrumbList, Person, Organization |
| Single Product Page | Product with Offer | BreadcrumbList, AggregateRating |
| FAQ Page | FAQPage | BreadcrumbList, Organization |
| How-To Guide | HowTo | BreadcrumbList, Person |
| Blog Post | Article or BlogPosting | BreadcrumbList, Person, Organization |
| Comparison Page | ItemList or Product + Review | BreadcrumbList, FAQPage |
| Software/Tool Review | SoftwareApplication + Review | BreadcrumbList, FAQPage, ItemList |
| Homepage | Organization, WebSite (with SearchAction) | BreadcrumbList |
| Category/List Page | ItemList (of Products or Articles) | BreadcrumbList, Organization |
| Contact/About Page | Organization or Person | BreadcrumbList |

## CORE RULES

### Format
- **ALWAYS JSON-LD** — never Microdata or RDFa. JSON-LD is Google's preferred format, doesn't pollute HTML, and is easier to maintain.
- Place JSON-LD in `<head>` or `<body>` — either works. Convention: bottom of `<body>` before `</body>`.
- One `<script type="application/ld+json">` per schema block. You CAN combine multiple @graph entries in one script, but separate scripts are often clearer.

### Data Quality
- Dates: ISO 8601 format (`2026-03-12T00:00:00Z` or `2026-03-12`)
- Images: absolute URLs, minimum 1200x630px for Article, 696px+ for Product
- URLs: always absolute (`https://...`), never relative
- Currency: ISO 4217 codes (`USD`, `EUR`, `GBP`)
- Language: `en-US` or appropriate BCP 47 tag

### Validation
- Every schema block MUST pass Google Rich Results Test before deployment
- Check at: https://search.google.com/test/rich-results
- Also validate at: https://validator.schema.org/
- No errors allowed. Warnings should be reviewed and fixed when possible.

### Nesting
- Nest related schemas inside parent types (Review inside Product, Offer inside Product)
- Use `@id` references to avoid duplication when the same entity appears multiple times
- For multiple schema types on one page, use `@graph` array or separate scripts

### Affiliate-Specific Rules
- Product schema is ESSENTIAL on every product review/comparison page
- AggregateRating requires real user reviews — don't fabricate ratings
- Always include `offers` with `price`, `priceCurrency`, `availability`, and `url` (affiliate link)
- ItemList for "best of" roundups with `numberOfItems` and ordered `itemListElement`
- FAQ schema for any FAQ section — drives FAQ rich results in SERPs
- BreadcrumbList on every page for breadcrumb rich results

## OPERATIONS

### 1. Generate Schema
When given a URL or page content:
1. Identify the page type (product review, comparison, guide, blog post, etc.)
2. Determine primary schema type + supporting types needed
3. Extract or request required fields (name, description, images, prices, ratings, etc.)
4. Generate complete JSON-LD with all required AND recommended properties
5. Include `@id` references for entities that appear in multiple schemas
6. Output validated, production-ready JSON-LD

### 2. Validate Schema
When given JSON-LD to validate:
1. Check syntax (valid JSON, correct @context, @type)
2. Verify all required properties for the schema type are present
3. Check data formats (dates, URLs, currencies, ratings range)
4. Flag missing recommended properties
5. Identify rich result eligibility
6. Provide fix instructions for any issues

### 3. Deploy Schema
When asked to deploy:
1. Provide the exact `<script type="application/ld+json">` block
2. For WordPress: provide functions.php snippet or shortcode approach
3. For static sites: provide placement instructions
4. For CMS plugins: recommend appropriate plugin + configuration
5. Include deployment verification steps

### 4. Stack Multiple Schemas
When a page needs multiple schema types:
1. Use `@graph` to combine schemas in one script block, OR
2. Use separate script blocks for clarity
3. Link related schemas with `@id` references
4. Ensure no conflicting or duplicate data
5. Example: Article + FAQPage + BreadcrumbList + Organization on a blog post

## IMPLEMENTATION PATTERNS

### WordPress: functions.php Approach
```php
// Add schema to specific page templates
function add_schema_markup() {
    if (is_single() || is_page()) {
        $schema = array(
            '@context' => 'https://schema.org',
            '@type' => 'Article',
            'headline' => get_the_title(),
            // ... additional properties
        );
        echo '<script type="application/ld+json">' . json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . '</script>';
    }
}
add_action('wp_footer', 'add_schema_markup');
```

### WordPress: Custom Field Approach (for dynamic product data)
```php
function get_product_schema() {
    $schema = array(
        '@context' => 'https://schema.org',
        '@type' => 'Product',
        'name' => get_field('product_name'),
        'description' => get_field('product_description'),
        'image' => get_field('product_image'),
        'brand' => array(
            '@type' => 'Brand',
            'name' => get_field('product_brand')
        ),
        'offers' => array(
            '@type' => 'Offer',
            'price' => get_field('product_price'),
            'priceCurrency' => 'USD',
            'availability' => 'https://schema.org/InStock',
            'url' => get_field('affiliate_link')
        )
    );
    
    // Add aggregate rating if available
    $rating = get_field('product_rating');
    $review_count = get_field('product_review_count');
    if ($rating && $review_count) {
        $schema['aggregateRating'] = array(
            '@type' => 'AggregateRating',
            'ratingValue' => $rating,
            'bestRating' => '5',
            'reviewCount' => $review_count
        );
    }
    
    return $schema;
}
```

### Static HTML: Template Pattern
```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
    <!-- Head content -->
</head>
<body>
    <!-- Page content -->
    
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@graph": [
            { /* BreadcrumbList */ },
            { /* Primary schema */ },
            { /* Supporting schemas */ }
        ]
    }
    </script>
</body>
</html>
```

## VALIDATION SCRIPT

Use the included Python validation script at `scripts/validate-schema.py`:
```bash
python3 scripts/validate-schema.py schema.json
python3 scripts/validate-schema.py --url https://example.com
python3 scripts/validate-schema.py --inline '{"@context":"https://schema.org","@type":"Product",...}'
```

## FIELD REQUIREMENTS QUICK REFERENCE

### Product (Required for rich results)
- `name` (required)
- `image` (required - at least one)
- `aggregateRating` OR `review` (at least one for stars)
- `offers` (required for price rich results)

### Article
- `headline` (required, <110 chars for AMP)
- `image` (required, 1200x630+)
- `datePublished` (required)
- `dateModified` (recommended)
- `author` (required, Person or Organization)
- `publisher` (recommended)

### FAQPage
- `mainEntity` array of Question objects
- Each Question needs `name` and `acceptedAnswer` with `text`

### HowTo
- `name` (required)
- `step` array (required, each with `text` or `itemListElement`)
- `totalTime` (recommended, ISO 8601 duration)

### ItemList
- `numberOfItems` (recommended)
- `itemListElement` array (required, each with `position` and `item`)
- Use `ListItem` as @type for each element

### BreadcrumbList
- `itemListElement` array (required)
- Each element: `position` (number), `name` (string), `item` (URL)

### SoftwareApplication
- `name` (required)
- `applicationCategory` (required)
- `operatingSystem` (recommended)
- `offers` (for pricing)
- `aggregateRating` (for stars)

### Organization
- `name` (required)
- `url` (required)
- `logo` (recommended)
- `sameAs` (recommended - social profiles)

## RICH RESULT ELIGIBILITY

| Schema Type | Rich Result | Key Requirements |
|---|---|---|
| Product | Price, availability, reviews | offers + aggregateRating or review |
| FAQPage | FAQ accordion | mainEntity with Question/Answer |
| HowTo | HowTo carousel | step array with text |
| Article | Top Stories, headline | headline + image + datePublished |
| BreadcrumbList | Breadcrumb trail | itemListElement with position/name/item |
| ItemList | Carousel/List | itemListElement with ListItem elements |
| SoftwareApplication | App listing | name + applicationCategory |
| Review/AggregateRating | Star ratings | ratingValue + bestRating + reviewCount |
| Organization | Knowledge panel | name + url + logo + sameAs |
| Video | Video carousel | Requires VideoObject schema |
| Recipe | Recipe rich result | Specific recipe properties |

## QUICK REFERENCE CARD

**Cheatsheet for common affiliate page schemas:**

1. **Product Review Page**: Product + Review + BreadcrumbList + Organization
2. **"Best X" Roundup**: ItemList (of Products) + BreadcrumbList + Organization
3. **Comparison Page**: ItemList or 2x Product + BreadcrumbList + FAQPage
4. **How-To Guide**: HowTo + Article + BreadcrumbList + Organization
5. **Blog Post**: Article + BreadcrumbList + Organization + (optional FAQPage)
6. **Software Review**: SoftwareApplication + Review + BreadcrumbList + FAQPage
7. **Category Page**: ItemList + BreadcrumbList + Organization
8. **Homepage**: Organization + WebSite + SearchAction

**For all page types, also include:**
- BreadcrumbList (every page)
- Organization (every page, or once site-wide)

## Do NOT Use This For
- General SEO auditing or site diagnosis (→ seo-audit-playbook)
- Content strategy or keyword research (→ content-strategy-planning)
- Writing or editing on-page content (→ editorial-post-enhancement)
- Setting up conversion tracking (→ tracking-measurement)

## Checks
- Every schema block MUST pass Google Rich Results Test before deployment
- Use ISO 8601 dates, absolute URLs, and properly formatted currencies
- Product schema requires `offers` with price, currency, availability, and URL for rich results
- AggregateRating requires real review data — never fabricate ratings
- Multiple schema types on one page should use @graph or linked @id references

## Resources
- `references/schema-templates.md` — Full JSON-LD templates for every type
- `references/affiliate-schema-guide.md` — Affiliate-specific implementation patterns
- `references/rich-result-optimization.md` — Rich result optimization strategies
- `scripts/validate-schema.py` — Schema validation script (run before deployment)

## Output Contract
**Artifact**: Schema markup implementation
**Evidence**: Schema validator output, rich result eligibility
**Decision**: Schema deployed and validated
**Next**: Monitor rich result appearance in search results
