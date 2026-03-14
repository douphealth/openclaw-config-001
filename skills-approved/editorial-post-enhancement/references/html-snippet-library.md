# HTML Snippet Library

Use these as adaptable patterns for WordPress editorial upgrades. Adjust colors/content to fit the article and site style.

## 1. Hero / intro box
```html
<div style="background:linear-gradient(135deg,#0f172a 0%,#1e3a8a 100%);border-radius:24px;padding:28px 24px;color:#fff;margin:0 0 28px 0;box-shadow:0 18px 50px rgba(15,23,42,.18);">
  <div style="font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;opacity:.9;margin-bottom:10px;">Topic label</div>
  <h2 style="font-size:34px;line-height:1.15;margin:0 0 12px 0;color:#fff;">Strong supporting headline</h2>
  <p style="font-size:18px;line-height:1.7;margin:0;max-width:900px;">Short high-value intro that clarifies the article promise.</p>
</div>
```

## 2. Quick answer box
```html
<div style="border:1px solid #dbeafe;background:#f8fbff;border-radius:18px;padding:22px;margin:0 0 28px 0;">
  <h3 style="margin:0 0 12px 0;font-size:22px;color:#0f172a;">Quick answer</h3>
  <p style="margin:0;line-height:1.8;">Direct concise answer first.</p>
</div>
```

## 3. Feature / insight cards
```html
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin:28px 0;">
  <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:18px;padding:18px;">
    <h3 style="margin:0 0 8px 0;font-size:18px;">Card title</h3>
    <p style="margin:0;line-height:1.8;">Useful supporting explanation.</p>
  </div>
</div>
```

## 4. Comparison table shell
```html
<table style="width:100%;border-collapse:collapse;margin:22px 0;border:1px solid #e2e8f0;border-radius:16px;overflow:hidden;box-shadow:0 8px 20px rgba(15,23,42,.06);">
  <thead>
    <tr style="background:#0f172a;color:#fff;">
      <th style="padding:14px;text-align:left;">Column 1</th>
      <th style="padding:14px;text-align:left;">Column 2</th>
      <th style="padding:14px;text-align:left;">Column 3</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff;">
      <td style="padding:14px;border-top:1px solid #e2e8f0;">Value</td>
      <td style="padding:14px;border-top:1px solid #e2e8f0;">Value</td>
      <td style="padding:14px;border-top:1px solid #e2e8f0;">Value</td>
    </tr>
  </tbody>
</table>
```

## 5. Callout / warning block
```html
<div style="background:#fff7ed;border-left:6px solid #f97316;border-radius:16px;padding:20px 20px 20px 18px;margin:28px 0;">
  <h3 style="margin:0 0 10px 0;font-size:20px;">Important note</h3>
  <p style="margin:0;line-height:1.8;">Use for mistakes, warnings, or critical advice.</p>
</div>
```

## 6. FAQ card item
```html
<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:18px;padding:18px 18px 16px 18px;margin:0 0 14px 0;box-shadow:0 8px 18px rgba(15,23,42,.05);">
  <h3 style="margin:0 0 8px 0;font-size:19px;color:#0f172a;">Question goes here?</h3>
  <p style="margin:0;line-height:1.8;color:#334155;">Direct answer first, then supporting detail.</p>
</div>
```

## 7. Figure with caption
```html
<figure style="margin:28px 0;">
  <img src="IMAGE_URL" alt="Descriptive alt text" style="width:100%;height:auto;border-radius:20px;display:block;box-shadow:0 14px 36px rgba(2,6,23,.10);" />
  <figcaption style="font-size:13px;color:#64748b;margin-top:8px;">Useful caption.</figcaption>
</figure>
```

## 8. Video embed wrapper
```html
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:20px;box-shadow:0 14px 36px rgba(2,6,23,.14);margin:18px 0 28px 0;">
  <iframe src="https://www.youtube.com/embed/VIDEO_ID" title="Video title" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" allowfullscreen></iframe>
</div>
```

## Rules
- Adapt snippets to the article; do not paste every block blindly.
- Keep spacing and border radius visually consistent.
- Use snippets to improve reading flow, not to bloat the page.
