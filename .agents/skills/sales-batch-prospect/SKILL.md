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
   - source-backed account reason

   For target accounts, "reason" must not mean "approved", "matches ICP", or "has regulation evidence" by itself. It must explain why this specific company deserves sales attention using researched evidence, such as:
   - recent news, funding, partnership, expansion, hiring, leadership change, acquisition, or product launch
   - relevant blog/resource/video/podcast/social post from the company or a leader
   - website evidence showing a business model, market focus, product line, or operational change that connects to the user's offer
   - public regulatory, directory, or marketplace evidence that creates a specific sales angle

   If only ICP-level evidence exists, mark the account as `needs_account_research` rather than treating it as personalized.

4. Prioritize:
   - A: enrich and personalize now
   - B: standard research and cadence
   - C: nurture or test segment
   - D: skip

5. Set research depth:
   - Account insight complete: company has at least one specific, sourced account-level reason and a researched problem hypothesis.
   - ICP-only fit: company matches the segment, but evidence is generic to the category.
   - Needs manual review: source evidence conflicts, is stale, or cannot be verified.

   A researched problem hypothesis must include:
   - the observed evidence
   - the source URL or source name
   - the reasoning chain from evidence to likely problem
   - confidence level

   Do not write a company-level problem as fact unless the company explicitly stated it. Use "problem hypothesis" for inferred problems and explain the inference.

6. Handoff:
   - send A/B accounts to `sales-enrich-contacts`
   - send uncertain accounts to `sales-research` or `sales-qualify`
   - send campaign-ready accounts to `sales-build-cadence`

## Output

Produce a batch prospecting table with these fields:

| account | domain | priority | fit score | signal score | confidence | why this account matters | evidence source | problem hypothesis | problem reasoning | next skill |
|---|---|---:|---:|---:|---|---|---|---|---|---|

For large lists, summarize segment counts and provide a sample of top accounts rather than writing an exhaustive report.

When updating HubSpot, prefer these company-level fields when available:

- `why_this_account`
- `account_research_summary`
- `problem_hypothesis`
- `problem_evidence`
- `problem_reasoning`
- `problem_confidence`
- `personalization_evidence`
- `evidence_source_urls`
- `research_confidence`
- `last_researched_date`

Do not mark a company `contact_enrichment_ready` unless the account has either account insight complete or the user has explicitly approved ICP-only enrichment.
