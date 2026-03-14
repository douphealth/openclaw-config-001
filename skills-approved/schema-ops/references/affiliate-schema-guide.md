# Affiliate Schema Implementation Guide

Comprehensive guide for implementing structured data on affiliate marketing sites. Covers page-level schema mapping, dynamic generation with PHP, and advanced techniques.

---

## Page Type → Schema Mapping

### 1. Single Product Review Page

**Page structure:** In-depth review of one product

**Required schemas:**
- `Product` (with `Review` nested inside)
- `BreadcrumbList`
- `Organization` (once site-wide)

**Recommended additions:**
- `FAQPage` (if FAQ section exists)
- `Person` (author — if not site-wide)
- `VideoObject` (if video review embedded)

**Implementation pattern:**
```php
// In single-product-review.php or functions.php
function product_review_schema() {
    if (!is_single() || !has_category('reviews')) return;
    
    $product = get_product_data(); // Your custom function
    
    $schema = [
        '@context' => 'https://schema.org',
        '@graph' => [
            get_breadcrumb_schema(),
            [
                '@type' => 'Product',
                '@id' => get_permalink() . '#product',
                'name' => $product['name'],
                'description' => $product['description'],
                'image' => $product['images'],
                'brand' => ['@type' => 'Brand', 'name' => $product['brand']],
                'sku' => $product['sku'],
                'aggregateRating' => [
                    '@type' => 'AggregateRating',
                    'ratingValue' => $product['rating'],
                    'bestRating' => '5',
                    'reviewCount' => $product['review_count']
                ],
                'review' => [
                    '@type' => 'Review',
                    'reviewRating' => [
                        '@type' => 'Rating',
                        'ratingValue' => $product['our_rating'],
                        'bestRating' => '5'
                    ],
                    'author' => [
                        '@type' => 'Person',
                        'name' => get_the_author(),
                        'url' => get_author_posts_url(get_the_author_meta('ID'))
                    ],
                    'datePublished' => get_the_date('c'),
                    'dateModified' => get_the_modified_date('c'),
                    'reviewBody' => wp_strip_all_tags(get_the_excerpt())
                ],
                'offers' => [
                    '@type' => 'Offer',
                    'url' => $product['affiliate_url'],
                    'priceCurrency' => $product['currency'],
                    'price' => $product['price'],
                    'availability' => $product['in_stock'] 
                        ? 'https://schema.org/InStock' 
                        : 'https://schema.org/OutOfStock',
                    'priceValidUntil' => date('Y-m-d', strtotime('+30 days'))
                ]
            ]
        ]
    ];
    
    echo '<script type="application/ld+json">' . 
         json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . 
         '</script>';
}
add_action('wp_footer', 'product_review_schema');
```

---

### 2. "Best Of" Roundup Page

**Page structure:** "Best X in YYYY" — ranked list of products

**Required schemas:**
- `ItemList` (containing `Product` items)
- `BreadcrumbList`

