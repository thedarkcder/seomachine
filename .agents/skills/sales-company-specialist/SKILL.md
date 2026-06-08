---
name: sales-company-specialist
description: "Use this Codex sales specialist skill to turn COMPANY-RESEARCH.md into SDR-ready company fit, buying triggers, likely buyers, pain hypotheses, and outreach angles."
---

# Sales Company Specialist

## Purpose

Interpret company research for SDR action.

This skill does not perform deep research from scratch unless `COMPANY-RESEARCH.md` is missing.

It consumes research evidence and answers:

1. Should we target this company?
2. Why now?
3. Who is likely to care?
4. What pain might exist?
5. What should an SDR say first?

---

## Inputs

Use the best available input in this order:

1. `COMPANY-RESEARCH.md`
2. Discovery briefing from `sales-prospect`
3. User-provided company notes
4. Public website/search results if research is missing

If `COMPANY-RESEARCH.md` exists, treat it as the main evidence source.

---

## Operating Rules

- Be concise.
- Do not write a long company profile.
- Do not duplicate `sales-research`.
- Separate fact from inference.
- Every recommendation must link back to evidence.
- If evidence is weak, say so.
- Prioritize recent triggers.
- Think like an SDR, not an analyst.

---

## Analysis Process

### Step 1: Read Research Evidence

Review available research for:

- Company size
- Industry
- Products
- Customers
- Partners
- Funding
- Hiring
- Leadership
- Technology stack
- Recent news
- Expansion
- Market activity

---

### Step 2: Identify Sales Signals

Look for evidence of:

- Growth
- Change
- Operational complexity
- Digital transformation
- New leadership
- New funding
- Hiring
- Partnerships
- Acquisitions
- Technology investment
- Customer expansion
- Regulatory or market pressure

---

### Step 3: Convert Signals Into SDR Intelligence

For each useful signal, generate:

```yaml
evidence:
signal_type:
hypothesis:
likely_buyer:
why_now:
outreach_angle:
confidence:
```

Use confidence levels:

- High: directly supported by clear evidence
- Medium: reasonable inference from evidence
- Low: weak signal or limited source coverage

---

## Scoring

Score each dimension from 0-10.

| Dimension | Meaning |
|---|---|
| Size Fit | Company appears large enough and not too complex for the offer |
| Industry Fit | Company matches the target market or adjacent ICP |
| Growth / Change | Evidence of movement, investment, hiring, expansion, or change |
| Tech Readiness | Technology maturity suggests they can adopt a new solution |
| Budget Signal | Evidence they may have budget or willingness to invest |

Company Fit Score:

```text
(Size Fit + Industry Fit + Growth / Change + Tech Readiness + Budget Signal) / 5 * 10
```

---

## Output

Write `COMPANY-INTELLIGENCE.md`.

Use this format:

```markdown
# Company Intelligence: [Company Name]

**Company Fit Score:** [X]/100
**Confidence:** [High / Medium / Low]

---

## SDR Summary

[3-5 concise bullets explaining whether this company is worth targeting and why.]

---

## Score Breakdown

| Dimension | Score | Evidence |
|---|---:|---|
| Size Fit | X/10 | |
| Industry Fit | X/10 | |
| Growth / Change | X/10 | |
| Tech Readiness | X/10 | |
| Budget Signal | X/10 | |

---

## Buying Triggers

| Trigger | Evidence | Why Now | Urgency |
|---|---|---|---|
| | | | |

---

## Likely Buyers

| Persona / Role | Why They Care | Priority |
|---|---|---|
| | | |

---

## Current Initiatives

| Initiative | Evidence | Likely Owner |
|---|---|---|
| | | |

---

## Pain Hypotheses

| Hypothesis | Evidence | Confidence |
|---|---|---|
| | | |

---

## Outreach Angles

| Angle | Evidence | Suggested Opener |
|---|---|---|
| | | |

---

## Risks / Reasons to Deprioritize

| Risk | Evidence | Impact |
|---|---|---|
| | | |

---

## Top 5 SDR Insights

1.
2.
3.
4.
5.

---

## Handoff to Next Skills

### For `sales-contacts-specialist`
[People/personas to investigate first.]

### For `sales-opportunity-specialist`
[Qualification questions and gaps.]

### For `sales-strategy-specialist`
[Best messaging direction.]
```

---

## Terminal Summary

Also print:

```text
=== COMPANY INTELLIGENCE COMPLETE ===

Company: [name]
Company Fit Score: [X]/100
Confidence: [High/Medium/Low]

Top Trigger: [trigger]
Best Persona: [persona]
Best Outreach Angle: [angle]

Saved to: COMPANY-INTELLIGENCE.md
```

---

## What This Skill Should Not Do

Do not:
- produce a full company dossier
- perform contact-level research
- write a full email sequence
- update CRM records
- invent private contact details
- overstate weak evidence

Those belong to other skills.
