# SEO Machine

A specialized Codex workspace for creating long-form, SEO-optimized blog content for any business. This system helps you research, write, analyze, and optimize content that ranks well and serves your target audience.

## Overview

SEO Machine is built on Codex and provides:
- **Codex Skills**: `$seo-machine-research`, `$seo-machine-write`, `$seo-machine-rewrite`, `$seo-machine-analyze-existing`, `$seo-machine-optimize`, `$seo-machine-performance-review`, `$seo-machine-publish-draft`, `$seo-machine-article`, `$seo-machine-priorities`, plus specialized research and landing page skills
- **AI SDR Skills**: `$sales`, account sourcing, batch prospecting, contact enrichment, verification, intent signals, lead scoring, cadence planning, approval queues, prospect research, outreach, follow-up, meeting prep, proposals, and sales reporting skills
- **Specialist Skills**: Content analyzer, SEO optimization, meta element creation, internal linking, keyword mapping, editor, performance analysis, headline generator, CRO analyst, landing page optimizer
- **Marketing Skills**: 26 marketing skills for copywriting, CRO, A/B testing, email sequences, pricing strategy, and more
- **Advanced SEO Analysis**: Search intent detection, keyword density & clustering, content length comparison, readability scoring, SEO quality rating (0-100)
- **Data Integrations**: Google Analytics 4, Google Search Console, DataForSEO for real-time performance insights
- **Context-Driven**: Brand voice, style guide, SEO guidelines, and examples guide all content
- **Workflow Organization**: Structured directories for topics, research, drafts, and published content

## Getting Started

