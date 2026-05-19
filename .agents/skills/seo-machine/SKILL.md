---
name: seo-machine
description: "Use this skill for SEO Machine workflows in Codex: SEO research, article writing, rewriting, optimization, performance reviews, landing pages, AI citation research, marketing strategy, and WordPress publishing."
---

# SEO Machine for Codex

SEO Machine is a Codex-ready workspace for researching, writing, optimizing, refreshing, repurposing, and publishing SEO-focused content. It combines project context files, specialist review skills, Python analysis modules, and structured output folders.

## Operating Rules

1. Pick the most specific skill below for the user request.
2. Read relevant project context from `context/` before producing content or recommendations.
3. Use specialist skills for SEO, metadata, internal links, keyword mapping, editing, CRO, headlines, performance, and cluster strategy when a workflow calls for them.
4. Use Python modules in `data_sources/modules/` and root research scripts for deterministic analytics or scoring when credentials and dependencies are available.
5. If live credentials are unavailable, complete the static/offline portions and clearly state what could not be verified live.
6. Save generated work in the repo folders used by the workflow: `research/`, `topics/`, `drafts/`, `rewrites/`, `audits/`, `landing-pages/`, `repurposed/`, `published/`, or `output/`.

## Content Workflow Skills

- `$seo-machine-analyze-existing`: `Analyze Existing Skill`
- `$seo-machine-article`: `Article Skill`
- `$seo-machine-cluster`: `Cluster Skill`
- `$seo-machine-content-calendar`: `Content Calendar Skill`
- `$seo-machine-landing-audit`: `Landing Page Audit Skill`
- `$seo-machine-landing-competitor`: `Landing Page Competitor Analysis Skill`
- `$seo-machine-landing-publish`: `Landing Page Publish Skill`
- `$seo-machine-landing-research`: `Landing Page Research Skill`
- `$seo-machine-landing-write`: `Landing Page Write Skill`
- `$seo-machine-optimize`: `Optimize Skill`
- `$seo-machine-performance-review`: `Performance Review Skill`
- `$seo-machine-priorities`: `Priorities Skill`
- `$seo-machine-publish-draft`: `Publish Draft to WordPress`
- `$seo-machine-repurpose`: `Repurpose Skill`
- `$seo-machine-research-ai-citations`: `Research AI Citations Skill`
- `$seo-machine-research-gaps`: `Research Gaps Skill`
- `$seo-machine-research-performance`: `Research Performance Skill`
- `$seo-machine-research-serp`: `Research SERP Skill`
- `$seo-machine-research-topics`: `Research Topics Skill`
- `$seo-machine-research-trending`: `Research Trending Skill`
- `$seo-machine-research`: `Research Skill`
- `$seo-machine-rewrite`: `Rewrite Skill`
- `$seo-machine-scrub`: `Scrub Skill`
- `$seo-machine-write`: `Write Skill`

## Specialist Review Skills

- `$seo-machine-cluster-strategist-specialist`: `Cluster Strategist Specialist`
- `$seo-machine-content-analyzer-specialist`: `Content Analyzer Specialist`
- `$seo-machine-cro-analyst-specialist`: `CRO Analyst Specialist`
- `$seo-machine-editor-specialist`: `Editor Specialist`
- `$seo-machine-headline-generator-specialist`: `Headline Generator Specialist`
- `$seo-machine-internal-linker-specialist`: `Internal Linker Specialist`
- `$seo-machine-keyword-mapper-specialist`: `Keyword Mapper Specialist`
- `$seo-machine-landing-page-optimizer-specialist`: `Landing Page Optimizer Specialist`
- `$seo-machine-meta-creator-specialist`: `Meta Creator Specialist`
- `$seo-machine-performance-specialist`: `Performance Specialist`
- `$seo-machine-seo-optimizer-specialist`: `SEO Optimizer Specialist`

## Data Setup

Install Python dependencies with:

```bash
pip install -r data_sources/requirements.txt
```

Copy and fill environment files only when live integrations are needed:

```bash
cp .env.example data_sources/config/.env
```

Codex requires normal Codex/OpenAI authentication. The live integrations require their own credentials, such as GA4, Search Console, DataForSEO, or WordPress.
