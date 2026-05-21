---
name: sales-source-accounts
description: "Use this Codex sales skill for AI SDR account sourcing. Builds targeted account lists from an ICP, campaign goal, filters, exclusions, buying signals, and quality rules before contact enrichment or outreach."
---

# Account Sourcing

Use this skill when the user needs to find companies to target before researching contacts or writing outreach.

## Inputs

- ICP or rough target market
- Campaign goal: net-new outbound, ABM, event follow-up, expansion, competitive displacement
- Target geographies, industries, company sizes, revenue bands, funding stages, and technologies
- Exclusions: customers, active opportunities, competitors, do-not-contact accounts, unsupported regions
- Desired list size and personalization depth

If the user has not supplied enough context, make reasonable assumptions and ask only the most important 1-2 questions.

## Workflow

1. Define the account-level ICP:
   - firmographics: industry, size, geography, revenue, funding, growth
   - technographics: current stack, complementary tools, competitor usage
   - business signals: hiring, funding, launches, leadership changes, category intent
   - negative filters: poor-fit sectors, unsupported regions, low-budget segments

2. Build a sourcing plan:
   - state the account sources the user could query
   - specify exact filters and search logic
   - estimate expected list size and quality risks
   - separate account criteria from contact/persona criteria

3. Segment the accounts:
   - Tier 1: high ICP fit plus active buying signal
   - Tier 2: strong ICP fit without current signal
   - Tier 3: adjacent fit worth testing
   - Skip: weak fit, unavailable market, or compliance risk

4. Prepare the handoff:
   - output a target account table
   - include priority, reason to target, segment, likely buyer personas, and personalization angles
   - recommend next skill: `sales-enrich-contacts`, `sales-intent-signals`, or `sales-batch-prospect`

   `reason to target` must be source-backed where possible. Do not use "regulation proven", "approved", or "matches ICP" as the final reason unless the user only requested broad list building. For AI SDR execution, route ICP-only accounts to account research before contact enrichment.

## Output

Create an account sourcing brief with:

- ICP summary
- inclusion filters
- exclusion filters
- account tiering rules
- recommended list size
- target account table if companies are provided or discoverable
- next-step enrichment plan

Do not invent specific company facts. Use sourced facts when available and mark assumptions clearly.
