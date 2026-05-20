---
name: sales-crm-fields
description: "Use this Codex sales skill to define the canonical CRM/source-of-truth fields needed for AI SDR workflows, including accounts, contacts, scores, sequence status, consent, suppression, and handoff metadata."
---

# CRM Field Schema

Use this skill when the user needs a clean data model for AI SDR workflows, CSV imports, CRM sync, or MCP/API execution later.

## Canonical Objects

Account fields:

- account_name
- domain
- industry
- employee_count
- revenue_range
- geography
- account_tier
- account_fit_score
- intent_score
- source
- owner
- lifecycle_status
- suppression_status

Contact fields:

- first_name
- last_name
- full_name
- title
- seniority
- department
- buying_committee_role
- email
- email_verification_status
- phone
- linkedin_url
- contact_fit_score
- personalization_hook
- consent_basis
- do_not_contact

Campaign fields:

- campaign_name
- segment
- cadence_name
- cadence_step
- approval_status
- last_touch_date
- reply_status
- next_action
- notes

## Workflow

1. Choose required fields for the user's current flow.
2. Define allowed values for statuses and roles.
3. Map existing fields to canonical names.
4. Identify missing fields that block enrichment, scoring, approval, or execution.
5. Produce an import-ready schema if requested.

## Output

Create a field map:

| object | canonical field | required | allowed values | source field | notes |
|---|---|---|---|---|---|

Prefer stable, lowercase snake_case field names when designing new CSV or database schemas.
