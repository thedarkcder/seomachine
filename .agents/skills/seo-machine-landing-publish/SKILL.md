---
name: seo-machine-landing-publish
description: "Use for SEO Machine landing-publish work in Codex. Use this skill to publish landing pages to WordPress as pages (not blog posts)."
---

# Landing Page Publish Skill

This is a Codex-native SEO Machine skill. Use it directly with `$seo-machine-landing-publish` and pass the same argument you would give the workflow, such as a topic, URL, file path, keyword, or options.

## Codex Operating Notes

- Read relevant files in `context/` before producing strategy, research, copy, metadata, or publishing payloads.
- Run any named specialist reviews by using the matching `seo-machine-*-specialist` skill instructions in `.agents/skills/`.
- Use `data_sources/modules/` and the root Python scripts when a workflow calls for deterministic analysis.
- If GA4, Search Console, DataForSEO, or the WordPress MCP connection is missing, complete the offline parts and clearly list skipped live-data checks.
- Save artifacts in the output directories named by the workflow.

Use this skill to publish landing pages to WordPress as pages (not blog posts).

## Codex Invocation
`$seo-machine-landing-publish [file path] [options]`

**Options:**
- `--noindex`: Set noindex meta (for PPC pages)
- `--template [slug]`: Use specific WordPress page template

**Examples:**
- `$seo-machine-landing-publish landing-pages/product-hosting-beginners-2025-12-11.md`
- `$seo-machine-landing-publish landing-pages/free-trial-ppc-2025-12-11.md --noindex`
- `$seo-machine-landing-publish landing-pages/pricing-comparison-2025-12-11.md --template landing-page`

## What This Skill Does

1. Validates the landing page file
2. Checks landing page score (must be ≥75)
3. Parses markdown and metadata
4. Creates WordPress page via the connected WordPress MCP server
5. Sets SEO fields when the MCP server exposes them
6. Returns edit URL for review

## Prerequisites

Before publishing, ensure:
1. Landing page score is ≥75 (run `$seo-machine-landing-audit` first)
2. No critical issues remain
3. All required metadata is present
4. Content has been scrubbed for AI watermarks

## File Format Requirements

Landing page files must include this metadata:

```markdown
# [H1 Headline]

**Meta Title**: [50-60 characters]
**Meta Description**: [150-160 characters]
**Target Keyword**: [primary keyword]
**Page Type**: seo | ppc
**Conversion Goal**: trial | demo | lead
**URL Slug**: /[page-slug]/

---

[Content...]
```

## Publishing Process

### Step 1: Validation

Check file exists and contains required fields:
- Meta Title (required)
- Meta Description (required)
- Target Keyword (required for SEO pages)
- Page Type
- Conversion Goal
- URL Slug

### Step 2: Score Check

Run landing page scorer:
```python
from data_sources.modules.landing_page_scorer import score_landing_page

score = score_landing_page(content, page_type, goal, meta_title, meta_description, keyword)

if score['overall_score'] < 75:
    print("Score too low. Fix issues before publishing.")
    print(f"Current score: {score['overall_score']}")
    print(f"Critical issues: {score['critical_issues']}")
    # Abort publishing
```

### Step 3: Content Preparation

1. Parse metadata from file header
2. Extract main content (markdown)
3. Convert markdown to HTML
4. Prepare Yoast SEO fields

### Step 4: WordPress MCP Call

Use the connected WordPress MCP tools to:

1. Discover available WordPress abilities/tools.
2. Create a WordPress page draft.
3. Set title, slug, excerpt, content HTML, status `draft`, template, and SEO metadata where supported.
4. Return the WordPress edit URL for user review.

If the default MCP server exposes abilities through `mcp-adapter/execute-ability`, first discover the relevant create/update abilities, then execute them with the prepared page payload.

### Step 5: Additional Settings

**For PPC Pages (--noindex):**
Set noindex metadata through MCP if the site exposes that ability. If no MCP ability supports it, note that the user must set noindex in WordPress/Yoast before publishing.

**For Page Templates:**
Set the page template through MCP if supported. If not supported, include the requested template slug in the final handoff.

## WordPress MCP Requirement

Publishing is MCP-first. Configure WordPress through the official `wordpress/mcp-adapter` package and connect Codex to that MCP server before using this skill.

