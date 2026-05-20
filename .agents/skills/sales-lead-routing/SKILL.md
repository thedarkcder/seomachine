---
name: sales-lead-routing
description: "Use this Codex sales skill to design lead routing and ownership rules for AI SDR workflows, including territory, round-robin, score-based routing, SLA, capacity, and fallback logic."
---

# Lead Routing

Use this skill once leads or accounts need assignment to reps, owners, queues, or follow-up paths.

## Routing Models

- round-robin: equal distribution for generalist teams
- territory: geography, vertical, segment, or named account ownership
- score-based: hot leads to senior reps, lower score to SDR/nurture
- account-based: existing account owner wins
- hybrid: waterfall of the above

## Workflow

1. Gather routing context:
   - team structure
   - territories or segments
   - lead sources
   - lead volume
   - current ownership conflicts
   - speed-to-lead expectations

2. Define routing waterfall:
   - suppression or customer check
   - existing account owner
   - named account owner
   - territory or segment owner
   - score-based queue
   - round-robin fallback

3. Define SLA:
   - demo request: immediate or under 5 minutes
   - high-intent reply: under 1 hour
   - standard outbound lead: same business day
   - nurture lead: scheduled follow-up

4. Define fallback rules:
   - owner out of office
   - capacity reached
   - missing account match
   - disputed ownership

## Output

Create routing rules:

| priority | condition | owner/queue | SLA | fallback | notes |
|---:|---|---|---|---|---|

Flag any routing rule that depends on fields missing from `sales-crm-fields`.
