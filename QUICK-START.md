# Quick Start Guide

Get SEO Machine running in **10 minutes** ⚡

## Step 1: Install Dependencies (2 min)

```bash
# Install Python dependencies for analysis modules
pip install -r data_sources/requirements.txt
```

## Step 2: Configure Context Files (5 min)

Fill out these **3 essential files** with your company info:

### 1. Brand Voice (`context/brand-voice.md`)
- Define 3-5 voice pillars
- Add tone guidelines
- Include do's and don'ts

💡 **Tip**: Check `examples/castos/brand-voice.md` for a complete example

### 2. Features (`context/features.md`)
- List your product/service features
- Add value propositions
- Include key differentiators

### 3. Writing Examples (`context/writing-examples.md`)
- Copy/paste 3-5 of your best blog posts
- Include full content (not just excerpts)
- Note what makes each example great

**Optional but recommended**:
- `internal-links-map.md` - Map your key pages
- `target-keywords.md` - Add keyword research

## Step 3: Create Your First Article (3 min)

```bash
# Open in Codex
codex .

# Research a topic
$seo-machine-research [your topic]

# Review the research brief in research/ directory

# Write the article
$seo-machine-write [your topic]

# Check /drafts/ for your article + optimization reports
```

## That's It! 🎉

You now have:
- ✅ A comprehensive, SEO-optimized article (2000+ words)
- ✅ Meta elements (title, description, keywords)
- ✅ SEO optimization report
- ✅ Internal linking suggestions
- ✅ Keyword analysis

## Next Steps

**To publish:**
1. Review the article in `/drafts/`
2. Make any final edits
3. Copy to your CMS
4. Publish and watch it rank!

**To improve quality:**
- Add more writing examples to `context/writing-examples.md`
- Refine your brand voice in `context/brand-voice.md`
- Map more internal links in `context/internal-links-map.md`

## Common Skills

```text
# Core workflow
$seo-machine-research [topic]           # Research before writing
$seo-machine-write [topic]              # Create new article
$seo-machine-article [topic]            # Simplified article creation
$seo-machine-rewrite [topic]            # Update old content
$seo-machine-optimize [file]            # Final SEO polish
$seo-machine-scrub [file]               # Remove AI watermarks
$seo-machine-publish-draft [file]       # Publish to WordPress

# Analysis
$seo-machine-analyze-existing [URL]     # Analyze existing post
$seo-machine-performance-review         # Analytics-driven priorities
$seo-machine-priorities                 # Content prioritization matrix

# Research
$seo-machine-research-serp [keyword]    # SERP analysis
$seo-machine-research-gaps              # Competitor content gaps
$seo-machine-research-trending          # Trending topics
$seo-machine-research-topics            # Topic clusters

# Landing pages
$seo-machine-landing-write [topic]      # Create landing page
$seo-machine-landing-audit [file]       # Audit for CRO issues
$seo-machine-landing-research [topic]   # Research positioning
```

## Need Help?

- Full Documentation: See README.md
- Real Example: Check `examples/castos/` directory
- Issues: https://github.com/thedarkcder/seomachine/issues

---

**Pro Tip**: The quality of your output depends on the quality of your context files. Spend time filling them out thoroughly!