Recommended connection options:

- **Local WordPress site**: use WP-CLI STDIO with `wp mcp-adapter serve --server=mcp-adapter-default-server`.
- **Remote WordPress site**: use `@automattic/mcp-wordpress-remote` to proxy from Codex's STDIO MCP connection to the site's HTTP endpoint.

Default MCP endpoint:

```text
/wp-json/mcp/mcp-adapter-default-server
```

Remote HTTP proxy environment:

```text
WP_API_URL=https://yoursite.com/wp-json/mcp/mcp-adapter-default-server
WP_API_USERNAME=your-username
WP_API_PASSWORD=your-application-password
```

Application Passwords are used by the remote MCP proxy, not by SEO Machine directly.

## Fallback: REST Publisher

If WordPress MCP is unavailable but the user explicitly wants a fallback, use `data_sources/modules/wordpress_publisher.py`. This legacy fallback requires direct WordPress REST credentials in the environment or `.env`.

## Output

### Successful Publish
```
=== Landing Page Published ===

Status: Draft created
Page ID: [ID]
Edit URL: https://yoursite.com/wp-admin/post.php?post=[ID]&action=edit

Next Steps:
1. Review the page in WordPress
2. Check formatting and images
3. Set featured image if needed
4. Publish when ready

Landing Page Score: [X]/100
```

### Failed Publish
```
=== Publishing Failed ===

Reason: [Error message]

If score too low:
- Current Score: [X]/100
- Required Score: 75/100
- Critical Issues:
  1. [Issue 1]
  2. [Issue 2]

Run `$seo-machine-landing-audit landing-pages/[file].md` for full analysis.
```

## Differences from $seo-machine-publish-draft

| Aspect | $seo-machine-publish-draft (Blog) | $seo-machine-landing-publish (Pages) |
|--------|----------------------|--------------------------|
| WordPress Type | Post | Page |
| Categories/Tags | Yes | No |
| Score Required | Content score ≥70 | Landing page score ≥75 |
| noindex Option | No | Yes (for PPC) |
| Template Option | No | Yes |
| Output Directory | drafts/ | landing-pages/ |

## Pre-Publish Checklist

Before running this skill, verify:

### Content
- [ ] Headline is benefit-focused
- [ ] Value proposition is clear
- [ ] CTAs use action verbs
- [ ] Trust signals present
- [ ] Risk reversal near CTAs
- [ ] FAQ section (for SEO pages)

### Meta
- [ ] Meta title 50-60 characters
- [ ] Meta title includes keyword
- [ ] Meta description 150-160 characters
- [ ] Meta description includes CTA
- [ ] URL slug is clean and short

### Technical
- [ ] Content scrubbed for AI watermarks
- [ ] Landing page score ≥75
- [ ] No critical issues
- [ ] Proper markdown formatting

## Post-Publish Tasks

After publishing to WordPress:

1. **Review in WordPress**
   - Check formatting displays correctly
   - Verify all links work
   - Ensure CTAs are prominent

2. **Add Visuals**
   - Set featured image
   - Add any hero images
   - Add trust badges/logos

3. **Final SEO Check**
   - Verify Yoast green lights
   - Check mobile preview
   - Validate schema if applicable

4. **Publish Live**
   - Change status from Draft to Published
   - Clear any caches
   - Verify live page loads correctly

## Rollback

If issues are found after publishing:

1. In WordPress, revert to draft status
2. Fix issues in the markdown file
3. Re-run `$seo-machine-landing-audit` to verify score
4. Re-publish with `$seo-machine-landing-publish`

## Integration with Other Skills

**Typical Workflow:**
```bash
# 1. Research (optional)
$seo-machine-landing-research "product hosting" --type seo

# 2. Create landing page
$seo-machine-landing-write "product hosting" --type seo --goal trial

# 3. Audit the draft
$seo-machine-landing-audit landing-pages/product-hosting-2025-12-11.md

# 4. Fix any issues (if needed)
# Edit the file manually

# 5. Re-audit until score ≥75
$seo-machine-landing-audit landing-pages/product-hosting-2025-12-11.md

# 6. Publish
$seo-machine-landing-publish landing-pages/product-hosting-2025-12-11.md
```
