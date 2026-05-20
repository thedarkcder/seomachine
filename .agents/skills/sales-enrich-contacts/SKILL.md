---
name: sales-enrich-contacts
description: "Use this Codex sales skill for contact and company enrichment planning. Defines which decision makers to find, required fields, enrichment waterfall, confidence scoring, and enrichment handoff before verification or outreach."
---

# Contact Enrichment

Use this skill after target accounts are identified and before outreach copy is written.

## Required Fields

For each contact, try to collect or request:

- full name
- title
- department/function
- seniority
- company
- domain
- LinkedIn/profile URL if available
- email
- phone if needed
- location/time zone
- source and last verified date

## Workflow

1. Define personas:
   - economic buyer
   - champion
   - technical evaluator
   - blocker or compliance stakeholder
   - day-to-day user

2. Build enrichment rules:
   - enrich only accounts that meet minimum fit score
   - dedupe contacts before enrichment
   - prioritize email first unless call-heavy motion is specified
   - use waterfall logic conceptually: primary source, fallback source, manual research fallback

3. Score contact confidence:
   - High: title, company, and contact details are current and sourced
   - Medium: contact looks right but data is incomplete or stale
   - Low: inferred contact or unverifiable details

4. Prepare verification:
   - route emails to `sales-verify-emails`
   - route unclear buying committees to `sales-buying-committee`
   - route enriched records to `sales-lead-score`

## Output

Create a contact enrichment table:

| account | contact | title | role in buying committee | email status | confidence | source | next action |
|---|---|---|---|---|---|---|---|

Do not claim an email is valid unless it has been verified by a suitable source or the user provided it as verified.
