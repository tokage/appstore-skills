---
name: App Store Screenshot Generator
description: Generate professional App Store marketing screenshots by compositing app screenshots into device bezels with custom backgrounds and text overlays
---

# App Store Screenshot Generator Skill

This skill helps you create professional, eye-catching App Store marketing screenshots that meet Apple's strict requirements. It composites your app screenshots into realistic device bezels with gradient backgrounds and text overlays.

## Overview

The skill automates the creation of marketing screenshots by:
- **Auto-detecting device type** from screenshot dimensions
- **Compositing screenshots** into realistic iPhone bezels
- **Adding gradient backgrounds** with customizable colors
- **Overlaying text** (app name and tagline) with proper styling
- **Meeting App Store requirements** for dimensions and format
- **Batch processing** multiple screenshots at once

## When to Use This Skill

Use this skill when you need to:
- Create marketing screenshots for App Store submission
- Generate promotional images for your app's product page
- Produce consistent, professional-looking screenshot sets
- Add branding and context to raw app screenshots
- Quickly iterate on different color schemes and messaging

## Prerequisites

Before using this skill, ensure you have:
1. **Raw app screenshots** captured from Xcode Simulator or actual devices
2. **App information** (app name, taglines for each feature)
3. **Brand colors** (optional, for custom gradient backgrounds)
4. **Python 3.7+** installed on your system

## Usage Workflow

### Step 1: Gather App Screenshots

First, collect your raw app screenshots:

**From Xcode Simulator:**
```bash
# Run your app in simulator, navigate to desired screen, press Cmd+S
# Screenshots are saved to Desktop by default
```

**Required screenshot dimensions** (portrait):
- **iPhone 6.9"** (1320 x 2868) - **REQUIRED** for App Store
- iPhone 6.7" (1290 x 2796)
- iPhone 6.3" (1206 x 2622)
- iPhone 6.1" (1179 x 2556)

**Tips:**
- Capture screenshots showing your app's best features
- Use realistic, attractive content (no placeholder text)
- Ensure UI is in final state
- Take 5-10 screenshots highlighting different features

### Step 2: Analyze App Context

To generate appropriate titles and taglines, gather:

1. **Product documentation**
   - PRD or README with feature descriptions
   - Value propositions for each feature
   
2. **Marketing materials** (if available)
   - App Store description
   - Brand guidelines (colors, tone of voice)
   - Existing taglines or slogans

3. **Screenshot inventory**
   - List all screenshot files
   - Note what feature each screenshot shows

### Step 3: Generate Configuration

Ask the AI assistant to analyze your screenshots and generate a configuration file:

**Basic request:**
```
"I have 5 app screenshots in screenshots/:
- screenshots/home.png (main screen)
- screenshots/dice.png (dice feature)
- screenshots/wheel.png (wheel feature)
- screenshots/balloon.png (balloon game)
- screenshots/drum.png (drum game)

Please analyze each screenshot and generate a screenshots_config.json file with:
- Appropriate titles and taglines for each
- Gradient colors that match my app's playful, colorful theme
- Proper device detection
"
```

**Advanced request with context:**
```
"I have 5 app screenshots and additional context:
- Screenshots in screenshots/ folder
- PRD.md with feature descriptions
- app-store-listing-zh.md with App Store copy

Please analyze these materials and generate screenshots_config.json with:
- Titles/taglines aligned with our brand voice (fun, energetic)
- Gradient colors incorporating our brand palette
- Each tagline highlighting the specific feature shown
"
```

**What the AI will do:**
- Detect device type from screenshot dimensions
- Analyze screenshot content to understand features
- Review context documents for brand voice and messaging
- Suggest titles/taglines aligned with your brand
- Recommend color schemes matching your brand
- Generate a complete, ready-to-use JSON configuration

### Step 4: Review and Customize Configuration

The generated `screenshots_config.json` will look like:

```json
{
  "canvas_size": "iPhone 6.9",
  "bezels_dir": "product-bezels",
  "screenshots": [
    {
      "input": "screenshots/home.png",
      "title": "PartyPal",
      "tagline": "聚会玩具箱",
      "background": {
        "top": "#A855F7",
        "bottom": "#3B82F6"
      },
      "output": "marketing/screenshot_1.png"
    },
    {
      "input": "screenshots/dice.png",
      "title": "PartyPal",
      "tagline": "Q弹骰子 真实物理",
      "color": "Deep Blue",
      "background": {
        "top": "#10B981",
        "bottom": "#3B82F6"
      },
      "output": "marketing/screenshot_2.png"
    }
  ]
}
```

