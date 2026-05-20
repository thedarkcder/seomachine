---
name: sales-deliverability
description: "Use this Codex sales skill for outbound email deliverability readiness, including domain authentication, mailbox warmup, list hygiene, bounce risk, volume limits, and spam-risk copy review."
---

# Deliverability Readiness

Use this skill before a campaign is launched or when email performance suggests spam, bounce, or reputation issues.

## Workflow

1. Check infrastructure assumptions:
   - dedicated outbound domain or subdomain
   - SPF configured
   - DKIM configured
   - DMARC configured
   - custom tracking domain if tracking is used
   - mailbox age and warmup status

2. Check list quality:
   - verified email percentage
   - risky/catch-all percentage
   - prior bounce or unsubscribe suppression
   - list age
   - role-based emails removed

3. Check sending plan:
   - daily volume per mailbox
   - ramp schedule
   - mailbox rotation
   - target regions and compliance constraints
   - unsubscribe handling

4. Check message risk:
   - spammy claims or formatting
   - deceptive subject lines
   - excessive links or tracking
   - attachments in cold outreach
   - weak relevance causing complaint risk

## Output

Create a deliverability launch checklist:

- infrastructure status
- list hygiene status
- copy risk status
- volume recommendation
- launch decision: ready, ready with cautions, or hold

Default to conservative recommendations when bounce risk or domain health is unclear.
