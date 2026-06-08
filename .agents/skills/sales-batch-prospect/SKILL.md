---
name: sales-batch-prospect
description: "Use this Codex sales skill for running AI SDR prospecting across a list of companies, domains, or rows. Produces batch research, scoring, prioritization, and outreach handoff instructions."
---

# Batch Prospecting

Use this skill when the user provides a list of companies, domains, accounts, or CSV rows and wants the SDR workflow applied across the batch.

When the user asks for deep research, account enrichment, or HubSpot company enrichment, do not stop at classification. Route each selected company through `sales-research` and apply that skill's Deep Research Completion Standard before counting the company as researched.

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

   For deep research runs, a light account pass is only selection and triage. It is not the final research output.

4. Prioritize:
   - A: enrich and personalize now
   - B: standard research and cadence
   - C: nurture or test segment
   - D: skip

5. Set research depth:
   - Account insight complete: company has at least one specific, sourced account-level reason and a researched problem hypothesis.
   - ICP-only fit: company matches the segment, but evidence is generic to the category.
   - Needs manual review: source evidence conflicts, is stale, or cannot be verified.
   - Source-limited: a real deep search was attempted but did not find useful company content, external account signals, or recent activity.

   A researched problem hypothesis must include:
   - the observed evidence
   - the source URL or source name
   - the reasoning chain from evidence to likely problem
   - confidence level

   Do not write a company-level problem as fact unless the company explicitly stated it. Use "problem hypothesis" for inferred problems and explain the inference.

   Do not classify source-of-record evidence alone as deep research. FCA, Companies House, directories, and third-party profiles can support account fit, but they are not enough by themselves for `research_confidence = high`, `problem_confidence = high`, or `next_action = decision_maker_research`.

   A completed deep-research record should include source coverage:
   - primary website pages checked
   - company content searched/found
   - external account signals searched/found
   - source-of-record checked where relevant
   - what was missing

6. Handoff:
   - send A/B accounts to `sales-enrich-contacts`
   - send uncertain accounts to `sales-research` or `sales-qualify`
   - send campaign-ready accounts to `sales-build-cadence`

7. Present a HubSpot review set before writes:
   - show every field that would be created or changed
   - include current value, proposed value, source evidence, reasoning, and confidence
   - group records into approve, edit, skip, and manual-review queues
   - ask for explicit approval before applying any HubSpot updates
   - after approval, write only the approved records and fields

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

For deep research loops, do not count a company toward the requested total if the result is only classification. Count it only when either:

- deep research fields were updated with source coverage and account-specific insight, or
- the record was marked `Source-limited` with searched source groups and missing evidence documented.

## HubSpot Review Output

Before mutating HubSpot, produce a compact review table:

| company | HubSpot ID | field | current value | proposed value | evidence/source | reasoning | confidence | action |
|---|---|---|---|---|---|---|---|---|

Allowed actions:

- `approve_update`
- `needs_edit`
- `skip`
- `manual_review`

Ask the user to approve, edit, or reject the proposed changes. Do not update HubSpot from the same step that first proposes the changes.
