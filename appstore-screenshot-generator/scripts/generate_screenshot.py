#!/usr/bin/env python3
"""
App Store Screenshot Generator

Generate professional marketing screenshots for App Store submissions by compositing
app screenshots into device bezels with custom backgrounds and text overlays.

Usage:
    python generate_screenshot.py --screenshot app.png --device "iPhone 17 Pro Max" \\
        --color "Silver" --title "MyApp" --tagline "Amazing App" --output result.png
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Tuple, Optional

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)


# Device screen area coordinates (x, y, width, height) relative to bezel image
# Calibrated for actual bezel images (1470 x 3000 for portrait)
# Screen area is the transparent region where the app screenshot should be placed
DEVICE_SCREEN_AREAS = {
    "iPhone 17 Pro Max": {
        "portrait": (75, 68, 1320, 2868),  # 6.9" - 1320x2868
        "landscape": (68, 75, 2868, 1320),
    },
    "iPhone 17 Pro": {
        "portrait": (75, 68, 1206, 2622),  # 6.3" - 1206x2622 (centered in bezel)
        "landscape": (68, 75, 2622, 1206),
    },
    "iPhone 17": {
        "portrait": (75, 68, 1320, 2868),  # Using Pro Max bezel
        "landscape": (68, 75, 2868, 1320),
    },
    "iPhone Air": {
        "portrait": (105, 66, 1260, 2736),  # 6.5" - 1260x2736 (centered in bezel)
        "landscape": (66, 105, 2736, 1260),
    },
}

# App Store screenshot dimensions
APPSTORE_DIMENSIONS = {
    "iPhone 6.9": (1320, 2868),  # Portrait
    "iPhone 6.7": (1290, 2796),
    "iPhone 6.3": (1206, 2622),
    "iPad 13": (2048, 2732),
}

# iPhone screen sizes mapping (portrait width x height)
# Maps actual screenshot dimensions to device models
IPHONE_SCREEN_SIZES = {
    (1320, 2868): "iPhone 17 Pro Max",  # 6.9" - iPhone 17 Pro Max, 16 Pro Max
    (1290, 2796): "iPhone 17 Pro",      # 6.7" - iPhone 15 Pro Max, 15 Plus, 14 Pro Max
    (1284, 2778): "iPhone 17 Pro",      # 6.5" - iPhone 13 Pro Max, 12 Pro Max
    (1260, 2736): "iPhone Air",         # 6.5" - iPhone 17 Air
    (1206, 2622): "iPhone 17 Pro",      # 6.3" - iPhone 17 Pro
    (1179, 2556): "iPhone 17",          # 6.1" - iPhone 15, 14, 13, 12
    (1242, 2208): "iPhone 17",          # 5.5" - iPhone 8 Plus, 7 Plus
    (1170, 2532): "iPhone 17",          # 6.1" - Alternative resolution
    # Landscape versions
    (2868, 1320): "iPhone 17 Pro Max",
    (2796, 1290): "iPhone 17 Pro",
    (2778, 1284): "iPhone 17 Pro",
    (2736, 1260): "iPhone Air",
    (2622, 1206): "iPhone 17 Pro",
    (2556, 1179): "iPhone 17",
    (2208, 1242): "iPhone 17",
    (2532, 1170): "iPhone 17",
}


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def create_gradient_background(
    width: int,
    height: int,
    color_top: str,
    color_bottom: str
) -> Image.Image:
    """Create a vertical gradient background."""
    base = Image.new('RGB', (width, height), color_top)
    top_rgb = hex_to_rgb(color_top)
    bottom_rgb = hex_to_rgb(color_bottom)
    
    # Create gradient
    for y in range(height):
        # Calculate interpolation factor
        factor = y / height
        
        # Interpolate each color channel
        r = int(top_rgb[0] + (bottom_rgb[0] - top_rgb[0]) * factor)
        g = int(top_rgb[1] + (bottom_rgb[1] - top_rgb[1]) * factor)
        b = int(top_rgb[2] + (bottom_rgb[2] - top_rgb[2]) * factor)
        
        # Draw horizontal line
        draw = ImageDraw.Draw(base)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return base


def add_text_overlay(
    image: Image.Image,
    title: str,
    tagline: Optional[str] = None,
    title_size: int = 160,
    tagline_size: int = 100,
    text_color: str = "#FFFFFF",
    y_offset: int = 150
) -> Image.Image:
    """Add text overlay to image."""
    draw = ImageDraw.Draw(image)
    width, height = image.size
    
    # Try to load a nice font, fall back to default if not available
    try:
        # Try Hiragino Sans GB (good for Chinese and English, available on macOS)
        title_font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", title_size)
        tagline_font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", tagline_size)
        print("✓ Using font: Hiragino Sans GB")
    except Exception as e:
        print(f"✗ Hiragino Sans GB not available: {e}")
        try:
            # Try STHeiti Medium (Chinese font, available on macOS)
            title_font = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", title_size)
            tagline_font = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", tagline_size)
            print("✓ Using font: STHeiti Medium")
        except Exception as e:
            print(f"✗ STHeiti Medium not available: {e}")
            try:
                # Try Helvetica as fallback
                title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", title_size)
                tagline_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", tagline_size)
                print("✓ Using font: Helvetica")
            except Exception as e:
                print(f"✗ Helvetica not available: {e}")
                try:
                    # Try SF fonts
                    title_font = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", title_size)
                    tagline_font = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", tagline_size)
                    print("✓ Using font: SF")
                except Exception as e:
                    print(f"✗ SF not available: {e}")
                    # Fall back to default font
                    title_font = ImageFont.load_default()
                    tagline_font = ImageFont.load_default()
                    print("⚠ Using default bitmap font (limited quality)")
    
    rgb_color = hex_to_rgb(text_color)
    
    # Draw title
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    title_x = (width - title_width) // 2
    title_y = y_offset
    
    # Add shadow for better readability
    # shadow_offset = 4
    # draw.text((title_x + shadow_offset, title_y + shadow_offset), title, 
    #           font=title_font, fill=(0, 0, 0, 128))
    draw.text((title_x, title_y), title, font=title_font, fill=rgb_color)
    
    # Draw tagline if provided
    if tagline:
        tagline_bbox = draw.textbbox((0, 0), tagline, font=tagline_font)
        tagline_width = tagline_bbox[2] - tagline_bbox[0]
        tagline_x = (width - tagline_width) // 2
        tagline_y = title_y + title_height + 30
        
        # draw.text((tagline_x + shadow_offset, tagline_y + shadow_offset), tagline,
        #           font=tagline_font, fill=(0, 0, 0, 128))
        draw.text((tagline_x, tagline_y), tagline, font=tagline_font, fill=rgb_color)
    
    return image


def find_bezel_path(
    device: str,
    color: str = "Deep Blue",
    orientation: str = "Portrait",
    bezels_dir: str = "product-bezels"
) -> Optional[Path]:
    """Find the bezel image file."""
    bezel_dir = Path(bezels_dir) / device
    
    if not bezel_dir.exists():
        print(f"Bezel directory not found: {bezel_dir}")
        return None
    
    # Construct expected filename
    orientation_str = orientation.capitalize()
    filename = f"{device} - {color} - {orientation_str}.png"
    bezel_path = bezel_dir / filename
    
    if bezel_path.exists():
        return bezel_path
    
    print(f"Bezel file not found: {bezel_path}")
    return None


def create_rounded_rectangle_mask(
    width: int,
    height: int,
    radius: int
) -> Image.Image:
    """Create a rounded rectangle mask for clipping screenshots.
    
    Args:
        width: Width of the mask
        height: Height of the mask
        radius: Corner radius in pixels
    
    Returns:
        PIL Image with rounded rectangle mask (L mode)
    """
    # Create a mask with rounded corners
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    
    # Draw rounded rectangle
    draw.rounded_rectangle(
        [(0, 0), (width, height)],
        radius=radius,
        fill=255
    )
    
    return mask


def detect_device_from_screenshot(screenshot_path: str) -> tuple[str, str]:
    """Detect appropriate device model based on screenshot dimensions.
    
    Args:
        screenshot_path: Path to the screenshot file
    
    Returns:
        Tuple of (device_name, orientation)
    
    Raises:
        ValueError: If screenshot dimensions don't match any known device
    """
    img = Image.open(screenshot_path)
    width, height = img.size
    
    # Check if dimensions match any known iPhone size
    if (width, height) in IPHONE_SCREEN_SIZES:
        device = IPHONE_SCREEN_SIZES[(width, height)]
        orientation = "portrait" if height > width else "landscape"
        return device, orientation
    
    # If exact match not found, try to find closest match
    # This helps with slightly different resolutions
    min_diff = float('inf')
    best_match = None
    best_orientation = None
    
    for (known_width, known_height), device_name in IPHONE_SCREEN_SIZES.items():
        diff = abs(width - known_width) + abs(height - known_height)
        if diff < min_diff:
            min_diff = diff
            best_match = device_name
            best_orientation = "portrait" if known_height > known_width else "landscape"
    
    # If difference is small (within 50 pixels), use the closest match
    if min_diff < 50 and best_match:
        print(f"Warning: Screenshot dimensions ({width}x{height}) don't exactly match any device.")
        print(f"Using closest match: {best_match} ({best_orientation})")
        return best_match, best_orientation
    
    # No match found
    raise ValueError(
        f"Screenshot dimensions ({width}x{height}) don't match any known iPhone size.\n"
        f"Supported sizes:\n" +
        "\n".join([f"  {w}x{h} - {device}" for (w, h), device in sorted(IPHONE_SCREEN_SIZES.items())])
    )


def composite_screenshot_into_bezel(
    screenshot_path: str,
    bezel_path: Path,
    device: str,
    orientation: str
) -> Image.Image:
    """Composite app screenshot into device bezel with rounded corners and bezel overlay.
    
    Combines rounded corner clipping with bezel overlay for perfect alignment.
    """
    # Load images
    screenshot = Image.open(screenshot_path).convert("RGBA")
    bezel = Image.open(bezel_path).convert("RGBA")
    
    # Get screen area for this device
    if device not in DEVICE_SCREEN_AREAS:
        raise ValueError(f"Unknown device: {device}")
    
    screen_area = DEVICE_SCREEN_AREAS[device][orientation]
    x, y, screen_width, screen_height = screen_area
    
    # Resize screenshot to fit screen area
    screenshot_resized = screenshot.resize(
        (screen_width, screen_height),
        Image.Resampling.LANCZOS
    )
    
    # Create rounded corner mask
    # iPhone screens have approximately 55 pixel corner radius at this resolution
    corner_radius = 85
    mask = create_rounded_rectangle_mask(screen_width, screen_height, corner_radius)
    
    # Apply rounded corners to screenshot
    screenshot_with_corners = Image.new('RGBA', (screen_width, screen_height), (0, 0, 0, 0))
    screenshot_with_corners.paste(screenshot_resized, (0, 0))
    screenshot_with_corners.putalpha(mask)
    
    # Create a canvas the size of the bezel
    bezel_width, bezel_height = bezel.size
    result = Image.new('RGBA', (bezel_width, bezel_height), (0, 0, 0, 0))
    
    # Paste the rounded screenshot at the screen position
    result.paste(screenshot_with_corners, (x, y), screenshot_with_corners)
    
    # Overlay the bezel on top for final polish
    result = Image.alpha_composite(result, bezel)
    
    return result


def generate_marketing_screenshot(
    screenshot_path: str,
    device: Optional[str] = None,
    color: str = "Deep Blue",
    orientation: Optional[str] = None,
    title: str = "",
    tagline: Optional[str] = None,
    bg_top: str = "#A855F7",
    bg_bottom: str = "#3B82F6",
    output_path: str = "output.png",
    bezels_dir: str = "product-bezels",
    canvas_size: str = "iPhone 6.9"
) -> None:
    """Generate a complete marketing screenshot.
    
    Args:
        screenshot_path: Path to the app screenshot
        device: Device model (optional, auto-detected from screenshot size if not provided)
        color: Bezel color (default: "Deep Blue")
        orientation: Orientation (optional, auto-detected if not provided)
        title: App title text
        tagline: App tagline text (optional)
        bg_top: Top gradient color
        bg_bottom: Bottom gradient color
        output_path: Output file path
        bezels_dir: Directory containing device bezels
        canvas_size: App Store canvas size (default: "iPhone 6.9")
    """
    
    # Validate inputs
    if not os.path.exists(screenshot_path):
        raise FileNotFoundError(f"Screenshot not found: {screenshot_path}")
    
    # Auto-detect device and orientation if not provided
    if device is None or orientation is None:
        detected_device, detected_orientation = detect_device_from_screenshot(screenshot_path)
        if device is None:
            device = detected_device
            print(f"Auto-detected device: {device}")
        if orientation is None:
            orientation = detected_orientation
            print(f"Auto-detected orientation: {orientation}")
    
    # Find bezel
    bezel_path = find_bezel_path(device, color, orientation, bezels_dir)
    if not bezel_path:
        raise FileNotFoundError(
            f"Bezel not found for {device} - {color} - {orientation}\n"
            f"Available devices: {', '.join(DEVICE_SCREEN_AREAS.keys())}"
        )
    
    print(f"Using bezel: {bezel_path}")
    
    # Get App Store canvas dimensions
    if canvas_size not in APPSTORE_DIMENSIONS:
        raise ValueError(
            f"Unknown canvas size: {canvas_size}\n"
            f"Available sizes: {', '.join(APPSTORE_DIMENSIONS.keys())}"
        )
    
    canvas_width, canvas_height = APPSTORE_DIMENSIONS[canvas_size]
    print(f"Canvas size: {canvas_width}x{canvas_height} ({canvas_size})")
    
    # Load bezel to get dimensions
    bezel = Image.open(bezel_path)
    bezel_width, bezel_height = bezel.size
    print(f"Bezel size: {bezel_width}x{bezel_height}")
    
    # Calculate scaling to fit bezel within canvas with margins
    # Reserve space for text at top
    text_space = 400
    available_height = canvas_height - text_space
    
    # Calculate scale factor to fit bezel with 10% margins
    margin_percent = 0.10
    max_bezel_width = canvas_width * (1 - 2 * margin_percent)
    max_bezel_height = available_height * (1 - margin_percent)
    
    scale_width = max_bezel_width / bezel_width
    scale_height = max_bezel_height / bezel_height
    scale = min(scale_width, scale_height)
    
    # Calculate scaled bezel dimensions
    scaled_bezel_width = int(bezel_width * scale)
    scaled_bezel_height = int(bezel_height * scale)
    
    print(f"Scaling bezel by {scale:.2f}x to {scaled_bezel_width}x{scaled_bezel_height}")
    
    # Create gradient background
    print("Creating gradient background...")
    background = create_gradient_background(canvas_width, canvas_height, bg_top, bg_bottom)
    
    # Add text overlay
    print("Adding text overlay...")
    background = add_text_overlay(background, title, tagline)
    
    # Composite screenshot into bezel
    print("Compositing screenshot into bezel...")
    device_with_screenshot = composite_screenshot_into_bezel(
        screenshot_path, bezel_path, device, orientation
    )
    
    # Scale the bezel to fit within canvas
    if scale != 1.0:
        print(f"Resizing bezel from {bezel_width}x{bezel_height} to {scaled_bezel_width}x{scaled_bezel_height}...")
        device_with_screenshot = device_with_screenshot.resize(
            (scaled_bezel_width, scaled_bezel_height),
            Image.Resampling.LANCZOS
        )
    
    # Calculate bezel position
    # X: centered horizontally
    bezel_x = (canvas_width - scaled_bezel_width) // 2
    
    # Y: centered in the available space below text
    available_vertical_space = canvas_height - text_space
    vertical_margin_top = (available_vertical_space - scaled_bezel_height) // 2
    bezel_y = text_space + vertical_margin_top
    
    print(f"Placing bezel at position: ({bezel_x}, {bezel_y})")
    background.paste(device_with_screenshot, (bezel_x, bezel_y), device_with_screenshot)
    
    # Save result
    print(f"Saving to {output_path}...")
    background.save(output_path, "PNG", quality=95)
    print(f"✓ Marketing screenshot generated: {output_path}")
    print(f"  Canvas: {canvas_width}x{canvas_height} ({canvas_size})")
    print(f"  Bezel: {scaled_bezel_width}x{scaled_bezel_height} at ({bezel_x}, {bezel_y})")


def generate_from_config(config_path: str, default_bezels_dir: str = 'product-bezels', default_canvas_size: str = 'iPhone 6.9') -> None:
    """Generate screenshots from a JSON configuration file.
    
    Args:
        config_path: Path to JSON configuration file
        default_bezels_dir: Default bezels directory (from command-line), used if not specified in config
        default_canvas_size: Default canvas size (from command-line), used if not specified in config
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Get global settings from config, or use command-line defaults
    global_bezels_dir = config.get('bezels_dir', default_bezels_dir)
    global_canvas_size = config.get('canvas_size', default_canvas_size)
    
    screenshots = config.get('screenshots', [])
    
    for i, screenshot_config in enumerate(screenshots, 1):
        print(f"\n[{i}/{len(screenshots)}] Generating screenshot...")
        
        # Per-screenshot settings override global settings
        bezels_dir = screenshot_config.get('bezels_dir', global_bezels_dir)
        canvas_size = screenshot_config.get('canvas_size', global_canvas_size)
        
        generate_marketing_screenshot(
            screenshot_path=screenshot_config['input'],
            device=screenshot_config.get('device'),  # Optional, will auto-detect if not provided
            color=screenshot_config.get('color', 'Deep Blue'),
            orientation=screenshot_config.get('orientation'),  # Optional, will auto-detect if not provided
            title=screenshot_config.get('title', ''),
            tagline=screenshot_config.get('tagline'),
            bg_top=screenshot_config.get('background', {}).get('top', '#A855F7'),
            bg_bottom=screenshot_config.get('background', {}).get('bottom', '#3B82F6'),
            output_path=screenshot_config['output'],
            bezels_dir=bezels_dir,
            canvas_size=canvas_size
        )