**Recommended additions:**
- `Article` (for the editorial content)
- `FAQPage` (buyer's guide FAQ section)
- `Organization`

**Key decisions:**
- Use `ItemList` with `ListItem` elements
- Each `ListItem.item` should be a `Product` with offers
- Position field = your ranking number
- Include `numberOfItems` for clarity

**Implementation pattern:**
```php
function roundup_itemlist_schema($products) {
    // $products is array of product data from your DB/CMB2/ACF
    // Sorted by your ranking
    
    $list_items = [];
    foreach ($products as $i => $p) {
        $list_items[] = [
            '@type' => 'ListItem',
            'position' => $i + 1,
            'item' => [
                '@type' => 'Product',
                '@id' => get_permalink() . '#product' . ($i + 1),
                'name' => $p['name'],
                'image' => $p['image'],
                'url' => $p['review_url'] ?: get_permalink(),
                'brand' => ['@type' => 'Brand', 'name' => $p['brand']],
                'aggregateRating' => [
                    '@type' => 'AggregateRating',
                    'ratingValue' => $p['rating'],
                    'reviewCount' => $p['review_count']
                ],
                'offers' => [
                    '@type' => 'Offer',
                    'price' => $p['price'],
                    'priceCurrency' => $p['currency'],
                    'availability' => $p['in_stock'] 
                        ? 'https://schema.org/InStock' 
                        : 'https://schema.org/OutOfStock',
                    'url' => $p['affiliate_url']
                ]
            ]
        ];
    }
    
    $schema = [
        '@context' => 'https://schema.org',
        '@type' => 'ItemList',
        'name' => get_the_title(),
        'description' => wp_strip_all_tags(get_the_excerpt()),
        'numberOfItems' => count($products),
        'itemListElement' => $list_items
    ];
    
    return $schema;
}
```

**Data requirements per product in the list:**
| Field | Required? | Notes |
|-------|-----------|-------|
| name | Yes | Product display name |
| image | Yes | Absolute URL, 696px+ wide |
| rating | Yes* | Your site's rating or aggregate |
| review_count | Yes* | Number of reviews |
| price | Yes | Current price |
| currency | Yes | ISO 4217 code |
| affiliate_url | Yes | Your tracked affiliate link |
| in_stock | Yes | Boolean |
| brand | Recommended | Brand name |
| review_url | Recommended | Link to individual review on your site |

---

### 3. Comparison Page ("X vs Y")

**Page structure:** Head-to-head comparison of 2+ products

**Required schemas:**
- `ItemList` (containing compared products)
- `BreadcrumbList`

**Recommended:**
- `FAQPage` (frequently asked comparison questions)
- `Product` schema per product (can nest inside ItemList)

**Pattern:** Same as roundup but typically with 2-3 items. Include your rating and affiliate link for each product.

---

### 4. How-To Guide

**Page structure:** Step-by-step tutorial related to a product

**Required schemas:**
- `HowTo`
- `BreadcrumbList`

**Recommended:**
- `Article`
- `FAQPage`
- `VideoObject` (if video tutorial)

**Key points:**
- Each step needs `name` and `text` at minimum
- Add `image` and `url` per step when available
- Include `totalTime` as ISO 8601 duration (`PT15M` = 15 minutes)
- `tool` array lists required tools/items

---

### 5. Blog Post (Informational)

**Page structure:** Topical blog post (not a review)

**Required schemas:**
- `Article` or `BlogPosting`
- `BreadcrumbList`

**Recommended:**
- `FAQPage` (if FAQ section exists)
- `Organization`
- `Person` (author)

**Notes:**
- Use `Article` for longer, editorial content
- Use `BlogPosting` for shorter blog entries
- Include `datePublished` and `dateModified`
- `headline` should be <110 characters

---

### 6. Category/Archive Page

**Page structure:** List of reviews or posts in a category

**Required schemas:**
- `ItemList` (of Articles or Products)
- `BreadcrumbList`

**Notes:**
- `ItemList` should reference items by URL
- Use `CollectionPage` as the page type alongside ItemList

---

## Dynamic Schema with ACF (Advanced Custom Fields)

### ACF Field Group Setup

Create an ACF field group named "Product Review Data" with these fields:

| Field Name | Field Type | Required | Notes |
|------------|------------|----------|-------|
| product_name | Text | Yes | |
| product_brand | Text | Yes | |
| product_description | Textarea | Yes | Short description |
| product_image | Image | Yes | Returns URL |
| product_images | Gallery | No | Multiple product images |
| product_sku | Text | No | |
| product_price | Number | Yes | Use '.' decimal |
| product_currency | Select | Yes | Options: USD, EUR, GBP |
| product_affiliate_url | URL | Yes | Your affiliate link |
| product_in_stock | True/False | Yes | Default: true |
| product_rating | Number | Yes | 1-5 scale (use 0.1 steps) |
| product_review_count | Number | Yes | Total review count |
| our_rating | Number | Yes | Your editorial rating |
| product_price_valid_until | Date Picker | No | |
| product_gtin | Text | No | GTIN/UPC/EAN |

### PHP: Generate Schema from ACF Fields

```php
function generate_product_schema_from_acf() {
    if (!get_field('product_name')) return '';
    
    $schema = [
        '@context' => 'https://schema.org',
        '@type' => 'Product',
        'name' => get_field('product_name'),
        'description' => get_field('product_description'),
        'image' => [],
        'brand' => [
            '@type' => 'Brand',
            'name' => get_field('product_brand')
        ],
        'offers' => [
            '@type' => 'Offer',
            'url' => get_field('product_affiliate_url'),
            'price' => strval(get_field('product_price')),
            'priceCurrency' => get_field('product_currency'),
            'availability' => get_field('product_in_stock')
                ? 'https://schema.org/InStock'
                : 'https://schema.org/OutOfStock'
        ]
    ];
    
    // Handle images
    $main_image = get_field('product_image');
    if ($main_image) {
        $schema['image'][] = is_array($main_image) 
            ? $main_image['url'] 
            : $main_image;
    }
    $gallery = get_field('product_images');
    if ($gallery) {
        foreach ($gallery as $img) {
            $schema['image'][] = $img['url'];
        }
    }
    
    // Handle GTIN
    $gtin = get_field('product_gtin');
    if ($gtin) {
        if (strlen($gtin) == 13) $schema['gtin13'] = $gtin;
        elseif (strlen($gtin) == 12) $schema['gtin12'] = $gtin;
        elseif (strlen($gtin) == 8) $schema['gtin8'] = $gtin;
    }
    
    // Handle SKU
    $sku = get_field('product_sku');
    if ($sku) $schema['sku'] = $sku;
    
    // Handle price validity
    $price_valid = get_field('product_price_valid_until');
    if ($price_valid) {
        $schema['offers']['priceValidUntil'] = $price_valid;
    }
    
    // Handle ratings
    $rating = get_field('product_rating');
    $review_count = get_field('product_review_count');
    if ($rating && $review_count) {
        $schema['aggregateRating'] = [
            '@type' => 'AggregateRating',
            'ratingValue' => strval($rating),
            'bestRating' => '5',
            'worstRating' => '1',
            'reviewCount' => strval($review_count)
        ];
    }
    
    // Handle editorial review
    $our_rating = get_field('our_rating');
    if ($our_rating) {
        $schema['review'] = [
            '@type' => 'Review',
            'reviewRating' => [
                '@type' => 'Rating',
                'ratingValue' => strval($our_rating),
                'bestRating' => '5'
            ],
            'author' => [
                '@type' => 'Person',
                'name' => get_the_author()
            ],
            'datePublished' => get_the_date('c'),
            'dateModified' => get_the_modified_date('c'),
            'reviewBody' => wp_strip_all_tags(get_the_excerpt())
        ];
    }
    
    return $schema;
}
```

---

## Breadcrumb Helper Function

```php
function get_breadcrumb_schema() {
    $breadcrumbs = [];
    $position = 1;
    
    // Home
    $breadcrumbs[] = [
        '@type' => 'ListItem',
        'position' => $position++,
        'name' => 'Home',
        'item' => home_url('/')
    ];
    
    // Category (if post has category)
    if (is_single()) {
        $categories = get_the_category();
        if (!empty($categories)) {
            $cat = $categories[0]; // Primary category
            $breadcrumbs[] = [
                '@type' => 'ListItem',
                'position' => $position++,
                'name' => $cat->name,
                'item' => get_category_link($cat->term_id)
            ];
        }
    }
    
    // Current page (no 'item' URL on last element per Google's guidance)
    if (is_single() || is_page()) {
        $breadcrumbs[] = [
            '@type' => 'ListItem',
            'position' => $position,
            'name' => get_the_title()
        ];
    }
    
    return [
        '@type' => 'BreadcrumbList',
        'itemListElement' => $breadcrumbs
    ];
}
```

---

## FAQ Schema Helper

```php
// Assumes FAQ content is in a repeater ACF field
function get_faq_schema() {
    $faqs = get_field('faq_items'); // ACF repeater
    if (!$faqs || empty($faqs)) return null;
    
    $questions = [];
    foreach ($faqs as $faq) {
        $questions[] = [
            '@type' => 'Question',
            'name' => $faq['question'],
            'acceptedAnswer' => [
                '@type' => 'Answer',
                'text' => wp_kses_post($faq['answer']) // Allow basic HTML
            ]
        ];
    }
    
    return [
        '@type' => 'FAQPage',
        'mainEntity' => $questions
    ];
}
```

---

## Software Application Schema (for SaaS/Tool Reviews)

```php
function get_software_schema() {
    return [
        '@context' => 'https://schema.org',
        '@type' => 'SoftwareApplication',
        'name' => get_field('software_name'),
        'description' => get_field('software_description'),
        'url' => get_field('software_website'),
        'applicationCategory' => get_field('software_category'), // e.g., "BusinessApplication"
        'operatingSystem' => get_field('software_platforms'), // e.g., "Web, iOS, Android"
        'softwareVersion' => get_field('software_version'),
        'screenshot' => get_field('software_screenshot'),
        'featureList' => get_field('software_features'), // comma-separated
        'offers' => [
            '@type' => 'Offer',
            'price' => get_field('software_price'),
            'priceCurrency' => get_field('software_currency'),
            'url' => get_field('affiliate_url')
        ],
        'aggregateRating' => [
            '@type' => 'AggregateRating',
            'ratingValue' => get_field('software_rating'),
            'bestRating' => '5',
            'reviewCount' => get_field('software_review_count')
        ]
    ];
}
```

---

## Site-Wide Schema (functions.php)

Add Organization + WebSite schemas to every page:

```php
function site_wide_schema() {
    $schema = [
        '@context' => 'https://schema.org',
        '@graph' => [
            [
                '@type' => 'Organization',
                '@id' => home_url('/#organization'),
                'name' => get_bloginfo('name'),
                'url' => home_url('/'),
                'logo' => [
                    '@type' => 'ImageObject',
                    'url' => get_theme_mod('custom_logo') 
                        ? wp_get_attachment_url(get_theme_mod('custom_logo'))
                        : home_url('/images/logo.png')
                ],
                'sameAs' => [
                    get_option('twitter_url', ''),
                    get_option('facebook_url', ''),
                    get_option('youtube_url', ''),
                    get_option('instagram_url', '')
                ]
            ],
            [
                '@type' => 'WebSite',
                '@id' => home_url('/#website'),
                'name' => get_bloginfo('name'),
                'url' => home_url('/'),
                'publisher' => ['@id' => home_url('/#organization')],
                'potentialAction' => [
                    '@type' => 'SearchAction',
                    'target' => [
                        '@type' => 'EntryPoint',
                        'urlTemplate' => home_url('/?s={search_term_string}')
                    ],
                    'query-input' => 'required name=search_term_string'
                ]
            ]
        ]
    ];
    
    // Only output Organization on non-homepage, full stack on homepage
    if (is_front_page()) {
        echo '<script type="application/ld+json">' . 
             json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . 
             '</script>';
    } else {
        // Just Organization on other pages
        $org_schema = [
            '@context' => 'https://schema.org',
            '@type' => 'Organization',
            '@id' => home_url('/#organization'),
            'name' => get_bloginfo('name'),
            'url' => home_url('/'),
            'logo' => $schema['@graph'][0]['logo']
        ];
        echo '<script type="application/ld+json">' . 
             json_encode($org_schema, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . 
             '</script>';
    }
}
add_action('wp_footer', 'site_wide_schema');
```

---

## Combining Multiple Schemas on One Page

Best practice: use `@graph` with `@id` references.

```php
function output_page_schemas() {
    $graph = [];
    
    // Always add breadcrumb
    $graph[] = get_breadcrumb_schema();
    
    // Add page-specific schema
    if (get_field('product_name')) {
        $graph[] = generate_product_schema_from_acf();
    }
    
    // Add FAQ if present
    $faq = get_faq_schema();
    if ($faq) {
        $graph[] = $faq;
    }
    
    // Add author
    $graph[] = [
        '@type' => 'Person',
        '@id' => get_author_posts_url(get_the_author_meta('ID')) . '#person',
        'name' => get_the_author(),
        'url' => get_author_posts_url(get_the_author_meta('ID'))
    ];
    
    $output = [
        '@context' => 'https://schema.org',
        '@graph' => $graph
    ];
    
    echo '<script type="application/ld+json">' . 
         json_encode($output, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . 
         '</script>';
}
```

---

## Advanced Techniques

### SameAs for Entity Disambiguation

Link your Organization to its official social profiles:

```json
"sameAs": [
    "https://twitter.com/yoursite",
    "https://facebook.com/yoursite",
    "https://youtube.com/channel/yourchannel",
    "https://en.wikipedia.org/wiki/Your_Site"
]
```

### about and mentions for Topical Authority

On article pages, declare what the article is about:

```json
{
  "@type": "Article",
  "about": [
    { "@type": "Thing", "name": "wireless headphones" },
    { "@type": "Thing", "name": "noise cancellation technology" }
  ],
  "mentions": [
    { "@type": "Product", "name": "Sony WH-1000XM5" },
    { "@type": "Product", "name": "Bose QuietComfort Ultra" }
  ]
}
```

### mainEntity for FAQ Pages

The `mainEntity` property connects a page to its primary entity:

```json
{
  "@type": "FAQPage",
  "@id": "https://yoursite.com/faq/#faq",
  "mainEntity": [
    { "@type": "Question", "name": "...", "acceptedAnswer": {...} }
  ]
}
```

### subjectOf for Product Pages

Link a product to content that discusses it:

```json
{
  "@type": "Product",
  "name": "Sony WH-1000XM5",
  "subjectOf": {
    "@type": "Article",
    "name": "Sony WH-1000XM5 Full Review",
    "url": "https://yoursite.com/sony-wh-1000xm5-review/"
  }
}
```

### hasPart/isPartOf for Content Series

```json
// On the series hub page:
{
  "@type": "Article",
  "name": "Ultimate Headphone Guide 2026",
  "hasPart": [
    { "@type": "Article", "url": "https://yoursite.com/best-wireless-headphones/" },
    { "@type": "Article", "url": "https://yoursite.com/best-wired-headphones/" },
    { "@type": "Article", "url": "https://yoursite.com/best-budget-headphones/" }
  ]
}

// On each part article:
{
  "@type": "Article",
  "name": "Best Wireless Headphones 2026",
  "isPartOf": {
    "@type": "Article",
    "name": "Ultimate Headphone Guide 2026",
    "url": "https://yoursite.com/headphone-guide-2026/"
  }
}
```

---

## WordPress Plugin Recommendations

### If Not Using Custom Code

| Plugin | Best For | Schema Types |
|--------|----------|-------------|
| **Schema Pro** | All-around best | Product, Review, Article, FAQ, HowTo, Breadcrumb, Organization, Person |
| **Rank Math** | SEO + Schema combo | All major types, auto-detection |
| **Yoast SEO** | SEO + basic schema | Article, Breadcrumb, Organization, WebSite |
| **Schema & Structured Data** | Lightweight | FAQ, HowTo, Product, Review, Breadcrumb |
| **WP Product Review** | Affiliate reviews specifically | Product, Review, AggregateRating |

### Plugin vs Custom Code

**Use custom code when:**
- You have specific schema needs plugins don't cover
- You want full control over output
- You're comfortable with PHP
- You need dynamic data from custom fields

**Use plugins when:**
- You need quick setup
- Non-technical team members manage content
- You're okay with slightly less control
- The plugin covers all your needed types
