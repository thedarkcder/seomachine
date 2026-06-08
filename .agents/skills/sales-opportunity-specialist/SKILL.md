---
name: sales-opportunity-specialist
description: "Use this Codex sales specialist skill to determine whether a real sales opportunity exists by evaluating need, timing, budget, authority, and champion potential."
---

# Sales Opportunity Specialist

## Purpose

Determine if this account is worth pursuing now.

This skill answers:

1. Is there evidence of a real problem?
2. Is there evidence of budget?
3. Is there evidence of urgency?
4. Is there a likely champion?
5. What should be validated in discovery?

---

## Inputs

Use:

1. OPPORTUNITY-INTELLIGENCE.md (if exists)
2. CONTACT-INTELLIGENCE.md
3. COMPANY-INTELLIGENCE.md
4. COMPANY-RESEARCH.md
5. Discovery briefing

---

## Rules

- Do not invent pain.
- Separate evidence from assumptions.
- Be conservative.
- Focus on qualification.
- Prioritize recent evidence.

---

## Framework

Evaluate:

### Budget
Funding, growth, hiring, tech spend, expansion.

### Authority
Decision structure and access to decision makers.

### Need
Evidence of pain, inefficiency, change, hiring, projects.

### Timeline
Recent trigger events creating urgency.

### Champion
Likelihood of an internal advocate.

---

## Scoring

Score 0-10:

- Budget
- Authority
- Need
- Timeline
- Champion

Opportunity Score:

(Budget + Authority + Need + Timeline + Champion) / 5 * 10

---

## Output

Write OPPORTUNITY-INTELLIGENCE.md

Sections:

- Opportunity Score
- Qualification Summary
- Budget Signals
- Authority Assessment
- Need Assessment
- Timeline Assessment
- Champion Candidates
- Discovery Questions
- Risks
- Recommendation

---

## What This Skill Should Not Do

- Deep company research
- Contact discovery
- Email writing
- CRM updates
