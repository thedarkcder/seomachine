---
name: revops-campaign-tracking
description: "Use this Codex RevOps skill to design campaign tracking, UTM conventions, lead source taxonomy, campaign naming, attribution readiness, and reporting hygiene for sales and marketing."
---

# Campaign Tracking

Use this skill when marketing and sales activity needs to be measurable and consistent across campaigns, CRM records, and reports.

## Workflow

1. Define tracking goals:
   - pipeline by campaign
   - lead quality by source
   - channel performance
   - outbound campaign performance
   - content or event attribution

2. Build a source taxonomy:
   - original_source
   - latest_source
   - source_detail
   - campaign_name
   - channel
   - medium
   - content_asset
   - audience_segment

3. Define UTM standards:
   - `utm_source`: platform or source
   - `utm_medium`: channel type
   - `utm_campaign`: campaign family and date
   - `utm_content`: creative, asset, or variation
   - `utm_term`: keyword or audience where relevant

4. Define naming rules:
   - lowercase where possible
   - no spaces
   - consistent date format
   - stable campaign family names
   - no ad hoc abbreviations

5. Define QA:
   - required fields before launch
   - sample link checks
   - CRM field mapping
   - dashboard visibility
   - owner for campaign setup

## Output

Create a campaign tracking plan:

| field | purpose | allowed values or format | owner | required |
|---|---|---|---|---|

Include example campaign names and UTM examples for the user's motion.
