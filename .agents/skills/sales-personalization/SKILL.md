---
name: sales-personalization
description: "Use this Codex sales skill to turn account research, contact research, and intent signals into specific outbound personalization snippets, pain hypotheses, value props, and first-line options."
---

# Sales Personalization

Use this skill after research, enrichment, scoring, or intent analysis and before writing a cadence.

## Personalization Levels

- Level 1: name, company, title
- Level 2: industry, segment, company size, persona pain
- Level 3: account-specific trigger such as hiring, funding, launch, tech stack, content, or role change
- Level 4: contact-specific insight such as post, interview, talk, article, or career move

Default to Level 3 for Tier 1 and Tier 2 cold outbound. Use Level 2 only for lower-priority scale campaigns.

## Workflow

1. Extract hooks:
   - company trigger
   - contact trigger
   - likely business pain
   - relevant proof point
   - reason now

   Separate hooks into:
   - Account-level hook: sourced evidence about the company, such as a news item, blog post, video, hiring signal, regulatory listing, partnership, product/service page, award, or expansion.
   - Contact-level hook: sourced evidence about the person, such as a post, article, talk, interview, role change, or public profile detail.
   - ICP-level hook: segment or persona assumption only. This is usable for lower-priority campaigns, but it is not deep personalization.

2. Convert hooks into useful assets:
   - first-line options
   - pain hypothesis
   - value prop angle
   - CTA angle
   - follow-up angle

3. Quality checks:
   - specific but not invasive
   - tied to a business problem
   - not fake familiarity
   - not a generic compliment
   - source-backed where factual
   - never treat "approved target account" or "matches ICP" as the personalization reason
   - if no account-level or contact-level source is found, mark personalization depth as ICP-only

## Output

Create a personalization table:

| prospect | personalization depth | hook | source | first line | pain hypothesis | value angle | confidence |
|---|---|---|---|---|---|---|---|

If facts are uncertain, mark the hook as low confidence and provide a safer generic alternative.
