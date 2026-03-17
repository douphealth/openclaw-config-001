---
name: schema-ops
description: Enterprise-grade JSON-LD structured data operations for affiliate marketing sites. Generate, validate, deploy, and optimize schema markup for Product, Review, FAQ, HowTo, Article, ItemList, SoftwareApplication, BreadcrumbList, Organization, Person, and AggregateRating. Use when a user asks for rich snippet markup, schema validation, JSON-LD generation, rich result optimization, affiliate schema deployment, or stacked schema design for any page type.
---

# Schema Ops

Enterprise structured data system for affiliate marketing sites. Generate, validate, deploy, and optimize JSON-LD markup that wins rich results.

## Decision Tree: Which Schema Type?

```
Page needs schema markup
│
├── What type of page is it?
│   ├── Product review → Review + Product + BreadcrumbList + Person
│   ├── "Best X" roundup → ItemList → Product (per item) + BreadcrumbList
│   ├── Single product page → Product with Offer + AggregateRating + BreadcrumbList
│   ├── FAQ section → FAQPage + BreadcrumbList
│   ├── How-to guide → HowTo + BreadcrumbList + Person
│   ├── Blog post → Article + BreadcrumbList + Person + Organization
│   ├── Comparison page → ItemList or 2× Product + BreadcrumbList + FAQPage
│   ├── Software review → SoftwareApplication + Review + BreadcrumbList + FAQPage
│   ├── Homepage → Organization + WebSite with SearchAction
│   ├── Category/list page → ItemList + BreadcrumbList + Organization
│   └── Contact/about → Organization or Person + BreadcrumbList
│
├── Does the page have multiple content types?
│   └── YES → Use @graph array to stack schemas in one script block
│
└── Does the same entity appear in multiple schemas?
    └── YES → Use @id references to avoid duplication
```

## When to Use

- Schema markup, JSON-LD, structured data, rich snippets
- Product/Review/FAQ/HowTo schema generation or optimization
- Star ratings in SERPs, FAQ rich results, product rich results
- Schema validation (Google Rich Results Test, schema errors)
- "Best of" list schema, comparison schema, software review schema
- WordPress schema implementation
- Schema stacking (multiple schemas per page)
- Breadcrumb, author, organization markup

**Do NOT use for:** general SEO auditing (→ `seo-audit-playbook`), content strategy or keyword research (→ `content-strategy-planning`).

## Core Rules

### Format
- **ALWAYS JSON-LD** — never Microdata or RDFa
- One `<script type="application/ld+json">` per schema block (or use `@graph` for multiple)
- Place in `<head>` or bottom of `<body>` before `</body>`

### Data Quality
| Field | Format | Example |
|-------|--------|---------|
| Dates | ISO 8601 | `2026-03-12` or `2026-03-12T00:00:00Z` |
| Images | Absolute URLs, min 1200×630 (Article), 696px+ (Product) | `https://site.com/img.jpg` |
| URLs | Always absolute | `https://site.com/page` |
| Currency | ISO 4217 | `USD`, `EUR`, `GBP` |
| Language | BCP 47 | `en-US` |

### Validation
- Every schema MUST pass Google Rich Results Test before deployment
- URL: https://search.google.com/test/rich-results
- Also: https://validator.schema.org/
- No errors allowed; review and fix warnings

### Affiliate-Specific Rules
- Product schema ESSENTIAL on every product review/comparison page
- AggregateRating requires real user reviews — never fabricate ratings
- Always include `offers` with `price`, `priceCurrency`, `availability`, `url` (affiliate link)
- ItemList for "best of" roundups with `numberOfItems` and ordered `itemListElement`
- FAQ schema for any FAQ section — drives FAQ rich results
- BreadcrumbList on every page for breadcrumb rich results

## Operational Procedures

### 1. Generate Schema

```
Step 1: Identify page type (from decision tree above)
Step 2: Determine primary + supporting schema types
Step 3: Extract or request required fields (name, images, prices, ratings)
Step 4: Generate complete JSON-LD with required AND recommended properties
Step 5: Include @id references for entities appearing in multiple schemas
Step 6: Validate output
Step 7: Deliver production-ready markup
```

### 2. Validate Schema

