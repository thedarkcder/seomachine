---
name: revops-lifecycle-stages
description: "Use this Codex RevOps skill to define lifecycle stages, funnel stages, ownership, entry criteria, exit criteria, disqualification reasons, and sales/marketing/customer handoff points."
---

# Lifecycle Stages

Use this skill when the team needs shared definitions for leads, accounts, opportunities, customers, renewals, or expansion.

## Workflow

1. Identify the business motion:
   - inbound-led
   - outbound-led
   - product-led
   - sales-led enterprise
   - agency/services
   - hybrid

2. Define lifecycle stages:
   - Subscriber or visitor
   - Lead
   - Marketing Qualified Lead
   - Sales Accepted Lead
   - Sales Qualified Lead
   - Opportunity
   - Closed Won
   - Customer
   - Expansion or renewal opportunity
   - Closed Lost or disqualified

3. For each stage, define:
   - entry criteria
   - exit criteria
   - owner
   - required fields
   - allowed next stages
   - disqualification reasons
   - SLA or follow-up requirement

4. Check for ambiguity:
   - MQL should not mean "any form fill"
   - SQL should require sales-validated fit or intent
   - Opportunity should require a real deal motion, not just interest
   - Closed lost and disqualified should have reason codes

## Output

Create a lifecycle stage table:

| stage | definition | entry criteria | exit criteria | owner | required fields | next stage |
|---|---|---|---|---|---|---|

Add a short section for disqualification reasons and recycling rules.
