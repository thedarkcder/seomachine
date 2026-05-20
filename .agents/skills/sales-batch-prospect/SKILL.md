---
name: sales-batch-prospect
description: "Use this Codex sales skill for running AI SDR prospecting across a list of companies, domains, or rows. Produces batch research, scoring, prioritization, and outreach handoff instructions."
---

# Batch Prospecting

Use this skill when the user provides a list of companies, domains, accounts, or CSV rows and wants the SDR workflow applied across the batch.

## Workflow

1. Confirm the batch structure:
   - company name
   - domain or website
   - industry, size, geography if available
   - existing owner, status, or suppression fields if available

2. Normalize the list:
   - dedupe by domain first, then company name
   - preserve original row IDs
   - flag missing domains or ambiguous company names
   - apply do-not-contact and customer exclusions if provided

3. Run a light account pass:
   - fit score
   - visible buying signals
   - likely buying committee
   - research confidence
   - recommended next action

4. Prioritize:
   - A: enrich and personalize now
   - B: standard research and cadence
   - C: nurture or test segment
   - D: skip

5. Handoff:
   - send A/B accounts to `sales-enrich-contacts`
   - send uncertain accounts to `sales-research` or `sales-qualify`
   - send campaign-ready accounts to `sales-build-cadence`

## Output

Produce a batch prospecting table with these fields:

| account | domain | priority | fit score | signal score | confidence | reason | next skill |
|---|---|---:|---:|---:|---|---|---|

For large lists, summarize segment counts and provide a sample of top accounts rather than writing an exhaustive report.
