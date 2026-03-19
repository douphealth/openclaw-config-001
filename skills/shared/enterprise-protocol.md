# Enterprise Operations Protocol

Every skill MUST follow these protocols. No exceptions.

## 1. Pre-Flight Check (MANDATORY — before ANY operation)

```
□ Target accessibility — can I reach the site/system?
  → curl -s -o /dev/null -w "%{http_code}" --max-time 10 https://TARGET/
  → If HTTP != 200, STOP. Report issue. Do NOT proceed.

□ Credentials verified — do auth credentials work?
  → Test with a minimal API call (GET /wp-json/wp/v2/posts?per_page=1)
  → If 401/403, STOP. Check credentials.

□ Current state captured — what exists before changes?
  → GET before POST. Always.
  → Store raw response for rollback.

□ Rollback plan — how do I undo if this breaks?
  → Back up to ops/backups/{site}/{post-id}.json
  → Know the REST endpoint to restore (POST /wp-json/wp/v2/posts/{id})

□ Scope defined — how many items? What's the batch size?
  → If >20 items, use parallel processing
  → If >100 items, use concurrent.futures with max_workers=5
```

## 2. Mandatory Backup (before ANY modification)

```python
# ALWAYS backup before modifying
import os, json
os.makedirs(f'ops/backups/{site_name}/', exist_ok=True)
with open(f'ops/backups/{site_name}/post-{id}.json', 'w') as f:
    json.dump(original_data, f)
```

**Never skip backup. Even for single-post operations.**

## 3. Retry Logic (for all API calls)

```python
import time
def api_call(method, url, **kwargs):
    for attempt in range(3):
        try:
            r = requests.request(method, url, timeout=60, **kwargs)
            if r.status_code == 429:  # Rate limited
                wait = int(r.headers.get('Retry-After', 5))
                time.sleep(wait)
                continue
            if r.status_code >= 500:  # Server error
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            return r
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            if attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise
    raise Exception(f"Failed after 3 attempts: {url}")
```

## 4. Batch Processing (for operations on multiple items)

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_batch(items, worker_fn, max_workers=5):
    """Process items in parallel with error tracking."""
    results = {'success': 0, 'error': 0, 'details': []}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(worker_fn, item): item for item in items}
        for future in as_completed(futures):
            item = futures[future]
            try:
                result = future.result(timeout=120)
                results['success'] += 1
                results['details'].append(f"✓ {item['id']}")
            except Exception as e:
                results['error'] += 1
                results['details'].append(f"✗ {item['id']}: {str(e)[:60]}")
    return results
```

## 5. Progress Reporting (every N items)

```python
# Print progress every 10 items
if (i + 1) % 10 == 0:
    print(f"Progress: {i+1}/{total} | ✓ {success} | ✗ {errors}")
```

## 6. Verification (after each modification)

```python
# Verify the change was applied
def verify_change(url, expected_pattern, retries=2):
    for _ in range(retries):
        r = api_call('GET', url)
        if expected_pattern in r.text:
            return True
        time.sleep(1)
    return False
```

## 7. Health Check (during long operations)

```python
# Check site health every 50 items
if (i + 1) % 50 == 0:
    r = requests.get(f'{base}/', timeout=10)
    if r.status_code != 200:
        print(f"⚠ Site down at item {i+1}. Pausing 30s...")
        time.sleep(30)
        # Re-check
        r = requests.get(f'{base}/', timeout=10)
        if r.status_code != 200:
            print(f"✗ Site still down. Stopping. {success} completed, {errors} failed.")
            break
```

## 8. Error Recovery

After 2 failures on same item:
1. Try alternative approach (different endpoint, different method)
2. If alternative fails → skip item, log error, continue batch
3. After batch → report all skipped items for manual review

## 9. Completion Report

```
=== OPERATION COMPLETE ===
Total: {total} items
✓ Success: {success} ({success/total*100:.0f}%)
✗ Errors: {errors}
⏭ Skipped: {skipped}
⏱ Duration: {duration}
📁 Backup: ops/backups/{site}/
```

## 10. Anti-Patterns (NEVER do these)

- ❌ Modify without backup
- ❌ Skip health check before operations
- ❌ Use infinite retry loops (max 3 attempts)
- ❌ Process all items sequentially when >20 (use parallel)
- ❌ Ignore 429 rate limit responses
- ❌ Claim success without verification
- ❌ Leave no progress trail for long operations
