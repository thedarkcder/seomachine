---
name: sales-verify-emails
description: "Use this Codex sales skill for email verification workflow design. Classifies email risk, bounce risk, catch-all domains, suppression rules, and send readiness before outbound cadences."
---

# Email Verification

Use this skill before any outbound sequence is considered send-ready.

## Verification Statuses

- `verified`: safe to use, low bounce risk
- `risky`: deliverable uncertain, catch-all, role-based, or stale
- `unknown`: no verification result
- `invalid`: do not send
- `suppressed`: do not contact because of opt-out, customer status, legal hold, or internal rule

## Workflow

1. Normalize email fields:
   - lowercase addresses
   - remove obvious malformed records
   - dedupe by email
   - separate personal and business emails

2. Classify risk:
   - syntax invalid
   - disposable domain
   - role address such as `info@` or `sales@`
   - catch-all domain
   - stale verification date
   - prior bounce or unsubscribe

3. Define send rules:
   - send only to `verified` for cold outbound at scale
   - allow `risky` only for high-value manual outreach
   - never send to `invalid` or `suppressed`
   - reverify lists older than 90 days

4. Handoff:
   - clean records go to `sales-lead-score` or `sales-build-cadence`
   - risky records go back to `sales-enrich-contacts`
   - suppression conflicts go to `sales-data-hygiene`

## Output

Produce a verification summary:

- total records
- verified count and percentage
- risky count and reason breakdown
- invalid/suppressed count
- recommended sendable audience
- cleanup actions before launch
