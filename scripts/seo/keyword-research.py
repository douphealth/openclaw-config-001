#!/usr/bin/env python3
"""
Keyword Research Mastery — Enterprise keyword discovery & prioritization
Combines GSC data, Google Autocomplete, PAA mining, and competitor analysis.
"""

import json, os, sys, time, argparse
from datetime import datetime
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    print("ERROR: pip install requests")
    sys.exit(1)

CACHE_DIR = os.path.expanduser('~/.openclaw/workspace/cache/seo-intel/')
OUTPUT_DIR = os.path.expanduser('~/.openclaw/workspace/cache/keyword-research/')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === Google Autocomplete ===

def get_autocomplete(seed, lang='en'):
    """Get Google Autocomplete suggestions."""
    try:
        resp = requests.get(
            "http://suggestqueries.google.com/complete/search",
            params={'client': 'firefox', 'q': seed, 'hl': lang},
            timeout=5
        )
        return resp.json()[1]
    except:
        return []

def alphabet_soup(seed):
    """Expand seed keyword with alphabet soup method."""
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(get_autocomplete, f"{seed} {letter}"): letter for letter in 'abcdefghijklmnopqrstuvwxyz'}
        for future in as_completed(futures):
            results.extend(future.result())
    return list(set(results))

def question_expansion(seed):
    """Expand with question words."""
    questions = []
    q_words = ['how to', 'what is', 'why does', 'when to', 'where to', 'can you', 'is it', 'should I']
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(get_autocomplete, f"{qw} {seed}"): qw for qw in q_words}
        for future in as_completed(futures):
            questions.extend(future.result())
    return list(set(questions))

# === Intent Classification ===

INTENT_SIGNALS = {
    'informational': ['what', 'how', 'why', 'when', 'who', 'where', 'guide', 'tutorial', 'tips', 'learn', 'explain', 'meaning', 'definition', 'examples', 'ideas'],
    'commercial': ['best', 'top', 'vs', 'versus', 'review', 'comparison', 'alternatives', 'cheap', 'affordable', 'worth', 'pros and cons'],
    'transactional': ['buy', 'price', 'cost', 'deal', 'discount', 'coupon', 'order', 'purchase', 'near me', 'hire', 'book', 'get'],
    'navigational': ['login', 'sign in', 'website', 'official', 'download', 'app'],
}

def classify_intent(keyword):
    """Classify search intent based on keyword signals."""
    kw_lower = keyword.lower()
    scores = {}
    for intent, signals in INTENT_SIGNALS.items():
        score = sum(1 for s in signals if s in kw_lower)
        if score > 0:
            scores[intent] = score
    if not scores:
        return 'informational'  # Default
    return max(scores, key=scores.get)

def geo_relevance(keyword):
    """Score GEO relevance (1-5) for AI search visibility."""
    kw_lower = keyword.lower()
    if any(w in kw_lower for w in ['what is', 'definition', 'meaning', 'vs', 'versus', 'difference']):
        return 5
    if any(w in kw_lower for w in ['how to', 'how do', 'steps', 'tutorial']):
        return 4
    if any(w in kw_lower for w in ['best', 'top', 'comparison', 'review']):
        return 3
    if any(w in kw_lower for w in ['near me', 'local', 'hire', 'service']):
        return 2
    return 1

# === GSC Data Integration ===

def load_gsc_data(domain):
    """Load cached GSC data for a domain."""
    cache_file = os.path.join(CACHE_DIR, f'{domain}.json')
    if os.path.exists(cache_file):
        with open(cache_file) as f:
            return json.load(f)
    return None

def find_gsc_opportunities(gsc_data, min_impressions=10):
    """Extract keyword opportunities from GSC data."""
    if not gsc_data:
        return []
    
    opportunities = []
    for q in gsc_data.get('top_queries', []):
        kw = q['query']
        imp = q.get('imp', q.get('impressions', 0))
        clicks = q.get('clicks', 0)
        ctr = q.get('ctr', 0)
        pos = q.get('pos', q.get('position', 100))
        
        if imp < min_impressions:
            continue
        
        opp_type = []
        if clicks == 0 and imp >= 50:
            opp_type.append('no_clicks')
        if 5 <= pos <= 15:
            opp_type.append('page2')
        if pos <= 10 and ctr < 0.02 and imp >= 100:
            opp_type.append('low_ctr')
        
        if opp_type:
            opportunities.append({
                'keyword': kw,
                'impressions': imp,
                'clicks': clicks,
                'ctr': ctr,
                'position': pos,
                'opportunity_types': opp_type,
                'intent': classify_intent(kw),
                'geo_score': geo_relevance(kw),
                'source': 'gsc'
            })
    
    return sorted(opportunities, key=lambda x: x['impressions'], reverse=True)

