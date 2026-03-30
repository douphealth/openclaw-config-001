---
name: amazon-affiliate-product-box
description: Create, improve, or verify premium Amazon affiliate product boxes for blog posts when product fit is genuinely strong. Use when selecting a tightly matched Amazon product, retrieving/normalizing affiliate links and images, minimizing SerpApi burn, enforcing the configured Amazon Associates tag from local secrets, generating paste-ready HTML for WordPress, or auditing whether a post should get a product box at all.
---

# Amazon Affiliate Product Box

Create one strong, editorial-feeling Amazon product box only when it materially helps the reader.

## Core rule
Do **not** add a box just because a page can carry one. Add it only when the article naturally points to a product that solves the exact problem discussed.

## Fast workflow
1. Score post-to-product fit before searching.
2. Choose one best product type.
3. Retrieve secrets safely.
4. Run one precise, low-burn SerpApi query.
5. Normalize the Amazon URL and enforce the affiliate tag from local secrets.
6. Build one premium HTML box.
7. Verify fit, link, image, and markup before claiming success.

## Safe secret retrieval
Keep keys out of chat, memory, and published files.

Preferred order:
1. Read `/home/openclaw/.openclaw/workspace/.secrets/amazon-affiliate-product-box.env`.
2. Read the key-pool path from `SERPAPI_KEYS_FILE` inside that env file.
3. Use environment-backed config only if the workspace intentionally maps these same values from `${ENV_VAR}`.
4. Use an inbound key file only if the task explicitly provides one.

Rules:
- Never paste a raw SerpApi key into chat, docs, ledgers, or HTML.
- Never paste the raw Amazon Associates tag into normal docs, memory, or chat.
- Never hardcode keys or the affiliate tag into the skill, scripts, templates, or notes.
- If multiple keys are supplied, treat them as a rotation pool and report only the key index used, not the key value.
- If no safe secret source is available, stop and say the skill cannot complete retrieval safely.
- See `SECURE_SETUP.md` in this skill folder for the local secret layout.

## Fit scoring before search
Score fit on a 0-3 scale. Spend SerpApi only on score **3** posts, or rare score **2** posts with a clearly implied product.

### Score 3: direct product fit
The article explicitly solves a problem where a physical product is a natural next step.
Examples:
- plant support, soil, grow light, humidity, pruning, pest-control tool
- pet feeder, crate accessory, training aid, grooming tool
- tutorial/tool-driven how-to content

### Score 2: possible but not automatic fit
A product could help, but the post may still work without one.
Use only if one product clearly improves execution and can be explained honestly.

### Score 1: weak fit
Commercial insertion would feel bolted on.
Skip.

### Score 0: no fit / trust-sensitive
About, contact, policy, abstract explainer, medical/safety-sensitive content where affiliate intent would degrade trust.
Skip.

## Product-type selection
Pick the narrowest useful product type, not a vague shopping category.

Good:
- sphagnum moss pole
- full-spectrum clip-on grow light
- slow-feeder dog bowl
- reptile digital hygrometer

Weak:
- plant accessory
- pet item
- home tool

Selection rules:
- Prefer the product most tightly tied to the article's main action.
- Prefer stable, mainstream utility over novelty.
- Prefer one box per post section, usually one box total.
- If torn between two categories, choose the one easier to justify in one sentence without sounding promotional.

## Provider-aware SerpApi usage
Use the provider/mode that gets an Amazon product page with the fewest retries.

Preferred pattern:
- Use SerpApi only after fit and product type are locked.
- Prefer an Amazon-scoped search mode when available from the current provider/account.
- If the provider/account does not support Amazon-native results, use a web/organic query that intentionally targets Amazon product pages.
- Avoid broad shopping comparison results unless the task explicitly wants cross-store comparison.

Practical guidance:
- First choice: Amazon-focused search result path from SerpApi if supported.
- Fallback: precise web query targeting Amazon, product type, and 1-2 qualifiers.
- Do not fan out across multiple engines just to browse.
- Rotate keys only on auth, quota, or provider failure — not because the first result looked imperfect.

## Low-burn query logic
Use one strong query first. Retry only if the failure mode is clear.

Query template:
- `{exact product type} {critical qualifier} amazon`
- add a second qualifier only when it removes ambiguity

Examples:
- `sphagnum moss pole monstera amazon`
- `slow feeder bowl french bulldog amazon`
- `full spectrum clip on grow light seedlings amazon`
- `snake plant potting mix indoor amazon`

Avoid:
- adjective spam (`best amazing top premium`)
- broad category fishing
- synonym loops for the same intent
- repeated retries before refining the product type

