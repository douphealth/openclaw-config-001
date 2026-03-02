# Keyword-Entity Extractor Skill (Skill 2)

## Skill Profile

**Name:** Keyword-Entity Extractor (NLP + Web Validation)
**Category:** Content Analysis & Entity Recognition
**Version:** 1.0.0
**Status:** Production Ready
**Dependencies:** spacy, nltk, sklearn, requests

## Purpose

Extracts key topics, entities, and high-value keywords from validated blog content using advanced NLP techniques combined with web search validation. Provides semantic enrichment for downstream content generation.

## Core Capabilities

1. **Advanced Keyword Extraction**
   - TF-IDF analysis (top 20 keywords)
   - RAKE (Rapid Automatic Keyword Extraction)
   - TextRank algorithm for keyword graphs
   - Keyword clustering and deduplication
   - Keyword ranking by relevance (0-100 score)

2. **Named Entity Recognition (NER)**
   - Person entities (names, titles)
   - Organization entities (companies, brands)
   - Location entities (cities, countries, regions)
   - Product/Technology entities
   - Event entities
   - Relationship mapping between entities

3. **Web Validation & Enrichment**
   - Cross-reference keywords with trending searches
   - Entity authority scoring (0-100)
   - Related concept discovery
   - SEO difficulty estimation
   - Social media trend alignment

## Data Models

### Input: Content Object from Blog Monitor
```json
{
  "content_id": "uuid",
  "title": "Article Title",
  "content": "Full article text...",
  "feed_source": "Example Blog",
  "category": "technology",
  "published_date": "2025-03-15T10:30:00Z"
}
```

### Output: Enriched Content with Keywords & Entities
```json
{
  "content_id": "uuid",
  "keywords": [
    {
      "term": "keyword",
      "score": 92,
      "frequency": 5,
      "type": "entity|topic|technical",
      "seo_difficulty": 35,
      "search_volume_monthly": 12500,
      "trend_score": 78,
      "validated": true
    }
  ],
  "entities": [
    {
      "name": "Entity Name",
      "type": "PERSON|ORG|LOCATION|PRODUCT|EVENT",
      "confidence": 0.95,
      "authority_score": 85,
      "related_keywords": ["keyword1", "keyword2"],
      "mentions_count": 3,
      "unique_identifier": "optional_id"
    }
  ],
  "concept_graph": {
    "primary_concepts": ["concept1", "concept2"],
    "secondary_concepts": ["concept3"],
    "concept_relationships": [
      {
        "source": "concept1",
        "target": "concept2",
        "relationship_type": "related|causes|implements|requires",
        "strength": 0.87
      }
    ]
  },
  "trending_alignment": {
    "is_trending": true,
    "trend_score": 76,
    "trending_keywords": ["keyword1", "keyword4"],
    "social_platforms": ["twitter", "linkedin"],
    "trend_velocity": "accelerating|stable|declining"
  },
  "seo_metrics": {
    "primary_keyword": "main keyword",
    "keyword_density": 2.3,
    "keyword_distribution": "good",
    "lsi_keywords": ["lsi_keyword1", "lsi_keyword2"],
    "average_seo_difficulty": 28
  },
  "topics": [
    {
      "topic": "topic name",
      "relevance_score": 89,
      "word_count": 250,
      "coverage_percentage": 18
    }
  ],
  "enrichment_metadata": {
    "processing_time_ms": 342,
    "keywords_extracted": 45,
    "entities_recognized": 12,
    "concepts_identified": 8,
    "web_validation_status": "complete|partial|failed",
    "confidence_average": 0.88
  },
  "payload_format_version": "1.0"
}
```

## Processing Logic

### Step 1: Text Preprocessing
```
1. Normalize whitespace and remove special characters
2. Convert to lowercase
3. Tokenize into sentences and words
4. Remove stopwords (use domain-aware stopword lists)
5. Lemmatization/Stemming
6. Identify capitalized proper nouns for NER
```

