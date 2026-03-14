# skills-approved

Production-curated OpenClaw skill set (v3). Only these skills are active for routing.

## All 36 Skills

### Content & Copy
| Skill | Role | Lines |
|-------|------|-------|
| conversion-copywriting | Conversion copy for landing pages, homepages, CTAs | 109 |
| editorial-post-enhancement | Enhance articles with SEO, links, media | 428 |
| copy-editing-sweeps | Line-by-line copy editing | 89 |
| content-strategy-planning | Topic clusters, cannibalization, content planning | 118 |
| technical-writing | Docs, READMEs, guides, SOPs | 123 |

### SEO
| Skill | Role | Lines |
|-------|------|-------|
| seo-audit-playbook | Full SEO audit (crawlability, technical, on-page, keywords) | 586 |
| seo-command-center | Multi-skill SEO orchestration | 85 |
| schema-ops | Structured data (Article, FAQPage, Product, LocalBusiness) | 73 |
| programmatic-seo-blueprints | Scalable pSEO page templates | 735 |

### Email Marketing
| Skill | Role | Lines |
|-------|------|-------|
| email-marketing-engine | Brevo/email platform setup, lists, sender | 121 |
| email-automation-debugging | Debug broken email funnels, sequences, triggers | 97 |
| lifecycle-email-sequences | Welcome, nurture, onboarding, re-engagement sequences | 104 |
| lead-magnet-delivery-ops | Lead capture → asset delivery flow | 84 |

### Site & WordPress
| Skill | Role | Lines |
|-------|------|-------|
| wordpress-growth-ops | WordPress site improvements (copy, funnels, plugins) | 112 |
| revenue-site-execution | Revenue-path work on managed portfolio sites | 111 |
| offer-positioning | Clarify, strengthen, reframe offers | 98 |
| service-funnel-architecture | Service funnels (homepage → CTA → booking) | 92 |

### Operations & Infrastructure
| Skill | Role | Lines |
|-------|------|-------|
| infrastructure-ops | Server/DevOps, nginx, SSL, cron | 45 |
| monitoring-ops | Uptime, logs, performance monitoring | 75 |
| notification-engine | Alert routing (Telegram, email, webhooks) | 82 |

### Analytics & Measurement
| Skill | Role | Lines |
|-------|------|-------|
| analytics-reporting | KPI dashboards, performance reports | 114 |
| tracking-measurement | GA4, GTM, pixels, conversion tracking | 113 |
| paid-media-audit | Google/Meta Ads audit, wasted spend analysis | 106 |

### Testing & Quality
| Skill | Role | Lines |
|-------|------|-------|
| test-automation-ops | Site testing (SEO, health, integration) | 89 |
| experiment-tracking | A/B tests, CRO experiments | 97 |
| launch-readiness-audit | Pre-launch checklist and gate | 101 |
| money-path-verification | End-to-end checkout/funnel verification | 75 |

### Tooling & Integration
| Skill | Role | Lines |
|-------|------|-------|
| api-integration-builder | REST/GraphQL API integrations | 88 |
| tool-evaluation | Compare software, vendors, platforms | 103 |

### Orchestration & System
| Skill | Role | Lines |
|-------|------|-------|
| swarm-orchestrator | Director/worker/verifier multi-agent patterns | 102 |
| skill-router | Master task → skill routing guide | 143 |
| skill-authoring-standard | Create/edit enterprise-grade skills | 135 |
| memory-operations | Organize memory files, entity memory | 103 |

### Workflow & Automation
| Skill | Role | Lines |
|-------|------|-------|
| workflow-macros | 5 pre-built multi-skill pipelines with verification gates | 137 |
| quality-scorecard | Skill quality scoring (0-100) on 5 dimensions | 59 |
| auto-verification | Auto-verify completion claims with proof | 68 |

## Quality Standards (v3)
Every skill MUST have:
- ✅ `## Do NOT Use This For` boundary section
- ✅ `## Output Contract` section
- Recommended: `scripts/` and `references/` directories
- Recommended: Cross-references (→) to related skills

## Rules
- Only skills listed in MANIFEST.yaml are production-active
- Every skill must have a SKILL.md with frontmatter
- No secrets in any skill file
- Run `make validate` before releasing
- Archive before deleting any skill

## Adding a new skill
1. Add skill folder here with SKILL.md (must meet quality standards)
2. Add entry to MANIFEST.yaml
3. Run `make validate`
4. Commit and push

## Removing a skill
1. Move to skills-archive/ first
2. Remove from MANIFEST.yaml
3. Run `make validate`
4. Commit and push
