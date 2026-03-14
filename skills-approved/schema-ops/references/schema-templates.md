# Schema Templates — Complete JSON-LD Reference

Production-ready JSON-LD templates for every schema type used in affiliate marketing.

---

## 1. Product Schema

### Basic Product with Offer
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://yoursite.com/product/#product",
  "name": "Sony WH-1000XM5 Wireless Headphones",
  "description": "Industry-leading noise cancellation with Auto NC Optimizer, crystal-clear hands-free calling, and up to 30 hours of battery life.",
  "image": [
    "https://yoursite.com/images/sony-xm5-front.jpg",
    "https://yoursite.com/images/sony-xm5-side.jpg",
    "https://yoursite.com/images/sony-xm5-folded.jpg"
  ],
  "brand": {
    "@type": "Brand",
    "name": "Sony"
  },
  "sku": "WH1000XM5/B",
  "mpn": "WH1000XM5B",
  "gtin13": "4548736133195",
  "offers": {
    "@type": "Offer",
    "@id": "https://yoursite.com/product/#offer",
    "url": "https://example.com/affiliate-link",
    "priceCurrency": "USD",
    "price": "348.00",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "seller": {
      "@type": "Organization",
      "name": "Amazon"
    }
  }
}
```

### Product with AggregateRating
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://yoursite.com/product/#product",
  "name": "Sony WH-1000XM5 Wireless Headphones",
  "description": "Industry-leading noise cancellation with Auto NC Optimizer.",
  "image": "https://yoursite.com/images/sony-xm5-front.jpg",
  "brand": {
    "@type": "Brand",
    "name": "Sony"
  },
  "sku": "WH1000XM5/B",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.7",
    "bestRating": "5",
    "worstRating": "1",
    "ratingCount": "2847",
    "reviewCount": "1523"
  },
  "review": [
    {
      "@type": "Review",
      "@id": "https://yoursite.com/product/#review1",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "4.8",
        "bestRating": "5",
        "worstRating": "1"
      },
      "author": {
        "@type": "Person",
        "name": "John Smith"
      },
      "datePublished": "2026-02-15",
      "reviewBody": "Excellent noise cancellation and sound quality. Battery life is outstanding at 30+ hours. Comfortable for all-day wear. The touch controls take some getting used to but work well once learned."
    }
  ],
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/affiliate-link",
    "priceCurrency": "USD",
    "price": "348.00",
    "availability": "https://schema.org/InStock"
  }
}
```

### Product with Multiple Offers (Price Comparison)
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://yoursite.com/product/#product",
  "name": "Sony WH-1000XM5 Wireless Headphones",
  "image": "https://yoursite.com/images/sony-xm5-front.jpg",
  "brand": {
    "@type": "Brand",
    "name": "Sony"
  },
  "offers": {
    "@type": "AggregateOffer",
    "offerCount": "3",
    "lowPrice": "328.00",
    "highPrice": "398.00",
    "priceCurrency": "USD",
    "offers": [
      {
        "@type": "Offer",
        "url": "https://example.com/affiliate-link-amazon",
        "price": "348.00",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "seller": { "@type": "Organization", "name": "Amazon" }
      },
      {
        "@type": "Offer",
        "url": "https://example.com/affiliate-link-bh",
        "price": "328.00",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "seller": { "@type": "Organization", "name": "B&H Photo" }
      },
      {
        "@type": "Offer",
        "url": "https://example.com/affiliate-link-bestbuy",
        "price": "398.00",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "seller": { "@type": "Organization", "name": "Best Buy" }
      }
    ]
  }
}
```

---

## 2. Review Schema

### Standalone Review
```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "Product",
    "name": "Sony WH-1000XM5",
    "image": "https://yoursite.com/images/sony-xm5-front.jpg",
    "brand": { "@type": "Brand", "name": "Sony" }
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "4.7",
    "bestRating": "5",
    "worstRating": "1"
  },
  "author": {
    "@type": "Person",
    "name": "Jane Doe",
    "url": "https://yoursite.com/author/jane-doe"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Your Site Name",
    "url": "https://yoursite.com"
  },
  "datePublished": "2026-02-15",
  "dateModified": "2026-03-01",
  "reviewBody": "After testing these headphones for 3 months, here's our comprehensive review...",
  "headline": "Sony WH-1000XM5 Review: The Best Noise-Canceling Headphones in 2026"
}
```

---

## 3. FAQPage Schema

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are the Sony WH-1000XM5 worth it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, the Sony WH-1000XM5 are worth it for most users who prioritize noise cancellation and sound quality. They offer industry-leading ANC, 30-hour battery life, and excellent comfort. However, if you're on a tighter budget, the XM4 offers 80% of the performance at a lower price."
      }
    },
    {
      "@type": "Question",
      "name": "How long does the battery last on the WH-1000XM5?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Sony WH-1000XM5 deliver up to 30 hours of battery life with ANC enabled, and up to 40 hours with ANC off. A 3-minute quick charge gives you 3 hours of playback."
      }
    },
    {
      "@type": "Question",
      "name": "Can you use the WH-1000XM5 while charging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, you can use the Sony WH-1000XM5 while charging via USB-C. However, they do not support wired audio playback through the USB-C port — you'd need to use the included 3.5mm audio cable for wired listening."
      }
    }
  ]
}
```

