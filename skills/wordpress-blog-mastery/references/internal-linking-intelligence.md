# Internal Linking Intelligence

## Internal Link Map (mandatory pre-write)
Use this structure for each post:

```yaml
internal_link_map:
  this_post:
    url: ""
    primary_keyword: ""
    cluster: ""
    hub_page: ""
    intent_type: "informational|commercial|transactional"

  links_OUT_from_this_post:
    to_hub:
      target_url: ""
      anchor_text: ""
      placement: "intro or first relevant section"
      rationale: "Reinforces cluster relationship"

    to_siblings:
      - target_url: ""
        anchor_text: ""
        placement: ""
        rationale: ""

    to_adjacent_clusters:
      - target_url: ""
        anchor_text: ""
        placement: ""
        rationale: ""

    to_money_pages:
      - target_url: ""
        anchor_text: ""
        placement: ""
        rationale: "Only when genuinely relevant"

  links_IN_to_this_post:
    - source_url: ""
      anchor_text: ""
      insertion_point: ""
      rationale: ""
```

## Link Quantity Guidelines
| Post length | Internal links OUT | Internal links IN (to add) |
|---|---:|---:|
| < 1,500 words | 4–6 | 2–3 |
| 1,500–3,000 words | 6–10 | 3–5 |
| 3,000–5,000 words | 10–15 | 5–8 |
| 5,000+ words | 15–20 | 8–12 |

### Hard limits
- Never exceed **1 internal link per 150 words**.
- Never publish with fewer than **3 internal links**.
- Never link to the same target URL more than **2 times**.
- Never place more than **3 links in one paragraph**.

## Semantic Anchor Text Engineering

### Anchor spectrum
- **Exact match**: high risk when overused
- **Descriptive partial/semantic variant**: ideal default
- **Generic anchors** ("click here", "read more", "here"): disallowed

### Anchor patterns by link type
| Link type | Pattern | Example |
|---|---|---|
| Hub/pillar page | Topical authority phrase | "our complete guide to WordPress performance" |
| Sibling cluster page | Related subtopic phrase | "how server-side caching works" |
| Definition/explainer | Concept phrase | "understanding Core Web Vitals" |
| How-to/tutorial | Action phrase | "step-by-step plugin installation guide" |
| Comparison/review | Evaluation phrase | "our hands-on comparison of hosting providers" |
| Money page (affiliate) | Solution-oriented phrase | "top-rated managed WordPress hosts" |
| Tool/resource | Tool-specific phrase | "our WordPress site speed checker" |

### Anchor text generation process
For each planned internal link:
1. Identify target page’s primary keyword/topic.
2. Inspect sentence context where link will be placed.
3. Generate 3 candidates:
   - Variant A: keyword-adjacent
   - Variant B: semantic synonym
   - Variant C: intent-descriptive
4. Select candidate that is most natural, destination-accurate, and not already overused.

### Anchor rules (strict)
1. Make anchors descriptive and contextual.
2. Never use naked URLs as anchor text.
3. Never use generic anchors.
4. Vary anchors pointing to same URL across the site.
5. Use semantic variants naturally.
6. Keep keyword relevance without exact-match spam.
7. Match destination expectation (how-to anchor -> how-to page).
8. Front-load meaning in 3–8 words.

### Anchor anti-patterns (auto-fail)
| Anti-pattern | Why it fails | Fix |
|---|---|---|
| Exact-match anchor on every link to same page | Over-optimization signal | Use 3+ variants |
| "Click here" / "Read more" / "Learn more" | No semantic value | Replace with descriptive phrase |
| Entire sentence as anchor | Diluted relevance | Use 3–8 word anchor |
| Anchor text mismatch | Confuses users + crawlers | Align anchor to destination intent |
| Image-only linking without nearby text link | Weak accessibility/semantic signal | Add text link in proximity |
| Same anchor text for different pages | Relevance ambiguity | Use unique target-specific anchors |
| Keyword-stuffed anchors | Unnatural/spam signal | One concept per anchor |

## Link Placement Intelligence

### Scroll-depth link value model
| Scroll depth | Link value | Why |
|---|---|---|
| 0–15% | ★★★★★ | Highest crawl priority and reader attention |
| 15–40% | ★★★★ | Core comprehension zone; strongest contextual relevance |
| 40–70% | ★★★ | Mid-content depth and expansion |
| 70–90% | ★★ | Decision/transition stage |
| 90–100% | ★★★ | Related-reading retention before exit |

### Placement rules
| Placement zone | Link type | Rationale |
|---|---|---|
| Introduction (first ~200 words) | 1 hub/pillar link | Establish cluster relationship early |
| After first major insight | 1–2 supporting links | Natural “go deeper” moment |
| Within each H2 section | 0–2 contextual links | Add only when intent truly overlaps |
| Comparison/decision sections | Review/comparison links | Support high-intent evaluation flow |
| FAQ answers | 1 link per 2–3 answers | Concise answer + depth path |
| Before conclusion | 1–2 next-step links | Forward journey routing |
| Related Reading block | 3–5 curated links | Final retention opportunity |

### Contextual integration patterns
1. **Natural extension**: when concept needs deeper treatment.
2. **Supporting evidence**: link to benchmark/methodology proof page for claims.
3. **Decision branch**: when user must choose option path A/B.
4. **Definition bridge**: when term may need quick explainer depth.
5. **Comparison reference**: when options are mentioned but full comparison exists.
6. **Related reading block**: section-end curated links for retention.

Example related-reading block:
```html
<div class="related-reading">
  <p><strong>Related:</strong>
    <a href="/wordpress-caching-guide/">Complete WordPress Caching Guide</a> ·
    <a href="/cdn-setup-tutorial/">How to Set Up a CDN</a> ·
    <a href="/image-optimization/">Image Optimization Best Practices</a>
  </p>
</div>
```

## Cluster-Aware Link Routing
### Priority matrix
| Priority | Link to | When | Why |
|---|---|---|---|
| 1 | Hub/pillar page of same cluster | Always (>=1x/post) | Reinforces topical authority structure |
| 2 | Sibling page extending current point | Section overlap exists | Highest contextual reader utility |
| 3 | Money page with genuine relevance | Natural commercial intent appears | Organic conversion path |
| 4 | High-performing page needing support | Topic aligned | Strategic authority distribution |
| 5 | New page needing discovery | Topic aligned | Prevent orphaning |
| 6 | Adjacent cluster hub | Clear topic bridge | Cross-cluster authority transfer |

### Anti-cannibalization linking
- Stronger page receives more inbound links with intent-relevant anchors.
- Weaker/overlapping page should link to stronger page as the canonical depth route.
- Do not interlink competing pages with identical anchors.

### Orphan prevention protocol
After publishing any new post:
1. Add contextual inbound links from 3–5 existing related posts.
2. Use varied descriptive anchors (no repeated exact-match spam).
3. Verify links render and resolve correctly on source pages.

## Internal Link Quality Checklist (per post)
- [ ] Hub link present in high-value zone (intro/early body)
- [ ] Link count within size guideline and hard limits
- [ ] No generic anchors; no naked URLs
- [ ] Anchor-to-destination expectation matches
- [ ] No duplicate anchor text mapped to different URLs
- [ ] At least one next-step/action-path link near conclusion
- [ ] Related-reading block present where useful
- [ ] 3–5 planned inbound links queued from existing posts

## Anti-over-optimization checks
- No forced exact-match anchor repetition.
- No irrelevant links inserted to meet volume targets.
- No multiple links to similar intent pages in the same sentence.
