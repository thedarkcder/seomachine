---
name: sales-approval-queue
description: "Use this Codex sales skill to prepare AI SDR outreach for human review, including approval status, risk flags, missing data, personalization confidence, and launch readiness."
---

# Approval Queue

Use this skill whenever outbound drafts, cadences, or prospect batches should be reviewed before execution.

## Workflow

1. Compile each outbound item:
   - account
   - contact
   - score
   - sequence or message
   - personalization hooks
   - source evidence
   - verification status
   - compliance flags

2. Classify status:
   - approved: ready for execution by a configured tool or user
   - needs edit: copy, personalization, or CTA issue
   - needs data: missing contact, verification, or source
   - blocked: suppression, invalid email, compliance risk, poor fit

3. Review checks:
   - no unsupported factual claims
   - no private or creepy intent references
   - no invalid/suppressed contacts
   - clear opt-out or compliance handling where required
   - value prop matches segment and persona

4. Handoff:
   - approved items can move to execution tooling when the user explicitly approves
   - blocked items go to enrichment, verification, hygiene, or research

## Output

Create an approval table:

| account | contact | asset | status | risk flags | required fix | owner |
|---|---|---|---|---|---|---|

Do not send outreach or mutate CRM records from this skill.
