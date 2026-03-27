# TOOLS.md - Local Notes

Skills define how tools work. This file is for setup-specific operational notes.

## OpenClaw

- **Workspace:** `C:\Users\User\.openclaw\workspace`
- **Config:** `C:\Users\User\.openclaw\openclaw.json`
- **Skills root:** `C:\Users\User\.openclaw\workspace\skills`
- **Secrets dir:** `C:\Users\User\.openclaw\workspace\.secrets`
- **Gateway:** local scheduled task / local gateway install
- **Primary model:** `openai-codex/gpt-5.4`
- **Fallbacks:** `ollama/minimax-m2.1:cloud`

## Secrets / Sensitive Material

- Keep API keys and credentials in `.secrets/`, not in memory or docs.
- OpenClaw runtime secrets are now intended to live in `C:\Users\User\.openclaw\.env` and be referenced from config via `${ENV_VAR}` substitution.
- `openclaw.json` should stay reference-based for secrets wherever supported, not plaintext.
- Do not paste gateway tokens, bot tokens, app passwords, or provider keys into chats.
- Prefer redacted-by-default documentation.

## Models / Providers

- **OpenAI Codex:** OAuth
- **OpenAI:** provider configured
- **Ollama:** local fallback endpoint configured at `http://127.0.0.1:11434/v1`

## Channels

### Telegram
- configured and paired
- dedicated bot token expected per OpenClaw instance
- pairing code is **not** the bot token
- rotate exposed bot tokens in BotFather immediately if leaked

### WhatsApp
- logs previously showed stale-socket restarts and reconnection churn
- if delivery seems flaky, inspect provider health before blaming the model layer

## Infrastructure Notes

### Workspace / Runtime
- Repo reference for imported curated skills: `workspace/repo_openclaw_config_001/`
- Prefer managed edits in workspace skills over editing bundled skills
- Treat repo reference as baseline and workspace as the active operating copy

### Services / Recovery
- If gateway health degrades, check scheduled task / local gateway install first
- Verify actual running processes, not just CLI success text
- If install/update fails with `EPERM` or `EBUSY`, suspect file locks or another live node/npm process
- For persistent lock issues, restart the machine before deeper surgery

## WordPress Access

- WordPress credentials stored in `.secrets/wordpress-sites.json`
- File includes wp-admin credentials and REST API credentials where provided
- Use that file when admin or REST access is needed for:
  - Affiliatemarketingforsuccess.com
  - Mysticaldigits.com
  - Gearuptogrow.com
  - FrenchyFab.com
  - Plantastichaven.com
  - Gearuptofit.com
  - Micegoneguide.com
  - EfficientGPTPrompts.com
  - Outdoormisting.com

## Ops Patterns / Verification Traps

- Check real runtime state after any restart attempt: process list, logs, health endpoint, or message flow
- "Command said restarted" is not proof
- Prefer fewer, higher-value writes over noisy one-item loops when using external APIs
- After important edits, verify the result and update memory/docs if it matters later
- For visual/UI/page styling work, use the local browser helper at `ops/browser-visual/browser_ops.js` and the `browser-visual-ops` skill for desktop/mobile screenshots before claiming success
- Current browser helper defaults are tuned for this environment: `domcontentloaded` + `load` + settle delay, animations disabled, viewport screenshots by default, full-page only when explicitly needed
- For mobile breakage, use `node ops/browser-visual/browser_ops.js overflow --url <url> --device mobile` to identify likely overflowing elements before patching CSS blindly
- Use `ops/browser-visual/capture_pair.sh` for fast baseline/proof capture and `ops/browser-visual/diagnose_mobile.sh` for overflow + mobile screenshot in one step
- For meaningful page/post changes, follow `skills/shared/page-operations-standard.md`
- Daily backup workflow reference: `ops/backups/README.md`

## TODO / Local Reference

- Add device names, SSH hosts, voice prefs, cron inventory, and any stable infra notes here
- Rotate previously exposed provider/channel/gateway tokens as a follow-up hardening step