**Customization options:**
- `title`: App name or feature title
- `tagline`: Short description (3-5 words work best)
- `background.top` / `background.bottom`: Hex colors for gradient
- `color`: Bezel color ("Deep Blue", "Silver", "Cosmic Orange")
- `device`: Device model (optional, auto-detected if omitted)
- `orientation`: "portrait" or "landscape" (optional, auto-detected)

### Step 5: Run Screenshot Generator

Execute the Python script to generate marketing screenshots:

**Single screenshot:**
```bash
python scripts/generate_screenshot.py \
  --screenshot screenshots/home.png \
  --title "PartyPal" \
  --tagline "聚会玩具箱" \
  --output marketing/screenshot_1.png
```

**Batch generation from config:**
```bash
python scripts/generate_screenshot.py --config screenshots_config.json
```

**The script will:**
1. Auto-detect device type from screenshot dimensions
2. Load appropriate device bezel
3. Composite screenshot into bezel with rounded corners
4. Create gradient background
5. Add text overlay (title and tagline)
6. Save final marketing screenshot

### Step 6: Review and Iterate

After generation:

1. **Review output quality**
   - Check text readability
   - Verify screenshot alignment
   - Ensure colors match brand

2. **Test variations** (if needed)
   - Try different gradient colors
   - Adjust tagline wording
   - Test different bezel colors

