#!/usr/bin/env python3
"""
Restore or forward-fix one canary record before wave rollout.
Usage:
  recovery_canary.py backup.json https://site.com user pass [post_id]
"""
import json, sys, requests

if len(sys.argv) < 5:
    print("Usage: recovery_canary.py backup.json https://site.com user pass [post_id]")
    sys.exit(1)

backup_path, base, user, pwd = sys.argv[1:5]
with open(backup_path) as f:
    data = json.load(f)
post_id = sys.argv[5] if len(sys.argv) > 5 else str(data.get('id'))

payload = {}
if 'content' in data and isinstance(data['content'], dict):
    payload['content'] = data['content'].get('raw', '')
if 'title' in data and isinstance(data['title'], dict):
    payload['title'] = data['title'].get('raw') or data['title'].get('rendered')
if 'excerpt' in data and isinstance(data['excerpt'], dict):
    payload['excerpt'] = data['excerpt'].get('raw', '')
if 'meta' in data:
    payload['meta'] = data['meta']

r = requests.post(f"{base.rstrip('/')}/wp-json/wp/v2/posts/{post_id}", auth=(user, pwd), json=payload, timeout=60)
print(r.status_code)
print(r.text[:500])
