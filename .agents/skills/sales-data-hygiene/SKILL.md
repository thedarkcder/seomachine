---
name: sales-data-hygiene
description: "Use this Codex sales skill for AI SDR data quality work, including deduplication, normalization, stale data detection, suppression handling, enrichment safety, and CRM/list cleanup."
---

# Sales Data Hygiene

Use this skill before enrichment, scoring, routing, or campaign launch when data quality is uncertain.

## Workflow

1. Audit data quality:
   - duplicate accounts or contacts
   - missing required fields
   - stale titles, companies, or emails
   - inconsistent company names, industries, countries, and phone formats
   - invalid or risky email statuses
   - missing suppression or consent data

2. Deduplicate:
   - exact email match for contacts
   - domain match for accounts
   - fuzzy company-name match only with manual review
   - preserve source and history fields

3. Normalize:
   - lowercase domains and emails
   - standardize country/region names
   - normalize seniority and department values
   - split full names only when confidence is high

4. Protect compliance:
   - never re-add unsubscribed contacts
   - keep suppression fields through merges
   - flag contacts needing consent review
   - archive stale records rather than deleting by default

5. Handoff:
   - clean records to `sales-enrich-contacts`
   - verified records to `sales-lead-score`
   - schema issues to `sales-crm-fields`

## Output

Create a data hygiene report:

- data quality score
- duplicate count
- required-field completeness
- suppression risks
- recommended cleanup order
- records safe to enrich or score
