#!/bin/bash
# Quick verification script for App Store Screenshot Generator Skill

echo "🔍 Verifying App Store Screenshot Generator Skill..."
echo ""

# Check Python
echo "1. Checking Python installation..."
if command -v python3 &> /dev/null; then
    echo "   ✅ Python 3 found: $(python3 --version)"
else
    echo "   ❌ Python 3 not found"
    exit 1
fi

# Check script exists
echo ""
echo "2. Checking screenshot generator script..."
if [ -f "scripts/generate_screenshot.py" ]; then
    echo "   ✅ Script found: scripts/generate_screenshot.py"
else
    echo "   ❌ Script not found"
    exit 1
fi

# Check resources
echo ""
echo "3. Checking device bezels..."
if [ -d "resources/product-bezels" ]; then
    BEZEL_COUNT=$(find resources/product-bezels -name "*.png" | wc -l)
    echo "   ✅ Bezels directory found: $BEZEL_COUNT bezel images"
else
    echo "   ❌ Bezels directory not found"
    exit 1
fi

# Check dependencies
echo ""
echo "4. Checking Python dependencies..."
if python3 -c "import PIL" 2>/dev/null; then
    echo "   ✅ Pillow library installed"
else
    echo "   ⚠️  Pillow not installed. Run: pip install -r scripts/requirements.txt"
fi

# List available devices
echo ""
echo "5. Available devices:"
python3 scripts/generate_screenshot.py --list-devices 2>/dev/null | grep "  -" | head -5

echo ""
echo "✅ Skill verification complete!"
echo ""
echo "📚 Next steps:"
echo "   1. Install dependencies: pip install -r scripts/requirements.txt"
echo "   2. Prepare app screenshots in screenshots/ folder"
echo "   3. Generate config: Ask AI to analyze screenshots"
echo "   4. Run generator: python scripts/generate_screenshot.py --config config.json"