3. **Prepare for upload**
   - Verify dimensions (1320 x 2868 for iPhone 6.9")
   - Check file format (PNG)
   - Ensure all screenshots are consistent

## Implementation Guide for AI Assistants

When a user requests screenshot generation, follow this workflow:

### Phase 1: Information Gathering

```markdown
I'll help you generate App Store marketing screenshots. Let me gather the necessary information.

**Looking for:**
- App screenshots in your project
- Product documentation (PRD, README)
- App Store listing or marketing materials
- Brand guidelines or color preferences
```

**Use these tools:**
- `find_by_name` - Find screenshot files (*.png in screenshots/, publish/, etc.)
- `view_file` - Read PRD, app descriptions, brand guidelines
- `grep_search` - Search for brand colors, feature descriptions
- `list_dir` - Explore project structure

### Phase 2: Screenshot Analysis

For each screenshot found:
1. **Identify the feature** shown
   - Match with PRD feature descriptions
   - Understand the user benefit
   
2. **Determine appropriate messaging**
   - Extract value proposition from docs
   - Create concise, compelling tagline
   - Ensure consistency with brand voice

3. **Select color scheme**
   - Extract brand colors from guidelines
   - Choose complementary gradients
   - Maintain visual consistency across screenshots

### Phase 3: Configuration Generation

Create `screenshots_config.json` with:

```json
{
  "canvas_size": "iPhone 6.9",
  "bezels_dir": "product-bezels",
  "screenshots": [
    {
      "input": "<screenshot_path>",
      "title": "<app_name>",
      "tagline": "<feature_benefit>",
      "background": {
        "top": "<hex_color>",
        "bottom": "<hex_color>"
      },
      "color": "<bezel_color>",
      "output": "marketing/screenshot_<n>.png"
    }
  ]
}
```

**Configuration guidelines:**
- Use consistent app name in `title` field
- Make taglines benefit-focused (not feature lists)
- Choose gradients that complement each other
- Use same bezel color for consistency (or vary strategically)
- Number outputs sequentially (screenshot_1.png, screenshot_2.png, etc.)

### Phase 4: Script Execution

Provide the user with:

1. **Installation instructions** (if needed):
```bash
cd <project_directory>
pip install Pillow
```

2. **Execution command**:
```bash
python scripts/generate_screenshot.py --config screenshots_config.json
```

3. **Expected output**:
```
[1/5] Generating screenshot...
Auto-detected device: iPhone 17 Pro Max
Auto-detected orientation: portrait
Using bezel: product-bezels/iPhone 17 Pro Max/iPhone 17 Pro Max - Deep Blue - Portrait.png
✓ Marketing screenshot generated: marketing/screenshot_1.png
...
```

### Phase 5: Review and Iteration

After generation, help the user:

1. **Verify output quality**
   - Check if text is readable
   - Ensure screenshots are properly aligned
   - Confirm colors match expectations

2. **Suggest improvements** (if needed)
   - Alternative tagline wording
   - Different color combinations
   - Bezel color variations

3. **Prepare for App Store**
   - Confirm dimensions meet requirements
   - Verify file format (PNG)
   - Check consistency across all screenshots

## Technical Specifications

### App Store Requirements

**iPhone Screenshots (Required):**
- **6.9" Display**: 1320 x 2868 (portrait) or 2868 x 1320 (landscape)
- **File Format**: PNG or JPEG
- **Color Space**: RGB (no CMYK)
- **Transparency**: Not allowed
- **Quantity**: 1-10 screenshots per localization

**Supported Devices:**
- iPhone 17 Pro Max (6.9" - 1320x2868)
- iPhone 17 Pro (6.3" - 1206x2622)
- iPhone 17 Air (6.5" - 1260x2736)
- iPhone 17 (6.1" - 1179x2556)
- Plus older models (iPhone 15, 14, 13, 12 series)

### Generator Features

**Auto-Detection:**
- Device model from screenshot dimensions
- Orientation (portrait/landscape)
- Optimal bezel placement

**Customization:**
- Gradient backgrounds (any hex colors)
- Text overlays (title + tagline)
- Bezel colors (Deep Blue, Silver, Cosmic Orange)
- Font support for Chinese and English

**Output:**
- App Store standard dimensions (1320 x 2868)
- High-quality PNG format
- Properly aligned device bezels
- Rounded corner clipping

## Best Practices

### Screenshot Content

✅ **Do:**
- Show your app's best features first
- Use realistic, attractive content
- Ensure text is readable
- Highlight unique value propositions
- Keep UI in final, polished state

❌ **Don't:**
- Use placeholder text ("Lorem ipsum")
- Show test data or debug information
- Include outdated UI elements
- Display inappropriate content

### Text Overlays

✅ **Do:**
- Keep titles short (1-2 words)
- Make taglines concise (3-5 words)
- Use benefit-focused language
- Ensure readability against background
- Localize for target markets

❌ **Don't:**
- Write long paragraphs
- Use technical jargon
- Repeat what's visible in screenshot
- Forget to localize text

### Color Selection

✅ **Do:**
- Match your app's brand colors
- Use complementary gradients
- Maintain consistency across screenshots
- Test readability of white text
- Consider cultural color associations

❌ **Don't:**
- Use clashing color combinations
- Make backgrounds too dark for text
- Change style drastically between screenshots
- Ignore brand guidelines

### Marketing Strategy

**Screenshot order matters:**
1. **Screenshot 1**: Core value proposition (appears in search)
2. **Screenshot 2**: Key feature or benefit
3. **Screenshot 3**: Another important feature
4. **Screenshots 4-10**: Additional features, use cases

**Tell a story:**
- Show user journey through your app
- Highlight different use cases
- Build narrative flow
- End with call-to-action or social proof

## Common Issues and Solutions

### Issue: "Screenshot dimensions don't match any device"

**Solution:**
- Verify screenshot was captured at correct resolution
- Check if device is supported (run `--list-devices`)
- Ensure screenshot wasn't resized or cropped

### Issue: "Bezel not found"

**Solution:**
- Verify `product-bezels` directory exists
- Check device name spelling (case-sensitive)
- Confirm bezel color is available
- Ensure orientation is correct

### Issue: "Text is too small/large"

**Solution:**
- Text size is auto-calculated based on canvas
- For custom sizes, modify script's font size parameters
- Ensure title/tagline aren't too long

### Issue: "Colors don't look right"

**Solution:**
- Use 6-digit hex codes (e.g., `#A855F7`)
- Include `#` prefix
- Test gradients with online tools first
- Verify RGB color space

### Issue: "Screenshot looks pixelated"

**Solution:**
- Use high-resolution source screenshots
- Capture at native device resolution
- Don't upscale smaller screenshots
- Ensure source quality is good

## Example Configurations

### Example 1: Colorful Party App

```json
{
  "screenshots": [
    {
      "input": "screenshots/home.png",
      "title": "PartyPal",
      "tagline": "聚会玩具箱",
      "background": {"top": "#A855F7", "bottom": "#3B82F6"},
      "output": "marketing/screenshot_1.png"
    },
    {
      "input": "screenshots/dice.png",
      "title": "PartyPal",
      "tagline": "Q弹骰子 真实物理",
      "background": {"top": "#10B981", "bottom": "#3B82F6"},
      "output": "marketing/screenshot_2.png"
    },
    {
      "input": "screenshots/wheel.png",
      "title": "PartyPal",
      "tagline": "奇迹转盘 选择困难症救星",
      "background": {"top": "#F59E0B", "bottom": "#EF4444"},
      "output": "marketing/screenshot_3.png"
    }
  ]
}
```

### Example 2: Professional Productivity App

```json
{
  "screenshots": [
    {
      "input": "screenshots/tasks.png",
      "title": "TaskMaster",
      "tagline": "Get Things Done",
      "color": "Silver",
      "background": {"top": "#1F2937", "bottom": "#111827"},
      "output": "marketing/screenshot_1.png"
    },
    {
      "input": "screenshots/calendar.png",
      "title": "TaskMaster",
      "tagline": "Plan Your Week",
      "color": "Silver",
      "background": {"top": "#374151", "bottom": "#1F2937"},
      "output": "marketing/screenshot_2.png"
    }
  ]
}
```

### Example 3: Fitness App

```json
{
  "screenshots": [
    {
      "input": "screenshots/workout.png",
      "title": "FitTrack",
      "tagline": "Your Personal Trainer",
      "color": "Cosmic Orange",
      "background": {"top": "#F59E0B", "bottom": "#EF4444"},
      "output": "marketing/screenshot_1.png"
    },
    {
      "input": "screenshots/progress.png",
      "title": "FitTrack",
      "tagline": "Track Your Progress",
      "color": "Cosmic Orange",
      "background": {"top": "#EF4444", "bottom": "#DC2626"},
      "output": "marketing/screenshot_2.png"
    }
  ]
}
```

## Script Installation

The screenshot generator requires Python and the Pillow library.

**Install dependencies:**
```bash
pip install Pillow
```

**Verify installation:**
```bash
python scripts/generate_screenshot.py --list-devices
```

## Command-Line Reference

**Single screenshot generation:**
```bash
python scripts/generate_screenshot.py \
  --screenshot <path> \
  --title "<title>" \
  --tagline "<tagline>" \
  --bg-top "<hex>" \
  --bg-bottom "<hex>" \
  --output <output_path>
```

**Batch generation:**
```bash
python scripts/generate_screenshot.py --config <config.json>
```

**List available devices:**
```bash
python scripts/generate_screenshot.py --list-devices
```

**All options:**
- `--screenshot`: Path to app screenshot (required for single mode)
- `--device`: Device model (optional, auto-detected)
- `--color`: Bezel color (default: "Deep Blue")
- `--orientation`: "portrait" or "landscape" (optional, auto-detected)
- `--title`: App title text
- `--tagline`: Tagline text (optional)
- `--bg-top`: Top gradient color (hex, default: #A855F7)
- `--bg-bottom`: Bottom gradient color (hex, default: #3B82F6)
- `--output`: Output file path (default: output.png)
- `--bezels-dir`: Bezels directory (default: product-bezels)
- `--canvas-size`: Canvas size (default: "iPhone 6.9")
- `--config`: JSON config file for batch generation

## Integration with App Store Listing Skill

This skill works perfectly with the **App Store Listing Generator** skill:

1. **Use Listing Generator** to create app description and taglines
2. **Extract taglines** from the generated listing
3. **Use Screenshot Generator** to create visual marketing materials
4. **Upload both** to App Store Connect

**Workflow:**
```
App Store Listing Generator → taglines and messaging
           ↓
Screenshot Generator → visual marketing screenshots
           ↓
App Store Connect → complete product page
```

## Resources

**Color Tools:**
- [Coolors.co](https://coolors.co/) - Generate color schemes
- [Adobe Color](https://color.adobe.com/) - Color wheel and harmony
- [uiGradients](https://uigradients.com/) - Gradient inspiration

**Design Inspiration:**
- [App Launch Pad](https://theapplaunchpad.com/) - Screenshot examples
- [Mobbin](https://mobbin.com/) - App design patterns

**Apple Guidelines:**
- [Screenshot Specifications](https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications)
- [App Store Product Page](https://developer.apple.com/app-store/product-page/)

## Notes

- Always verify screenshot dimensions match App Store requirements
- Test text readability on mobile devices
- Keep consistent style across all screenshots
- Update screenshots when app UI changes
- Localize text overlays for different markets
- First screenshot is most important (appears in search results)
