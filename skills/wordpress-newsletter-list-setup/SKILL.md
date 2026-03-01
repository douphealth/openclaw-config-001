---
name: wordpress-newsletter-list-setup
description: Configure WordPress-native newsletter list infrastructure with segmentation, double opt-in, consent logging, and hygiene automation. Use when building or repairing email list growth foundations.
---

# WordPress Newsletter List Setup

## Scope Ownership
### Own
- Execute Configure WordPress-native newsletter list infrastructure with segmentation, double opt-in, consent logging, and hygiene automation. Use when building or repairing email list growth foundations.
- Apply workflows, gates, and outputs defined in this file and its references/scripts.

### Do Not Own
- Do not override responsibilities of more specific domain skills when one clearly matches.
- Do not claim completion for adjacent systems without their direct verification gates.

## Objective
Build a clean, segmented, permission-based list ready for automation.

## Recommended stack
- CRM: FluentCRM or MailPoet
- Forms: Fluent Forms or WPForms
- Optional: WooCommerce/EDD behavior signals

## Mandatory steps
1. create lists/tags by source, intent, lifecycle
2. enable double opt-in
3. add consent checkbox + privacy link + consent logging
4. deploy high-intent capture placements
5. configure lead-magnet delivery automation
6. separate transactional and marketing streams
7. enable hygiene rules (bounces + unengaged suppression)

## Quality gates
- no purchased/cold imports
- consent/unsubscribe compliance verified
- segmentation rules tested
- suppression and bounce logic active

## Output
- list/tag schema
- placement map
- compliance verification
- hygiene configuration