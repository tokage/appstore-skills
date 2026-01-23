# App Store Screenshot Generator Skill

Generate professional App Store marketing screenshots by compositing app screenshots into device bezels with custom backgrounds and text overlays.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r scripts/requirements.txt
   ```

2. **Prepare your app screenshots** (captured from Xcode Simulator or device)

3. **Ask AI to generate configuration:**
   ```
   "I have 5 app screenshots. Please analyze them and generate a screenshots_config.json file with appropriate titles, taglines, and colors."
   ```

4. **Run the generator:**
   ```bash
   python scripts/generate_screenshot.py --config screenshots_config.json
   ```

## Features

- ✅ Auto-detects device type from screenshot dimensions
- ✅ Composites screenshots into realistic iPhone bezels
- ✅ Adds gradient backgrounds with customizable colors
- ✅ Overlays text (app name and tagline) with proper styling
- ✅ Meets App Store requirements (1320 x 2868 for iPhone 6.9")
- ✅ Batch processes multiple screenshots
- ✅ Supports Chinese and English fonts

## Directory Structure

```
appstore-screenshot-generator/
├── SKILL.md                    # Complete skill documentation
├── README.md                   # This file
├── scripts/
│   ├── generate_screenshot.py  # Main screenshot generator script
│   └── requirements.txt        # Python dependencies
├── resources/
│   ├── README.md               # Resources documentation
│   └── product-bezels/         # Device bezel images (iPhone models)
└── examples/
    ├── README.md               # Examples documentation
    └── screenshots_config_basic.json  # Basic configuration template
```

## Usage

See [SKILL.md](SKILL.md) for complete documentation including:
- Detailed workflow
- Configuration options
- Best practices
- Troubleshooting
- Integration with App Store Listing Generator skill

## Requirements

- Python 3.7+
- Pillow library
- Device bezel images (included in `resources/product-bezels/`)

## App Store Requirements

**iPhone Screenshots (Required):**
- 6.9" Display: 1320 x 2868 (portrait)
- File Format: PNG or JPEG
- Color Space: RGB
- Quantity: 1-10 screenshots

## Example Configuration

```json
{
  "screenshots": [
    {
      "input": "screenshots/home.png",
      "title": "MyApp",
      "tagline": "Amazing Feature",
      "background": {
        "top": "#A855F7",
        "bottom": "#3B82F6"
      },
      "output": "marketing/screenshot_1.png"
    }
  ]
}
```

## Integration

Works seamlessly with the **App Store Listing Generator** skill:
1. Generate app description and taglines
2. Use taglines in screenshot configuration
3. Create visual marketing materials
4. Upload to App Store Connect

## Support

For detailed instructions, see [SKILL.md](SKILL.md).
