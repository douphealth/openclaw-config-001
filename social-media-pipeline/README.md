# Enterprise-Grade Social Media Automation Pipeline

**Version:** 1.0-production-ready  
**Status:** 🚀 Ready to Deploy  
**Last Updated:** March 2, 2026

## 🎯 Overview

A fully autonomous social media publishing system powered by OpenClaw that transforms your blog content into viral, platform-optimized posts across Facebook, Instagram, Pinterest, and Google My Business.

**Full Pipeline Flow:**
```
Blog RSS Feed
    ↓
Blog Monitor (Skill 1) - RSS Ingestion
    ↓
Keyword Extraction (Skill 2) - NLP + Web Validation  
    ↓
Content Generation (Skill 3) - Platform-Specific Viral Copy
    ↓
Image Creation (Skill 4) - Canva API Auto-Design
    ↓
Publishing (Skill 5) - Publer Multi-Platform Scheduling
    ↓
Optimal Posting (Scheduler) - 4-Platform Coordination
    ↓
🎊 PUBLISHED - Fully Autonomous
```

## 📋 Prerequisites

### API Credentials Required
1. **OpenAI Codex 5.3** - LLM reasoning engine
   - ChatGPT OAuth token via device login
   - Context window: 128,000 tokens
   - Reasoning enabled

2. **Publer API Key**
   - Multi-platform social publishing
   - Supports: Facebook, Instagram, Pinterest, Google My Business
   - Optimal scheduling engine

3. **Canva OAuth Credentials**
   - Client ID
   - Client Secret
   - Scopes: designcontentread, designcontentwrite, assetread, assetwrite

### Configuration Files
- Blog RSS URLs (comma-separated)
- Brand name
- Brand website

## 🏗️ System Architecture

### 5 Core Skills

#### Skill 1: Blog Monitor (RSS Ingestion)
- **Trigger:** Every 4 hours (configurable)
- **Function:** Monitor RSS feeds, detect new blog posts
- **Output:** Filtered list of new, unprocessed posts

#### Skill 2: Keyword-Entity Extraction Engine
- **Input:** Blog post (title, content, URL)
- **Process:**
  - Extract named entities (people, brands, products)
  - Extract conceptual entities (trends, methodologies)
  - Score by demand, competition, viral potential
  - Validate with live web search
- **Output:** Single winning keyword + 5 runners-up

#### Skill 3: Social Content Generator
- **Input:** Keyword data + blog post
- **Platforms:**
  - Facebook - 150-300 word engaging post
  - Instagram - 7-slide carousel + caption
  - Pinterest - SEO-optimized tall pin
  - Google My Business - Local business post
- **Output:** Platform-specific viral content

#### Skill 4: Canva Image Creator
- **Input:** Content bundles + image prompts
- **Actions:**
  - OAuth2 authentication
  - Design creation per platform
  - Dimension optimization (1200x630, 1080x1080, 1000x1500, 1200x900)
  - Text overlay + branding
- **Output:** Optimized images ready to publish

#### Skill 5: Publer Publisher
- **Input:** Content + images + scheduling data
- **Actions:**
  - Upload media to Publer
  - Schedule posts across platforms
  - Set first comments + CTAs
  - Platform-specific formatting
- **Output:** Scheduled posts across all 4 platforms

## 🚀 Quick Start

### Step 1: Environment Setup
```bash
# Set environment secrets
openclaw secret set PUBLERAPIKEY your-key-here
openclaw secret set CANVACLIENTID your-id-here
openclaw secret set CANVACLIENTSECRET your-secret-here
openclaw secret set BLOGRSSURLS https://blog1.com/feed,https://blog2.com/feed
openclaw secret set BRANDNAME "Your Brand"
openclaw secret set BRANDWEBSITE https://yourbrand.com

# OpenAI authentication
openclaw onboard --auth-choice openai-codex
# Visit https://auth.openai.com/device and enter the code provided
```

### Step 2: Install Skills
```bash
openclaw skill install ./social-media-pipeline/skills/blog-monitor
openclaw skill install ./social-media-pipeline/skills/keyword-entity-extractor
openclaw skill install ./social-media-pipeline/skills/social-content-generator
openclaw skill install ./social-media-pipeline/skills/canva-image-creator
openclaw skill install ./social-media-pipeline/skills/publer-publisher
```

### Step 3: Create Master Agent
```bash
openclaw agent create \
  --name social-media-empire \
  --model openaigpt-5.3-codex \
  --auth chatgpt-oauth \
  --skills blog-monitor,keyword-entity-extractor,social-content-generator,canva-image-creator,publer-publisher \
  --heartbeat every4h \
  --review-mode human-in-loop \
  --notifications telegram \
  --verbose true
```

### Step 4: Start the Pipeline
```bash
openclaw agent start social-media-empire
```

## 📊 What Happens Automatically

### Every 4 Hours (Configurable)
1. ✅ Check all blog RSS feeds
2. ✅ Detect new posts (24-hour lookback)
3. ✅ Deduplicate against processed posts
4. ✅ Extract best keyword-entity with live validation
5. ✅ Generate viral content for all 4 platforms
6. ✅ Create optimized images via Canva
7. ✅ Schedule posts at optimal times
8. ✅ Send summary notification

### Per Blog Post
- **Blog Title Extraction** - Semantic title parsing
- **Content Analysis** - Reading level, word count, content type
- **Keyword Scoring** - Demand, competition, viral potential, evergreen score
- **Web Search Validation** - Confirm high demand & low competition
- **Trending Check** - Real-time trend validation
- **Hashtag Generation** - Platform-specific, layered by reach (1M, 100K, 10K, <10K)
- **Image Generation** - Dimension-perfect per platform
- **Schedule Optimization** - Algorithm-aligned posting times