---

## 4. HowTo Schema

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Set Up Sony WH-1000XM5 for the Best Sound Quality",
  "description": "Step-by-step guide to configure your Sony WH-1000XM5 headphones for optimal audio performance and noise cancellation.",
  "totalTime": "PT20M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "USD",
    "value": "0"
  },
  "tool": [
    {
      "@type": "HowToTool",
      "name": "Sony WH-1000XM5 headphones"
    },
    {
      "@type": "HowToTool",
      "name": "Smartphone with Sony Headphones Connect app"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Download the Sony Headphones Connect App",
      "text": "Download and install the Sony Headphones Connect app from the App Store or Google Play Store on your smartphone.",
      "image": "https://yoursite.com/images/step1-app-download.jpg",
      "url": "https://yoursite.com/guide#step1"
    },
    {
      "@type": "HowToStep",
      "name": "Pair via Bluetooth",
      "text": "Press and hold the power button on your XM5 for 7 seconds until you hear 'Bluetooth pairing'. Select 'WH-1000XM5' from your phone's Bluetooth settings.",
      "image": "https://yoursite.com/images/step2-bluetooth.jpg",
      "url": "https://yoursite.com/guide#step2"
    },
    {
      "@type": "HowToStep",
      "name": "Configure Sound Settings",
      "text": "Open the Headphones Connect app and adjust the equalizer to your preference. We recommend the 'Excited' preset for most music genres.",
      "image": "https://yoursite.com/images/step3-eq-settings.jpg",
      "url": "https://yoursite.com/guide#step3"
    }
  ]
}
```

---

## 5. Article Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "https://yoursite.com/best-headphones-2026/#article",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://yoursite.com/best-headphones-2026/"
  },
  "headline": "Best Wireless Headphones in 2026: 10 Picks Tested and Ranked",
  "description": "We tested 50+ wireless headphones over 6 months to find the 10 best for every budget and use case. Updated March 2026.",
  "image": {
    "@type": "ImageObject",
    "url": "https://yoursite.com/images/best-headphones-2026-og.jpg",
    "width": 1200,
    "height": 630
  },
  "datePublished": "2026-01-15T08:00:00Z",
  "dateModified": "2026-03-10T14:30:00Z",
  "author": {
    "@type": "Person",
    "@id": "https://yoursite.com/author/jane-doe/#person",
    "name": "Jane Doe",
    "url": "https://yoursite.com/author/jane-doe"
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://yoursite.com/#organization",
    "name": "Your Site Name",
    "url": "https://yoursite.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://yoursite.com/images/logo.png",
      "width": 600,
      "height": 60
    }
  },
  "wordCount": "4850",
  "articleSection": "Technology",
  "keywords": ["best wireless headphones", "wireless headphones 2026", "bluetooth headphones review"]
}
```