### Step 2: Keyword Extraction (Multi-Algorithm)
```
Algorithm 1: TF-IDF
  - Calculate term frequency and inverse document frequency
  - Score each term (0-100)
  - Select top 20 by score

Algorithm 2: RAKE (Rapid Automatic Keyword Extraction)
  - Extract multi-word phrases
  - Calculate co-occurrence matrix
  - Score by word degree and frequency

Algorithm 3: TextRank
  - Build word co-occurrence graph
  - Apply PageRank algorithm
  - Extract single and multi-word keywords

Combine and Deduplicate:
  - Merge results from all algorithms
  - Remove duplicates and near-duplicates (>0.9 similarity)
  - Final ranking by aggregate score
```

### Step 3: Named Entity Recognition
```
Using spaCy's pretrained model (en_core_web_md):
  1. Run NER pipeline on full content
  2. Extract entities by type (PERSON, ORG, LOCATION, etc.)
  3. Resolve entity aliases and variations
  4. Score confidence for each entity
  5. Extract entity relationships from sentence structure
```

### Step 4: Web Validation & Enrichment
```
For each extracted keyword:
  1. Query Google Trends API for search volume
  2. Estimate SEO difficulty (0-100 scale)
  3. Check social media mentions
  4. Validate entity authority via web search
  5. Identify trending status
  6. Extract related/LSI keywords

Timeout: 30 seconds per keyword (max 20 keywords validated)
```

### Step 5: Concept Mapping & Relationships
```
1. Identify primary concepts (highest-scoring keywords)
2. Map relationships between concepts
3. Calculate concept co-occurrence in text
4. Determine relationship types:
   - related_to: Concepts appear together
   - causes: Causal relationship
   - requires: Dependency
   - implements: Technical implementation
5. Create graph representation
```

## API Specification

### Invocation
```bash
POST /skill/keyword-entity-extractor/run

Payload:
{
  "content": { /* Content object from Blog Monitor */ },
  "extraction_mode": "full|keywords_only|entities_only",
  "validate_with_web": true,
  "timeout_seconds": 60,
  "min_keyword_score": 40,
  "max_keywords": 30
}
```

### Response Format
```json
{
  "skill_id": "keyword-entity-extractor-1",
  "execution_id": "uuid",
  "status": "success|partial_failure|failure",
  "processing_time_seconds": 3.2,
  "output": { /* Enriched content with keywords and entities */ },
  "stats": {
    "keywords_extracted": 28,
    "entities_recognized": 9,
    "concepts_identified": 6,
    "web_validations_performed": 20,
    "web_validations_successful": 18,
    "average_keyword_score": 76,
    "average_confidence": 0.87
  },
  "errors": [],
  "payload_format_version": "1.0"
}
```

## Enterprise Requirements

- **Scalability:** Process 50+ articles per minute
- **Accuracy:** 90%+ NER accuracy, 85%+ keyword relevance
- **Latency:** <5 seconds per article
- **Web Integration:** Graceful degradation if web validation unavailable
- **Caching:** Cache web validation results for 7 days
- **Monitoring:** Track extraction quality metrics
- **Error Handling:** Retry failed web validations, continue with local results

## Configuration Example

```yaml
skill:
  id: keyword-entity-extractor-1
  name: Keyword-Entity Extractor
  extraction:
    min_keyword_score: 50
    max_keywords: 30
    enable_web_validation: true
    web_validation_timeout: 30
  ner:
    enabled: true
    model: en_core_web_md
    confidence_threshold: 0.6
  algorithms:
    - tfidf
    - rake
    - textrank
```

## Integration Points

- **Inputs from:** Blog Monitor (Skill 1)
- **Outputs to:** Social Content Generator (Skill 3)
- **Dependencies:** spaCy NER model, Google Trends (optional)
- **Triggers:** Automatically on Blog Monitor output
- **Caching:** 24-hour cache for web validation results
