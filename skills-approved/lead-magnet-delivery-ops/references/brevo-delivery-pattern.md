# Brevo API Delivery Pattern

For immediate asset delivery after form submission.

## When to use
When the lead magnet should be delivered via email immediately after signup, bypassing CRM mailer limitations.

## Implementation

### 1. Form submission creates contact
Use the CRM's form/API to create the contact record. Don't try to bypass this.

### 2. Fast lane sends delivery email
A separate process (cron or webhook) detects new signups and sends the delivery email via Brevo API:

```python
import json
from urllib.request import Request, urlopen

def send_delivery_email(to_email, first_name, asset_url, api_key):
    payload = {
        'sender': {'email': 'info@yoursite.com', 'name': 'Your Brand'},
        'to': [{'email': to_email}],
        'subject': 'Your download is ready',
        'htmlContent': f'''
            <p>Hey {first_name},</p>
            <p>Here's your download: <a href="{asset_url}">Download Now</a></p>
            <p>— Your Brand</p>
        ''',
    }
    # Only add name if non-empty (Brevo returns 400 for empty name)
    if first_name:
        payload['to'][0]['name'] = first_name

    data = json.dumps(payload).encode()
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }
    req = Request('https://api.brevo.com/v3/smtp/email', data=data, headers=headers, method='POST')
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())
```

### 3. Verify delivery
Check email history via CRM API to confirm the email was created with correct content and delivery status.

## Critical checks
- Asset URL must return 200
- Sender domain must be verified in Brevo
- DKIM/SPF/DMARC must be configured
- Test with a real email before going live
