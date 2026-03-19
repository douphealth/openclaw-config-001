#!/usr/bin/env python3
"""
Remove saved Link Whisper related-post blocks from WP post content.
Use when the live page shows duplicate Related Posts because one copy is saved in raw content
and another is injected at render time.
"""
import re, requests, json, sys, time

PAT = re.compile(r'<div id="link-whisper-related-posts-widget" class="link-whisper-related-posts lwrp">.*?</div>\s*</div>\s*</div>', re.S)

def fix_raw(raw):
    new, count = PAT.subn('', raw)
    new = re.sub(r'\n{3,}', '\n\n', new).strip()
    return new, count

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage: remove_linkwhisper_duplicates.py BASE USER PASS POST_ID [POST_ID...]')
        sys.exit(1)
    base, user, pwd = sys.argv[1:4]
    ids = sys.argv[4:]
    ua={'User-Agent':'OpenClaw recovery script'}
    for pid in ids:
        r=requests.get(f'{base.rstrip('/')}/wp-json/wp/v2/posts/{pid}?context=edit', auth=(user,pwd), headers=ua, timeout=60)
        txt=r.text
        if txt and txt[0]=='\ufeff': txt=txt[1:]
        post=json.loads(txt)
        raw=post['content']['raw']
        new,count=fix_raw(raw)
        if count:
            rr=requests.post(f'{base.rstrip('/')}/wp-json/wp/v2/posts/{pid}', auth=(user,pwd), headers=ua, json={'content':new}, timeout=60)
            print(pid, rr.status_code, count)
        else:
            print(pid, 'nochange', 0)
        time.sleep(0.5)