### BlogPosting Variant (lighter, for blog posts)
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Sony WH-1000XM5 vs Bose 700: Which Should You Buy?",
  "image": "https://yoursite.com/images/xm5-vs-bose700.jpg",
  "datePublished": "2026-02-20T09:00:00Z",
  "dateModified": "2026-03-01T12:00:00Z",
  "author": {
    "@type": "Person",
    "name": "Jane Doe",
    "url": "https://yoursite.com/author/jane-doe"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Your Site Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://yoursite.com/images/logo.png"
    }
  },
  "description": "We compare Sony's flagship XM5 against Bose's 700 in noise cancellation, sound quality, comfort, and value."
}
```

---

## 6. BreadcrumbList Schema

```json
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
      "name": "Electronics",
      "item": "https://yoursite.com/electronics/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Headphones",
      "item": "https://yoursite.com/electronics/headphones/"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "Sony WH-1000XM5 Review",
      "item": "https://yoursite.com/electronics/headphones/sony-wh-1000xm5-review/"
    }
  ]
}
```

---

## 7. ItemList Schema (for "Best Of" Roundup Pages)

### Ordered List of Products
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "@id": "https://yoursite.com/best-headphones-2026/#itemlist",
  "name": "Best Wireless Headphones 2026",
  "description": "Our top 10 picks for the best wireless headphones, tested and ranked.",
  "numberOfItems": 10,
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Product",
        "@id": "https://yoursite.com/best-headphones-2026/#product1",
        "name": "Sony WH-1000XM5",
        "image": "https://yoursite.com/images/sony-xm5-front.jpg",
        "url": "https://yoursite.com/sony-wh-1000xm5-review/",
        "brand": { "@type": "Brand", "name": "Sony" },
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4.7",
          "reviewCount": "1523"
        },
        "offers": {
          "@type": "Offer",
          "price": "348.00",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "url": "https://example.com/affiliate-link-xm5"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Product",
        "@id": "https://yoursite.com/best-headphones-2026/#product2",
        "name": "Bose QuietComfort Ultra",
        "image": "https://yoursite.com/images/bose-qc-ultra.jpg",
        "url": "https://yoursite.com/bose-qc-ultra-review/",
        "brand": { "@type": "Brand", "name": "Bose" },
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4.5",
          "reviewCount": "987"
        },
        "offers": {
          "@type": "Offer",
          "price": "379.00",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "url": "https://example.com/affiliate-link-bose"
        }
      }
    }
  ]
}
```

---

## 8. Organization Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://yoursite.com/#organization",
  "name": "Your Site Name",
  "url": "https://yoursite.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://yoursite.com/images/logo.png",
    "width": 600,
    "height": 60
  },
  "image": "https://yoursite.com/images/og-default.jpg",
  "description": "Honest, in-depth reviews of tech products. We test everything so you don't have to.",
  "foundingDate": "2020-01-01",
  "founder": {
    "@type": "Person",
    "name": "Your Name"
  },
  "sameAs": [
    "https://twitter.com/yoursite",
    "https://facebook.com/yoursite",
    "https://youtube.com/yoursite",
    "https://linkedin.com/company/yoursite"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "hello@yoursite.com"
  }
}
```

---

## 9. Person Schema (Author)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://yoursite.com/author/jane-doe/#person",
  "name": "Jane Doe",
  "url": "https://yoursite.com/author/jane-doe",
  "image": {
    "@type": "ImageObject",
    "url": "https://yoursite.com/images/authors/jane-doe.jpg",
    "width": 400,
    "height": 400
  },
  "jobTitle": "Senior Tech Reviewer",
  "description": "Jane has been reviewing consumer electronics for 8 years and has tested over 500 products.",
  "sameAs": [
    "https://twitter.com/janedoe",
    "https://linkedin.com/in/janedoe",
    "https://youtube.com/janedoe"
  ],
  "worksFor": {
    "@type": "Organization",
    "name": "Your Site Name",
    "url": "https://yoursite.com"
  },
  "knowsAbout": ["headphones", "wireless audio", "consumer electronics", "tech reviews"]
}
```

---

