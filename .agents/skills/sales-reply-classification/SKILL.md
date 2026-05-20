---
name: sales-reply-classification
description: "Use this Codex sales skill to classify inbound sales replies and recommend next actions, including interested, objection, referral, not-now, unsubscribe, out-of-office, wrong person, and competitor responses."
---

# Reply Classification

Use this skill when replies need to be interpreted and turned into next actions.

## Reply Categories

- interested: wants more information or a meeting
- objection: price, timing, relevance, authority, competitor, trust
- referral: points to another person
- not now: timing issue but possible future fit
- wrong person: asks to contact someone else or says not their area
- unsubscribe/do not contact: suppress immediately
- out of office: pause and retry after return date
- negative: no fit or hostile response
- unclear: needs manual review

## Workflow

1. Classify the reply.
2. Extract key facts:
   - sentiment
   - urgency
   - requested action
   - new contact or referral
   - suppression requirement
   - follow-up date
3. Recommend next action:
   - book meeting
   - answer objection
   - follow up later
   - enrich referred contact
   - update approval queue
   - suppress contact
4. Draft response if appropriate.

## Output

Create a reply handling record:

| contact | category | confidence | next action | owner | due date | suggested response |
|---|---|---|---|---|---|---|

Always treat unsubscribe or do-not-contact language as binding.
