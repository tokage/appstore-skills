---
name: App Store Listing Generator
description: Generate App Store listing materials with ASO optimization by analyzing PRD, design docs, and code
---

# App Store Listing Generator Skill

This skill helps you generate comprehensive App Store listing materials optimized for search visibility (ASO - App Store Optimization). It analyzes your app's PRD, design documents, and codebase to create compelling, keyword-optimized content.

## Overview

The skill collects information from multiple sources and generates:
- App Name (optimized for search)
- Subtitle (30 characters)
- Promotional Text (170 characters)
- Description (4000 characters max)
- Keywords (100 characters, comma-separated)
- What's New (release notes)
- Privacy Policy summary
- Support URL content suggestions

## Usage

### Step 1: Gather App Information

Collect the following materials from the project:

1. **Product Requirements Document (PRD)**
   - Look for files like `PRD.md`, `README.md`, `PRODUCT.md`, or similar
   - Extract: core features, target audience, value proposition, use cases

2. **Design Documents**
   - UI/UX specifications
   - User flows and interaction patterns
   - Visual design principles

3. **Codebase Analysis**
   - Main features from view files (SwiftUI views, React components, etc.)
   - Key functionality from service/business logic files
   - Localization files for existing copy
   - Configuration files for app metadata

4. **Existing Marketing Materials**
   - Current app descriptions
   - Website copy
   - Social media descriptions

### Step 2: ASO Keyword Research

**Keyword Optimization Strategy:**

1. **Primary Keywords** (High priority)
   - Core functionality keywords (e.g., "party games", "decision maker", "random picker")
   - Category-defining terms
   - Problem-solution keywords

2. **Secondary Keywords** (Medium priority)
   - Feature-specific terms
   - Use case keywords
   - Alternative phrasings

3. **Long-tail Keywords** (Lower competition)
   - Specific feature combinations
   - Niche use cases

**ASO Best Practices:**
- Front-load important keywords in title and subtitle
- Use keywords naturally in description (first 2-3 lines are critical)
- Avoid keyword stuffing
- Include action verbs and emotional triggers
- Consider localization for target markets
- Research competitor keywords

### Step 3: Generate Content

Create content following App Store guidelines:

#### App Name (30 characters max)
- Include primary keyword if possible
- Keep it memorable and brandable
- Format: `[Brand Name] - [Primary Keyword]` or `[Brand Name]: [Value Prop]`

#### Subtitle (30 characters max)
- Clarify what the app does
- Include secondary keyword
- Complement the app name

#### Promotional Text (170 characters max)
- Highlight current features or promotions
- Can be updated without new version
- Use for seasonal content or new features

