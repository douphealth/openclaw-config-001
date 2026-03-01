# WordPress Incident Response (Critical)

Use for: source code leakage, broken templates, malformed head output, mass canonical corruption, plugin conflicts causing rendering failure.

## Immediate containment
1. Freeze non-essential writes.
2. Snapshot affected files/content/state.
3. Confirm blast radius (homepage + top templates + high-traffic URLs).
4. Revert latest risky change first.
5. Purge site/cache/CDN as needed.

## Rapid diagnosis
- Check theme file integrity (`functions.php`, `header.php`, custom snippets).
- Check active SEO/cache/minify plugin conflicts.
- Check if admin/login and public rendering are both impacted.
- Check PHP execution sanity (no escaped/raw PHP in output).

## Recovery sequence
1. Restore known-good theme/plugin/file state.
2. Validate homepage and 3-5 critical URLs.
3. Validate canonical/self-reference + schema presence.
4. Reopen writes only after stable verification.

## Closure evidence
- Before/after snapshots
- URL-level verification list
- Root cause hypothesis + prevention step
- Residual risks and follow-up ETA
