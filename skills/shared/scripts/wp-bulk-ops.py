#!/usr/bin/env python3
"""
WordPress Bulk Operations — Enterprise-grade helper for batch WP REST API work.
Implements: health check, backup, retry, parallel processing, verification, progress.
"""
import requests, json, os, time, sys
from concurrent.futures import ThreadPoolExecutor, as_completed

class WPSite:
    def __init__(self, base_url, username, password, site_name="site"):
        self.base = base_url.rstrip('/')
        self.auth = (username, password)
        self.name = site_name
        self.UA = {"User-Agent": f"OpenClaw/{site_name}"}
        self.results = {'success': 0, 'error': 0, 'skipped': 0}

    def health_check(self, timeout=10):
        """Verify site is accessible."""
        try:
            r = requests.get(self.base, timeout=timeout)
            return r.status_code == 200
        except:
            return False

    def api_get(self, path, retries=3, timeout=60):
        """GET with retry logic and exponential backoff."""
        for attempt in range(retries):
            try:
                r = requests.get(
                    f'{self.base}{path}',
                    auth=self.auth,
                    headers=self.UA,
                    timeout=timeout
                )
                if r.status_code == 429:
                    wait = int(r.headers.get('Retry-After', 5))
                    time.sleep(wait)
                    continue
                if r.status_code >= 500:
                    time.sleep(2 ** attempt)
                    continue
                if r.status_code == 200:
                    txt = r.text
                    if txt and txt[0] == '\ufeff': txt = txt[1:]
                    return json.loads(txt)
                return None
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                if attempt < retries - 1:
                    time.sleep(2 ** attempt)
                    continue
        return None

    def api_post(self, path, data, retries=3, timeout=60):
        """POST with retry logic."""
        for attempt in range(retries):
            try:
                r = requests.post(
                    f'{self.base}{path}',
                    auth=self.auth,
                    headers=self.UA,
                    json=data,
                    timeout=timeout
                )
                if r.status_code == 429:
                    wait = int(r.headers.get('Retry-After', 5))
                    time.sleep(wait)
                    continue
                if r.status_code >= 500:
                    time.sleep(2 ** attempt)
                    continue
                return r.status_code
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                if attempt < retries - 1:
                    time.sleep(2 ** attempt)
                    continue
        return 0

    def backup(self, post_id, post_data):
        """Backup a post before modification."""
        os.makedirs(f'ops/backups/{self.name}/', exist_ok=True)
        with open(f'ops/backups/{self.name}/post-{post_id}.json', 'w') as f:
            json.dump(post_data, f)

    def backup_all_posts(self, max_posts=500):
        """Backup all posts."""
        os.makedirs(f'ops/backups/{self.name}/', exist_ok=True)
        saved = 0
        for page in range(1, 20):
            posts = self.api_get(f'/wp-json/wp/v2/posts?per_page=100&page={page}&_fields=id')
            if not posts or isinstance(posts, dict) or len(posts) == 0: break
            for p in posts:
                data = self.api_get(f'/wp-json/wp/v2/posts/{p["id"]}?context=edit')
                if data:
                    self.backup(p['id'], data)
                    saved += 1
            if len(posts) < 100: break
        return saved

    def get_all_posts(self, fields='id,title,slug'):
        """Get all posts with pagination."""
        all_posts = []
        for page in range(1, 20):
            posts = self.api_get(f'/wp-json/wp/v2/posts?per_page=100&page={page}&_fields={fields}')
            if not posts or isinstance(posts, dict) or len(posts) == 0: break
            all_posts.extend(posts)
            if len(posts) < 100: break
        return all_posts

    def process_posts(self, worker_fn, max_workers=5, batch_size=50, health_interval=50):
        """
        Process all posts with parallel workers.
        worker_fn(post_data) -> (modified_content, changes_made)
        Returns results dict.
        """
        posts = self.get_all_posts()
        total = len(posts)
        print(f"Processing {total} posts with {max_workers} workers...")

        def process_one(post_brief):
            pid = post_brief['id']
            post = self.api_get(f'/wp-json/wp/v2/posts/{pid}?context=edit')
            if not post:
                return ('error', pid, 'fetch failed')

            raw = post.get('content', {}).get('raw', '')
            self.backup(pid, post)

            try:
                new_content, changes = worker_fn(pid, raw, post)
                if new_content and new_content != raw:
                    status = self.api_post(f'/wp-json/wp/v2/posts/{pid}', {'content': new_content})
                    if status == 200:
                        return ('success', pid, changes)
                    else:
                        return ('error', pid, f'HTTP {status}')
                else:
                    return ('skipped', pid, 'no changes')
            except Exception as e:
                return ('error', pid, str(e)[:60])

        # Process in batches
        for batch_start in range(0, total, batch_size):
            batch = posts[batch_start:batch_start + batch_size]

            # Health check before batch
            if not self.health_check():
                print(f"⚠ Site down at batch {batch_start//batch_size + 1}. Waiting 30s...")
                time.sleep(30)
                if not self.health_check():
                    print(f"✗ Site still down. Stopping.")
                    break

            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {executor.submit(process_one, p): p for p in batch}
                for i, future in enumerate(as_completed(futures)):
                    result = future.result(timeout=120)
                    status, pid, info = result
                    if status == 'success':
                        self.results['success'] += 1
                        print(f"  ✓ ID {pid}: {info}")
                    elif status == 'error':
                        self.results['error'] += 1
                        print(f"  ✗ ID {pid}: {info}")
                    else:
                        self.results['skipped'] += 1

            done = min(batch_start + batch_size, total)
            print(f"Progress: {done}/{total} | ✓ {self.results['success']} | ✗ {self.results['error']} | ⏭ {self.results['skipped']}")

            time.sleep(1)  # Rate limiting between batches

        return self.results

    def audit_posts(self, check_fn):
        """Audit all posts for specific patterns."""
        posts = self.get_all_posts()
        issues = []
        for i, p in enumerate(posts):
            data = self.api_get(f'/wp-json/wp/v2/posts/{p["id"]}?context=edit&_fields=content')
            if not data: continue
            raw = data.get('content', {}).get('raw', '')
            found = check_fn(p['id'], raw, p)
            if found:
                issues.extend(found)
            if (i + 1) % 20 == 0:
                print(f"  Audited {i+1}/{len(posts)} posts...")
            time.sleep(0.2)
        return issues

    def report(self, duration=None):
        """Print completion report."""
        r = self.results
        total = r['success'] + r['error'] + r['skipped']
        print(f"\n{'='*50}")
        print(f"OPERATION COMPLETE")
        print(f"{'='*50}")
        print(f"Total: {total} items")
        print(f"✓ Success: {r['success']} ({r['success']*100//max(total,1)}%)")
        print(f"✗ Errors: {r['error']}")
        print(f"⏭ Skipped: {r['skipped']}")
        if duration:
            print(f"⏱ Duration: {duration:.0f}s")
        print(f"📁 Backup: ops/backups/{self.name}/")
        print(f"{'='*50}")


if __name__ == '__main__':
    print("wp-bulk-ops.py — WordPress Bulk Operations Helper")
    print("Import this module and use WPSite class.")
    print("Example:")
    print("  from wp_bulk_ops import WPSite")
    print("  site = WPSite('https://example.com', 'user', 'pass', 'mysite')")
    print("  site.health_check()")
    print("  site.backup_all_posts()")
    print("  site.process_posts(worker_fn, max_workers=5)")
