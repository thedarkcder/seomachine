---
name: sales-build-cadence
description: "Use this Codex sales skill to design AI SDR outbound cadences with email, LinkedIn, phone, timing, A/B tests, personalization tokens, and send-readiness checks."
---

# Build Outbound Cadence

Use this skill when the user needs a complete multi-touch outbound sequence, not just a single email.

## Inputs

- target segment or persona
- campaign goal
- value proposition
- available channels
- desired duration
- personalization fields
- deliverability and compliance constraints

## Workflow

1. Select cadence type:
   - cold outbound
   - signal-triggered
   - event follow-up
   - re-engagement
   - expansion into existing account

2. Design the sequence:
   - 6-12 touches for most cold outbound
   - 14-30 day duration depending on persona and urgency
   - avoid three same-channel touches in a row
   - put call tasks soon after strong emails where phone is available
   - include a clear breakup or close-the-loop touch

3. Write each step:
   - email subject A/B variants
   - email body under 125 words for cold outreach
   - LinkedIn connection or message copy
   - call opener and voicemail
   - personalization tokens

4. Add test plan:
   - one variable per test
   - positive reply rate as primary metric
   - sufficient sample size before calling a winner

5. Handoff:
   - route to `sales-approval-queue` before sending
   - route to `sales-deliverability` if launch readiness is unclear

## Output

Produce a cadence table:

| day | step | channel | action | copy | personalization | success metric |
|---:|---:|---|---|---|---|---|

Do not send or schedule messages. Generate execution-ready drafts only.
