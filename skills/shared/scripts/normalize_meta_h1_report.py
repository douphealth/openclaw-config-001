#!/usr/bin/env python3
"""
Generate a quick title/meta/H1 integrity report for a list of URLs.
"""
import requests, re, sys, json
ua={'User-Agent':'OpenClaw verify'}
urls=sys.argv[1:]
out=[]
for url in urls:
    try:
        txt=requests.get(url, headers=ua, timeout=30).text
        title=re.search(r'<title[^>]*>(.*?)</title>', txt, re.I|re.S)
        desc=re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', txt, re.I|re.S)
        out.append({
            'url': url,
            'title_len': len(title.group(1).strip()) if title else 0,
            'meta_desc_len': len(desc.group(1).strip()) if desc else 0,
            'h1_count': len(re.findall(r'<h1\b', txt, re.I)),
            'related_posts_count': txt.count('Related Posts')
        })
    except Exception as e:
        out.append({'url':url,'error':str(e)[:80]})
print(json.dumps(out, indent=2))
