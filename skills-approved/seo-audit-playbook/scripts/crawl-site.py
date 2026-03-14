import urllib.request
import re

def audit_robots_txt(domain):
    """Audit robots.txt for issues."""
    issues = []
    try:
        req = urllib.request.Request(f'https://{domain}/robots.txt', 
                                     headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode()
            
            # Check for blocking important paths
            blocks = re.findall(r'Disallow:\s*(/[^\s]*)', content, re.I)
            critical_paths = ['/', '/wp-content/', '/category/', '/tag/']
            for path in critical_paths:
                if path in blocks:
                    issues.append(f'CRITICAL: Robots.txt blocks {path}')
            
            # Check for sitemap declaration
            if 'Sitemap:' not in content:
                issues.append('WARNING: No Sitemap declaration in robots.txt')
            
            # Check for overly restrictive rules
            if re.search(r'Disallow:\s*/\s*$', content, re.M):
                issues.append('CRITICAL: Robots.txt blocks entire site!')
                
    except Exception as e:
        issues.append(f'ERROR: Cannot fetch robots.txt: {e}')
    
    return issues
