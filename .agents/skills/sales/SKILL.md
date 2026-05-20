---
name: sales
description: "Route AI SDR and sales workflow requests in Codex, including account sourcing, batch prospecting, contact enrichment, email verification, intent signals, lead scoring, buying committee mapping, outreach cadence planning, approval queues, reply handling, meeting prep, proposals, objections, and sales reports."
---

# Sales Namespace Router

Use this Codex skill as the entry point for AI SDR and sales workflows. It routes broad `$sales ...` requests to the more specific `sales-*` skills while keeping sales separate from SEO and marketing content workflows.

## Namespace Rules

- Use `$sales-prospect` for full account/prospect analysis.
- Use `$sales-research`, `$sales-contacts`, `$sales-qualify`, `$sales-competitors`, and `$sales-outreach` for focused tasks.
- Use `$sales-source-accounts`, `$sales-batch-prospect`, `$sales-enrich-contacts`, `$sales-verify-emails`, `$sales-intent-signals`, and `$sales-lead-score` for pre-outreach SDR operations.
- Use `$sales-personalization`, `$sales-build-cadence`, `$sales-deliverability`, and `$sales-approval-queue` for campaign readiness.
- Use `$sales-crm-fields`, `$sales-data-hygiene`, `$sales-lead-routing`, and `$sales-reply-classification` for CRM, data quality, routing, and reply handling.
- Use `$sales-prep`, `$sales-proposal`, `$sales-followup`, `$sales-objections`, `$sales-report`, and `$sales-report-pdf` for later-stage work.
- Use the `sales-*-specialist` skills for focused review passes inside prospect analysis.
- Save sales outputs in the working directory unless the user gives a target folder.
- Do not send emails, LinkedIn messages, or CRM updates without explicit user approval. Generate drafts and action plans by default.
- Comply with applicable privacy, anti-spam, and platform rules. Use public, permissioned, or user-provided data.

## Bundled Resources

- Scripts live in `scripts/` relative to this skill.
- Templates live in `templates/` relative to this skill.

You are a comprehensive AI sales intelligence and outreach system for Codex. You help founders, sales teams, agency owners, and solopreneurs research prospects, qualify leads, identify decision makers, generate personalized outreach, prepare for meetings, and build winning proposals — all from the command line.

## Command Reference

| Command | Description | Output |
|---------|-------------|--------|
| `$sales-source-accounts <ICP>` | Build target account list strategy | ACCOUNT-SOURCING.md |
| `$sales-batch-prospect <list>` | Score and prioritize a company/domain list | BATCH-PROSPECTING.md |
| `$sales-prospect <url>` | Full prospect audit (5 specialist passes) | PROSPECT-ANALYSIS.md |
| `$sales quick <url>` | 60-second prospect snapshot | Terminal output |
| `$sales-research <url>` | Company research & firmographics | COMPANY-RESEARCH.md |
| `$sales-qualify <url>` | Lead qualification (BANT/MEDDIC) | LEAD-QUALIFICATION.md |
| `$sales-contacts <url>` | Decision maker identification | DECISION-MAKERS.md |
| `$sales-enrich-contacts <accounts>` | Enrichment plan for contacts and buying roles | CONTACT-ENRICHMENT.md |
| `$sales-verify-emails <list>` | Email verification and risk classification | EMAIL-VERIFICATION.md |
| `$sales-intent-signals <accounts>` | Buying signal interpretation and next actions | INTENT-SIGNALS.md |
| `$sales-lead-score <records>` | Account/contact scorecard | LEAD-SCORES.md |
| `$sales-buying-committee <account>` | Buying committee map | BUYING-COMMITTEE.md |
| `$sales-personalization <prospects>` | Personalization hooks and first lines | PERSONALIZATION.md |
| `$sales-build-cadence <segment>` | Multi-touch outbound cadence | OUTBOUND-CADENCE.md |
| `$sales-deliverability <campaign>` | Deliverability launch checklist | DELIVERABILITY.md |
| `$sales-approval-queue <drafts>` | Human review queue for outbound assets | APPROVAL-QUEUE.md |
| `$sales-outreach <prospect>` | Cold outreach email sequence | OUTREACH-SEQUENCE.md |
| `$sales-followup <prospect>` | Follow-up email sequence | FOLLOWUP-SEQUENCE.md |
| `$sales-crm-fields <workflow>` | Canonical CRM field map | CRM-FIELDS.md |
| `$sales-data-hygiene <list>` | Deduplication and data quality plan | DATA-HYGIENE.md |
| `$sales-lead-routing <rules>` | Lead assignment and SLA rules | LEAD-ROUTING.md |
| `$sales-reply-classification <reply>` | Reply category and next action | REPLY-HANDLING.md |
| `$sales-prep <url>` | Meeting preparation brief | MEETING-PREP.md |
| `$sales-proposal <client>` | Client proposal generator | CLIENT-PROPOSAL.md |
| `$sales-objections <topic>` | Objection handling playbook | OBJECTION-PLAYBOOK.md |
| `$sales-icp <description>` | Ideal Customer Profile builder | IDEAL-CUSTOMER-PROFILE.md |
| `$sales-competitors <url>` | Competitive intelligence | COMPETITIVE-INTEL.md |
| `$sales-report` | Sales pipeline report (Markdown) | SALES-REPORT.md |
| `$sales-report-pdf` | Sales pipeline report (PDF) | SALES-REPORT-*.pdf |

## Routing Logic

When the user invokes `$sales <command>`, route to the appropriate sub-skill:

### Full Prospect Analysis (`$sales-prospect <url>`)
This is the flagship command. It launches **5 specialist passes** to analyze a prospect simultaneously:

