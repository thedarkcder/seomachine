---
name: seo-machine-research-serp
description: "Use for SEO Machine research-serp work in Codex. Deep SERP analysis for a specific keyword to understand what Google wants."
---

# Research SERP Skill

This is a Codex-native SEO Machine skill. Use it directly with `$seo-machine-research-serp` and pass the same argument you would give the workflow, such as a topic, URL, file path, keyword, or options.

## Codex Operating Notes

- Read relevant files in `context/` before producing strategy, research, copy, metadata, or publishing payloads.
- Run any named specialist reviews by using the matching `seo-machine-*-specialist` skill instructions in `.agents/skills/`.
- Use `data_sources/modules/` and the root Python scripts when a workflow calls for deterministic analysis.
- If GA4, Search Console, DataForSEO, WordPress, or other credentials are missing, complete the offline parts and clearly list skipped live-data checks.
- Save artifacts in the output directories named by the workflow.

Deep SERP analysis for a specific keyword to understand what Google wants.

## Codex Invocation
`$seo-machine-research-serp "keyword phrase"`

## What This Skill Does

Analyzes the top 10 ranking results for a keyword to provide detailed content requirements:
- Content type patterns (listicle, how-to, guide, etc.)
- Average word count and recommended length
- SERP features present (featured snippet, PAA, video, etc.)
- Freshness requirements
- Competitive difficulty
- Search intent
- Common content structure

Generates comprehensive content brief for creating or updating content.

## Process

Execute SERP analysis for a keyword:
```bash
python3 research_serp_analysis.py "your target keyword"
```

This will:
1. Fetch top 20 organic results from DataForSEO
2. Analyze content patterns in top 10
3. Detect content types from titles
4. Fetch word counts for each result
5. Identify SERP features
6. Analyze search intent
7. Assess competitive difficulty
8. Generate content brief
9. Create report: `research/serp-analysis-[keyword].md`

## Output

The report includes:

### Content Requirements
- Recommended word count (based on top 10 average + 10%)
- Dominant content type (what format works)
- Content type distribution

### SERP Features
- Featured snippet opportunity
- People Also Ask questions
- Video/image requirements
- Other SERP features present

### Content Brief
- Target specifications (word count, type, tone)
- Must-have elements
- Recommended structure
- SERP features to target
- Freshness requirements

### Competitive Analysis
- Domain authority mix
- Difficulty assessment
- Timeframe expectations

### Action Plan
Step-by-step process from research to publishing

## Example Use Cases

**Before creating new content**:
```
$seo-machine-research-serp "best project management tools"
```
Understand: Is this a listicle? How long should it be? What features to include?

**Before updating existing content**:
```
$seo-machine-research-serp "how to choose the right software"
```
Check if SERP patterns have changed, update to match current expectations

## Integration

After running `$seo-machine-research-serp`:
- Use the content brief to guide writing
- Use `$seo-machine-write [keyword]` with insights from SERP analysis
- Ensure content matches recommended structure and length

## Time & Cost

**Time:** 1-2 minutes per keyword
**API Cost:** ~$0.02 per keyword (DataForSEO)
**Cost:** Free for word count (if pages accessible)

## When to Run

- **Before creating any new content**: Know requirements upfront
- **Before major content updates**: Check current SERP expectations
- **When stuck on format**: See what type of content ranks
- **For competitive research**: Understand difficulty before committing
