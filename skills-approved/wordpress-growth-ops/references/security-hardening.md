# WordPress Security Hardening

## REST API Security

### Disable Public REST API Access
```php
// In functions.php or mu-plugin
// Remove anonymous access to REST API
add_filter('rest_authentication_errors', function($result) {
    if (!empty($result)) return $result;
    if (!is_user_logged_in()) {
        return new WP_Error('rest_forbidden', 'REST API requires authentication', array('status' => 401));
    }
    return $result;
});
```

### Restrict REST API by IP
```php
add_filter('rest_authentication_errors', function($result) {
    if (!is_user_logged_in()) {
        $allowed_ips = ['YOUR.IP.HERE'];
        if (!in_array($_SERVER['REMOTE_ADDR'], $allowed_ips)) {
            return new WP_Error('rest_forbidden', 'IP not allowed', array('status' => 403));
        }
    }
    return $result;
});
```

### Disable XML-RPC (If Not Needed)
```php
add_filter('xmlrpc_enabled', '__return_false');
// Or via .htaccess:
// <Files xmlrpc.php>
//   Require all denied
// </Files>
```

## Authentication Hardening

### Application Passwords
- Use for REST API only (not dashboard login)
- Rotate regularly (delete old, create new)
- Use descriptive names (e.g., "OpenClaw Agent - Production")
- Store in `.secrets/` directory, never in code

### Password Best Practices
- Minimum 12 characters
- Mix of upper/lower/numbers/special
- Use WordPress password generator
- Enable 2FA for admin accounts

## File Security

### wp-config.php Hardening
```php
define('DISALLOW_FILE_EDIT', true);  // Disable theme/plugin editor
define('DISALLOW_FILE_MODS', true);  // Disable plugin/theme installation
define('FORCE_SSL_ADMIN', true);     // Force HTTPS for admin
define('WP_AUTO_UPDATE_CORE', 'minor'); // Auto-update minor only
```

### Directory Permissions
```
wp-config.php: 440 or 400
wp-content/: 755
wp-content/uploads/: 755
wp-content/plugins/: 755
wp-content/themes/: 755
.htaccess: 444
```

### Block Direct PHP Execution in Uploads
```apache
# In .htaccess
<FilesMatch "\.php$">
    <If "%{REQUEST_URI} =~ m#/wp-content/uploads/#">
        Require all denied
    </If>
</FilesMatch>
```

## Database Security

### Change Default Table Prefix
```php
// In wp-config.php
$table_prefix = 'wp_x9k2_';  // Not just 'wp_'
```

### Disable Database User Privileges
```sql
-- Application user should only have:
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, INDEX
ON database_name.* TO 'wp_user'@'localhost';
-- Do NOT grant: GRANT, ALTER ROUTINE, CREATE ROUTINE, FILE, PROCESS
```

## Plugin/Theme Security

### Audit Installed Plugins
```bash
# Check for known vulnerabilities
wp plugin list --field=name | xargs -I{} wp plugin status {}

# Remove inactive plugins (they're still attack surface)
wp plugin list --status=inactive --field=name | xargs wp plugin deactivate
```

### Remove Unused Themes
```bash
wp theme list --status=inactive --field=name | xargs wp theme delete
```

## Cloudflare Security

### Recommended Firewall Rules
1. Block known bad IPs/Botnets
2. Rate limit `/wp-admin/` and `/wp-login.php`
3. Enable Bot Fight Mode
4. Challenge suspicious countries (if traffic is geo-specific)

### Security Headers via Cloudflare
```
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
Content-Security-Policy: (configure per-site)
```

## Security Audit Checklist
- [ ] REST API requires authentication for write operations
- [ ] XML-RPC disabled
- [ ] Application passwords rotated (< 90 days)
- [ ] File editor disabled (`DISALLOW_FILE_EDIT`)
- [ ] Non-admin users have minimal capabilities
- [ ] Unused plugins/themes removed
- [ ] Uploads directory blocks PHP execution
- [ ] Cloudflare security headers enabled
- [ ] Debug mode disabled in production (`WP_DEBUG = false`)
- [ ] File permissions set correctly