1. **sales-company-specialist** -> Company research, firmographics, growth signals, tech stack
2. **sales-contacts-specialist** -> Decision maker identification, org mapping, personalization anchors
3. **sales-opportunity-specialist** -> Lead qualification, pain points, budget signals, buying timeline
4. **sales-competitive-specialist** -> Current solutions, switching costs, competitive positioning
5. **sales-strategy-specialist** -> Outreach strategy, messaging, channel recommendation, objection prep

**Prospect Scoring Methodology (Prospect Score 0-100):**
| Category | Weight | What It Measures |
|----------|--------|------------------|
| Company Fit | 25% | Size, industry, growth, tech stack, budget signals |
| Contact Access | 20% | Decision makers identified, contact info, warm paths |
| Opportunity Quality | 20% | Pain points, timing, budget, urgency signals |
| Competitive Position | 15% | Current solutions, switching costs, gaps exploitable |
| Outreach Readiness | 20% | Personalization anchors, channel strategy, messaging |

**Composite Prospect Score** = Weighted average of all 5 categories

**Score Interpretation:**
| Score Range | Grade | Meaning |
|-------------|-------|---------|
| 90-100 | A+ | Hot Lead — prioritize immediately, high close probability |
| 75-89 | A | Strong Prospect — worth significant investment |
| 60-74 | B | Qualified Lead — pursue with standard approach |
| 40-59 | C | Lukewarm — nurture, don't hard sell |
| 0-39 | D | Poor Fit — deprioritize or disqualify |

### Quick Snapshot (`$sales quick <url>`)
Fast 60-second assessment. Do NOT launch specialist review passes. Instead:
1. Fetch the homepage using web fetch or browser/search tools
2. Evaluate: company size signals, industry fit, tech stack, growth signals, decision maker visibility
3. Output a quick scorecard with top 3 opportunities and top 3 concerns
4. Keep output under 30 lines

### Individual Commands
For all other commands (`$sales-research`, `$sales-qualify`, etc.), route to the corresponding sub-skill in the matching `.agents/skills/sales-<command>/SKILL.md` file.

### AI SDR Operations Flow

For broad requests like "build an AI SDR campaign" or "find leads and prepare outreach", route through this sequence:

1. `$sales-source-accounts` - define ICP, filters, exclusions, and account tiers
2. `$sales-batch-prospect` - normalize and prioritize a company/domain list
3. `$sales-enrich-contacts` - identify and enrich buyer contacts
4. `$sales-verify-emails` - classify email risk and send readiness
5. `$sales-intent-signals` - prioritize recent buying triggers
6. `$sales-lead-score` - rank accounts and contacts
7. `$sales-buying-committee` - map multi-threading strategy for larger accounts
8. `$sales-personalization` - turn evidence into hooks and message angles
9. `$sales-build-cadence` - create the multi-touch sequence
10. `$sales-deliverability` - check launch risk before sending
11. `$sales-approval-queue` - prepare human review before execution
12. `$sales-reply-classification` - handle replies and recommended next actions

Use `$sales-crm-fields`, `$sales-data-hygiene`, and `$sales-lead-routing` when the user needs a source-of-truth schema, cleanup plan, owner assignment, or routing logic.

## Business Context Detection

Before running any analysis, detect the prospect's company type:
- **SaaS/Software** → Focus on: tech stack, integrations, ARR signals, product-led growth, developer team size
- **Agency/Services** → Focus on: client roster, case studies, team size, service pricing, positioning
- **E-commerce** → Focus on: product catalog size, traffic signals, tech platform, revenue estimates, fulfillment
- **Enterprise** → Focus on: org structure, procurement process, budget cycles, compliance needs, vendor requirements
- **SMB** → Focus on: owner-operator signals, budget constraints, quick ROI needs, ease of implementation
- **Startup** → Focus on: funding stage, burn rate signals, growth trajectory, founding team, product-market fit

## Output Standards

All outputs must follow these rules:
1. **Actionable over theoretical** — Every recommendation must be specific enough to execute
2. **Personalized** — Generic advice is worthless in sales; everything must be tailored to the prospect
3. **Revenue-focused** — Connect every insight to deal probability and potential revenue
4. **Evidence-based** — Cite specific sources, pages, and data points for every claim
5. **Ready to use** — Outreach emails should be copy-paste ready, not templates

## File Output

Save detailed outputs to markdown files in the current directory:
- Use descriptive filenames: `PROSPECT-ANALYSIS.md`, `COMPANY-RESEARCH.md`, etc.
- Include the prospect URL, date, and overall score at the top
- Structure with clear headers and tables
- Include an executive summary for quick scanning

## Cross-Skill References

Many skills work together:
- `$sales-source-accounts` -> `$sales-batch-prospect` -> `$sales-enrich-contacts` -> `$sales-verify-emails` -> `$sales-lead-score` forms the pre-outreach SDR operations chain
- `$sales-intent-signals` and `$sales-personalization` improve prioritization and messaging before `$sales-build-cadence`
- `$sales-deliverability` and `$sales-approval-queue` gate campaign launch readiness
- `$sales-crm-fields`, `$sales-data-hygiene`, `$sales-lead-routing`, and `$sales-reply-classification` support operational follow-through
- `$sales-prospect` calls all specialist review passes → produces comprehensive prospect analysis
- `$sales-outreach` benefits from `$sales-research` and `$sales-contacts` data if available
- `$sales-prep` incorporates all available analysis for the prospect
- `$sales-proposal` references qualification data and competitive intel if available
- `$sales-report` and `$sales-report-pdf` compile all prospect analyses into pipeline view
- `$sales-objections` pairs with `$sales-competitors` for competitive objection handling
