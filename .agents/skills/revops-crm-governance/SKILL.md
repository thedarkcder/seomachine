---
name: revops-crm-governance
description: "Use this Codex RevOps skill to define CRM governance, required fields, ownership rules, automation controls, permission principles, data quality checks, and change management."
---

# CRM Governance

Use this skill when the CRM needs rules that prevent messy data, broken automation, inconsistent reporting, or unclear ownership.

## Workflow

1. Define governance scope:
   - objects: leads, contacts, accounts, opportunities, campaigns, activities
   - users: marketing, SDR, AE, CS, ops, leadership
   - systems: CRM, marketing automation, sales engagement, support, product analytics

2. Define field governance:
   - required fields by lifecycle stage
   - allowed values
   - source of truth
   - who can edit
   - automation-owned fields
   - audit fields

3. Define ownership rules:
   - account owner
   - contact owner
   - opportunity owner
   - campaign owner
   - queue owner
   - escalation owner

4. Define automation governance:
   - naming conventions
   - owner
   - purpose
   - trigger
   - affected fields
   - rollback plan
   - testing requirement

5. Define data quality controls:
   - duplicate checks
   - required field completeness
   - stale record review
   - suppression protection
   - source attribution checks
   - monthly governance review

6. For HubSpot-only workflows, create approved custom properties with the repo script:
   - use `scripts/create_hubspot_revops_properties.py` from the repo root
   - require `HUBSPOT_PRIVATE_APP_TOKEN` or `HUBSPOT_API_KEY` in `.env`
   - run `python3 scripts/create_hubspot_revops_properties.py` first as a dry run
   - show the planned property changes to the user
   - after explicit approval, run `python3 scripts/create_hubspot_revops_properties.py --apply`
   - record which properties already existed and which were created

The script is for the minimal HubSpot-only AI SDR/RevOps property set. Do not create additional custom properties unless the workflow has made them repeatable and worth governing.

## Output

Create a CRM governance plan:

| area | rule | owner | enforcement | review cadence |
|---|---|---|---|---|

Include a change-control checklist for new fields, workflows, lists, and dashboard changes.

When HubSpot custom properties are needed, include the script dry-run summary and the approval status before applying changes.
