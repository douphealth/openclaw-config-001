# Publer Publisher Skill (Skill 5)

**Name:** Publer Publisher | **Category:** Content Publishing & Scheduling | **Version:** 1.0.0

## Purpose
Schedules and publishes social media posts across all platforms using Publer API. Handles posting, scheduling, analytics collection, and performance tracking. Acts as the distribution and monitoring layer.

## Core Capabilities
1. Multi-platform publishing (Twitter, LinkedIn, Facebook, Instagram)
2. Optimal posting time scheduling
3. Campaign/batch management
4. Performance analytics tracking
5. Engagement monitoring
6. Retry logic for failed posts
7. Post analytics collection

## Processing Steps
1. Validate post content and assets
2. Schedule posts at optimal times per platform
3. Execute publish via Publer API
4. Track delivery status
5. Monitor engagement metrics in real-time
6. Collect post performance data
7. Generate analytics reports

## Data Models
- Input: Social posts + images from Skills 3-4
- Output: Published post IDs, scheduling confirmations, engagement metrics
- Batch: 4-15 posts per article (4 platforms × 3-5 variations)

## API
**POST /skill/publer-publisher/run**
```json
{"posts": [...], "images": [...], "schedule_immediately": false, "optimal_times": true}
```

## Enterprise Requirements
- Reliability: 99.9%+ delivery rate
- Latency: <5 seconds per post publish
- Analytics: Real-time engagement tracking
- Scheduling: Timezone-aware optimal posting
- Monitoring: 24/7 performance tracking

## Integration
- **Inputs from:** Canva Image Creator (Skill 4)
- **Analytics Output:** Dashboard, reports
- **API:** Publer API v2.0+, social platform APIs