def main():
    parser = argparse.ArgumentParser(
        description='Generate App Store marketing screenshots',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate a single screenshot
  python generate_screenshot.py \\
    --screenshot app.png \\
    --device "iPhone 17 Pro Max" \\
    --color "Silver" \\
    --orientation portrait \\
    --title "MinFit" \\
    --tagline "Gym for Brain" \\
    --output marketing.png

  # Generate from config file
  python generate_screenshot.py --config screenshots.json
        """
    )
    
    parser.add_argument('--screenshot', help='Path to app screenshot')
    parser.add_argument('--device', help='Device model (e.g., "iPhone 17 Pro Max")')
    parser.add_argument('--color', help='Bezel color (Silver, Deep Blue, Cosmic Orange)', default='Deep Blue')
    parser.add_argument('--orientation', choices=['portrait', 'landscape'], 
                        default='portrait', help='Screenshot orientation')
    parser.add_argument('--title', help='App title text')
    parser.add_argument('--tagline', help='App tagline text (optional)')
    parser.add_argument('--bg-top', default='#A855F7', 
                        help='Background gradient top color (hex)')
    parser.add_argument('--bg-bottom', default='#3B82F6',
                        help='Background gradient bottom color (hex)')
    parser.add_argument('--output', default='output.png', help='Output file path')
    parser.add_argument('--bezels-dir', default='product-bezels',
                        help='Directory containing device bezels')
    parser.add_argument('--canvas-size', default='iPhone 6.9',
                        help='App Store canvas size (default: iPhone 6.9)')
    parser.add_argument('--config', help='JSON configuration file for batch generation')
    parser.add_argument('--list-devices', action='store_true',
                        help='List available devices and exit')
    
    args = parser.parse_args()
    
    # List devices
    if args.list_devices:
        print("Available devices:")
        for device in DEVICE_SCREEN_AREAS.keys():
            print(f"  - {device}")
        print("\nSupported screenshot sizes:")
        for (width, height), device in sorted(IPHONE_SCREEN_SIZES.items()):
            if height > width:  # Only show portrait
                print(f"  {width}x{height} - {device}")
        print("\nAvailable canvas sizes:")
        for size, (width, height) in APPSTORE_DIMENSIONS.items():
            print(f"  {size}: {width}x{height}")
        return
    
    # Batch generation from config
    if args.config:
        generate_from_config(args.config, args.bezels_dir, args.canvas_size)
        return
    
    # Single screenshot generation
    if not args.screenshot:
        parser.error("--screenshot is required (or use --config for batch generation)")
    
    try:
        generate_marketing_screenshot(
            screenshot_path=args.screenshot,
            device=args.device,
            color=args.color,
            orientation=args.orientation,
            title=args.title,
            tagline=args.tagline,
            bg_top=args.bg_top,
            bg_bottom=args.bg_bottom,
            output_path=args.output,
            bezels_dir=args.bezels_dir,
            canvas_size=args.canvas_size
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
