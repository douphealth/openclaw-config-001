#!/usr/bin/env python3
import requests, re, json, sys

def check_url(url, timeout=30):
    r = requests.get(url, timeout=timeout, headers={'User-Agent':'OpenClaw verify'})
    txt = r.text
    return {
        'url': url,
        'status': r.status_code,
        'title_len': len(re.search(r'<title[^>]*>(.*?)</title>', txt, re.I|re.S).group(1).strip()) if re.search(r'<title[^>]*>(.*?)</title>', txt, re.I|re.S) else 0,
        'meta_desc_len': len(re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', txt, re.I|re.S).group(1).strip()) if re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', txt, re.I|re.S) else 0,
        'h1_count': len(re.findall(r'<h1\b', txt, re.I)),
        'related_posts_count': txt.count('Related Posts'),
        'has_embedded_doctype': '<!DOCTYPE html>' in txt[4000:]
    }

if __name__ == '__main__':
    print(json.dumps([check_url(u) for u in sys.argv[1:]], indent=2))