### Prerequisites
- [Codex](https://developers.openai.com/codex) installed
- OpenAI account for Codex

### Installation

1. Clone this repository:
```bash
git clone https://github.com/thedarkcder/seomachine.git
cd seomachine
```

2. Install Python dependencies for analysis modules:
```bash
pip install -r data_sources/requirements.txt
```

This installs:
- Google Analytics/Search Console integrations
- DataForSEO API client
- NLP libraries (nltk, textstat)
- Machine learning (scikit-learn)
- Web scraping tools (beautifulsoup4)
- PDF report support for sales pipeline reports (reportlab)

3. Open in Codex:
```bash
codex .
```

4. **Customize Context Files** (Important!):

   All context files are provided as templates. Fill them out with your company's information:

   - `context/brand-voice.md` - Define your brand voice and messaging *(see examples/castos/ for reference)*
   - `context/writing-examples.md` - Add 3-5 exemplary blog posts from your site
   - `context/features.md` - List your product/service features and benefits
   - `context/internal-links-map.md` - Map your key pages for internal linking
   - `context/style-guide.md` - Fill in your style preferences
   - `context/target-keywords.md` - Add your keyword research and topic clusters
   - `context/competitor-analysis.md` - Add competitor analysis and insights
   - `context/seo-guidelines.md` - Review and adjust SEO requirements

   **Quick Start**: Check out `examples/castos/` to see a complete real-world example of all context files filled out for a podcast hosting SaaS company.

## Workflows

### AI SDR Sales Workflows

Sales skills use the `sales-*` namespace and are separate from SEO/content workflows.

```text
$sales-prospect https://example.com        # Full prospect audit
$sales-source-accounts "B2B SaaS CFOs"     # Account sourcing strategy
$sales-batch-prospect accounts.csv         # Batch score/prioritize accounts
$sales-enrich-contacts accounts.csv        # Contact enrichment plan
$sales-verify-emails contacts.csv          # Email verification/risk pass
$sales-intent-signals accounts.csv         # Buying signal prioritization
$sales-lead-score contacts.csv             # Lead/account scorecard
$sales-personalization contacts.csv        # Hooks and first-line angles
$sales-build-cadence "Series B SaaS CFOs"  # Multi-touch cadence
$sales-approval-queue drafts.md            # Human review queue
$sales-research https://example.com        # Company research
$sales-qualify https://example.com         # BANT + MEDDIC qualification
$sales-contacts https://example.com        # Buying committee mapping
$sales-outreach acme                       # Cold outreach sequence
$sales-followup acme                       # Follow-up sequence
$sales-prep https://example.com            # Meeting prep brief
$sales-proposal acme                       # Proposal draft
$sales-report                              # Pipeline report
```

The `$sales` router can also orient broad requests. The full AI SDR operations flow is: source accounts → batch prospect → enrich contacts → verify emails → read intent signals → score leads → personalize → build cadence → check deliverability → approval queue. Sales workflows generate drafts, recommendations, and reports by default; they do not send outreach or mutate CRM records without explicit approval and a configured tool.

### Creating New Content

#### 1. Start with Research
```
$seo-machine-research [topic]
```

**What it does**:
- Performs keyword research
- Analyzes top 10 competitors
- Identifies content gaps
- Creates comprehensive research brief
- Saves to `research/` directory

**Example**:
```
$seo-machine-research content marketing strategies for B2B SaaS
```

#### 2. Write the Article
```
$seo-machine-write [topic or research brief]
```

**What it does**:
- Creates 2000-3000+ word SEO-optimized article
- Maintains your brand voice from `context/brand-voice.md`
- Integrates keywords naturally
- Includes internal and external links
- Provides meta elements (title, description, keywords)
- Runs optimization specialist reviews
- Saves to `/drafts/` directory

**Example**:
```
$seo-machine-write content marketing strategies for B2B SaaS
```

**Specialist Review Passes**:
After writing, these specialists analyze the content:
- **SEO Optimizer**: On-page SEO recommendations
- **Meta Creator**: Multiple meta title/description options
- **Internal Linker**: Specific internal linking suggestions
- **Keyword Mapper**: Keyword placement and density analysis

#### 3. Final Optimization
```
$seo-machine-optimize [article file]
```

**What it does**:
- Comprehensive SEO audit
- Validates all elements meet requirements
- Provides final polish recommendations
- Generates publishing readiness score
- Creates optimization report

**Example**:
```
$seo-machine-optimize drafts/content-marketing-strategies-2025-10-29.md
```

### Updating Existing Content

#### 1. Analyze Existing Post
```
$seo-machine-analyze-existing [URL or file path]
```

**What it does**:
- Fetches and analyzes current content
- Evaluates SEO performance
- Identifies outdated information
- Assesses competitive positioning
- Provides content health score (0-100)
- Recommends update priority and scope
- Saves analysis to `research/` directory

**Examples**:
```
$seo-machine-analyze-existing https://yoursite.com/blog/marketing-guide
$seo-machine-analyze-existing published/marketing-guide-2024-01-15.md
```

#### 2. Rewrite/Update Content
```
$seo-machine-rewrite [topic or analysis file]
```

**What it does**:
- Updates content based on analysis findings
- Refreshes statistics and examples
- Improves SEO optimization
- Adds new sections to fill gaps
- Maintains what works from original
- Tracks changes made
- Saves to `rewrites/` directory

**Example**:
```
$seo-machine-rewrite marketing guide
```

## Skills Reference

### `$seo-machine-research [topic]`
Comprehensive keyword and competitive research for new content.

**Output**: Research brief in `research/brief-[topic]-[date].md`

**Includes**:
- Primary and secondary keywords
- Competitor analysis (top 10)
- Content gaps and opportunities
- Recommended outline
- Internal linking strategy
- Meta elements preview

---

### `$seo-machine-write [topic]`
Create long-form SEO-optimized article (2000-3000+ words).

**Output**: Article in `/drafts/[topic]-[date].md`

**Includes**:
- Complete article with H1/H2/H3 structure
- SEO-optimized content
- Internal and external links
- Meta elements (title, description, keywords)
- SEO checklist

**Auto-Triggers**:
- SEO Optimizer specialist
- Meta Creator specialist
- Internal Linker specialist
- Keyword Mapper specialist

---

### `$seo-machine-rewrite [topic]`
Update and improve existing content.

**Output**: Updated article in `rewrites/[topic]-rewrite-[date].md`

**Includes**:
- Rewritten/updated content
- Change summary
- Before/after comparison
- Updated SEO elements

---

### `$seo-machine-analyze-existing [URL or file]`
Analyze existing blog posts for improvement opportunities.

**Output**: Analysis report in `research/analysis-[topic]-[date].md`

**Includes**:
- Content health score (0-100)
- Quick wins (immediate improvements)
- Strategic improvements
- Rewrite priority and scope
- Research brief for rewrite

---

### `$seo-machine-optimize [file]`
Final SEO optimization pass before publishing.

**Output**: Optimization report in `/drafts/optimization-report-[topic]-[date].md`

**Includes**:
- SEO score (0-100)
- Priority fixes
- Quick wins
- Meta element options
- Link enhancement suggestions
- Publishing readiness assessment

---

### `$seo-machine-publish-draft [file]`
Create a WordPress draft through the connected WordPress MCP server, with SEO metadata where the site exposes it.

---

### `$seo-machine-article [topic]`
Simplified article creation workflow.

---

### `$seo-machine-priorities`
Content prioritization matrix using analytics data to identify highest-impact content tasks.

---

### `$seo-machine-scrub [file]`
Remove AI watermarks and patterns from content (em-dashes, filler phrases, robotic patterns).

---

### Research Skills

| Skill | Description |
|---------|-------------|
| `$seo-machine-research-serp [keyword]` | SERP analysis for a target keyword |
| `$seo-machine-research-gaps` | Competitor content gap analysis |
| `$seo-machine-research-trending` | Trending topic opportunities |
| `$seo-machine-research-performance` | Performance-based content priorities |
| `$seo-machine-research-topics` | Topic cluster research |

---

### Landing Page Skills

| Skill | Description |
|---------|-------------|
| `$seo-machine-landing-write [topic]` | Create conversion-optimized landing page |
| `$seo-machine-landing-audit [file]` | Audit landing page for CRO issues |
| `$seo-machine-landing-research [topic]` | Research competitors and positioning |
| `$seo-machine-landing-competitor [URL]` | Deep competitor landing page analysis |
| `$seo-machine-landing-publish [file]` | Publish landing page to WordPress |

## Specialists

Specialized specialists that analyze content and provide expert recommendations.

### Content Analyzer (NEW!)
**Purpose**: Comprehensive, data-driven content analysis using 5 specialized modules

**Analyzes**:
- Search intent classification (informational/navigational/transactional/commercial)
- Keyword density and clustering with topic detection
- Content length comparison vs top SERP competitors
- Readability scoring (Flesch Reading Ease, Flesch-Kincaid Grade Level)
- SEO quality rating (0-100 score with category breakdowns)
- Keyword stuffing risk detection
- Passive voice ratio and sentence complexity
- Distribution heatmap showing keyword placement by section

**Output**:
- Executive summary with publishing readiness assessment
- Priority action plan (critical/high priority/optimization)
- Competitive positioning analysis
- Detailed recommendations for each analysis area
- Exact metrics and benchmarks for improvements

**Powered by**:
- `search_intent_analyzer.py` - Search intent detection
- `keyword_analyzer.py` - Keyword density, clustering, LSI keywords
- `content_length_comparator.py` - SERP competitor analysis
- `readability_scorer.py` - Multiple readability metrics
- `seo_quality_rater.py` - Comprehensive SEO scoring

---

### SEO Optimizer
**Purpose**: On-page SEO analysis and optimization recommendations

**Analyzes**:
- Keyword optimization and density
- Content structure and headings
- Internal and external links
- Meta elements
- Readability and user experience
- Featured snippet opportunities

**Output**: SEO score (0-100) with specific improvement recommendations

---

### Meta Creator
**Purpose**: Generate high-converting meta titles and descriptions

**Creates**:
- 5 meta title variations (50-60 chars)
- 5 meta description variations (150-160 chars)
- Testing recommendations
- SERP preview
- Conversion-optimized copy

**Output**: Multiple options with recommendation and reasoning

---

### Internal Linker
**Purpose**: Strategic internal linking recommendations

**Provides**:
- 3-5 specific internal link suggestions
- Exact placement locations
- Anchor text recommendations
- User journey mapping
- SEO impact prediction

**References**: `context/internal-links-map.md`

---

### Keyword Mapper
**Purpose**: Keyword placement and integration analysis

**Analyzes**:
- Keyword density and distribution
- Critical placement checklist
- Natural language integration quality
- LSI keyword coverage
- Cannibalization risk

**Output**: Distribution map, gap analysis, specific revision suggestions

---

### Editor
**Purpose**: Transform technically accurate content into human-sounding, engaging articles

**Analyzes**:
- Voice and personality
- Specificity of examples
- Readability and flow
- Robotic vs. human patterns
- Engagement and storytelling

**Provides**:
- Humanity score (0-100)
- Critical edits with before/after
- Pattern analysis
- Specific rewrites to inject personality
- Readability improvements

**Output**: Editorial report with specific improvements to make content sound human

---

### Performance
**Purpose**: Data-driven content prioritization using real analytics

**Analyzes**:
- Google Analytics traffic and trends
- Google Search Console rankings and CTR
- DataForSEO competitive data
- Quick wins (position 11-20)
- Declining content
- Low CTR opportunities
- Trending topics

**Provides**:
- Priority queue of content tasks
- Opportunity scores (0-100)
- Impact and effort estimates
- Week-by-week roadmap
- Success metrics

**Output**: Comprehensive performance report with actionable priorities

---

### Headline Generator
**Purpose**: Generate high-converting headline variations and A/B testing recommendations

**Provides**:
- 10+ headline variations using proven formulas
- Conversion potential scoring
- A/B testing strategies
- Audience-specific headline options

---

### CRO Analyst
**Purpose**: Conversion rate optimization analysis for landing pages

**Analyzes**:
- Above-the-fold effectiveness
- CTA quality and distribution
- Trust signal presence
- Friction points
- Page structure

---

### Landing Page Optimizer
**Purpose**: Comprehensive landing page optimization recommendations

**Provides**:
- CRO scoring (0-100) with category breakdowns
- Above-fold, CTA, trust signal, structure, and SEO analysis
- A/B testing recommendations
- Priority action list

## Marketing Skills

SEO Machine includes 26 marketing skills accessible as skills:

| Category | Skills |
|----------|--------|
| **Copywriting** | `/copywriting`, `/copy-editing` |
| **CRO** | `/page-cro`, `/form-cro`, `/signup-flow-cro`, `/onboarding-cro`, `/popup-cro`, `/paywall-upgrade-cro` |
| **Strategy** | `/content-strategy`, `/pricing-strategy`, `/launch-strategy`, `/marketing-ideas` |
| **Channels** | `/email-sequence`, `/social-content`, `/paid-ads` |
| **SEO** | `/seo-audit`, `/schema-markup`, `/programmatic-seo`, `/competitor-alternatives` |
| **Analytics** | `/analytics-tracking`, `/ab-test-setup` |
| **Other** | `/referral-program`, `/free-tool-strategy`, `/marketing-psychology` |

## Data Sources

### Integration with Analytics

SEO Machine integrates with real-time data sources to inform content strategy:

**Google Analytics 4**:
- Traffic and engagement metrics
- Conversion tracking
- Trend analysis
- Traffic sources

**Google Search Console**:
- Keyword rankings and positions
- Impressions and clicks
- CTR analysis
- Query performance

**DataForSEO**:
- Competitive rankings
- SERP features
- Keyword metrics
- Competitor gap analysis

### Advanced SEO Analysis Modules (NEW!)

SEO Machine includes 5 specialized Python modules for comprehensive content analysis:

**Search Intent Analyzer** (`search_intent_analyzer.py`):
- Classifies queries into informational, navigational, transactional, or commercial intent
- Analyzes SERP features and content patterns
- Provides confidence scores and content alignment recommendations

**Keyword Analyzer** (`keyword_analyzer.py`):
- Calculates exact keyword density and distribution
- Detects keyword stuffing risk with warnings
- Performs topic clustering using TF-IDF and K-means
- Generates distribution heatmap by section
- Identifies LSI (semantically related) keywords

**SEO Quality Rater** (`seo_quality_rater.py`):
- Rates content against SEO best practices (0-100 score)
- Category breakdowns: content, keywords, meta, structure, links, readability
- Identifies critical issues, warnings, and suggestions
- Determines publishing readiness

**Content Length Comparator** (`content_length_comparator.py`):
- Fetches and analyzes top 10-20 SERP competitor word counts
- Calculates median, 75th percentile, and optimal length
- Shows competitive positioning and gap to target
- Provides data-driven expansion recommendations

**Readability Scorer** (`readability_scorer.py`):
- Flesch Reading Ease and Flesch-Kincaid Grade Level
- Sentence and paragraph structure analysis
- Passive voice detection and ratio calculation
- Complex word identification
- Transition word usage analysis
- Overall readability score (0-100)

All modules can be used directly in Python or through the Content Analyzer specialist.

### CRO Analysis Modules

Six Python modules for landing page conversion optimization:

- `above_fold_analyzer.py` - Above-the-fold content analysis (headline, value prop, CTA, trust)
- `cta_analyzer.py` - CTA effectiveness scoring (quality, distribution, goal alignment)
- `trust_signal_analyzer.py` - Trust signal detection (testimonials, social proof, risk reversals)
- `landing_page_scorer.py` - Overall landing page scoring (0-100 with category breakdowns)
- `landing_performance.py` - Landing page performance tracking via GA4/GSC
- `cro_checker.py` - CRO best practices checklist validation

### Additional Analysis Modules

- `opportunity_scorer.py` - 8-factor opportunity scoring for content prioritization
- `content_scorer.py` - 5-dimension content quality scoring (humanity, specificity, structure, SEO, readability)
- `engagement_analyzer.py` - Content engagement pattern analysis
- `competitor_gap_analyzer.py` - Competitive content gap identification
- `article_planner.py` - Data-driven article planning
- `section_writer.py` - Section-level content guidance
- `social_research_aggregator.py` - Social media research aggregation

### Python Research Scripts

Run from repo root:

```bash
# Content research
python3 research_quick_wins.py
python3 research_competitor_gaps.py
python3 research_performance_matrix.py
python3 research_priorities_comprehensive.py
python3 research_serp_analysis.py
python3 research_topic_clusters.py
python3 research_trending.py

# SEO analysis (config-driven - set up config/competitors.json first)
python3 seo_baseline_analysis.py
python3 seo_bofu_rankings.py
python3 seo_competitor_analysis.py

# Test API connectivity
python3 test_dataforseo.py
```

**Note**: SEO analysis scripts load competitor lists and keywords from `config/competitors.json`. Copy `config/competitors.example.json` and customize for your business.

### WordPress Integration

Publishing is MCP-first through the official [`wordpress/mcp-adapter`](https://github.com/wordpress/mcp-adapter). SEO Machine prepares the draft payload, then Codex uses the connected WordPress MCP tools to create draft posts or pages.

**Setup**:
1. Install and initialize `wordpress/mcp-adapter` on your WordPress site.
2. For local WordPress development, connect Codex with WP-CLI STDIO:
   ```bash
   wp mcp-adapter serve --server=mcp-adapter-default-server
   ```
3. For remote WordPress sites, use the `@automattic/mcp-wordpress-remote` proxy against:
   ```text
   https://yoursite.com/wp-json/mcp/mcp-adapter-default-server
   ```
4. Use the legacy REST publisher only as a fallback when MCP is unavailable.

See `wordpress/README.md` for fallback REST notes.

See `data_sources/README.md` for analytics setup instructions.

## Directory Structure

```
seomachine/
├── .agents/skills/
│   ├── skills/          # Custom workflow skills
│   │   ├── analyze-existing.md
│   │   ├── research.md
│   │   ├── write.md
│   │   ├── rewrite.md
│   │   ├── optimize.md
│   │   ├── scrub.md
│   │   ├── performance-review.md
│   │   ├── publish-draft.md
│   │   ├── article.md
│   │   ├── priorities.md
│   │   ├── research-serp.md
│   │   ├── research-gaps.md
│   │   ├── research-trending.md
│   │   ├── research-performance.md
│   │   ├── research-topics.md
│   │   ├── landing-write.md
│   │   ├── landing-audit.md
│   │   ├── landing-research.md
│   │   ├── landing-competitor.md
│   │   └── landing-publish.md
│   ├── specialists/            # Specialized analysis specialists
│   │   ├── content-analyzer.md
│   │   ├── seo-optimizer.md
│   │   ├── meta-creator.md
│   │   ├── internal-linker.md
│   │   ├── keyword-mapper.md
│   │   ├── editor.md
│   │   ├── performance.md
│   │   ├── headline-generator.md
│   │   ├── cro-analyst.md
│   │   └── landing-page-optimizer.md
│   └── skills/            # 26 marketing skills
├── data_sources/          # Analytics integrations
│   ├── modules/          # Python analysis modules
│   │   ├── google_analytics.py
│   │   ├── google_search_console.py
│   │   ├── dataforseo.py
│   │   ├── data_aggregator.py
│   │   ├── search_intent_analyzer.py
│   │   ├── keyword_analyzer.py
│   │   ├── seo_quality_rater.py
│   │   ├── content_length_comparator.py
│   │   ├── readability_scorer.py
│   │   ├── opportunity_scorer.py
│   │   ├── content_scorer.py
│   │   ├── engagement_analyzer.py
│   │   ├── social_research_aggregator.py
│   │   ├── competitor_gap_analyzer.py
│   │   ├── article_planner.py
│   │   ├── section_writer.py
│   │   ├── wordpress_publisher.py
│   │   ├── above_fold_analyzer.py
│   │   ├── cro_checker.py
│   │   ├── cta_analyzer.py
│   │   ├── landing_page_scorer.py
│   │   ├── landing_performance.py
│   │   └── trust_signal_analyzer.py
│   ├── config/           # API credentials (not in git)
│   ├── utils/            # Helper functions
│   ├── cache/            # Cached API responses
│   └── README.md         # Setup instructions
├── config/                # Configuration files
│   └── competitors.example.json  # Competitor config template
├── context/               # Configuration and guidelines
│   ├── brand-voice.md
│   ├── writing-examples.md
│   ├── style-guide.md
│   ├── seo-guidelines.md
│   ├── target-keywords.md
│   ├── internal-links-map.md
│   ├── competitor-analysis.md
│   └── cro-best-practices.md
├── wordpress/             # WordPress integration
│   ├── seo-machine-yoast-rest.php
│   ├── functions-snippet.php
│   └── README.md
├── topics/                # Raw topic ideas
├── research/              # Research briefs and analysis reports
├── drafts/                # Work in progress articles
├── review-required/       # Articles pending review
├── published/             # Final versions ready to publish
├── rewrites/              # Updated existing content
├── landing-pages/         # Landing page content
├── audits/                # Audit reports
└── README.md              # This file
```

## Context Files (Important!)

The quality of your content depends on well-configured context files:

### `context/brand-voice.md`
Defines your brand voice, tone, and messaging framework.

**Must include**:
- Voice pillars
- Tone guidelines by content type
- Core brand messages
- Writing style guidelines
- Terminology preferences

**Purpose**: Ensures all content sounds like your brand

---

### `context/writing-examples.md`
Contains 3-5 exemplary blog posts from your site.

**Must include**:
- Full article content
- What makes each example great
- Key takeaways for voice and structure

**Purpose**: Teaches AI your specific writing style through examples

---

### `context/style-guide.md`
Editorial and formatting standards.

**Must include**:
- Grammar and mechanics rules
- Capitalization conventions
- Formatting standards
- Preferred terminology

**Purpose**: Maintains consistency across all content

---

### `context/seo-guidelines.md`
SEO best practices and requirements.

**Includes**:
- Content length requirements
- Keyword optimization rules
- Meta element standards
- Link strategy guidelines
- Readability requirements

**Purpose**: Ensures all content meets SEO standards

---

### `context/target-keywords.md`
Keyword research organized by topic cluster.

**Must include**:
- Pillar keywords by cluster
- Cluster keywords (subtopics)
- Long-tail variations
- Search intent classification
- Current rankings

**Purpose**: Guides keyword targeting for new content

---

### `context/internal-links-map.md`
Catalog of key pages from your site for internal linking.

**Must include**:
- Product pages and features
- Pillar content URLs
- Top performing blog articles
- Topic cluster mapping
- Recommended anchor text

**Purpose**: Enables strategic internal linking in every article

---

### `context/competitor-analysis.md`
Competitive intelligence and content gaps.

**Must include**:
- Primary competitors
- Their content strategies
- Keyword gaps
- Differentiation opportunities

**Purpose**: Informs content strategy and competitive positioning

## Content Quality Standards

Every article must meet these requirements:

### Content
- [ ] Minimum 2,000 words (2,500-3,000+ preferred)
- [ ] Provides unique value vs. competitors
- [ ] Factually accurate and current
- [ ] Actionable advice for your target audience
- [ ] Brand voice maintained

### SEO
- [ ] Primary keyword density 1-2%
- [ ] Keyword in H1, first 100 words, 2-3 H2s
- [ ] 3-5 internal links with descriptive anchor text
- [ ] 2-3 external authority links
- [ ] Meta title 50-60 characters
- [ ] Meta description 150-160 characters
- [ ] Proper H1>H2>H3 hierarchy

### Readability
- [ ] 8th-10th grade reading level
- [ ] Average sentence length 15-20 words
- [ ] Paragraphs 2-4 sentences
- [ ] Subheadings every 300-400 words
- [ ] Lists and formatting for scannability

### Structure
- [ ] Compelling introduction (hook, problem, promise)
- [ ] Logical section flow
- [ ] Clear conclusion with CTA
- [ ] Examples and data included

## Best Practices

### Before Writing
1. **Research first**: Always run `$seo-machine-research` before `$seo-machine-write`
2. **Review context**: Read `brand-voice.md` and relevant `writing-examples.md`
3. **Check keywords**: Verify target keyword in `target-keywords.md`
4. **Plan internal links**: Review `internal-links-map.md` for linking opportunities

### During Writing
1. **Follow the brief**: Use research brief as your outline
2. **Natural keywords**: Integrate keywords naturally, never force them
3. **Add value**: Every section should provide actionable insights
4. **Use examples**: Include real scenarios and use cases from your industry
5. **Cite sources**: Link to statistics and data sources

### After Writing
1. **Review specialist output**: Read all specialist recommendations carefully
2. **Make improvements**: Address high-priority issues before optimizing
3. **Run optimize**: Use `$seo-machine-optimize` for final polish
4. **Self-edit**: Read article as if you're the target reader
5. **Check quality**: Verify all checklist items met

### For Rewrites
1. **Analyze first**: Run `$seo-machine-analyze-existing` to understand scope
2. **Determine strategy**: Light update vs. major rewrite?
3. **Preserve what works**: Keep effective sections
4. **Focus on gaps**: Add what's missing from competitive content
5. **Update everything**: Stats, examples, screenshots, links

## Workflow Examples

### Example 1: Creating New Content from Scratch

```
# Step 1: Add topic idea
# Create file in topics/ directory with initial thoughts

# Step 2: Research the topic
$seo-machine-research content marketing strategies

# Step 3: Review research brief
# Read research/brief-content-marketing-strategies-[date].md

# Step 4: Write article
$seo-machine-write content marketing strategies

# Step 5: Review specialist feedback
# Read all specialist reports in drafts/

# Step 6: Make improvements
# Edit article based on specialist recommendations

# Step 7: Final optimization
$seo-machine-optimize drafts/content-marketing-strategies-[date].md

# Step 8: Publish to WordPress (optional)
$seo-machine-publish-draft drafts/content-marketing-strategies-[date].md
```

### Example 2: Updating Existing Content

```
# Step 1: Analyze existing post
$seo-machine-analyze-existing https://yoursite.com/blog/product-comparison

# Step 2: Review analysis
# Read research/analysis-product-comparison-2025-10-29.md
# Check content health score and priority level

# Step 3: Rewrite content
$seo-machine-rewrite product comparison

# Step 4: Review changes
# Read rewrites/product-comparison-rewrite-2025-10-29.md
# Review change summary

# Step 5: Optimize
$seo-machine-optimize rewrites/product-comparison-rewrite-2025-10-29.md

# Step 6: Publish
# Move to published/ when ready
```

### Example 3: Quick Content Audit

```
# Analyze multiple existing posts to prioritize updates
$seo-machine-analyze-existing https://yoursite.com/blog/post-1
$seo-machine-analyze-existing https://yoursite.com/blog/post-2
$seo-machine-analyze-existing https://yoursite.com/blog/post-3

# Review content health scores
# Prioritize rewrites based on:
# - Lowest scores
# - Highest traffic potential
# - Strategic importance
```

## Tips & Tricks

### Maximizing Content Quality
- **Study examples**: Read your `writing-examples.md` before each writing session
- **Use data**: Always include current statistics and cite sources
- **Be specific**: "40% increase" beats "significant improvement"
- **Show, don't tell**: Use real examples and scenarios from your industry
- **Answer questions**: Address "People Also Ask" questions from research

### SEO Optimization
- **Keywords early**: Get primary keyword in first 100 words
- **Natural integration**: Read content aloud - if keywords sound forced, rewrite
- **Vary anchor text**: Don't use same anchor text for all internal links
- **Link strategically**: Link to pillar content and related cluster articles
- **Update regularly**: Refresh top-performing content every 6-12 months

### Workflow Efficiency
- **Batch research**: Research multiple topics in one session
- **Follow structure**: Use consistent article structure from `$seo-machine-write` skill
- **Address high-priority first**: Fix critical issues before optimizing details
- **Use specialists wisely**: Let specialists handle analysis, you focus on writing
- **Build templates**: Save commonly used sections for reuse

### Avoiding Common Mistakes
- ❌ Skipping research phase
- ❌ Ignoring brand voice guidelines
- ❌ Forcing keywords unnaturally
- ❌ Forgetting internal links
- ❌ Not citing data sources
- ❌ Publishing without optimization
- ❌ Copying competitor content instead of differentiating

## Maintenance

### Weekly
- Add new topic ideas to `/topics/`
- Update `target-keywords.md` with new keyword opportunities
- Check for broken links in `internal-links-map.md`

### Monthly
- Review published content performance
- Update `writing-examples.md` if better examples emerge
- Add newly published content to `internal-links-map.md`
- Track competitor activity in `competitor-analysis.md`

### Quarterly
- Full audit of context files
- Update SEO guidelines based on algorithm changes
- Comprehensive competitor analysis refresh
- Review and update topic clusters in `target-keywords.md`

## Troubleshooting

### "Content doesn't sound like my brand"
- **Solution**: Update `context/brand-voice.md` with more specific guidance
- **Solution**: Add more diverse examples to `context/writing-examples.md`
- **Solution**: Reference specific examples when using `$seo-machine-write` skill

### "Keyword density too high/low"
- **Solution**: Review `seo-guidelines.md` target density (1-2%)
- **Solution**: Use `$seo-machine-optimize` to get specific keyword placement suggestions
- **Solution**: Use Keyword Mapper specialist for distribution analysis

### "Internal links aren't relevant"
- **Solution**: Update `context/internal-links-map.md` with current pages
- **Solution**: Organize by topic cluster for easier specialist matching
- **Solution**: Provide more context about what each page covers

### "Articles too similar to competitors"
- **Solution**: Update `competitor-analysis.md` with differentiation opportunities
- **Solution**: Add your unique advantages to `brand-voice.md` and `features.md`
- **Solution**: Reference specific differentiation angles in `$seo-machine-research` skill

## Support & Contributions

### Getting Help
- Review this README thoroughly
- Check context files are properly configured
- Consult [Codex documentation](https://developers.openai.com/codex)

### Contributing
- Report issues via GitHub Issues
- Suggest improvements to skills or specialists
- Share successful workflows or tips

## License

[Add your license information]

## Credits

Built for Codex.

Originally developed for Castos, now available as an open-source tool for any business to streamline long-form SEO content creation.

## Examples & Community

**See It In Action**: Check out `examples/castos/` for a complete real-world example of how a podcast hosting SaaS company uses SEO Machine.

**Contributions Welcome**: Found a bug? Have a feature request? Want to share your own industry example? Contributions and PRs are welcome!

---

**Ready to start creating?**

1. Configure your context files (use the templates as your guide)
2. Run `$seo-machine-research [your topic]`
3. Review the brief
4. Run `$seo-machine-write [your topic]`
5. Publish amazing content!

Happy writing! 📝
