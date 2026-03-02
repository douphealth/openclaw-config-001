# Blog Monitor Skill (Skill 1)

## Skill Profile

**Name:** Blog Monitor (RSS Ingestion & Content Ingestion)
**Category:** Content Acquisition & Validation
**Version:** 1.0.0
**Status:** Production Ready
**Dependencies:** feedparser, requests, beautifulsoup4

## Purpose

Continuously monitors blog RSS feeds and ingests new content with automated validation, metadata extraction, and semantic quality assessment. Acts as the content acquisition layer for the entire social media automation pipeline.

## Core Capabilities

1. **Multi-Feed RSS Monitoring**
   - Parallel feed ingestion from multiple sources
   - Configurable polling intervals (1-60 minutes)
   - Feed health monitoring and error handling
   - Automatic retry logic for failed feeds

2. **Content Ingestion & Validation**
   - Article parsing and metadata extraction
   - Title, author, publication date extraction
   - Content duplication detection
   - Semantic quality scoring (0-100)
   - Word count validation (min: 500, max: 5000)
   - Reading time estimation (ML-powered)

3. **Metadata Enrichment**
   - SEO metadata extraction (meta description, keywords)
   - Open Graph tag parsing
   - Author and publication source tracking
   - Content category auto-detection
   - Sentiment analysis (positive/neutral/negative)

## Data Models

### Input: Feed Configuration
```json
{
  "feed_id": "blog-monitor-1",
  "feeds": [
    {
      "url": "https://example.com/feed.xml",
      "source_name": "Example Blog",
      "category": "technology",
      "polling_interval_minutes": 30,
      "enabled": true,
      "auth_type": "none|basic|bearer",
      "auth_token": "optional_token"
    }
  ],
  "validation_rules": {
    "min_word_count": 500,
    "max_word_count": 5000,
    "min_quality_score": 60,
    "reject_duplicate_threshold": 0.95,
    "required_metadata": ["title", "author", "published_date"]
  },
  "enrichment_config": {
    "enable_sentiment_analysis": true,
    "enable_category_detection": true,
    "enable_reading_time": true
  }
}
```

### Output: Validated Content Object
```json
{
  "content_id": "uuid",
  "feed_source": "Example Blog",
  "title": "Article Title",
  "url": "https://example.com/article",
  "author": "Author Name",
  "published_date": "2025-03-15T10:30:00Z",
  "ingested_date": "2025-03-15T11:00:00Z",
  "content": "Full article text...",
  "summary": "Auto-generated 2-3 sentence summary",
  "word_count": 1250,
  "reading_time_minutes": 5,
  "quality_score": 87,
  "metadata": {
    "seo_description": "Page meta description",
    "keywords": ["keyword1", "keyword2"],
    "og_image": "https://example.com/image.jpg",
    "content_type": "blog_post|case_study|tutorial|opinion",
    "sentiment": "positive",
    "category": "technology",
    "has_video": false,
    "has_images": true,
    "image_count": 3
  },
  "validation_status": "passed|failed",
  "validation_reasons": [],
  "payload_format_version": "1.0"
}
```

## Processing Logic

### Step 1: Feed Discovery & Validation
```
for each configured feed:
  1. Validate feed URL accessibility
  2. Parse feed with exponential backoff (max 3 retries)
  3. Extract all new articles since last poll
  4. Check for duplicates against last 30 days of content
  5. Filter by publication date (within 7 days by default)
```

### Step 2: Content Extraction
```
for each article in feed:
  1. Parse HTML/XML content
  2. Extract title, author, publication date
  3. Remove HTML tags and normalize whitespace
  4. Extract full article text (handle paywalls gracefully)
  5. Generate 2-3 sentence summary using extractive summarization
```

### Step 3: Quality Validation
```
Validation checks (all must pass):
  ✓ Title exists and length between 20-200 characters
  ✓ Content word count between 500-5000 words
  ✓ Publication date is valid and within 7 days
  ✓ Author information is present
  ✓ Quality score >= 60 (calculated from multiple factors)
  ✓ Uniqueness score >= 0.05 (5% minimum unique content)
  ✓ No adult/NSFW content detected
  ✓ No spam/promotional patterns detected

Quality Score Calculation:
  = (title_quality * 0.15) + 
    (content_depth * 0.25) + 
    (readability_score * 0.20) + 
    (authority_score * 0.20) + 
    (freshness_score * 0.20)

Where:
  - title_quality: 0-100 based on length, keyword usage
  - content_depth: 0-100 based on word count, structure
  - readability_score: 0-100 Flesch-Kincaid grade level
  - authority_score: 0-100 based on domain authority
  - freshness_score: 0-100 based on publication recency
```

### Step 4: Metadata Enrichment
```
1. Extract SEO metadata (meta tags, OG tags)
2. Perform keyword extraction (TF-IDF, top 10)
3. Sentiment analysis on title + summary
4. Content category detection (ML-based)
5. Calculate reading time (average 200 words/minute)
6. Image/video detection and extraction
7. Extract source authority metrics
```

## API Specification

### Invocation
```bash
GET /skill/blog-monitor/run
POST /skill/blog-monitor/run

Payload:
{
  "mode": "full_sync|incremental|validation_only",
  "feed_ids": ["blog-monitor-1"],
  "force_refresh": false,
  "timeout_seconds": 300
}
```

### Response Format
```json
{
  "skill_id": "blog-monitor-1",
  "execution_id": "uuid",
  "status": "success|partial_failure|failure",
  "total_feeds_checked": 5,
  "feeds_successful": 5,
  "feeds_failed": 0,
  "articles_found": 12,
  "articles_validated": 10,
  "articles_rejected": 2,
  "processing_time_seconds": 23.5,
  "output": [
    { /* validated content object */ }
  ],
  "errors": [
    {
      "feed_url": "https://failed-feed.com/rss",
      "error_type": "ConnectionError|ParseError|ValidationError",
      "error_message": "Error details"
    }
  ],
  "payload_format_version": "1.0"
}
```

## Enterprise Requirements

- **Scalability:** Handle 100+ feeds with <30 second total execution time
- **Reliability:** 99.9% uptime with automatic failover
- **Performance:** Cache validated content for 24 hours
- **Security:** TLS 1.3 for all feed fetches, token encryption at rest
- **Monitoring:** Track feed health, success rates, latency metrics
- **Logging:** Comprehensive audit logs for all validation failures

## Configuration Example

```yaml
skill:
  id: blog-monitor-1
  name: Blog Monitor
  feeds:
    - url: https://techcrunch.com/feed/
      source_name: TechCrunch
      category: technology
      polling_interval_minutes: 60
    - url: https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml
      source_name: NY Times
      category: general
      polling_interval_minutes: 120
  validation:
    min_quality_score: 70
    min_word_count: 800
    reject_duplicates: true
```

## Integration Points

- **Outputs to:** Keyword-Entity-Extractor (Skill 2)
- **Requires:** Feed source configuration, validation rules
- **Triggers:** On schedule (every 30-60 minutes) or on-demand
- **Error Handling:** Failed feeds logged; processing continues with successful feeds
