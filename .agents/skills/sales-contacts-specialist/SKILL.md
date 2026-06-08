---
name: sales-contacts-specialist
description: "Use this Codex sales specialist skill to map the buying committee, identify priority contacts, assess contact access, and create SDR-ready personalization paths."
---

# Sales Contacts Specialist

## Purpose

Find the right people.

This skill turns company intelligence into a contact strategy.

It answers:

1. Who should we contact?
2. Why do they matter?
3. What role do they play in the buying process?
4. What can we personalize around?
5. Can we multi-thread the account?

---

## Inputs

Use the best available input in this order:

1. `COMPANY-INTELLIGENCE.md`
2. `COMPANY-RESEARCH.md`
3. Discovery briefing from `sales-prospect`
4. User-provided account notes
5. Public web/search results if needed

---

## Operating Rules

- Do not invent people.
- Do not guess private emails or phone numbers.
- Use public or user-provided information only.
- Prioritize quality over quantity.
- Mark inferred roles clearly.
- Separate confirmed facts from assumptions.
- Focus on SDR usefulness.

---

## Analysis Process

### Step 1: Identify Target Personas

From the company intelligence, identify likely personas.

Common roles:

- CEO / Founder
- CFO / Finance Director
- COO / Operations Director
- Commercial Director
- Head of Digital
- Head of Sales
- Head of Customer Experience
- CTO / Head of Technology
- Compliance Manager
- Product Owner
- Transformation Lead

---

### Step 2: Find Actual People

Search:

- Company website
- Team / leadership pages
- LinkedIn company page
- Press releases
- News articles
- Conference speaker pages
- Podcasts / webinars
- Blog authors
- Awards pages
- Partner announcements

For each person capture:

```yaml
name:
title:
company:
source:
current_role_confidence:
buying_role:
priority:
personalization_anchors:
```

---

### Step 3: Map Buying Committee

Classify people into:

| Buying Role | Description |
|---|---|
| Economic Buyer | Controls budget or final sign-off |
| Champion | Feels the pain and may advocate internally |
| Technical Evaluator | Reviews technical fit, data, integration, security |
| User Buyer | Team who would use or benefit from the product |
| Blocker | Legal, compliance, procurement, security, finance |
| Influencer | Advisor, board member, partner, or public voice |

---

### Step 4: Find Personalization Anchors

Look for:

- Recent promotion
- New role
- Public post
- Article
- Podcast
- Webinar
- Conference talk
- Award
- Quote in press
- Previous company experience
- Relevant project
- Hiring responsibility
- Product or transformation initiative

Rate each anchor:

- Strong: recent, specific, and relevant
- Medium: relevant but not personal
- Weak: generic or old

---

### Step 5: Build Contact Strategy

Create:

- top 3 priority contacts
- recommended first contact
- backup contact
- multi-threading plan
- warm path ideas
- contact gaps

---

## Scoring

Score each dimension 0-10.

| Dimension | Meaning |
|---|---|
| Decision Makers Identified | Named people found for key buying roles |
| Persona Fit | Contacts match likely buyers for the offer |
| Personalization Depth | Useful, specific hooks found |
| Contact Accessibility | Public professional channels are visible |
| Multi-Threading Potential | More than one useful stakeholder can be approached |

Contact Access Score:

```text
(Decision Makers Identified + Persona Fit + Personalization Depth + Contact Accessibility + Multi-Threading Potential) / 5 * 10
```

---

## Output

Write `CONTACT-INTELLIGENCE.md`.

Use this format:

```markdown
# Contact Intelligence: [Company Name]

**Contact Access Score:** [X]/100
**Confidence:** [High / Medium / Low]

---

## SDR Summary

[3-5 concise bullets.]

---

## Score Breakdown

| Dimension | Score | Evidence |
|---|---:|---|
| Decision Makers Identified | X/10 | |
| Persona Fit | X/10 | |
| Personalization Depth | X/10 | |
| Contact Accessibility | X/10 | |
| Multi-Threading Potential | X/10 | |

---

## Buying Committee Map

| Buying Role | Name | Title | Confidence | Source |
|---|---|---|---|---|
| Economic Buyer | | | | |
| Champion | | | | |
| Technical Evaluator | | | | |
| User Buyer | | | | |
| Blocker | | | | |
| Influencer | | | | |

---

## Priority Contacts

### 1. [Name] — [Title]

**Buying role:**
**Why this person matters:**
**Priority:** High / Medium / Low
**Source:**
**Personalization anchors:**
-
-

**Suggested opening angle:**

---

### 2. [Name] — [Title]

**Buying role:**
**Why this person matters:**
**Priority:** High / Medium / Low
**Source:**
**Personalization anchors:**
-
-

**Suggested opening angle:**

---

### 3. [Name] — [Title]

**Buying role:**
**Why this person matters:**
**Priority:** High / Medium / Low
**Source:**
**Personalization anchors:**
-
-

**Suggested opening angle:**

---

## Multi-Threading Plan

| Sequence | Contact | Reason | Channel |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## Warm Path Ideas

| Path | Detail | Confidence |
|---|---|---|
| Content engagement | | |
| Event / webinar | | |
| Shared network to check | | |
| Partner / customer route | | |

---

## Contact Gaps

-
-

---

## Handoff to Next Skills

### For `sales-opportunity-specialist`
[Authority gaps, qualification questions, buyer concerns.]

### For `sales-strategy-specialist`
[Best person to target first and the strongest personalization angle.]
```

---

## Terminal Summary

Also print:

```text
=== CONTACT INTELLIGENCE COMPLETE ===

Company: [name]
Contact Access Score: [X]/100
Confidence: [High/Medium/Low]

Best First Contact: [name/title]
Best Buying Role Found: [role]
Strongest Personalization Anchor: [anchor]

Saved to: CONTACT-INTELLIGENCE.md
```

---

## What This Skill Should Not Do

Do not:
- write full email sequences
- qualify the opportunity in detail
- perform broad company research
- invent contact data
- scrape private data
- update CRM records

Those belong to other skills.
