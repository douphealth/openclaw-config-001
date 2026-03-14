def analyze_serp_for_keyword(keyword):
    """Analyze what's ranking for the target keyword."""
    analysis = {
        'keyword': keyword,
        'intent': classify_search_intent(keyword),
        'top_results': [],
        'common_patterns': [],
        'content_gaps': [],
        'serp_features': [],
    }
    
    # Intent classification
    # Informational: how, what, why, guide, tutorial
    # Commercial: best, review, vs, comparison
    # Transactional: buy, price, coupon, deal
    
    return analysis
