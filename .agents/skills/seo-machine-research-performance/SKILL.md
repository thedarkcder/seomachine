---
name: seo-machine-research-performance
description: "Use for SEO Machine research-performance work in Codex. Categorize all content by traffic and rankings to prioritize optimization."
---

# Research Performance Skill

This is a Codex-native SEO Machine skill. Use it directly with `$seo-machine-research-performance` and pass the same argument you would give the workflow, such as a topic, URL, file path, keyword, or options.

## Codex Operating Notes

- Read relevant files in `context/` before producing strategy, research, copy, metadata, or publishing payloads.
- Run any named specialist reviews by using the matching `seo-machine-*-specialist` skill instructions in `.agents/skills/`.
- Use `data_sources/modules/` and the root Python scripts when a workflow calls for deterministic analysis.
- If GA4, Search Console, DataForSEO, WordPress, or other credentials are missing, complete the offline parts and clearly list skipped live-data checks.
- Save artifacts in the output directories named by the workflow.

Categorize all content by traffic and rankings to prioritize optimization.

## Codex Invocation
`$seo-machine-research-performance`

## What This Skill Does

Analyzes ALL your blog content and categorizes into 4 performance quadrants:

1. **⭐ Stars** - High traffic + Good rankings → Maintain & expand
2. **🚀 Overperformers** - High traffic + Poor rankings → Learn why, improve SEO
3. **⚠️ Underperformers** - Low traffic + Good rankings → Fix CTR (title/meta)
4. **📉 Declining** - Low traffic + Poor rankings → Refresh or redirect

For each piece:
- Traffic trends (rising/stable/declining)
- Expected vs actual traffic
- Specific action recommendations
- Priority level

## Process

Execute the performance matrix analysis:
```bash
python3 research_performance_matrix.py
```

This will:
1. Fetch all pages from GA4 (last 90 days)
2. Filter to content pages only
3. Enrich with GSC ranking data
4. Calculate traffic trends (180-day comparison)
5. Categorize into performance quadrants
6. Generate report: `research/performance-matrix-YYYY-MM-DD.md`

## Output

The report includes:
- Distribution across 4 quadrants
- Top performers in each category
- Specific action steps per article
- Expected traffic calculations
- Priority recommendations

## Key Insights

**Stars**: Your best content - keep fresh, expand with clusters
**Underperformers**: QUICK WINS - rewrite titles/meta for better CTR
**Declining**: Content losing traction - needs refresh or redirect
**Overperformers**: Getting traffic despite poor rankings - improve SEO

## Integration

After running `$seo-machine-research-performance`:
- Use `$seo-machine-analyze-existing [URL]` for detailed content analysis
- Fix underperformer titles/meta first (low effort, high impact)
- Refresh declining stars to prevent traffic loss

## Time & Requirements

**Time:** 2-4 minutes
**Requirements:** GA4 required, GSC recommended
**Cost:** Free

## When to Run

- **Monthly**: Monitor content health
- **After major updates**: Track impact
- **When traffic drops**: Identify declining content
