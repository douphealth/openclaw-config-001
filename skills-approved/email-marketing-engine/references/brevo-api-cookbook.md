# Brevo API Cookbook

## Send Transactional Email

```
POST https://api.brevo.com/v3/smtp/email
Headers:
  api-key: xkeysib-...
  Content-Type: application/json
  accept: application/json
```

### Payload
```json
{
  "sender": {"email": "info@domain.com", "name": "Brand Name"},
  "to": [{"email": "user@example.com", "name": "User"}],
  "subject": "Subject line",
  "htmlContent": "<html>...</html>",
  "textContent": "Plain text version",
  "headers": {
    "List-Unsubscribe": "<https://domain.com/unsubscribe>",
    "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
  }
}
```

### Critical gotchas
- **Never send `"name": ""`** — Brevo returns 400. Omit the name field if empty.
- **Sender email must be verified** in Brevo → Senders
- **Domain must be authenticated** (DKIM) for inbox delivery
- **Rate limit:** 40 emails/sec on Business plan, 300/day on free

## Get Account Info
```
GET https://api.brevo.com/v3/account
```

## Get Email Events (opens, clicks, bounces)
```
POST https://api.brevo.com/v3/smtp/statistics/events
Body: {"event": "opened", "limit": 500, "days": 1}
```

## Get Aggregated Stats
```
POST https://api.brevo.com/v3/smtp/statistics/aggregatedReport
Body: {"startDate": "2026-03-01T00:00:00Z", "endDate": "2026-03-13T00:00:00Z"}
```

## Error codes
- 400: Bad request (check payload format, especially "name" field)
- 401: Invalid API key
- 402: Account suspended or limit exceeded
- 404: Endpoint not found
- 429: Rate limited (back off and retry)

## Python urllib pattern
```python
from urllib.request import Request, urlopen
from urllib.error import HTTPError

def brevo_send(payload, api_key):
    data = json.dumps(payload).encode()
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json',
        'accept': 'application/json',
    }
    req = Request('https://api.brevo.com/v3/smtp/email', data=data, headers=headers, method='POST')
    try:
        with urlopen(req, timeout=30) as resp:
            return {'success': True, 'data': json.loads(resp.read())}
    except HTTPError as e:
        return {'success': False, 'error': e.code, 'body': e.read().decode()[:500]}
```
