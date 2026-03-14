def find_topic_gaps(article_html, competitor_html_list, target_keyword):
    """Find topics competitors cover that this article misses."""
    
    # Extract headings and key terms from article
    article_headings = set()
    article_entities = set()
    
    headings = re.findall(r'<h[2-6][^>]*>(.*?)</h[2-6]>', article_html, re.I | re.S)
    for h in headings:
        clean = re.sub(r'<[^>]+>', '', h).strip().lower()
        article_headings.add(clean)
    
    # Extract from competitors
    competitor_headings = set()
    competitor_entities = set()
    
    for comp_html in competitor_html_list:
        comp_headings = re.findall(r'<h[2-6][^>]*>(.*?)</h[2-6]>', comp_html, re.I | re.S)
        for h in comp_headings:
            clean = re.sub(r'<[^>]+>', '', h).strip().lower()
            competitor_headings.add(clean)
    
    # Find gaps
    missing_headings = competitor_headings - article_headings
    
    return {
        'missing_topics': list(missing_headings)[:10],
        'article_covers': len(article_headings),
        'competitors_average': len(competitor_headings) // max(len(competitor_html_list), 1),
    }
