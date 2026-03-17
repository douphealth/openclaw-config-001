# WordPress Error Pattern Database

> This file is auto-populated by `error-tracker.py`. New patterns are added dynamically.

## Active Patterns (Sorted by Frequency)

### EP-001: Slug Conflict (Page vs Post)
- **Frequency:** 4 | **Confidence:** 0.99
- **Cause:** PAGE and POST share same slug; WP routes to PAGE
- **Fix:** Force-delete conflicting page
- **Prevention:** Check slug uniqueness before content operations

### EP-002: wpautop Style Block Corruption
- **Frequency:** 380+ | **Confidence:** 0.95
- **Cause:** wpautop() injects <p> tags into <style> blocks
- **Fix:** Strip artifacts from style blocks, re-embed
- **Prevention:** Always wrap raw HTML in <!-- wp:html --> blocks

### EP-003: post_content Wiped to 0
- **Frequency:** 2 | **Confidence:** 0.98
- **Cause:** Batch operation error wipes post_content field
- **Fix:** Restore from rendered field via API
- **Prevention:** Verify raw content after every batch operation

### EP-004: Elementor Template Blocking Content
- **Frequency:** 1 | **Confidence:** 0.90
- **Cause:** elementor_header_footer template has no content area
- **Fix:** Change template or force-delete page
- **Prevention:** Check template before applying

### EP-005: Script Tag Sanitization
- **Frequency:** 10+ | **Confidence:** 0.92
- **Cause:** wp_filter_post_kses strips <script> from post content
- **Fix:** Migrate to Code Snippets plugin or mu-plugin
- **Prevention:** Never put scripts in post content via REST API
