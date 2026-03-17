# High-Signal Research Inputs

Structured sources and extraction methods for content strategy research.
Quality of input determines quality of output — mine these sources systematically.

## Source 1: Customer Language (Highest Value)

### Where to Find It
- **Support tickets:** Recurring questions, frustration patterns, feature requests
- **Sales call transcripts:** Objections, desired outcomes, comparison questions
- **Community forums:** Reddit, Quora, Stack Overflow, niche communities
- **Review sites:** G2, Capterra, Trustpilot, Amazon reviews (yours AND competitors)
- **Social media:** Twitter/X threads, LinkedIn comments, Facebook groups
- **Customer interviews:** Direct conversation with 5-10 customers

### What to Extract
| Signal | Example | Why It Matters |
|--------|---------|---------------|
| Repeated questions | "How do I connect HubSpot to my CMS?" | Reveals content gaps |
| Objections | "I tried tool X but it was too complicated" | Informs positioning |
| Exact phrases | "I need something that just works" | Copy language, not jargon |
| Misconceptions | "I thought SEO was dead" | Opportunity for myth-busting |
| Implementation struggles | "Setting up took 3 weeks and still doesn't work" | How-to content opportunity |
| Comparison behavior | "We tried A and B, switching to C because..." | Comparison content opportunity |

### Extraction Command (if you have a ticket database)
```sql
-- Most frequent support questions
SELECT question_text, COUNT(*) as frequency 
FROM support_tickets 
WHERE created_at > NOW() - INTERVAL '90 days'
GROUP BY question_text 
ORDER BY frequency DESC 
LIMIT 50;
```

## Source 2: Search Console / Search Data

### Where to Find It
- **Google Search Console:** Queries, pages, CTR, impressions
- **Keyword tools:** Ahrefs, SEMrush, Google Keyword Planner
- **SERP analysis:** People Also Ask, related searches, autocomplete

### What to Extract from GSC
```bash
# Top queries by impressions (high demand, may not rank well yet)
# Filter: impressions > 100, position > 10 → optimization opportunity
# Filter: high impressions, low CTR → title/meta rewrite opportunity

# Queries with high impressions but no dedicated page → content gap
```

### What to Extract from Keyword Tools
- Search volume trends (growing, stable, declining)
- Keyword difficulty scores
- SERP feature presence (featured snippets, People Also Ask, etc.)
- Related keywords and questions
- Parent topic assignments

### What to Extract from SERP
- **People Also Ask:** Direct question → content angle mapping
- **Related Searches:** Adjacent topics → cluster expansion
- **Top 3 page analysis:** Content format, depth, angle, what's missing
- **Featured snippet format:** Paragraph, list, table, or video → format your content to win it

## Source 3: Competitor Content Gaps

### Where to Find It
- **Competitor blogs:** What topics do they cover that you don't?
- **Competitor top pages:** Which of their pages get the most traffic?
- **Competitor social:** What content gets the most engagement?
- **Backlink analysis:** Which of their pages earn the most links?

### What to Extract
- Topics they rank for that you don't (content gap)
- Topics where their content is thin/outdated (opportunity to outperform)
- Content formats they use (and which you should adopt or improve upon)
- Their unique angles or data (and what you can do differently)
- Internal-linking patterns (how they build topical authority)

### Extraction Method
```bash
# Quick competitor top pages scan
curl -s "https://www.google.com/search?q=site:competitor.com&num=20" | extract titles
# Or use Screaming Frog crawl of competitor blog section
# Or Ahrefs/SEMrush "Top Pages" report
```

## Source 4: Existing Content Audit

### Where to Find It
- **WordPress post list:** All published content
- **Search Console:** Performance data per page
- **Analytics:** Traffic, engagement, conversion data

### What to Extract
```bash
# All published posts
wp post list --post_type=post --post_status=publish --fields=ID,post_title,post_date --format=csv

# Thin content (< 500 words)
wp post list --post_type=post --post_status=publish --fields=ID,post_title --format=csv

# Recently published (last 90 days) — still gaining traction
wp post list --post_type=post --post_status=publish --after="2025-12-17" --fields=ID,post_title

# Older content (>6 months) — may need refresh
wp post list --post_type=post --post_status=publish --before="2025-09-17" --fields=ID,post_title
```

### What to Flag
- Pages with high impressions but low clicks (CTR optimization opportunity)
- Pages with declining traffic (content decay → needs refresh)
- Pages targeting the same keyword (cannibalization risk)
- Pages with no internal links pointing to them (orphan content)
- Pages ranking positions 4-10 (close to page 1 → quick-win opportunity)

## Source 5: Forum & Community Questions

### Where to Find It
- **Reddit:** Subreddits related to your niche
- **Quora:** Questions with high follower counts
- **Stack Overflow / Stack Exchange:** Technical questions
- **Facebook Groups:** Community discussions
- **Slack/Discord Communities:** Real-time conversations
- **Product-specific communities:** (e.g., WordPress forums, Shopify community)

### What to Extract
- Questions asked 5+ times (high-demand topic)
- Questions with no good answers (content gap)
- Questions with wrong/outdated answers (update opportunity)
- Phrasing patterns (how people describe their problem)
- Emerging topics (new questions that signal trend shifts)

## Source 6: Internal Subject-Matter Expertise

### Where to Find It
- **Engineering/product teams:** Technical depth, architecture decisions
- **Sales team:** Common objections, competitive intelligence
- **Customer success:** Retention drivers, expansion patterns
- **Leadership:** Market trends, strategic vision
- **Case studies:** Real customer results and implementations

### What to Extract
- Technical details that competitors don't cover
- Real customer results (with permission) for case studies
- Market insights for thought leadership content
- Process knowledge for how-to content
- Competitive differentiators for comparison content

## Research Workflow

### Step 1: Collect (1-2 hours)
Pull data from all 6 sources. Don't analyze yet — just collect.

### Step 2: Deduplicate (30 minutes)
Merge overlapping topics. Use the customer's language as the canonical phrasing.

### Step 3: Map to Intent (30 minutes)
Label each topic with intent: informational, commercial, transactional.

### Step 4: Score with Priority Model (30 minutes)
Use the priority scoring model to rank all topics.

### Step 5: Cluster (1 hour)
Group topics by shared SERP overlap and topic relationship.

### Step 6: Gap Analysis (30 minutes)
Compare clusters against existing site coverage. Flag create/update/consolidate/prune.

## Quality Bar for Research

- Minimum 50 raw topic candidates before clustering
- At least 3 research sources consulted
- Customer language used for topic phrasing (not internal jargon)
- Competitor top 3 pages analyzed for each major cluster
- Existing content audit completed before recommending new pages
- Cannibalization check completed for every proposed new page
