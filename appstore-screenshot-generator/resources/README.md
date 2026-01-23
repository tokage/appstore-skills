# Resources Directory

This directory contains the device bezel images used by the screenshot generator.

## Product Bezels

The `product-bezels/` directory contains high-quality device bezel images for various iPhone models.

### Directory Structure

```
product-bezels/
├── iPhone 17 Pro Max/
│   ├── iPhone 17 Pro Max - Deep Blue - Portrait.png
│   ├── iPhone 17 Pro Max - Deep Blue - Landscape.png
│   ├── iPhone 17 Pro Max - Silver - Portrait.png
│   ├── iPhone 17 Pro Max - Silver - Landscape.png
│   ├── iPhone 17 Pro Max - Cosmic Orange - Portrait.png
│   └── iPhone 17 Pro Max - Cosmic Orange - Landscape.png
├── iPhone 17 Pro/
│   └── ... (same color variations)
├── iPhone 17/
│   └── ... (same color variations)
└── iPhone Air/
    └── ... (same color variations)
```

### Available Devices

- **iPhone 17 Pro Max** (6.9" - 1320x2868)
- **iPhone 17 Pro** (6.3" - 1206x2622)
- **iPhone 17 Air** (6.5" - 1260x2736)
- **iPhone 17** (6.1" - 1179x2556)

### Available Colors

- **Deep Blue** (default) - Professional, trustworthy
- **Silver** - Clean, neutral, elegant
- **Cosmic Orange** - Energetic, creative, bold

### Bezel Specifications

- **Format**: PNG with transparency
- **Quality**: High-resolution for crisp output
- **Screen Area**: Pre-calibrated transparent regions for screenshot placement
- **Rounded Corners**: Authentic iPhone corner radius

## Usage

The screenshot generator script automatically looks for bezels in this directory:

```python
# Default bezel path
bezels_dir = "resources/product-bezels"
```

When using the script from the skill directory:

```bash
python scripts/generate_screenshot.py \
  --screenshot app.png \
  --bezels-dir resources/product-bezels \
  --output result.png
```

Or in the JSON configuration:

```json
{
  "bezels_dir": "resources/product-bezels",
  "screenshots": [...]
}
```

## Notes

- Bezel images are essential for the screenshot generator to work
- Do not modify or rename bezel files
- File naming convention must be exact: `{Device} - {Color} - {Orientation}.png`
- All bezels are optimized for App Store marketing screenshots
