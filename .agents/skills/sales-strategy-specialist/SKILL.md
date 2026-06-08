---
name: sales-strategy-specialist
description: "Use this Codex sales specialist skill to convert company, contact, and opportunity intelligence into an SDR-ready outreach strategy, first message, follow-up cadence, and objection plan."
---

# Sales Strategy Specialist

## Purpose

Turn intelligence into action.

This skill creates the SDR plan.

It answers:

1. Who do we contact first?
2. What do we say?
3. Which channel should we use?
4. What trigger should we reference?
5. What objections should we expect?
6. What is the follow-up plan?

---

## Inputs

Use the best available inputs in this order:

1. `OPPORTUNITY-INTELLIGENCE.md`
2. `CONTACT-INTELLIGENCE.md`
3. `COMPANY-INTELLIGENCE.md`
4. `COMPANY-RESEARCH.md`
5. Discovery briefing from `sales-prospect`
6. User-provided notes

---

## Operating Rules

- Be concise.
- Do not duplicate research.
- Do not invent personalization.
- Do not use placeholders in final outreach drafts.
- Do not write spammy messages.
- Every message must reference real evidence.
- Prefer specific triggers over generic value props.
- Keep outreach human and direct.
- Avoid hype words like: revolutionize, game-changer, unlock, best-in-class, synergy.

---

## Analysis Process

### Step 1: Select Target Contact

Choose the best first contact from `CONTACT-INTELLIGENCE.md`.

Prioritize:

1. Strong buying role
2. Strong personalization
3. Clear connection to pain
4. Accessible professional channel
5. Ability to champion or influence

---

### Step 2: Choose Outreach Angle

Use the strongest evidence from:

- Buying trigger
- Pain hypothesis
- Current initiative
- Recent change
- Hiring signal
- Technology signal
- Expansion signal
- Funding signal

Convert it into one clear message angle.

---

### Step 3: Choose Channel

Rank:

- Email
- LinkedIn connection note
- LinkedIn DM
- Warm intro
- Event-based approach
- Content engagement first
- Phone

Select:

- Primary channel
- Secondary channel
- Backup channel

Explain why.

---

### Step 4: Select Messaging Framework

Choose one:

| Framework | Use When |
|---|---|
| Trigger-Based | There is a recent event |
| Problem-Led | There is strong pain evidence |
| Insight-Led | You can teach them something useful |
| Social Proof-Led | Peer comparison matters |
| Role-Based | Personalization is limited but role relevance is clear |
| Referral/Warm Intro | A warm path exists |

---

### Step 5: Build Objection Plan

Predict likely objections:

- Not a priority
- Already have a solution
- No budget
- Wrong person
- Too complex
- Timing not right
- Need compliance/security review
- Need to see proof

For each objection provide:

```yaml
objection:
real_concern:
response:
proof_needed:
```

---

### Step 6: Create Outreach Plan

Create:

- first message
- day 3 follow-up
- day 7 follow-up
- LinkedIn connection note
- cadence
- risk notes

---

## Scoring

Score 0-10:

| Dimension | Meaning |
|---|---|
| Personalization Quality | Strength of specific hooks |
| Message Fit | Message matches evidence and persona |
| Channel Fit | Channel suits person and context |
| Timing Strength | Clear reason to act now |
| Objection Readiness | Prepared for likely pushback |

Outreach Readiness Score:

```text
(Personalization Quality + Message Fit + Channel Fit + Timing Strength + Objection Readiness) / 5 * 10
```

---

## Output

Write `OUTREACH-STRATEGY.md`.

Use this format:

```markdown
# Outreach Strategy: [Company Name]

**Outreach Readiness Score:** [X]/100
**Confidence:** [High / Medium / Low]

---

## Strategy Summary

[3-5 concise bullets.]

---

## Best First Contact

| Field | Detail |
|---|---|
| Name | |
| Title | |
| Buying Role | |
| Why This Person | |
| Best Channel | |
| Best Trigger | |

---

## Messaging Strategy

| Item | Recommendation |
|---|---|
| Framework | |
| Core Angle | |
| Pain / Trigger | |
| Proof Needed | |
| CTA | |

---

## Channel Plan

| Priority | Channel | Purpose |
|---|---|---|
| Primary | | |
| Secondary | | |
| Backup | | |

---

## First Outreach Email

**Subject:** [subject]

[email body]

---

## LinkedIn Connection Note

[under 300 characters]

---

## LinkedIn DM

[message]

---

## Follow-Up Cadence

| Day | Channel | Message Goal |
|---|---|---|
| 1 | | |
| 3 | | |
| 7 | | |
| 14 | | |

---

## Follow-Up Messages

### Day 3

[message]

### Day 7

[message]

### Day 14

[message]

---

## Objection Plan

| Objection | Real Concern | Response | Proof Needed |
|---|---|---|---|
| | | | |

---

## Risks

-
-

---

## Handoff to `sales-outreach`

[Notes for creating a fuller sequence.]
```

---

## Terminal Summary

Also print:

```text
=== OUTREACH STRATEGY COMPLETE ===

Company: [name]
Outreach Readiness Score: [X]/100
Confidence: [High/Medium/Low]

First Contact: [name/title]
Primary Channel: [channel]
Core Angle: [angle]

Saved to: OUTREACH-STRATEGY.md
```

---

## What This Skill Should Not Do

Do not:
- run deep company research
- discover contacts from scratch
- qualify the opportunity from scratch
- create long nurture campaigns
- update CRM records
- send emails
