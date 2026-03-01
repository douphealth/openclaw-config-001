# Product Box Library (HTML/CSS)

## 1) Primary Review Product Box
```html
<div class="prm-product-box" role="region" aria-label="Primary Product Recommendation">
  <img src="PRODUCT_IMAGE_URL" alt="Product name front view with key feature highlight" loading="lazy" width="720" height="405">
  <div class="prm-product-box__content">
    <h3>PRODUCT_NAME</h3>
    <p class="prm-score">Score: <strong>8.9/10</strong></p>
    <p class="prm-summary">One-line buyer-focused verdict.</p>
    <ul>
      <li>Best for: ...</li>
      <li>Key strength: ...</li>
      <li>Main limitation: ...</li>
    </ul>
    <p class="prm-disclosure"><strong>Disclosure:</strong> Affiliate link. We may earn a commission at no extra cost to you.</p>
    <a href="AFFILIATE_URL" target="_blank" rel="sponsored nofollow noopener" class="prm-btn">Check latest price</a>
  </div>
</div>
```

## 2) Comparison Mini-Card
```html
<div class="prm-card">
  <img src="ALT_IMAGE_URL" alt="Alternative product image" loading="lazy" width="480" height="270">
  <h4>ALTERNATIVE_NAME</h4>
  <p>Best for ...</p>
  <a href="ALT_AFFILIATE_URL" target="_blank" rel="sponsored nofollow noopener">View current price</a>
</div>
```

## Base CSS
```css
.prm-product-box{display:grid;grid-template-columns:1fr;gap:14px;border:1px solid #e5e7eb;border-radius:12px;padding:14px;background:#f8fafc}
.prm-product-box img{width:100%;height:auto;border-radius:10px}
.prm-product-box__content h3{margin:0 0 6px 0}
.prm-score{margin:0 0 8px 0}
.prm-btn{display:inline-block;padding:10px 14px;background:#1d4ed8;color:#fff;text-decoration:none;border-radius:8px;font-weight:700}
.prm-btn:hover{background:#1e40af}
.prm-disclosure{font-size:.85rem;color:#555}
.prm-card{border:1px solid #e5e7eb;border-radius:10px;padding:10px;background:#fff}
@media (min-width:780px){.prm-product-box{grid-template-columns:1fr 1.2fr}}
```