## 📁 File Structure

```
social-media-pipeline/
├── README.md                          (This file)
├── openclaw.json                      (Master configuration)
├── credentials/
│   ├── env-template.sh               (Environment variables template)
│   └── setup.sh                      (Credential setup script)
├── skills/
│   ├── blog-monitor/
│   │   └── SKILL.md                  (RSS monitoring logic)
│   ├── keyword-entity-extractor/
│   │   └── SKILL.md                  (NLP + validation)
│   ├── social-content-generator/
│   │   └── SKILL.md                  (4-platform content)
│   ├── canva-image-creator/
│   │   └── SKILL.md                  (Image generation)
│   └── publer-publisher/
│       └── SKILL.md                  (Publishing)
├── agents/
│   └── social-media-empire.yaml      (Master agent config)
└── templates/
    ├── facebook-post-template.md
    ├── instagram-carousel-template.md
    ├── pinterest-pin-template.md
    └── gmb-post-template.md
```

## 💰 Cost Structure

### Included in Your Existing Plans
- ✅ OpenAI Codex 5.3 - ChatGPT subscription (no additional cost)
- ✅ Publer API - Your Publer plan
- ✅ Canva OAuth - Canva Pro plan
- ✅ Blog RSS - Your blog infrastructure

### Total Additional Cost
**$0 - Everything runs on your existing subscriptions**

## 🎓 How It Works: Deep Dive

### Keyword Extraction Logic
The keyword engine is the brain. It:
1. Extracts 20-30 potential keywords from the blog post
2. Scores each on 5 dimensions (demand, competition, viral, relevance, evergreen)
3. Uses composite scoring: `(demand×2) + (10-competition×2) + (viral×3) + (relevance×2) + (evergreen×1)`
4. Validates top candidate with live web search
5. Confirms or promotes from runners-up
6. Generates 20-30 platform-specific hashtags per network

### Content Generation Strategy
**Facebook:** Engagement-focused, question-based CTAs, 150-300 words  
**Instagram:** Carousel slides (7 slides), save/share CTAs, emoji-heavy  
**Pinterest:** SEO-dense titles/descriptions, tall pins (1000x1500), text overlays  
**GMB:** Local intent, professional tone, 150-250 words  

### Optimal Posting Schedule
```
Facebook:  Tuesday-Thursday 9am-12pm, Sunday 12-3pm
Instagram: Monday-Thursday 11am-1pm, Friday-Sunday 10am-2pm  
Pinterest: Saturday 8-11pm, Friday 3pm, Sunday all day
GMB:       Tuesday-Thursday 8-10am
```
Posts spread across 48 hours for maximum reach.

## 🔧 Customization

### Change RSS Feed Frequency
Edit `openclaw.json`, modify `heartbeat.interval` to:
- `hourly` - Every hour
- `twicedaily` - Every 12 hours (morning/evening)
- `daily` - Once per day
- `custom` - Custom interval

### Add More Blog Feeds
```bash
openclaw secret set BLOGRSSURLS "https://blog1.com/feed,https://blog2.com/feed,https://blog3.com/feed"
```

### Modify Keyword Scoring
Edit `skills/keyword-entity-extractor/SKILL.md`, adjust weights:
```
Composite Score = (demand×2) + (10-competition×2) + (viral×3) + (relevance×2) + (evergreen×1)
```

### Change Image Dimensions
Edit `skills/canva-image-creator/SKILL.md`, modify design dimensions:
```
Facebook: 1200×630 (currently optimized)
Instagram: 1080×1080 (currently optimized)
Pinterest: 1000×1500 (currently optimized)
GMB: 1200×900 (currently optimized)
```

## 📈 Metrics to Track

### Per Pipeline Run
- Posts detected
- Keywords extracted + validated
- Content generated (4 platforms)
- Images created successfully
- Posts scheduled
- Scheduling success rate

### Per Post (from Publer Analytics)
- Engagement rate by platform
- Best performing keyword
- Image performance
- Posting time impact
- Hashtag effectiveness

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| RSS feeds not updating | Check feed URLs in BLOGRSSURLS secret |
| Keyword extraction failing | Ensure OpenAI token is valid, increase context window |
| Image creation failing | Verify Canva credentials, check API quotas |
| Posts not publishing | Verify Publer API key, check platform auth |
| Optimal schedule miscalculation | Verify timezone settings in scheduler |

## 📞 Support

For issues or customization requests:
1. Check `data/` directory for execution logs
2. Review skill output files in `reports/`
3. Enable verbose mode: `--verbose true`
4. Check Publer dashboard for publishing issues

## 🚀 Production Checklist

- [ ] All secrets configured
- [ ] OpenAI OAuth authenticated
- [ ] Blog RSS URLs verified
- [ ] Brand name and website set
- [ ] All 5 skills installed
- [ ] Master agent created
- [ ] Test run completed
- [ ] Notification channel set (Telegram)
- [ ] Heartbeat interval configured
- [ ] Review mode enabled for first runs
- [ ] Monitoring dashboard active

## 📝 Next Steps

1. Review each skill file in `skills/` directory
2. Understand the keyword extraction scoring
3. Customize content templates for your brand voice
4. Run first test with human-in-loop review mode
5. Monitor Publer dashboard for engagement metrics
6. Optimize based on performance data
7. Adjust keyword weights based on results
8. Scale to additional blogs/feeds

This system transforms your content strategy into a fully autonomous, data-driven social media machine. Happy publishing!
