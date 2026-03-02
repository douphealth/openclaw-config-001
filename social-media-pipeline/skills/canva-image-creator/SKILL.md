# Canva Image Creator Skill (Skill 4)

**Name:** Canva Image Creator | **Category:** Visual Content Generation | **Version:** 1.0.0

## Purpose
Generates platform-optimized social media images and graphics using Canva API templates, text overlays, and brand guidelines. Creates visually compelling content that pairs with generated social media copy.

## Core Capabilities
1. Template selection (Twitter, LinkedIn, Facebook, Instagram-specific)
2. Dynamic text overlay (headline, subtitle, CTA)
3. Brand color/font application
4. Image/visual asset selection from library
5. Format optimization (16:9, 1:1, 9:16, etc.)
6. Watermark/attribution handling

## Processing Steps
1. Select Canva template matching platform and content theme
2. Extract key headline from social post
3. Apply brand colors, fonts, and guidelines
4. Select/generate background image
5. Add text overlays (headline, CTA, hashtags)
6. Export optimized formats

## API
**POST /skill/canva-image-creator/run**
```json
{"social_posts": [...], "brand_guidelines": {...}, "template_preference": "modern|minimal|bold"}
```

## Enterprise Requirements
- Latency: <30 seconds per image
- Quality: Professional-grade visuals
- Brand consistency: 99%+
- File size optimization <2MB

## Integration
- **Inputs from:** Social Content Generator (Skill 3)
- **Outputs to:** Publer Publisher (Skill 5)
- **API:** Canva API v1.0+