```
Step 1: Check syntax (valid JSON, correct @context, @type)
Step 2: Verify all required properties present for the schema type
Step 3: Check data formats (dates, URLs, currencies, rating ranges)
Step 4: Flag missing recommended properties
Step 5: Identify rich result eligibility
Step 6: Provide fix instructions for any issues
```

### 3. Deploy Schema

```
Step 1: Provide exact <script type="application/ld+json"> block
Step 2: For WordPress: functions.php snippet or shortcode approach
Step 3: For static sites: placement instructions
Step 4: For CMS plugins: recommend plugin + configuration
Step 5: Include deployment verification steps
```

### 4. Stack Multiple Schemas

```
Step 1: Use @graph to combine in one script block, OR separate scripts for clarity
Step 2: Link related schemas with @id references
Step 3: Ensure no conflicting or duplicate data
Step 4: Validate the complete @graph
```

## Implementation Patterns

### WordPress: functions.php
```php
function add_schema_markup() {
    if (is_single() || is_page()) {
        $schema = array(
            '@context' => 'https://schema.org',
            '@type' => 'Article',
            'headline' => get_the_title(),
            'datePublished' => get_the_date('c'),
            'dateModified' => get_the_modified_date('c'),
            'author' => array(
                '@type' => 'Person',
                'name' => get_the_author()
            )
        );
        echo '<script type="application/ld+json">' . json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . '</script>';
    }
}
add_action('wp_footer', 'add_schema_markup');
```

### WordPress: Custom Fields (Dynamic Product Data)
```php
function get_product_schema() {
    $schema = array(
        '@context' => 'https://schema.org',
        '@type' => 'Product',
        'name' => get_field('product_name'),
        'image' => get_field('product_image'),
        'description' => get_field('product_description'),
        'brand' => array('@type' => 'Brand', 'name' => get_field('product_brand')),
        'offers' => array(
            '@type' => 'Offer',
            'price' => get_field('product_price'),
            'priceCurrency' => 'USD',
            'availability' => 'https://schema.org/InStock',
            'url' => get_field('affiliate_link')
        )
    );
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

### Static HTML: @graph Template
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@graph": [
        { "@type": "BreadcrumbList", "@id": "#breadcrumb", ... },
        { "@type": "Article", "@id": "#article", ... },
        { "@type": "FAQPage", "@id": "#faq", ... }
    ]
}
</script>
```

## Field Requirements Quick Reference

### Product (Required for rich results)
| Property | Required? | Notes |
|----------|-----------|-------|
| `name` | ✅ Required | Product name |
| `image` | ✅ Required | At least one absolute URL |
| `aggregateRating` or `review` | ⚡ For stars | At least one for star ratings |
| `offers` | ✅ For price | Include price, priceCurrency, availability, url |

### Article
| Property | Required? | Notes |
|----------|-----------|-------|
| `headline` | ✅ Required | <110 chars for AMP |
| `image` | ✅ Required | 1200×630+ |
| `datePublished` | ✅ Required | ISO 8601 |
| `dateModified` | Recommended | ISO 8601 |
| `author` | ✅ Required | Person or Organization |
| `publisher` | Recommended | Organization |

### FAQPage
| Property | Required? | Notes |
|----------|-----------|-------|
| `mainEntity` | ✅ Required | Array of Question objects |
| Each Question → `name` | ✅ Required | The question text |
| Each Question → `acceptedAnswer.text` | ✅ Required | The answer text |

### HowTo
| Property | Required? | Notes |
|----------|-----------|-------|
| `name` | ✅ Required | Title of the how-to |
| `step` | ✅ Required | Array with `text` or `itemListElement` |
| `totalTime` | Recommended | ISO 8601 duration |

### ItemList
| Property | Required? | Notes |
|----------|-----------|-------|
| `numberOfItems` | Recommended | Total count |
| `itemListElement` | ✅ Required | Array of ListItem with position + item |

### BreadcrumbList
| Property | Required? | Notes |
|----------|-----------|-------|
| `itemListElement` | ✅ Required | Array with position, name, item (URL) |

### SoftwareApplication
| Property | Required? | Notes |
|----------|-----------|-------|
| `name` | ✅ Required | App/tool name |
| `applicationCategory` | ✅ Required | Category |
| `operatingSystem` | Recommended | OS requirements |
| `offers` | For pricing | Price and availability |