Retry ladder:
1. exact product type + one qualifier
2. exact product type + alternate qualifier
3. slightly broader but still specific category
4. stop if results remain ambiguous

## Link normalization and affiliate enforcement
Every final link must be cleaned before insertion.

Normalization rules:
1. Prefer a canonical Amazon product URL when possible.
2. Strip noisy tracking/query params that are not needed for page resolution.
3. Preserve or reconstruct the product path if the source includes extra redirect clutter.
4. Read the affiliate tag from `AMAZON_ASSOC_TAG` in local secrets and enforce it exactly once.
5. Do not keep competing affiliate tags, storefront refs, or unrelated campaign params.
6. Keep the link pointed at the intended product page, not search results, carts, or short-lived redirect endpoints.

Practical output target:
- good: `https://www.amazon.com/dp/ASIN/?tag=<AMAZON_ASSOC_TAG>`
- acceptable: clean product-path URL with `tag=<AMAZON_ASSOC_TAG>`
- bad: giant referral string, duplicate tags, `smile.` domains, short redirect junk, or non-product landing pages

If the source URL already has a `tag`, replace it with the value from `AMAZON_ASSOC_TAG`.

## Image rules
- Use the clearest product image available from the source result.
- Prefer a stable direct image URL when one is returned.
- Do not invent images or scrape questionable third-party image hosts.
- Ensure alt text is descriptive and product-specific.
- If image quality is bad but the product fit is strong, note the caveat rather than pretending it is premium.

## Placement intelligence standard
Do not place the box arbitrarily.

Always choose the most relevant insertion point based on where the article creates product desire naturally.

Preferred placement logic:
1. immediately after the section that proves why the product matters
2. immediately after a practical recommendation block where the product becomes the obvious next step
3. before a related video/embed only if the box strengthens the transition
4. never at the very top of the post unless the article is explicitly product-led
5. never buried so late that the product recommendation loses context

Best placement signals:
- the article explains why a tool, support, or material helps
- the reader has just learned the problem and the solution category
- the product box feels like a useful next action, not an interruption

Avoid placement:
- before the article earns trust
- inside a section where it breaks reading flow
- after unrelated sections just because there is empty space
- near another monetization element that creates clutter

Before insertion, identify:
- the exact section heading or paragraph after which the box belongs
- why this is the highest-intent moment in the article

## Premium HTML output standard
Generate HTML that looks polished even before theme styling and pastes cleanly into a WordPress Custom HTML block.

Required structure:
1. outer card
2. product image block
3. eyebrow or small label
4. product title
5. 1-2 sentence fit note tied to the article
6. 3 concise value bullets
7. CTA row
8. optional trust/disclosure microcopy

Required qualities:
- mobile-safe stacked layout
- neutral premium styling
- readable spacing and hierarchy
- clear CTA
- visually refined enough to feel intentional on a premium content site
- `target="_blank"` plus `rel="nofollow sponsored noopener"`
- no fake badges, fake ratings, fake scarcity, or hype sludge
- no cheap ad-box look

Copy rules:
- sound editorial, not advertorial
- name the product plainly
- explain fit in article-aware language
- keep bullets practical and specific
- keep CTA honest: `Buy on Amazon` or `Check price on Amazon`

## Acceptance gates
Do not mark complete unless all pass:

### Fit gate
- the recommendation clearly matches the post's main reader task
- the box improves usefulness, not just monetization

### Retrieval gate
- the chosen result resolves to the intended Amazon product page
- the query count stayed low and justified
- key handling stayed secret-safe

### Link gate
- final URL is normalized
- `tag=<AMAZON_ASSOC_TAG>` is present exactly once
- no conflicting affiliate/tracking junk remains

### Content gate
- title, fit note, bullets, and CTA are coherent and non-spammy
- the box makes sense even if read outside chat context

### Placement gate
- the chosen insertion point is the strongest contextual moment in the article
- the box appears directly after the section that makes the product recommendation feel natural
- the box does not interrupt comprehension or create monetization clutter

### Markup gate
- HTML is valid-looking, paste-ready, and mobile-safe
- image loads from a plausible source
- links use the proper rel attributes
- visual design is meaningfully premium, not just technically functional

If any gate fails, either fix it or decline to add the box.

## Deliverables
Return:
- fit score and brief justification
- chosen product type
- exact placement recommendation
- query used
- note on result source/provider path
- normalized Amazon URL
- image URL
- final HTML box
- any caveat worth preserving

## Final standard
A strong box should read like: “this tool naturally helps the reader do what the article just taught.”
If it feels like affiliate clutter, skip it.