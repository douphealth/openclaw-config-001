# Social Content Generator Skill (Skill 3)

**Name:** Social Content Generator | **Category:** Content Generation & Optimization | **Version:** 1.0.0

## Purpose
Transforms enriched blog content into platform-optimized social media posts with viral potential using LLM-powered generation (Claude/GPT-4) creating 3-5 distinct variations per platform while maintaining brand consistency.

## Core Capabilities
1. Multi-Platform Content Generation (Twitter, LinkedIn, Facebook, Instagram)
2. Viral Copy Optimization (hooks, power words, emotional triggers, CTAs)
3. Content Variation Generation (3-5 unique versions per platform)
4. Hashtag generation and optimization
5. Engagement score calculation (0-100)
6. Optimal posting time prediction

## Processing Steps
1. Extract key information from enriched content
2. Platform-specific generation with constraints (Twitter: 280 chars, LinkedIn: 3000 chars, etc.)
3. Apply viral copy techniques (hook in first 5 words, power words, emotional triggers)
4. Add platform-specific hashtags (Twitter: 2-4, LinkedIn: 3-5, Instagram: 15-30)
5. Score engagement potential
6. Estimate reach and engagement rate

## API
**POST /skill/social-content-generator/run**
```json
{
  "content": {...},
  "platforms": ["twitter", "linkedin", "facebook", "instagram"],
  "variations_per_platform": 3,
  "tone_preferences": ["educational", "entertaining"],
  "model_preference": "claude-3-opus"
}
```

## Output Per Post
- content, version, character_count, hashtags, engagement_score
- tone, includes_cta, keywords_used, has_question
- viral_potential_score, optimal_posting_time, estimated_reach

## Enterprise Requirements
- Scalability: 50+ posts/minute
- Quality: 85%+ quality score, <10% manual review
- Latency: <15 seconds per article
- Brand voice consistency across 4 platforms

## Integration
- **Inputs from:** Keyword-Entity Extractor (Skill 2)
- **Outputs to:** Canva Image Creator (Skill 4) & Publer Publisher (Skill 5)
- **Dependencies:** Claude API / OpenAI API
