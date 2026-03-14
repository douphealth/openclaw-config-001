def audit_core_web_vitals(url):
    """Check Core Web Vitals metrics."""
    # Use PageSpeed Insights API
    import json
    api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile'
    try:
        req = urllib.request.Request(api_url)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            cwv = data.get('loadingExperience', {}).get('metrics', {})
            
            issues = []
            
            # LCP (Largest Contentful Paint) - should be < 2.5s
            lcp = cwv.get('LARGEST_CONTENTFUL_PAINT_MS', {}).get('percentile', 0)
            if lcp > 4000:
                issues.append(f'CRITICAL: LCP is {lcp}ms (should be < 2500ms)')
            elif lcp > 2500:
                issues.append(f'WARNING: LCP is {lcp}ms (should be < 2500ms)')
            
            # CLS (Cumulative Layout Shift) - should be < 0.1
            cls = cwv.get('CUMULATIVE_LAYOUT_SHIFT_SCORE', {}).get('percentile', 0)
            if cls > 250:  # GSC reports CLS * 100
                issues.append(f'CRITICAL: CLS is {cls/100} (should be < 0.1)')
            
            # INP (Interaction to Next Paint) - should be < 200ms
            inp = cwv.get('INTERACTION_TO_NEXT_PAINT', {}).get('percentile', 0)
            if inp > 500:
                issues.append(f'CRITICAL: INP is {inp}ms (should be < 200ms)')
            elif inp > 200:
                issues.append(f'WARNING: INP is {inp}ms (should be < 200ms)')
                
            return issues
    except Exception as e:
        return [f'ERROR: Cannot fetch CWV data: {e}']
