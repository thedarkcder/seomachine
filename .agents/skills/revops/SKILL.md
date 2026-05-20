---
name: revops
description: "Route revenue operations workflow requests in Codex, including lifecycle stages, campaign tracking, SLA handoffs, dashboard design, and CRM governance for sales and marketing teams."
---

# RevOps Namespace Router

Use this skill as the entry point for revenue operations workflows. RevOps skills define the operating system around sales and marketing work: stages, ownership, reporting, governance, and handoffs.

## Namespace Rules

- Use `revops-*` for revenue operations design and governance.
- Use `sales-*` for AI SDR prospecting, enrichment, outreach, and deal support.
- Use marketing skills for campaign copy, CRO, paid ads, social, and content strategy.
- RevOps outputs should be decision-ready operating plans, field definitions, dashboards, or checklists.
- Do not mutate CRM records, automations, dashboards, or campaign settings without explicit user approval and an available tool.
- For HubSpot custom property creation, route to `$revops-crm-governance`; that skill uses `scripts/create_hubspot_revops_properties.py` after a dry run and explicit approval.

## Command Reference

| Command | Description | Output |
|---|---|---|
| `$revops-lifecycle-stages` | Define funnel/lifecycle stages and exit criteria | LIFECYCLE-STAGES.md |
| `$revops-campaign-tracking` | Define campaign source, UTM, and naming rules | CAMPAIGN-TRACKING.md |
| `$revops-sla-handoff` | Design handoffs between marketing, SDR, AE, and CS | SLA-HANDOFF.md |
| `$revops-dashboard-design` | Design revenue dashboards and KPI views | DASHBOARD-DESIGN.md |
| `$revops-crm-governance` | Define CRM rules, required fields, automation ownership, and data quality controls | CRM-GOVERNANCE.md |

## Routing Logic

For broad RevOps requests, route in this order:

1. `revops-lifecycle-stages` - define the funnel language first.
2. `revops-campaign-tracking` - make sources and campaign reporting measurable.
3. `revops-sla-handoff` - decide who owns each stage transition and response.
4. `revops-dashboard-design` - turn the operating model into management visibility.
5. `revops-crm-governance` - protect the system from data and automation drift.

For AI SDR-specific data fields, scoring, routing, or replies, use the existing `sales-crm-fields`, `sales-lead-score`, `sales-lead-routing`, and `sales-reply-classification` skills.
