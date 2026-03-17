# 🚨 Disaster Recovery Guide

## Quick Start (New Machine — 5 Minutes)

### Step 1: Install OpenClaw
```bash
npm install -g openclaw
openclaw configure
```

### Step 2: Clone This Repo
```bash
git clone https://github.com/douphealth/openclaw-config-001.git ~/.openclaw/workspace-temp
cd ~/.openclaw/workspace-temp
```

### Step 3: Run Restore Script
```bash
chmod +x scripts/disaster-recovery.sh
./disaster-recovery.sh restore backups/openclaw-disaster-recovery-*.tar.gz
```

### Step 4: Restore Secrets
Create these files in `~/.openclaw/workspace/.secrets/`:

**GSC Service Account** — `gsc-service-account.json`
(Get from Google Cloud Console → Service Accounts → Keys)

**Bing API Key** — `bing-api-key.txt`
(Get from Bing Webmaster Tools → Settings → API Access)

**WordPress Sites** — `{domain}.access.env`
```
WP_USERNAME=your_username
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx
```

Sites to configure:
- affiliatemarketingforsuccess.com
- efficientgptprompts.com
- frenchyfab.com
- gearuptofit.com
- gearuptogrow.com
- micegoneguide.com
- mysticaldigits.com
- plantastichaven.com

### Step 5: Install Dependencies
```bash
pip install google-api-python-client google-auth requests
```

### Step 6: Verify
```bash
openclaw status
python3 skills/seo/scripts/gsc-bing-intel.py --gsc --site https://plantastichaven.com --days 7
```

## What's Included in This Repo
- **47 enterprise skills** with /25 scorecards
- **SEO Intelligence** — GSC + Bing API integration
- **WordPress Mastery** — REST API, error recovery, performance
- **Content Enhancement** — Hormozi/Ferriss style, 8-phase system
- **Keyword Research** — Autocomplete, GSC mining, prioritization
- **AI Visibility** — GEO + AEO optimization
- **Self-Improvement** — Quality monitoring, performance patterns

## Scripts
- `scripts/disaster-recovery.sh` — Backup/restore tool
- `scripts/seo/gsc-bing-intel.py` — GSC + Bing data puller
- `scripts/seo/site-seo-audit.py` — Site-wide SEO audit
- `scripts/seo/keyword-research.py` — Keyword discovery pipeline
- `scripts/self-improvement/quality-monitor.py` — Skill quality tracking

## Support
- Repo: https://github.com/douphealth/openclaw-config-001
- OpenClaw docs: https://docs.openclaw.ai
- Community: https://discord.com/invite/clawd
