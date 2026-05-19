---
name: seo-machine-publish-draft
description: "Use for SEO Machine publish-draft work in Codex. Publishes a draft article from this project to WordPress as a Draft, with all SEO metadata auto-populated."
---

# Publish Draft to WordPress

This is a Codex-native SEO Machine skill. Use it directly with `$seo-machine-publish-draft` and pass the same argument you would give the workflow, such as a topic, URL, file path, keyword, or options.

## Codex Operating Notes

- Read relevant files in `context/` before producing strategy, research, copy, metadata, or publishing payloads.
- Run any named specialist reviews by using the matching `seo-machine-*-specialist` skill instructions in `.agents/skills/`.
- Use `data_sources/modules/` and the root Python scripts when a workflow calls for deterministic analysis.
- If GA4, Search Console, DataForSEO, or the WordPress MCP connection is missing, complete the offline parts and clearly list skipped live-data checks.
- Save artifacts in the output directories named by the workflow.

Publishes a draft article from this project to WordPress as a Draft, with all SEO metadata auto-populated.

## Codex Invocation
`$seo-machine-publish-draft [filename] [--type post|page|custom]`

### Examples

**Create a blog post (default):**
```
$seo-machine-publish-draft drafts/content-marketing-guide-2025-12-10.md
```

**Create a page:**
```
$seo-machine-publish-draft drafts/pricing-comparison.md --type page
```

**Create a custom post type:**
```
$seo-machine-publish-draft drafts/product-comparison.md --type compare
```

### Post Types
- `post` - Standard blog post (default) - supports categories and tags
- `page` - WordPress page - no categories/tags
- Custom types (e.g., `compare`) - must be registered in WordPress with REST API support

## What This Skill Does

1. **Parses the draft file** - Extracts all metadata from frontmatter
2. **Converts Markdown to HTML** - Formats content for WordPress
3. **Creates WordPress draft** - Uses the connected WordPress MCP server to create content with status "draft"
4. **Sets SEO fields when the MCP server exposes them**:
   - SEO Title (from Meta Title)
   - Meta Description
   - Focus Keyphrase (from Target Keyword)
5. **Assigns taxonomy** - Categories and Tags if specified
6. **Returns edit URL** - Direct link to edit the post in WordPress

## Metadata Mapping

| Draft Field | WordPress/Yoast Field |
|-------------|----------------------|
| H1 Title | Post Title |
| Meta Title | Yoast SEO Title |
| Meta Description | Yoast Meta Description + Excerpt |
| Target Keyword | Yoast Focus Keyphrase |
| URL Slug | Post Slug |
| Category | Post Categories |
| Tags | Post Tags |
| Content | Post Content (HTML) |

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

## Process

When you run this skill:

### Step 1: Validate File
- Confirm the draft file exists
- Parse metadata and content
- Display extracted fields for confirmation

### Step 2: Publish via WordPress MCP

Use the connected WordPress MCP tools to:

1. Discover available WordPress abilities/tools.
2. Create a draft item for `$POST_TYPE` (`post`, `page`, or a supported custom type).
3. Set title, slug, excerpt, content HTML, status `draft`, taxonomy terms, and SEO metadata where supported.
4. Never publish directly; always create or update drafts only.

If the default MCP server exposes abilities through `mcp-adapter/execute-ability`, first discover the relevant create/update abilities, then execute them with the prepared payload.

### Step 3: Confirm Success
Display the WordPress edit URL so the user can review and publish.

## Fallback: REST Publisher

If WordPress MCP is unavailable but the user explicitly wants a fallback, use the legacy Python REST publisher:

```bash
python data_sources/modules/wordpress_publisher.py "$FILE_PATH" --type "$POST_TYPE"
```

This fallback requires `WORDPRESS_URL`, `WORDPRESS_USERNAME`, and `WORDPRESS_APP_PASSWORD` in the environment or `.env`.

## Optional: Add Categories/Tags

To assign categories or tags, add these fields to your draft frontmatter:

```markdown
**Category**: [Your Category]
**Tags**: [your topic], beginner, getting started
```

Multiple categories/tags are comma-separated.

## Troubleshooting

### "No WordPress MCP tools available"
Configure the WordPress MCP adapter and restart Codex so the MCP tools are available.

### "401 Unauthorized"
- For remote MCP, verify `WP_API_USERNAME` and `WP_API_PASSWORD`
- Regenerate the WordPress Application Password used by the MCP proxy
- Ensure the user has permission to create drafts

### "SEO fields not available"
Use the WordPress MCP abilities that your site exposes. If Yoast metadata is not exposed through MCP, set title, excerpt, slug, and content first, then finish SEO fields in WordPress admin or use the REST fallback.

## Notes

- Posts are always created as **drafts** (never published automatically)
- The H1 heading from the article becomes the WordPress post title
- Images/media are not uploaded - only text content is transferred
- Prefer updating an existing draft through MCP when one already exists; otherwise create a new draft
