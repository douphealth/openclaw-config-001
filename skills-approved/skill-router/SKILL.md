---
name: skill-router
description: Use FIRST when a workspace task is ambiguous, operational, or could plausibly route to multiple OpenClaw skills. Collapses broad requests to the smallest high-value skill or workflow instead of over-loading many skills up front.
---

# Skill Router

## Purpose
Route ambiguous or multi-domain workspace requests to the smallest correct skill or ordered workflow with minimal token waste and minimal overlap.

## Use this when
- the request could fit multiple skills
- the user asks for a broad operational improvement
- the next skill is not obvious within 10-20 seconds
- the task may collapse to either one skill or one short workflow

## Do NOT use this for
- obvious single-skill requests
- routine direct execution where the target skill is already clear
- loading many skills “just in case”
- replacing real work with endless routing analysis

## Primary scope
This workspace is optimized for:
- OpenClaw configuration and repair
- model/provider/auth troubleshooting
- Telegram and channel operations
- gateway/runtime health work
- infrastructure and automation tasks
- skill authoring and skill cleanup
- verification, testing, and documentation

## Decision sequence
1. **Check for an obvious direct match.** If one skill clearly fits, load that skill and stop routing.
2. **Check for runtime/config changes.** If the task changes runtime, config, auth, gateway, or channel plumbing, start with `infrastructure-ops`.
3. **Check for proof intent.** If the task is mainly “verify”, “working?”, “done?”, “fixed?”, or “prove it”, use `auto-verification`.
4. **Check for orchestration need.** If the task has multiple independent deliverables or benefits from director/worker/verifier structure, use `swarm-orchestrator`.
5. **Check for a known reusable workflow.** If the request clearly matches a repeated multi-step operating pattern, use `workflow-macros`.
6. **If still ambiguous, choose the smaller/more specific skill.** Do not pick the broader skill unless the narrower one clearly fails to cover the request.
7. **Load one skill, not a pile.** Only expand after that skill proves insufficient.

## Route by intent
| User intent | Load this skill |
|---|---|
| Fix OpenClaw config, providers, auth, gateway, channels, automation plumbing | infrastructure-ops |
| Verify a claimed fix, restart, deployment, config change, or integration result | auto-verification |
| Monitor health, alerts, watchdogs, operational drift | monitoring-ops |
| Set up notifications, reminders, alert delivery, routing | notification-engine |
| Build or debug API integrations, webhooks, external service wiring | api-integration-builder |
| Create, audit, restructure, or improve a skill | skill-authoring-standard |
| Maintain memory files, promote notes, clean memory structure | memory-operations |
| Write docs, runbooks, procedures, or polished technical explanations | technical-writing |
| Design tests, regression checks, reproducible validation scripts | test-automation-ops |
| Compare tools, models, providers, or architecture options | tool-evaluation |
| Coordinate multi-step or multi-agent work | swarm-orchestrator |
| Reusable multi-step operating pattern needed | workflow-macros |
| Score or review process quality over time | quality-scorecard |
| Plan content clusters, topic maps, or anti-cannibalization strategy | content-strategy-planning |
| Improve landing-page copy, CTA language, or conversion messaging | conversion-copywriting |
| Edit copy for clarity, grammar, and plain-English sharpness | copy-editing-sweeps |
| Upgrade an article with links, SEO, media, or publish polish | editorial-post-enhancement |
| Configure email platforms, sender setup, or subscriber operations | email-marketing-engine |
| Debug broken email automations, flows, or delivery logic | email-automation-debugging |
| Design welcome, nurture, onboarding, or re-engagement sequences | lifecycle-email-sequences |
| Set up lead capture + asset delivery flow | lead-magnet-delivery-ops |
| Audit analytics, KPI reporting, or performance summaries | analytics-reporting |
| Fix GA4, GTM, pixel, or conversion tracking | tracking-measurement |
| Audit paid media performance or wasted spend | paid-media-audit |
| Run SEO audits, issue triage, or ranking diagnosis | seo-audit-playbook |
| Coordinate broader SEO execution across multiple sub-skills | seo-command-center |
| Add or repair structured data / schema | schema-ops |
| Design scalable programmatic SEO systems | programmatic-seo-blueprints |
| Improve WordPress growth systems, money pages, or plugin-level execution | wordpress-growth-ops |
| Verify conversion or checkout paths end to end | money-path-verification |
| Check launch readiness before going live | launch-readiness-audit |
| Clarify offer messaging and market positioning | offer-positioning |
| Build service funnels and service-page architecture | service-funnel-architecture |
| Execute revenue-path improvements across portfolio sites | revenue-site-execution |
| Measure experiments or structure A/B test readouts | experiment-tracking |

## High-value workflows
- **OpenClaw repair:** infrastructure-ops → auto-verification
- **Channel setup:** infrastructure-ops → auto-verification → notification-engine
- **Provider/model policy:** infrastructure-ops → tool-evaluation → auto-verification
- **New skill or skill cleanup:** skill-authoring-standard → auto-verification
- **Complex multi-step delivery:** swarm-orchestrator → target skill(s) → auto-verification
- **Operational docs after a fix:** technical-writing
- **Content pipeline:** workflow-macros → content-strategy-planning / editorial-post-enhancement / schema-ops / wordpress-growth-ops
- **SEO execution:** seo-command-center or workflow-macros → seo-audit-playbook → schema-ops / editorial-post-enhancement / test-automation-ops
- **Email system work:** workflow-macros → email-marketing-engine / lifecycle-email-sequences / lead-magnet-delivery-ops / tracking-measurement
- **Launch readiness:** workflow-macros → launch-readiness-audit → money-path-verification → tracking-measurement → notification-engine

## Tiebreakers
- If one skill can finish the task cleanly, do **not** choose orchestration.
- If two skills seem plausible, choose the smaller/more specific one.
- If work changes public systems, money paths, or live config, pair execution with `auto-verification`.
- If a request is broad but still clearly in one business domain, route to the domain skill before considering `workflow-macros`.
- If no specialized skill is clearly needed, answer directly without loading a skill.

## Checks and common mistakes
- Do not read multiple skills up front unless the first selected skill explicitly requires expansion.
- Do not route broad requests to the broadest skill by default.
- Do not confuse “big request” with “multi-skill request”.
- Do not use routing as a substitute for execution.
- Do not let a router decision persist when evidence shows a different skill is now clearly right.

## Output contract
**Artifact:** chosen skill or ordered workflow
**Evidence:** short rationale tied to the request
**Decision:** exact next skill to load
**Next:** execute with that skill, then verify if applicable
