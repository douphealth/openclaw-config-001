# Internal Link Anchor Text Guide

Contextual, varied anchor text formulas for building topical authority through internal linking.

## Anchor Text Categories

### 1. Exact-Match (use sparingly — 10-20% of links)
Anchor = target keyword exactly.
- `[email marketing automation]` → /blog/email-marketing-automation/
- `[on-page SEO checklist]` → /blog/on-page-seo-checklist/

**Risk:** Overuse looks manipulative. Limit to 1 per article.

### 2. Partial-Match (preferred — 40-50% of links)
Anchor contains keyword + additional context.
- `[our guide to email marketing automation for SaaS]` → /blog/email-marketing-automation/
- `[this on-page SEO checklist covers 27 ranking factors]` → /blog/on-page-seo-checklist/
- `[learn how to set up email automation from scratch]` → /blog/email-marketing-automation/

**Best for:** Primary topic links where you want relevance without over-optimizing.

### 3. Branded + Topic (15-20% of links)
Anchor = brand/entity name + topic context.
- `[HubSpot's lead scoring tutorial]` → /blog/hubspot-lead-scoring/
- `[our A/B testing framework]` → /blog/ab-testing-guide/
- `[the Revenue Operations playbook we use]` → /blog/revops-playbook/

**Best for:** Case studies, tool guides, methodology posts.

### 4. Natural/Descriptive (20-30% of links)
Anchor describes what the destination helps with.
- `[if you're struggling with low open rates, this guide breaks down the fix]` → /blog/email-open-rates/
- `[we covered the exact setup process in our WordPress SEO tutorial]` → /blog/wordpress-seo/
- `[here's the complete CRO audit checklist we use internally]` → /blog/cro-audit-checklist/

**Best for:** Supporting content, deeper dives, methodology explanations.

### 5. Generic (avoid — <5% of links)
- "click here", "read more", "this article", "learn more"

**Only acceptable when:** The surrounding sentence provides enough context for the link to be meaningful on its own.

## Anchor Text Formula Templates

### Linking to a Guide/How-To
```
- "see our [step-by-step guide to {topic}]({url})"
- "we break down the entire {process} in [{guide name}]({url})"
- "the [{specific methodology}]({url}) we use works like this..."
- "if you haven't set up {system} yet, [start with this walkthrough]({url})"
```

### Linking to a Tool/Resource
```
- "we use [{tool name}]({url}) for {specific purpose}"
- "[{tool} comparison]({url}) covers pricing, features, and {specific detail}"
- "our [{tool} setup guide]({url}) walks through {specific steps}"
```

### Linking to a Case Study/Example
```
- "as we showed in [the {industry} case study]({url}), {key result}"
- "[{specific example}]({url}) demonstrates exactly what {process} looks like"
- "we documented the full {process} in [{case study name}]({url})"
```

### Linking to Related Content
```
- "[{topic}]({url}) is closely related to {current topic} — here's why"
- "the opposite approach, [{alternative strategy}]({url}), works better when {condition}"
- "if you're dealing with {related problem}, [{article name}]({url}) covers {aspect}"
```

### Linking Forward (Next Step)
```
- "once you've {current step}, the next move is [{next step article}]({url})"
- "to take this further, [{advanced guide}]({url}) covers {next-level topic}"
- "[{monetization article}]({url}) shows how to turn {current topic} into revenue"
```

## Link Distribution Rules

### Per Article (1,500-2,500 words)
- **Minimum:** 2-3 contextual internal links
- **Maximum:** 5-7 (more feels forced)
- **Sweet spot:** 4-5 varied links

### Placement Distribution
| Section | Links | Anchor Type |
|---------|-------|-------------|
| Intro (first 200 words) | 0-1 | Natural/descriptive or partial-match |
| Early body (200-800 words) | 1-2 | Partial-match or natural |
| Mid body (800-1,500 words) | 1-2 | Partial-match or branded |
| Late body (1,500+) | 1-2 | Natural/descriptive or next-step |

### Spacing Rules
- Never two links in the same sentence
- Never two linked sentences back-to-back
- Keep at least 200 unlinked words between internal links
- Links should appear in the natural flow of reading, not be forced in

## Distribution Anti-Patterns

### ❌ Link Dumping
```
"Check out our [SEO guide](/seo), [content marketing post](/content), 
[internal linking article](/links), and [schema markup tutorial](/schema)."
```
**Fix:** Spread these across separate paragraphs where each is contextually relevant.

### ❌ Back-to-Back Links
```
"Read our [email automation guide](/email) for setup details. 
The [welcome sequence template](/welcome) will help you get started. 
[Segmentation strategies](/segmentation) are covered next."
```
**Fix:** Add unlinked explanatory text between each link.

### ❌ Generic Anchors
```
"Learn more about this topic [here](/topic)."
"Read [this article](/article) for details."
```
**Fix:** Replace "here" and "this article" with descriptive anchors.

### ❌ Exact-Match Overuse
```
"[SEO audit](/audit) is important. Our [SEO audit checklist](/checklist) 
covers [SEO audit](/audit) steps. The [SEO audit](/audit) process..."
```
**Fix:** Vary anchors: "our audit checklist", "the 27-step process we follow", "as we covered in the technical review"

## Self-Critique Checklist (Post-Enhancement)

After adding internal links, verify:

1. **Variety check:** Do anchors use at least 3 of the 5 categories above?
2. **Distribution check:** Are links spread evenly across the article?
3. **Readability check:** Read the article with links highlighted — does the flow feel natural?
4. **Relevance check:** Does each link add value to the reader's journey at that specific point?
5. **Anchor text length:** Are most anchors 4-10 words? (1-2 word anchors are too short, 15+ are too long)
6. **No duplicates:** Do any two links have the exact same anchor text pointing to the same URL?
7. **Target quality:** Do all target pages return HTTP 200 and have substantive content?
8. **Keyword balance:** Is the primary keyword NOT used as anchor text more than once?

## Quick Anchor Text Generator

When in doubt, use this pattern:

```
[verb or action] + [specific topic/benefit] + [format indicator]

Examples:
- "see how we [doubled email open rates] with [this 5-step framework]"
- "learn the [exact CRO audit process] we use [for e-commerce sites]"
- "our [WordPress speed optimization guide] covers [the 3 fixes that matter most]"
```

## Measuring Impact

After enhancing internal links, monitor over 4-8 weeks:
- Google Search Console: Click-through rate changes for linked pages
- Google Analytics: Time on page and pages per session changes
- Rank tracking: Position improvements for target keywords on linked pages
- Crawl stats: Increased discovery of previously buried pages