# === Priority Scoring ===

def estimate_difficulty(keyword):
    """Estimate KD based on keyword characteristics (heuristic)."""
    words = len(keyword.split())
    if words >= 5:
        return 15  # Long-tail = easy
    if words >= 4:
        return 25
    if words >= 3:
        return 40
    if words >= 2:
        return 55
    return 70  # Single word = hard

def score_priority(keyword_data):
    """Calculate priority score (0-5) for a keyword."""
    imp = keyword_data.get('impressions', keyword_data.get('volume_estimate', 0))
    kd = estimate_difficulty(keyword_data['keyword'])
    intent = keyword_data.get('intent', 'informational')
    geo = keyword_data.get('geo_score', 3)
    
    # Volume score (1-5)
    if imp >= 10000: vol_score = 5
    elif imp >= 5000: vol_score = 4
    elif imp >= 1000: vol_score = 3
    elif imp >= 500: vol_score = 2
    else: vol_score = 1
    
    # Difficulty score (1-5, lower KD = higher score)
    if kd <= 20: kd_score = 5
    elif kd <= 35: kd_score = 4
    elif kd <= 50: kd_score = 3
    elif kd <= 65: kd_score = 2
    else: kd_score = 1
    
    # Intent score
    intent_scores = {'transactional': 5, 'commercial': 4, 'informational': 3, 'navigational': 1}
    intent_score = intent_scores.get(intent, 3)
    
    # Business relevance (default 3, should be manually adjusted)
    biz_score = 3
    
    # Trend (default 3, would need historical data)
    trend_score = 3
    
    # Weighted score
    priority = (
        vol_score * 0.20 +
        kd_score * 0.25 +
        biz_score * 0.30 +
        intent_score * 0.15 +
        trend_score * 0.10
    )
    
    if priority >= 4.0: tier = 'P0'
    elif priority >= 3.0: tier = 'P1'
    elif priority >= 2.0: tier = 'P2'
    else: tier = 'P3'
    
    return round(priority, 2), tier

# === Main Research Pipeline ===

