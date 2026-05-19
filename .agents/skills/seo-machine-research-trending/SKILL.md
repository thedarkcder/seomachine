---
name: seo-machine-research-trending
description: "Use for SEO Machine research-trending work in Codex. Identify topics gaining search interest NOW for time-sensitive content opportunities."
---

# Research Trending Skill

This is a Codex-native SEO Machine skill. Use it directly with `$seo-machine-research-trending` and pass the same argument you would give the workflow, such as a topic, URL, file path, keyword, or options.

## Codex Operating Notes

- Read relevant files in `context/` before producing strategy, research, copy, metadata, or publishing payloads.
- Run any named specialist reviews by using the matching `seo-machine-*-specialist` skill instructions in `.agents/skills/`.
- Use `data_sources/modules/` and the root Python scripts when a workflow calls for deterministic analysis.
- If GA4, Search Console, DataForSEO, WordPress, or other credentials are missing, complete the offline parts and clearly list skipped live-data checks.
- Save artifacts in the output directories named by the workflow.

Identify topics gaining search interest NOW for time-sensitive content opportunities.

## Codex Invocation
`$seo-machine-research-trending`

## What This Skill Does

Analyzes search trends to find keywords experiencing rapid growth:
- Compares last 7 days vs previous 30 days
- Identifies topics with significant impression increases
- Calculates urgency based on growth rate
- Prioritizes by opportunity score
- Shows your current position for each trend

**⏰ TIME-SENSITIVE**: These are hot trends - act quickly before they cool or competition increases.

## Process

Execute trending analysis:
```bash
python3 research_trending.py
```

This will:
1. Get trending queries from GSC (7d vs 30d comparison)
2. Filter to minimum 20 impressions (avoid noise)
3. Enrich with search volume from DataForSEO
4. Analyze search intent
5. Calculate opportunity score based on:
   - Growth rate (40%)
   - Search volume (30%)
   - Current position advantage (30%)
6. Determine urgency level
7. Generate report: `research/trending-YYYY-MM-DD.md`

## Output

The report categorizes by urgency:

### 🔥 CRITICAL Urgency (+150% growth)
**Act within 1 week** - These topics are exploding NOW

Example:
- "ai content optimization" +429% growth
- Your position: 27
- Volume: 1,800/mo
- Action: Create comprehensive guide within 3-7 days

### ⚡ HIGH Urgency (+75% growth)
**Act within 2 weeks** - Strong upward trends

### ⏳ MODERATE Urgency (+30% growth)
**Act within 1 month** - Steady growth, monitor

For each trend:
- Growth percentage and trajectory
- Current position (your visibility)
- Search volume (if available)
- Opportunity score
- Specific action steps
- Timeline to act

## Key Actions

### If You Already Rank (Position ≤30)
**Quick Win!**
1. Update existing content immediately
2. Add trending angle/section
3. Update title with current year
4. Optimize for trending query
5. **Timeline**: 3-5 days

### If You Don't Rank (Position >30)
**New Content Needed**
1. Create comprehensive 2000+ word guide
2. Publish within 3-7 days
3. Promote on social immediately
4. Consider paid promotion to accelerate
5. **Timeline**: 1 week max

## Example Output

```
🔥 CRITICAL: "ai content optimization"
Growth: +429% (340 → 1,800 impressions)
Your Position: 27
Urgency: CRITICAL - Act within 1 week

Why It's Hot:
- Massive 4x growth spike
- Related queries also rising
- Topic will continue growing throughout 2025

Action: Create "Best AI Content Optimization Tools 2025"
Timeline: Complete within 7 days
```

## Strategy

### Week 1: Critical Trends Only
Focus all resources on 2-3 critical urgency trends
- Update existing content (if position ≤30)
- Create new content (if position >30)
- Publish and promote immediately

### Week 2: Monitor & High Urgency
- Check if critical trends maintained momentum
- Begin work on high urgency trends
- Track position changes for published content

### Week 3-4: Moderate Trends
- Work on moderate urgency items
- Run `$seo-machine-research-trending` again to catch new spikes

## Integration

After running `$seo-machine-research-trending`:
- Use `$seo-machine-research-serp [trending keyword]` for content requirements
- Use `$seo-machine-write [keyword]` to create content quickly
- Publish ASAP - timing is critical for trends

## Time & Cost

**Time:** 1-2 minutes
**API Cost:** ~$0.20-0.50 (if enriching with search volume)
**Cost:** Free for GSC trend data only

## When to Run

**WEEKLY** - Trends change fast, catch them early

- Monday morning: Identify weekend trends
- Before content planning: Prioritize time-sensitive content
- When traffic spikes: Understand what's driving it

## Warning

⚠️ **Not all trends sustain** - Some are temporary spikes

- Monitor trend continuation over 2-4 weeks
- Validate with search volume data if available
- Focus on trends aligned with your niche
- Seasonal spikes may not be worth pursuing
