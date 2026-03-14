# AFMS Special Case

Use for `affiliatemarketingforsuccess.com`.

## Known reality
- authoritative submit path is Fluent Forms AJAX, not plain form POST
- endpoint: `/wp-admin/admin-ajax.php`
- action: `fluentform_submit`
- form_id: `8`
- hidden values like `source` and `intent` matter
- homepage bot JS may need to create hidden inputs if absent

## Proof standard
Need fresh evidence for:
- AJAX success response with insert id
- contact creation
- deterministic first email path

## Warning
Do not treat manual provider sending or generic plugin connectivity as proof that the welcome automation works.