def research_domain(domain, seeds=None, expand=True):
    """Full keyword research pipeline for a domain."""
    print(f"\n{'='*60}")
    print(f"KEYWORD RESEARCH: {domain}")
    print(f"{'='*60}\n")
    
    all_keywords = []
    
    # 1. Load GSC data
    gsc_data = load_gsc_data(domain)
    if gsc_data:
        gsc_opps = find_gsc_opportunities(gsc_data)
        all_keywords.extend(gsc_opps)
        print(f"📊 GSC: {len(gsc_opps)} opportunities found")
    else:
        print(f"⚠️  No GSC data cached for {domain}")
    
    # 2. Expand from seeds
    if seeds:
        print(f"\n🔍 Expanding {len(seeds)} seed keywords...")
        for seed in seeds:
            # Autocomplete
            auto = get_autocomplete(seed)
            for kw in auto:
                all_keywords.append({
                    'keyword': kw,
                    'impressions': 0,
                    'intent': classify_intent(kw),
                    'geo_score': geo_relevance(kw),
                    'source': f'autocomplete:{seed}'
                })
            
            if expand:
                # Alphabet soup
                alpha = alphabet_soup(seed)
                for kw in alpha:
                    if not any(k['keyword'] == kw for k in all_keywords):
                        all_keywords.append({
                            'keyword': kw,
                            'impressions': 0,
                            'intent': classify_intent(kw),
                            'geo_score': geo_relevance(kw),
                            'source': f'alphabet:{seed}'
                        })
                
                # Questions
                questions = question_expansion(seed)
                for kw in questions:
                    if not any(k['keyword'] == kw for k in all_keywords):
                        all_keywords.append({
                            'keyword': kw,
                            'impressions': 0,
                            'intent': classify_intent(kw),
                            'geo_score': geo_relevance(kw),
                            'source': f'question:{seed}'
                        })
            
            time.sleep(0.2)  # Rate limit
        
        print(f"  → {len(all_keywords)} total keywords discovered")
    
    # 3. Score priorities
    for kw in all_keywords:
        score, tier = score_priority(kw)
        kw['priority_score'] = score
        kw['priority_tier'] = tier
    
    # 4. Sort by priority
    all_keywords.sort(key=lambda x: x['priority_score'], reverse=True)
    
    # 5. Deduplicate
    seen = set()
    unique_keywords = []
    for kw in all_keywords:
        if kw['keyword'].lower() not in seen:
            seen.add(kw['keyword'].lower())
            unique_keywords.append(kw)
    
    # 6. Report
    p0 = [k for k in unique_keywords if k['priority_tier'] == 'P0']
    p1 = [k for k in unique_keywords if k['priority_tier'] == 'P1']
    p2 = [k for k in unique_keywords if k['priority_tier'] == 'P2']
    
    print(f"\n📊 RESULTS: {len(unique_keywords)} unique keywords")
    print(f"  P0 (Must Target): {len(p0)}")
    print(f"  P1 (High Value):  {len(p1)}")
    print(f"  P2 (Opportunity): {len(p2)}")
    
    # Intent breakdown
    intents = Counter(k['intent'] for k in unique_keywords)
    print(f"\n🎯 Intent Distribution:")
    for intent, count in intents.most_common():
        print(f"  {intent}: {count} ({count/len(unique_keywords)*100:.0f}%)")
    
    # GEO distribution
    high_geo = sum(1 for k in unique_keywords if k['geo_score'] >= 4)
    print(f"\n🤖 GEO Relevance: {high_geo} keywords score 4+ (high AI visibility potential)")
    
    # Top opportunities
    print(f"\n🏆 TOP 20 KEYWORDS (by Priority Score)")
    print(f"{'#':>3} {'Keyword':<40} {'Score':>6} {'Tier':>4} {'Intent':<15} {'GEO':>3} {'Source':<20}")
    print("-" * 95)
    for i, kw in enumerate(unique_keywords[:20], 1):
        print(f"{i:3d} {kw['keyword'][:39]:<40} {kw['priority_score']:>6.2f} {kw['priority_tier']:>4} {kw['intent']:<15} {kw['geo_score']:>3} {kw['source'][:19]:<20}")
    
    # Save results
    output = {
        'domain': domain,
        'date': datetime.now().strftime('%Y-%m-%d'),
        'total_keywords': len(unique_keywords),
        'summary': {
            'p0': len(p0),
            'p1': len(p1),
            'p2': len(p2),
            'p3': len(unique_keywords) - len(p0) - len(p1) - len(p2),
            'intents': dict(intents),
            'high_geo': high_geo,
        },
        'keywords': unique_keywords
    }
    
    output_file = os.path.join(OUTPUT_DIR, f'{domain}.json')
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n💾 Saved to {output_file}")
    
    return output

# === CLI ===

def main():
    parser = argparse.ArgumentParser(description='Keyword Research Mastery')
    parser.add_argument('--domain', required=True, help='Domain to research (e.g., mysticaldigits.com)')
    parser.add_argument('--seeds', nargs='+', help='Seed keywords to expand')
    parser.add_argument('--no-expand', action='store_true', help='Skip alphabet/question expansion')
    parser.add_argument('--all', action='store_true', help='Research all 10 managed sites')
    
    args = parser.parse_args()
    
    if args.all:
        sites = [
            'affiliatemarketingforsuccess.com',
            'efficientgptprompts.com',
            'frenchyfab.com',
            'gearuptofit.com',
            'gearuptogrow.com',
            'micegoneguide.com',
            'mysticaldigits.com',
            'openclaw-skillshub.com',
            'outdoormisting.com',
            'plantastichaven.com',
        ]
        for domain in sites:
            try:
                research_domain(domain, args.seeds, not args.no_expand)
            except Exception as e:
                print(f"❌ {domain}: {e}")
    else:
        research_domain(args.domain, args.seeds, not args.no_expand)

if __name__ == '__main__':
    main()
