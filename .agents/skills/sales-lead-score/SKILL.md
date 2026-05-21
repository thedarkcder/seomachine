---
name: sales-lead-score
description: "Use this Codex sales skill to score accounts and contacts for AI SDR prioritization using ICP fit, contact fit, intent, timing, data quality, and outreach readiness."
---

# Lead Scoring

Use this skill to rank accounts or contacts before deciding what to research, enrich, personalize, or sequence.

## Default Score Model

| Dimension | Weight | What to evaluate |
|---|---:|---|
| Account fit | 25 | industry, size, geography, revenue, stage, budget fit |
| Contact fit | 20 | title, seniority, department, buying committee role |
| Intent/timing | 20 | fresh buying signals, urgency, leadership change, funding, hiring |
| Pain relevance | 15 | researched evidence plus reasoning that the account likely has a problem the offer solves |
| Data quality | 10 | verified email, complete fields, source confidence |
| Outreach readiness | 10 | personalization hooks, channel fit, compliance status |

Adjust the weights for the motion:

- outbound-led: increase account fit and contact fit
- inbound-led: increase behavioral/intent signals
- PLG: increase product usage and account expansion signals
- enterprise ABM: keep all dimensions balanced and require more evidence

## Workflow

1. Score each dimension from 0 to its max weight.
2. Record the evidence behind each score.
   For pain relevance, record the observed evidence, source, reasoning chain, confidence, and any plausible counterpoint. Do not score pain highly from segment fit alone.
3. Apply negative scoring:
   - do-not-contact or unsubscribe: disqualify
   - invalid email: hold
   - unsupported geography: disqualify or nurture
   - poor account fit: cap total score at 50
4. Assign a priority:
   - 85-100: A, work immediately
   - 70-84: B, standard outbound
   - 50-69: C, nurture or test
   - under 50: D, skip unless strategic reason exists

## Output

Produce a scorecard:

| account/contact | score | grade | strongest evidence | biggest risk | recommended next step |
|---|---:|---|---|---|---|

Do not let a strong signal override poor ICP fit without calling out the tradeoff.