## Rich Result Eligibility Matrix

| Schema Type | Rich Result | Key Requirements |
|------------|-------------|-----------------|
| Product | Price, availability, reviews | offers + aggregateRating or review |
| FAQPage | FAQ accordion | mainEntity with Question/Answer |
| HowTo | HowTo carousel | step array with text |
| Article | Top Stories, headline | headline + image + datePublished |
| BreadcrumbList | Breadcrumb trail | itemListElement with position/name/item |
| ItemList | Carousel/List | itemListElement with ListItem |
| SoftwareApplication | App listing | name + applicationCategory |
| Review/AggregateRating | Star ratings | ratingValue + bestRating + reviewCount |
| Organization | Knowledge panel | name + url + logo + sameAs |

## Affiliate Schema Cheat Sheet

| Page Type | Schema Stack |
|-----------|-------------|
| Product Review | Product + Review + BreadcrumbList + Organization |
| "Best X" Roundup | ItemList (of Products) + BreadcrumbList + Organization |
| Comparison | ItemList or 2×Product + BreadcrumbList + FAQPage |
| How-To Guide | HowTo + Article + BreadcrumbList + Organization |
| Blog Post | Article + BreadcrumbList + Organization + (optional FAQPage) |
| Software Review | SoftwareApplication + Review + BreadcrumbList + FAQPage |
| Category Page | ItemList + BreadcrumbList + Organization |
| Homepage | Organization + WebSite + SearchAction |

**For all page types:** Include BreadcrumbList (every page) and Organization (every page or site-wide).

## Common Mistakes & Anti-Patterns

| Anti-Pattern | Consequence | Prevention |
|-------------|-------------|-----------|
| Fabricating AggregateRating | Google penalty, trust loss | Use only real review data |
| Missing `offers` on Product | No price rich result | Always include offers block |
| Relative URLs in schema | Validation errors, ignored by Google | Absolute URLs only |
| Wrong date format | Schema error | ISO 8601 format |
| Not validating before deploy | Broken rich results | Always run through Rich Results Test |
| Multiple conflicting schemas | Google picks one (may be wrong) | Use @graph with @id references |

## Verification Steps

1. Parse JSON-LD — confirm valid JSON
2. Validate at https://search.google.com/test/rich-results — zero errors
3. Validate at https://validator.schema.org/ — zero errors
4. Check all required properties for the schema type
5. Verify absolute URLs, ISO dates, correct currency codes
6. Test @id references resolve correctly in @graph
7. Confirm rich result eligibility for target schema type


## Self-Critique Scorecard (/25)
After every operation, score yourself:

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Functionality** (1-5) | ? | Does it work perfectly and meet all requirements? |
| **Quality** (1-5) | ? | Is it enterprise-grade and production-ready? |
| **Verification** (1-5) | ? | Was it verified via multiple methods? |
| **Speed** (1-5) | ? | Was execution optimal with parallel operations? |
| **Learning** (1-5) | ? | Were new patterns documented and memory updated? |

**Target: 22+/25 before claiming completion**

### Pre-Flight Checklist
- [ ] Credentials verified and target exists
- [ ] Rollback plan identified
- [ ] Success criteria defined
- [ ] Anti-patterns reviewed

### Post-Flight Checklist
- [ ] Verified via API response + live check
- [ ] Quality score logged to memory/YYYY-MM-DD.md
- [ ] Skill references updated if new patterns discovered
- [ ] No common mistakes made

## Output Contract

| Field | Description |
|-------|-------------|
| **Artifact** | Production-ready JSON-LD schema markup |
| **Evidence** | Validation results from Google Rich Results Test and schema.org validator |
| **Decision** | Schema type(s) selected and rationale |
| **Next** | Deploy to page, monitor for rich result appearance in SERPs (2–4 weeks) |

## Resources

- `references/schema-templates.md` — Full JSON-LD templates for every type
- `references/affiliate-schema-guide.md` — Affiliate-specific implementation patterns
- `references/rich-result-optimization.md` — Rich result optimization strategies
- `scripts/validate-schema.py` — Schema validation script

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
