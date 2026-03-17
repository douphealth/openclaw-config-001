---
name: lead-magnet-delivery-ops
description: Use when setting up or fixing a lead magnet delivery flow — opt-in form through asset delivery, thank-you page, and first follow-up. Triggers on requests to launch a lead magnet, fix delivery flow, improve opt-in fulfillment, connect signup to asset delivery, or ensure a promised asset actually arrives in the subscriber's inbox or account.
---

# Lead Magnet Delivery Ops

## Purpose
Ensure every opt-in delivers the promised asset cleanly and moves the lead to the next commercial step. Capture without reliable delivery is wasted traffic.

## Use this when
- launching a new lead magnet and need the full delivery flow designed
- a lead magnet exists but subscribers report not receiving the asset
- the thank-you page is a dead end instead of a commercial bridge
- delivery method needs to change (e.g., email → instant download page)
- auditing why a lead magnet converts but produces no downstream revenue

## Do NOT use this for
- creating the lead magnet content itself (use `conversion-copywriting`)
- designing email nurture or drip sequences after delivery (use `lifecycle-email-sequences`)
- diagnosing why an existing email automation is broken (use `email-automation-debugging`)

## Do this

### 1. Define the promise and trigger
- State exactly what the subscriber gets (file name, format, access type).
- Identify the trigger event: form submission, tag applied, list subscription, webhook.
- Confirm the trigger fires reliably in the current tooling.

### 2. Map the delivery flow end-to-end
Map each step: `form submit → trigger → delivery action → thank-you/redirect → first follow-up`.
Choose delivery method:
- **Instant page delivery**: asset link on thank-you page. Fastest, no email dependency.
- **Email delivery**: asset link in confirmation email. Requires working sender, inbox placement.
- **Account/app access**: gated behind login. Adds friction, use only when ongoing access matters.
- **Hybrid**: page link + email copy for redundancy. Best reliability.

### 3. Verify every link and permission
- Test the asset link from a fresh browser (no cached sessions).
- Confirm file permissions allow public access (Google Drive, S3, etc.).
- Check sender domain SPF/DKIM if email delivery is used.
- Verify the thank-you page loads correctly on mobile.

### 4. Confirm the contact record
- Submit a test with a fresh email.
- Confirm the subscriber record is created in the CRM/email platform.
- Confirm tags, segments, or custom fields are applied correctly.
- Confirm no duplicate records are created on re-submission.

### 5. Build the next step
The thank-you page and first follow-up should advance the relationship:
- Offer a low-friction next CTA (book a call, read a guide, start a trial).
- Do not leave the page as a dead "thanks, you're done."
- First automated email (if any) should reinforce the asset value and introduce the next step.

### Example: PDF lead magnet on WordPress + ConvertKit

**Before (broken flow):**
- Form: ConvertKit embed on /free-guide page
- Thank-you: generic WordPress confirmation, no asset link
- Delivery: ConvertKit sequence email → goes to spam (no custom domain)
- Result: Subscribers added to list, but most never get the PDF

**After (working flow):**
- Form: same ConvertKit embed
- Thank-you: custom page at /free-guide/thank-you with direct PDF download link (hosted on site, no auth wall)
- Delivery: immediate page delivery (no email dependency for primary delivery)
- Follow-up: ConvertKit email sent 1 hour later with PDF re-link + soft CTA to book a call
- Verification: test submission from Gmail + Outlook → PDF downloaded from thank-you page, follow-up email received in inbox (not spam)

**Proof checklist:**
- [ ] Fresh email submission creates contact in ConvertKit
- [ ] Thank-you page displays PDF download link
- [ ] PDF downloads successfully in incognito browser
- [ ] Follow-up email arrives in primary inbox within 2 hours
- [ ] Contact tagged as "guide-downloaded"
- [ ] Thank-you page includes secondary CTA (book call)

## Resources
- `references/delivery-flow-checklist.md` — end-to-end testing checklist

## Checks and common mistakes
- Do not count form submission as successful fulfillment — the asset must actually arrive.
- Do not hide the asset behind an email that lands in spam — test inbox placement before launch.
- Do not leave the thank-you page commercially empty — it is the highest-intent moment.
- Do not ship without testing with at least one fresh email on Gmail and one on Outlook.
- Do not treat delivery and monetization as separate systems — the thank-you page and first follow-up are conversion surfaces.
- Do not use file hosts that require login (Google Drive "request access") for public lead magnets.

## Output Contract
**Artifact**: Complete lead magnet delivery flow documented and tested
**Evidence**:
- Test submission from a fresh email address (2+ providers) that: (1) creates a contact record with correct tags, (2) delivers the asset within 60 seconds (page) or within 2 hours (email, in inbox not spam), (3) displays a thank-you page with working asset link and secondary CTA
- Flow diagram or step list: form → trigger → delivery → thank-you → next CTA
- Asset link verified in incognito/private browser
**Decision**: Flow approved and live, or flagged for specific fixes
**Next**: Monitor opt-in-to-delivery completion rate and downstream conversion (delivery → next CTA click)
