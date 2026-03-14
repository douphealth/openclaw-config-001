# TOOLS.md — Infrastructure Cheat Sheet

_Local notes for YOUR setup. Skills define how tools work. This file is for what's unique to your deployment._

## WordPress Sites

| Site | URL | WP REST API | Auth |
|------|-----|-------------|------|
| _site-name_ | _https://example.com_ | _/wp-json/wp/v2/_ | _App Password (see .secrets/)_ |

## Email Platforms

| Platform | Account | List IDs | Sender IDs | API Key Location |
|----------|---------|----------|------------|------------------|
| _Brevo_ | _email_ | _List: X, Template: Y_ | _Sender: Z_ | `.secrets/brevo-api-key` |
| _Mailchimp_ | _email_ | _Audience: X_ | — | `.secrets/mailchimp-key` |

## Servers & Infrastructure

| Host | IP | SSH Key | Purpose |
|------|----|---------|---------|
| _vps-1_ | _1.2.3.4_ | `~/.ssh/id_vps` | _Main VPS_ |

## APIs & Services

| Service | Purpose | Auth Method | Docs |
|---------|---------|-------------|------|
| _OpenAI_ | _LLM_ | _API Key_ | _https://platform.openai.com/docs_ |
| _Brevo_ | _Email_ | _API Key_ | _https://developers.brevo.com_ |
| _Google Search Console_ | _SEO_ | _OAuth_ | _—_ |

## Cron Jobs

| Schedule | Script | Purpose |
|----------|--------|---------|
| `0 */6 * * *` | `ops/scripts/drip-enroller.py` | Email drip enrollment |
| `0 9 * * 1` | `ops/scripts/weekly-report.py` | Weekly analytics report |

## TTS / Voice

- **Engine**: _ElevenLabs / local TTS_
- **Preferred voice**: _Name (description)_
- **Default speaker**: _Room/device name_

## Cameras / IoT

| Device | Location | Notes |
|--------|----------|-------|
| _camera-1_ | _Living room_ | _180° wide angle_ |

## Swarm Notes

_(Store validated patterns here)_
- Preferred publishing patterns
- Known cache/plugin quirks
- Preferred worker roles for recurring workflows
- Verification traps to remember

---

**Keep secrets in `.secrets/`, not here. This file is for operational reference only.**
