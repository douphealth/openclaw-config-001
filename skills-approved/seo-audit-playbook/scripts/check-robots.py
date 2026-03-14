def audit_sitemap(domain):
    """Check sitemap health."""
    issues = []
    try:
        req = urllib.request.Request(f'https://{domain}/sitemap.xml',
                                     headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode()
            
            # Count URLs
            urls = re.findall(r'<loc>(.*?)</loc>', content)
            if len(urls) == 0:
                issues.append('CRITICAL: Sitemap has no URLs')
            elif len(urls) > 50000:
                issues.append(f'WARNING: Sitemap has {len(urls)} URLs (consider splitting)')
            
            # Check for non-canonical URLs
            for url in urls[:100]:  # Sample first 100
                if '?' in url and 'lang=' not in url:
                    issues.append(f'WARNING: Sitemap contains query string URL: {url}')
                    break
                    
    except Exception as e:
        issues.append(f'ERROR: Cannot fetch sitemap: {e}')
    
    return issues