## 10. SoftwareApplication Schema

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "@id": "https://yoursite.com/nordvpn-review/#software",
  "name": "NordVPN",
  "description": "NordVPN is a virtual private network service with 5,500+ servers in 60 countries, offering strong encryption, fast speeds, and a strict no-logs policy.",
  "url": "https://nordvpn.com",
  "applicationCategory": "SecurityApplication",
  "operatingSystem": ["Windows", "macOS", "Linux", "Android", "iOS", "Android TV"],
  "softwareVersion": "7.0",
  "offers": {
    "@type": "Offer",
    "price": "3.49",
    "priceCurrency": "USD",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "price": "3.49",
      "priceCurrency": "USD",
      "unitCode": "MON",
      "billingDuration": "P1M"
    },
    "url": "https://example.com/affiliate-link-nordvpn"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.6",
    "bestRating": "5",
    "ratingCount": "12450"
  },
  "screenshot": "https://yoursite.com/images/nordvpn-app-screenshot.jpg",
  "featureList": "No-logs policy, Double VPN, Kill Switch, Split tunneling, 5500+ servers"
}
```

---

## 11. WebSite Schema (with SearchAction)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://yoursite.com/#website",
  "name": "Your Site Name",
  "url": "https://yoursite.com",
  "description": "Honest, in-depth reviews of tech products.",
  "publisher": {
    "@id": "https://yoursite.com/#organization"
  },
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://yoursite.com/?s={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

---

## 12. Stacked Schema Example (Multiple Types on One Page)

### Blog Post with FAQ + Breadcrumbs + Organization
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BreadcrumbList",
      "@id": "https://yoursite.com/best-headphones-2026/#breadcrumb",
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
          "name": "Reviews",
          "item": "https://yoursite.com/reviews/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Best Wireless Headphones 2026",
          "item": "https://yoursite.com/best-headphones-2026/"
        }
      ]
    },
    {
      "@type": "Article",
      "@id": "https://yoursite.com/best-headphones-2026/#article",
      "mainEntityOfPage": {
        "@id": "https://yoursite.com/best-headphones-2026/"
      },
      "headline": "Best Wireless Headphones in 2026: 10 Picks Tested",
      "image": {
        "@type": "ImageObject",
        "url": "https://yoursite.com/images/best-headphones-og.jpg",
        "width": 1200,
        "height": 630
      },
      "datePublished": "2026-01-15T08:00:00Z",
      "dateModified": "2026-03-10T14:30:00Z",
      "author": {
        "@type": "Person",
        "@id": "https://yoursite.com/author/jane-doe/#person",
        "name": "Jane Doe",
        "url": "https://yoursite.com/author/jane-doe"
      },
      "publisher": {
        "@id": "https://yoursite.com/#organization"
      }
    },
    {
      "@type": "Organization",
      "@id": "https://yoursite.com/#organization",
      "name": "Your Site Name",
      "url": "https://yoursite.com",
      "logo": {
        "@type": "ImageObject",
        "url": "https://yoursite.com/images/logo.png"
      },
      "sameAs": [
        "https://twitter.com/yoursite",
        "https://facebook.com/yoursite"
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://yoursite.com/best-headphones-2026/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the best wireless headphone in 2026?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Sony WH-1000XM5 is our top pick for 2026, offering the best combination of noise cancellation, sound quality, and battery life."
          }
        },
        {
          "@type": "Question",
          "name": "How much should I spend on wireless headphones?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "For most users, $200-$400 offers the best value. Under $100 you'll find decent options like the Anker Soundcore Space A40. Over $400 you get premium options like the Apple AirPods Max."
          }
        }
      ]
    }
  ]
}
```

---

## 13. VideoObject Schema (for Embedded Review Videos)

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Sony WH-1000XM5 Review - 6 Months Later",
  "description": "Our full review of the Sony WH-1000XM5 after 6 months of daily use. Is it still the best?",
  "thumbnailUrl": "https://yoursite.com/images/video-thumb-xm5.jpg",
  "uploadDate": "2026-02-15T10:00:00Z",
  "duration": "PT15M32S",
  "contentUrl": "https://yoursite.com/videos/xm5-review.mp4",
  "embedUrl": "https://www.youtube.com/embed/VIDEO_ID",
  "interactionStatistic": {
    "@type": "InteractionCounter",
    "interactionType": { "@type": "WatchAction" },
    "userInteractionCount": 45230
  }
}
```

---

## 14. ItemList for Comparison Pages

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Sony WH-1000XM5 vs Bose QuietComfort Ultra Comparison",
  "description": "Side-by-side comparison of Sony XM5 and Bose QC Ultra headphones.",
  "numberOfItems": 2,
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Product",
        "name": "Sony WH-1000XM5",
        "image": "https://yoursite.com/images/sony-xm5.jpg",
        "url": "https://yoursite.com/sony-wh-1000xm5-review/",
        "brand": { "@type": "Brand", "name": "Sony" },
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4.7",
          "reviewCount": "1523"
        },
        "offers": {
          "@type": "Offer",
          "price": "348.00",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "url": "https://example.com/affiliate-link-xm5"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Product",
        "name": "Bose QuietComfort Ultra",
        "image": "https://yoursite.com/images/bose-qc-ultra.jpg",
        "url": "https://yoursite.com/bose-qc-ultra-review/",
        "brand": { "@type": "Brand", "name": "Bose" },
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4.5",
          "reviewCount": "987"
        },
        "offers": {
          "@type": "Offer",
          "price": "379.00",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "url": "https://example.com/affiliate-link-bose"
        }
      }
    }
  ]
}
```

---

## 15. Organization + WebSite + SearchAction (Homepage Stack)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://yoursite.com/#organization",
      "name": "Your Site Name",
      "url": "https://yoursite.com",
      "logo": {
        "@type": "ImageObject",
        "url": "https://yoursite.com/images/logo.png",
        "width": 600,
        "height": 60
      },
      "sameAs": [
        "https://twitter.com/yoursite",
        "https://facebook.com/yoursite",
        "https://youtube.com/yoursite"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://yoursite.com/#website",
      "name": "Your Site Name",
      "url": "https://yoursite.com",
      "publisher": {
        "@id": "https://yoursite.com/#organization"
      },
      "potentialAction": {
        "@type": "SearchAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": "https://yoursite.com/?s={search_term_string}"
        },
        "query-input": "required name=search_term_string"
      }
    }
  ]
}
```