> **⚠️ IMPORTANT: NO EMOJI IN APP STORE METADATA**
> 
> App Store metadata fields (App Name, Subtitle, Promotional Text, Description, Keywords, What's New) **DO NOT support emoji characters**. Using emoji will cause display issues or rejection.
> 
> - ❌ Don't use: 🎉 🎮 ✨ 🚀 or any emoji
> - ✅ Use instead: Text-based emphasis, bullet points, or descriptive language
> 
> Emoji can only be used in screenshots (as part of the app UI being captured).

#### Description (4000 characters max)

**Structure:**
1. **Hook (First 2-3 lines)** - Visible before "more" button
   - Clear value proposition
   - Include primary keywords
   - Emotional appeal or problem statement

2. **Key Features Section**
   - Bullet points for features
   - Benefit-focused (not just feature list)
   - Include relevant keywords naturally

3. **Use Cases / Who It's For**
   - Specific scenarios
   - Target audience identification

4. **Social Proof** (if available)
   - Awards, press mentions
   - User testimonials
   - Download/rating milestones

5. **Call to Action**
   - Encourage download
   - Highlight unique value

**Formatting Tips:**
- Use line breaks for readability
- Short paragraphs (2-3 lines max)
- Bullet points for features
- **NO EMOJI** - App Store metadata does not support emoji characters

#### Keywords (100 characters max)
- Comma-separated, no spaces after commas
- No app name repetition (waste of space)
- Singular vs plural (choose one)
- No duplicate keywords
- Mix of high-volume and long-tail terms

#### What's New (4000 characters max)
- Lead with most exciting changes
- Use bullet points
- Keep it concise and scannable
- Include keywords when natural
- Maintain brand voice

### Step 4: Localization Considerations

For each target market:
- Research local keyword trends
- Adapt cultural references
- Consider local competitors
- Adjust tone and style for market
- Translate naturally (not literal)

### Step 5: Review and Optimize

**Quality Checklist:**
- [ ] All character limits respected
- [ ] Primary keywords in title/subtitle
- [ ] Description hook is compelling
- [ ] Keywords are comma-separated, no spaces
- [ ] No prohibited content (superlatives without proof, emoji, etc.)
- [ ] No emoji characters (not supported in App Store metadata)
- [ ] Consistent brand voice
- [ ] Clear call-to-action
- [ ] Proofread for grammar/spelling
- [ ] Mobile-friendly formatting (short paragraphs)

## Implementation Guide

When a user requests App Store listing generation:

### 1. Information Collection Phase

```markdown
I'll help you generate App Store listing materials. Let me gather information about your app.

**Searching for:**
- Product documentation (PRD, README)
- Design specifications
- Main feature implementations
- Existing localization/marketing copy
```

Use these tools:
- `find_by_name` - Find PRD, README, design docs
- `grep_search` - Search for feature keywords, app descriptions
- `view_file` - Read documentation files
- `view_file_outline` - Understand code structure
- `view_code_item` - Analyze key features

### 2. Analysis Phase

Extract and synthesize:
- **Core Value Proposition**: What problem does it solve?
- **Key Features**: Top 5-7 features
- **Target Audience**: Who is this for?
- **Unique Differentiators**: What makes it special?
- **Use Cases**: When/why would someone use this?

### 3. Keyword Strategy Phase

Based on analysis:
1. Generate primary keyword candidates (5-10)
2. Generate secondary keywords (10-15)
3. Generate long-tail keywords (10-20)
4. Prioritize by relevance and search potential

### 4. Content Generation Phase

Create a comprehensive listing document with:
- Multiple app name options (with keyword variations)
- Subtitle options
- Promotional text options
- Full description (with ASO optimization)
- Keyword list (optimized for 100 char limit)
- What's New template

### 5. Review and Iteration

Present to user with:
- Rationale for keyword choices
- ASO strategy explanation
- Alternative options for key sections
- Suggestions for A/B testing

## Output Format

Generate a markdown file: `app-store-listing.md`

```markdown
# App Store Listing - [App Name]

## App Name Options

### Option 1 (Recommended)
**Name**: [Name] - [Keyword]
**Character Count**: X/30
**ASO Strategy**: [Explanation]

### Option 2
...

## Subtitle Options

### Option 1 (Recommended)
**Subtitle**: [Subtitle]
**Character Count**: X/30
**Keywords**: [Keywords used]

## Promotional Text

[170 character promotional text]
**Character Count**: X/170

## Description

[Full 4000 character description with sections clearly marked]

**Character Count**: X/4000
**Keywords Included**: [List of keywords naturally incorporated]

## Keywords

[Comma-separated keyword list]
**Character Count**: X/100

### Keyword Strategy
- **Primary**: [List]
- **Secondary**: [List]
- **Long-tail**: [List]

## What's New Template

[Template for release notes]

## Localization Notes

[Market-specific considerations]

## A/B Testing Suggestions

[Elements to test]
```

## ASO Advanced Tips

### Keyword Research Sources
1. **Competitor Analysis**
   - Search top apps in category
   - Analyze their titles, subtitles, descriptions
   - Note keyword patterns

2. **App Store Search**
   - Type partial keywords, see autocomplete
   - Check "You might also like" suggestions
   - Review category rankings

3. **User Language**
   - App reviews (how users describe the app)
   - Support tickets (problems they're solving)
   - Social media mentions

### Optimization Cycle
1. Launch with initial keywords
2. Monitor search rankings (App Store Connect)
3. Track conversion rates
4. A/B test variations
5. Update based on performance data
6. Repeat every 2-3 months

### Common Mistakes to Avoid
- ❌ Keyword stuffing (unnatural repetition)
- ❌ Using app name in keyword field
- ❌ Spaces after commas in keywords
- ❌ Duplicate keywords (singular/plural)
- ❌ Generic descriptions without keywords
- ❌ Burying value prop below fold
- ❌ Ignoring localization opportunities
- ❌ Superlatives without proof ("best", "top")
- ❌ **Using emoji in metadata fields** (not supported, will cause issues)

## Example Workflow

```
User: "Generate App Store listing for my app"

Agent:
1. Search for PRD/README in project
2. Analyze main view files for features
3. Check localization files for existing copy
4. Synthesize information
5. Generate keyword strategy
6. Create listing content with options
7. Present with ASO rationale
8. Iterate based on feedback
```

## Additional Resources

### Character Limits Reference
- App Name: 30 characters
- Subtitle: 30 characters
- Promotional Text: 170 characters
- Description: 4000 characters
- Keywords: 100 characters (comma-separated)
- What's New: 4000 characters

### App Store Guidelines
- No false claims or misleading information
- No references to other platforms
- No pricing info (unless IAP)
- Appropriate content rating
- Privacy policy required for certain categories

## Notes

- Always verify character counts
- Test readability on mobile (description preview)
- Consider seasonal updates to promotional text
- Keep brand voice consistent across all copy
- Update keywords based on performance data
- Localize for each target market, don't just translate
