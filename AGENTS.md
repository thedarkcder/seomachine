# AGENTS.md

This file provides guidance to Codex when working with code in this repository.

## Project Overview

SEO Machine is an open-source Codex workspace for creating SEO-optimized blog content. It combines Codex skills, specialist skills, and Python-based analytics to research, write, optimize, and publish articles for any business.

## Setup

```bash
pip install -r data_sources/requirements.txt
```

API credentials are configured in `data_sources/config/.env` (GA4, GSC, DataForSEO, WordPress). GA4 service account credentials go in `credentials/ga4-credentials.json`.

## Skills

All workflow and specialist skills are defined in `.agents/skills/` and invoked as skills:

- `$seo-machine-research [topic]` - Keyword/competitor research, generates brief in `research/`
- `$seo-machine-write [topic]` - Create full article in `drafts/`, runs follow-up optimization specialist passes
- `$seo-machine-rewrite [topic]` - Update existing content, saves to `rewrites/`
- `$seo-machine-optimize [file]` - Final SEO polish pass
- `$seo-machine-analyze-existing [URL or file]` - Content health audit
- `$seo-machine-performance-review` - Analytics-driven content priorities
- `$seo-machine-publish-draft [file]` - Publish to WordPress via REST API
- `$seo-machine-article [topic]` - Simplified article creation
- `$seo-machine-cluster [topic]` - Build complete topic cluster strategy with pillar + supporting articles + linking map
- `$seo-machine-priorities` - Content prioritization matrix
- `$seo-machine-research-serp`, `$seo-machine-research-gaps`, `$seo-machine-research-trending`, `$seo-machine-research-performance`, `$seo-machine-research-topics` - Specialized research skills
- `$seo-machine-research-ai-citations [topic]` - AI citation audit: generates prompts, clusters them, audits which sources AI cites
- `$seo-machine-repurpose [file]` - Adapts article for LinkedIn, Medium, Reddit, Quora distribution
- `$seo-machine-landing-write`, `$seo-machine-landing-audit`, `$seo-machine-landing-research`, `$seo-machine-landing-publish`, `$seo-machine-landing-competitor` - Landing page skills

## Architecture

### Skill-Specialist Model

**Workflow skills** (`.agents/skills/seo-machine-*`) orchestrate work. **Specialist skills** (`.agents/skills/seo-machine-*-specialist`) provide focused review passes. After `$seo-machine-write`, these specialists auto-run: SEO Optimizer, Meta Creator, Internal Linker, Keyword Mapper.

Key specialist skills: `seo-machine-content-analyzer-specialist`, `seo-machine-seo-optimizer-specialist`, `seo-machine-meta-creator-specialist`, `seo-machine-internal-linker-specialist`, `seo-machine-keyword-mapper-specialist`, `seo-machine-editor-specialist`, `seo-machine-headline-generator-specialist`, `seo-machine-cro-analyst-specialist`, `seo-machine-performance-specialist`, `seo-machine-cluster-strategist-specialist`.

### Python Analysis Pipeline

Located in `data_sources/modules/`. The Content Analyzer chains:
1. `search_intent_analyzer.py` - Query intent classification
2. `keyword_analyzer.py` - Density, distribution, stuffing detection
3. `content_length_comparator.py` - Benchmarks against top 10 SERP results
4. `readability_scorer.py` - Flesch Reading Ease, grade level
5. `seo_quality_rater.py` - Comprehensive 0-100 SEO score

### Data Integrations

- `google_analytics.py` - GA4 traffic/engagement data
- `google_search_console.py` - Rankings and impressions
- `dataforseo.py` - SERP positions, keyword metrics
- `data_aggregator.py` - Combines all sources into unified analytics
- `wordpress_publisher.py` - Publishes to WordPress with Yoast SEO metadata

### Opportunity Scoring

`opportunity_scorer.py` uses 8 weighted factors: Volume (25%), Position (20%), Intent (20%), Competition (15%), Cluster (10%), CTR (5%), Freshness (5%), Trend (5%).

## Running Python Scripts

```bash
# Research & analysis scripts (run from repo root)
python3 research_quick_wins.py
python3 research_competitor_gaps.py
python3 research_performance_matrix.py
python3 research_priorities_comprehensive.py
python3 research_serp_analysis.py
python3 research_topic_clusters.py
python3 research_trending.py
python3 seo_baseline_analysis.py
python3 seo_bofu_rankings.py
python3 seo_competitor_analysis.py

# Test API connectivity
python3 test_dataforseo.py
```

## Content Pipeline

`topics/` (ideas) → `research/` (briefs) → `drafts/` (articles) → `review-required/` (pending review) → `published/` (final)

Rewrites go to `rewrites/`. Landing pages go to `landing-pages/`. Audits go to `audits/`. Repurposed content goes to `repurposed/`.

## Context Files

`context/` contains brand guidelines that inform all content generation:
- `brand-voice.md` - Tone, messaging pillars
- `style-guide.md` - Grammar, formatting standards
- `seo-guidelines.md` - Keyword and structure rules
- `internal-links-map.md` - Key pages for internal linking
- `features.md` - Product features
- `competitor-analysis.md` - Competitive intelligence
- `cro-best-practices.md` - Conversion optimization guidelines
- `ai-citation-targets.md` - Directories/platforms where your brand should be cited by AI tools
- `reddit-strategy.md` - Reddit engagement strategy for AI SEO and community visibility

## WordPress Integration

Publishing uses the WordPress REST API with a custom MU-plugin (`wordpress/seo-machine-yoast-rest.php`) that exposes Yoast SEO fields. Articles are published in WordPress block format (HTML comments in Markdown files).
