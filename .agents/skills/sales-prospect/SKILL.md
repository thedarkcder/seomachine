---
name: sales-prospect
description: "Master SDR orchestrator. Runs all specialist skills in sequence, aggregates results, calculates final prospect score, and produces a concise PROSPECT-SUMMARY.md."
---

# Sales Prospect Orchestrator

## Purpose

This is the master skill.

It does not perform deep research itself.

Its job is to:

1. Run specialist skills
2. Aggregate results
3. Calculate overall score
4. Recommend next actions

---

## Workflow

Run skills in this order:

### 1. sales-research

Output:

- COMPANY-RESEARCH.md

---

### 2. sales-company-specialist

Input:

- COMPANY-RESEARCH.md

Output:

- COMPANY-INTELLIGENCE.md

---

### 3. sales-contacts-specialist

Inputs:

- COMPANY-RESEARCH.md
- COMPANY-INTELLIGENCE.md

Output:

- CONTACT-INTELLIGENCE.md

---

### 4. sales-opportunity-specialist

Inputs:

- COMPANY-RESEARCH.md
- COMPANY-INTELLIGENCE.md
- CONTACT-INTELLIGENCE.md

Output:

- OPPORTUNITY-INTELLIGENCE.md

---

### 5. sales-strategy-specialist

Inputs:

- COMPANY-RESEARCH.md
- COMPANY-INTELLIGENCE.md
- CONTACT-INTELLIGENCE.md
- OPPORTUNITY-INTELLIGENCE.md

Output:

- OUTREACH-STRATEGY.md

---

## Aggregation

Combine:

- Company Fit Score
- Contact Access Score
- Opportunity Score
- Outreach Readiness Score

Optional:

- Competitive Score

---

## Prospect Score

Default:

```text
Company Fit            25%
Contact Access         25%
Opportunity Quality    25%
Outreach Readiness     25%
```

If Competitive Intelligence exists:

```text
Company Fit            20%
Contact Access         20%
Opportunity Quality    20%
Competitive Position   20%
Outreach Readiness     20%
```

---

## Output

Write:

PROSPECT-SUMMARY.md

---

## Summary Structure

```markdown
# Prospect Summary

Company:
Industry:

Prospect Score:

## Score Breakdown

Company Fit:
Contact Access:
Opportunity:
Strategy:

## Best Buyer

Name:
Role:

## Best Trigger

## Best Pain Hypothesis

## Best Outreach Angle

## Best Channel

## Recommended Next Action

## Risks

## Confidence
```

---

## Confidence

High
Medium
Low

Based on:

- Research depth
- Source quality
- Data freshness
- Contact quality

---

## Rules

- Do not duplicate specialist reports.
- Summarize.
- Highlight the most important findings.
- Keep the final report under 2 pages.
- Prefer action over description.

---

## Terminal Output

```text
=== PROSPECT COMPLETE ===

Company:
Prospect Score:

Best Buyer:
Best Trigger:
Best Channel:

Next Action:

Saved:
PROSPECT-SUMMARY.md
```
