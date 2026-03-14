# Operational Traps

Common traps in WordPress growth work:
- admin/API updates succeed but front-end path still fails
- plugin UI suggests a setting is active but live behavior differs
- cached or rendered layers hide the real issue
- AJAX / nonce / JS submit behavior differs from plain form POST assumptions
- product description HTML breaks Woo rendering or trust

Always verify on the real user path after meaningful changes.
