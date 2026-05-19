---
name: seo-machine-scrub
description: "Use for SEO Machine scrub work in Codex. Use this skill to remove invisible AI-generated watermarks and telltale patterns from markdown content files."
---

# Scrub Skill

This is a Codex-native SEO Machine skill. Use it directly with `$seo-machine-scrub` and pass the same argument you would give the workflow, such as a topic, URL, file path, keyword, or options.

## Codex Operating Notes

- Read relevant files in `context/` before producing strategy, research, copy, metadata, or publishing payloads.
- Run any named specialist reviews by using the matching `seo-machine-*-specialist` skill instructions in `.agents/skills/`.
- Use `data_sources/modules/` and the root Python scripts when a workflow calls for deterministic analysis.
- If GA4, Search Console, DataForSEO, WordPress, or other credentials are missing, complete the offline parts and clearly list skipped live-data checks.
- Save artifacts in the output directories named by the workflow.

Use this skill to remove invisible AI-generated watermarks and telltale patterns from markdown content files.

## Codex Invocation
`$seo-machine-scrub [file path]`

## What This Skill Does
1. Removes invisible Unicode watermarks commonly embedded by AI systems
2. Replaces em-dashes with contextually appropriate punctuation
3. Cleans up whitespace and formatting artifacts
4. Makes content appear naturally human-written
5. Provides statistics on changes made

## Why This Matters

AI language models often embed invisible Unicode characters as watermarks or identifiers in generated content. Additionally, AI tends to overuse certain punctuation patterns like em-dashes. This skill removes these telltale signs to make content appear more naturally written.

## Process

### 1. Watermark Detection & Removal

The scrubber identifies and removes several types of invisible Unicode characters:

#### Invisible Characters Removed
- **Zero-width spaces** (U+200B): Often inserted between words
- **Byte Order Marks** (U+FEFF): BOM characters that shouldn't appear in content
- **Zero-width non-joiners** (U+200C): Invisible formatting characters
- **Word joiners** (U+2060): Non-breaking invisible characters
- **Soft hyphens** (U+00AD): Optional hyphenation points
- **Narrow no-break spaces** (U+202F): Special spacing characters
- **All format-control characters**: Unicode category Cf characters

### 2. Em-Dash Replacement

AI-generated content tends to overuse em-dashes (—). The scrubber intelligently replaces them based on context:

#### Contextual Rules
- **Attribution**: Replaces with comma when used for quotes or attribution
  - Example: "Text — Author Name" becomes "Text, Author Name"

- **Independent Clauses**: Replaces with semicolon when joining complete thoughts
  - Example: "First clause — second clause" becomes "First clause; second clause"

- **Strong Breaks**: Replaces with period when separating distinct sentences
  - Example: "Sentence one — Sentence two" becomes "Sentence one. Sentence two"

- **Simple Separation**: Replaces with comma for list items or simple separation
  - Example: "Item — detail" becomes "Item, detail"

- **Conjunctive Adverbs**: Replaces with semicolon before words like "however", "therefore", "moreover"
  - Example: "Text — however, more text" becomes "Text; however, more text"

### 3. Whitespace Normalization

After removing watermarks and replacing em-dashes, the scrubber cleans up formatting:

- **Multiple Spaces**: Reduces multiple consecutive spaces to single space
- **Punctuation Spacing**: Removes spaces before punctuation marks
- **Post-Punctuation Spacing**: Ensures single space after punctuation
- **Excessive Line Breaks**: Reduces 3+ consecutive line breaks to 2

## Output

The skill displays:

### Statistics Report
```
Content Scrubbing Complete:
  - Unicode watermarks removed: [count]
  - Format-control chars removed: [count]
  - Em-dashes replaced: [count]
```

### File Update
- Original file is overwritten with cleaned content
- All changes are applied in-place
- Original formatting and structure preserved (except cleaned elements)

## Integration with Writing Workflow

This skill is designed to run automatically after content generation:

### Automatic Execution
After `$seo-machine-write` or `$seo-machine-rewrite` skills save article files, the scrubber should run automatically on:
- Main article file in `drafts/` directory
- Any generated content that will be published

### Manual Execution
You can also manually scrub any markdown file:
- Testing content cleanliness
- Cleaning legacy content
- Processing externally generated content
- Verifying scrubbing was successful

## Technical Details

### Implementation
The scrubbing functionality is implemented in:
- **Module**: `data_sources/modules/content_scrubber.py`
- **Main Function**: `scrub_file(file_path, output_path, verbose)`
- **Class**: `ContentScrubber` with specialized methods for each cleaning operation

### Idempotency
The scrubber is idempotent - running it multiple times on already-cleaned content produces no additional changes. This makes it safe to:
- Run multiple times on same file
- Include in automated workflows
- Use as quality check without risk of over-processing

### Safety
The scrubbing process:
- Never modifies visible content or meaning
- Only removes invisible/problematic characters
- Preserves all markdown formatting
- Maintains document structure
- Safe for all content types

## Example Usage

### Basic Scrubbing
```
$seo-machine-scrub drafts/content-marketing-strategies-2025-10-31.md
```

### What Gets Changed

**Before:**
```
Content​ marketing​ is​ a​ powerful​ strategy—businesses can reach global audiences—and convert more customers.
```
(Contains zero-width spaces after words and em-dashes)

**After:**
```
Content marketing is a powerful strategy; businesses can reach global audiences, and convert more customers.
```
(Clean text with appropriate punctuation)

## Quality Standards

Every scrubbed file ensures:
- Zero invisible Unicode watermarks
- Natural punctuation patterns
- Clean whitespace formatting
- No telltale AI signatures
- Publish-ready cleanliness

## Best Practices

1. **Always Scrub Before Publishing**: Make this the final step before any content goes live
2. **Run on All AI-Generated Content**: Even if you edit the content, scrub it
3. **Check Statistics**: Review the stats to understand what was cleaned
4. **Test on Sample Content**: If unsure, scrub a copy first to verify results
5. **Include in Workflows**: Automate scrubbing in your content pipeline

This ensures all published content appears naturally written and free of AI indicators.
