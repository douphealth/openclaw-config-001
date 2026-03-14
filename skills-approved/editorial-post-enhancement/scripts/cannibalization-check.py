def check_article_cannibalization(article_url, article_keyword, site_content):
    """
    Verify this article won't cannibalize another page.
    
    Returns: dict with 'safe_to_optimize', 'conflicts', 'recommendation'
    """
    conflicts = []
    
    for page in site_content:
        if page['url'] == article_url:
            continue
        
        # Same target keyword?
        if page.get('target_keyword', '').lower() == article_keyword.lower():
            conflicts.append({
                'page': page['url'],
                'reason': 'Same target keyword',
                'severity': 'CRITICAL'
            })
        
        # Ranking for same keyword?
        if article_keyword.lower() in [kw.lower() for kw in page.get('ranking_keywords', [])]:
            conflicts.append({
                'page': page['url'],
                'reason': 'Also ranking for target keyword',
                'severity': 'HIGH'
            })
    
    safe = len([c for c in conflicts if c['severity'] == 'CRITICAL']) == 0
    
    return {
        'safe_to_optimize': safe,
        'conflicts': conflicts,
        'recommendation': 'Proceed with optimization' if safe else 'Resolve cannibalization first'
    }
