# Secure Setup — Amazon Affiliate Product Box

## Local secret pattern
Use these two workspace-local secret files only:

- `.secrets/amazon-affiliate-product-box.env`
- `.secrets/amazon-affiliate-product-box.serpapi.keys`

### What goes where
- `AMAZON_ASSOC_TAG` -> Amazon Associates tracking tag only
- `SERPAPI_KEYS_FILE` -> absolute path to the line-based key pool file
- `.serpapi.keys` -> one SerpApi key per line, first working key wins

This keeps the affiliate tag separate from normal docs and keeps the rotating key pool out of the skill file itself.

## Safe retrieval flow
Before using the skill in a local shell:

```bash
set -a
source /home/openclaw/.openclaw/workspace/.secrets/amazon-affiliate-product-box.env
set +a
```

Then read the key pool from `$SERPAPI_KEYS_FILE` and use the first non-comment, non-empty line.
Only fall through to the next line on auth, quota, or provider failure.

## Safe operating rules
- Never paste raw keys or the raw affiliate tag into chat, memory files, or normal docs.
- Never hardcode keys or tag values into `SKILL.md`, templates, scripts, or generated HTML.
- Do not log the full key; if needed, log only the line index used.
- The affiliate tag belongs only in the final Amazon URL construction step.
- If a tag rotates, update only `.secrets/amazon-affiliate-product-box.env`.
- If a SerpApi key rotates, update only `.secrets/amazon-affiliate-product-box.serpapi.keys`.

## Minimal usage expectation
1. Confirm article/product fit first.
2. Load `.secrets/amazon-affiliate-product-box.env`.
3. Read the first working key from `.secrets/amazon-affiliate-product-box.serpapi.keys`.
4. Run one precise product query.
5. Build the final Amazon link with `AMAZON_ASSOC_TAG` appended at the end.

## Final URL handling
Keep raw product URLs and affiliate-tagged URLs separate conceptually during work.
Only produce the tagged URL in the final output intended for publication.
