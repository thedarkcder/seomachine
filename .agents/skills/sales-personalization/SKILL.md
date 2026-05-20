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

## Output

Create a personalization table:

| prospect | hook | first line | pain hypothesis | value angle | confidence |
|---|---|---|---|---|---|

If facts are uncertain, mark the hook as low confidence and provide a safer generic alternative.
