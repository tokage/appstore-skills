from PIL import Image
import sys

def analyze_transparency(image_path):
    """
    Analyze a bezel image to find the inner transparent screen area.
    Scans from the center outwards to find the first non-transparent pixel.
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)
        
    width, height = img.size
    print(f"Image Size: {width}x{height}")
    
    center_x, center_y = width // 2, height // 2
    
    try:
        center_pixel = img.getpixel((center_x, center_y))
    except Exception:
        print("Error getting center pixel")
        return
    
    if center_pixel[3] != 0:
        print("Center pixel is NOT transparent. Bezel might not be a clear frame? Trying to find transparency nearby...")
        # Fallback logic could go here, but for now we assume center is screen
        return

    print("Center pixel is transparent. Scanning for inner bounds...")

    # Scan left
    x = center_x
    while x > 0 and img.getpixel((x, center_y))[3] == 0:
        x -= 1
    left = x + 1

    # Scan right
    x = center_x
    while x < width and img.getpixel((x, center_y))[3] == 0:
        x += 1
    right = x - 1

    # Scan up
    y = center_y
    while y > 0 and img.getpixel((center_x, y))[3] == 0:
        y -= 1
    top = y + 1

    # Scan down
    y = center_y
    while y < height and img.getpixel((center_x, y))[3] == 0:
        y += 1
    bottom = y - 1

    w = right - left + 1
    h = bottom - top + 1
    
    print(f"Inner Transparent Area: x={left}, y={top}, w={w}, h={h}")
    print(f"Coordinates tuple for script: ({left}, {top}, {w}, {h})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_bezel.py <image_path>")
        sys.exit(1)
    analyze_transparency(sys.argv[1])
