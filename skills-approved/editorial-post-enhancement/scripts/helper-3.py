def score_content_quality(html, target_keyword):
    """Score content quality 0-100."""
    score = 0
    feedback = []
    
    # Word count (20 points)
    text = re.sub(r'<[^>]+>', ' ', html)
    words = len(text.split())
    if words >= 2000:
        score += 20
    elif words >= 1000:
        score += 15
    elif words >= 500:
        score += 10
    elif words >= 300:
        score += 5
    else:
        feedback.append(f'Content too short: {words} words')
    
    # Keyword in title (10 points)
    title = re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
    if title and target_keyword.lower() in title.group(1).lower():
        score += 10
    else:
        feedback.append('Target keyword not in title')
    
    # Keyword in H1 (10 points)
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
    if h1 and any(target_keyword.lower() in h.lower() for h in h1):
        score += 10
    else:
        feedback.append('Target keyword not in H1')
    
    # Keyword in first 100 words (5 points)
    first_100 = ' '.join(text.split()[:100])
    if target_keyword.lower() in first_100.lower():
        score += 5
    
    # Headers structure (10 points)
    headers = re.findall(r'<h[2-6][^>]*>', html, re.I)
    if len(headers) >= 5:
        score += 10
    elif len(headers) >= 3:
        score += 5
    else:
        feedback.append('Add more headers for structure')
    
    # Internal links (10 points)
    internal_links = re.findall(r'href=["\']https?://[^"\']*(?:yourdomain|site\.com)[^"\']*["\']', html, re.I)
    if len(internal_links) >= 5:
        score += 10
    elif len(internal_links) >= 3:
        score += 5
    else:
        feedback.append('Add more internal links (aim for 5+)')
    
    # Schema markup (10 points)
    if 'application/ld+json' in html:
        score += 10
    else:
        feedback.append('Add JSON-LD schema markup')
    
    # FAQ section (10 points)
    if re.search(r'faq|frequently asked|common questions', html, re.I):
        score += 10
    else:
        feedback.append('Add FAQ section')
    
    # Images with alt text (10 points)
    images = re.findall(r'<img[^>]*>', html, re.I)
    images_with_alt = re.findall(r'<img[^>]*alt=["\'][^"\']+["\'][^>]*>', html, re.I)
    if images and len(images_with_alt) / len(images) >= 0.8:
        score += 10
    elif images_with_alt:
        score += 5
        feedback.append('Add alt text to all images')
    
    # Lists and tables (5 points)
    if re.search(r'<[ou]l[^>]*>', html, re.I) or re.search(r'<table[^>]*>', html, re.I):
        score += 5
    
    return {'score': score, 'feedback': feedback}
