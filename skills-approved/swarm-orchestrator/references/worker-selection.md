# Worker Selection

## Use content-operator for
- content rewrites
- article upgrades
- title/excerpt/FAQ/reference improvements

## Use publisher-operator for
- REST publishing
- page/post field updates
- slug/excerpt/status changes

## Use media-operator for
- media library search
- alt text updates
- YouTube selection
- embed/image placement

## Use research-operator for
- SERP and intent analysis
- source collection
- prioritization
- gap analysis

## Use tech-debugger for
- auth failures
- plugin/cache conflicts
- WooCommerce/payment issues
- automation bugs

## Use verifier for
- live page QA
- path testing
- regression checks
- claim validation

## Spawn pattern

Good:
- one worker per URL batch
- one worker per platform issue
- one worker per verification pass

Bad:
- one worker for an entire company worth of unrelated work
