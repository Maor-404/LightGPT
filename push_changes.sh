#!/bin/bash
# Push latest changes to GitHub

cd /workspaces/LightGPT

echo "🔄 Preparing to push changes..."

# Stage all changes
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "✓ No changes to commit"
else
    echo "📝 Committing changes..."
    git commit -m "feat(cheat-menu): add graphical interactive cheat menu for LightGPT

- Add cheat_menu.py with interactive ipywidgets-based GUI
- Create LightGPT_CheatMenu.ipynb standalone notebook
- Model mode selector (Overkill/Normal/Underkill)
- April Fools stupidity toggle integrated
- Real-time setting updates and code generation
- Comprehensive help and documentation

The cheat menu provides an easy way to:
- Configure model parameters visually
- Toggle April Fools mode with one click
- Generate ready-to-use Python code
- Experiment with different settings in Colab"
    
    echo "✓ Commit created"
fi

echo "📤 Pushing to GitHub..."
git push -u origin main

echo "✅ Push complete!"
echo ""
echo "🎮 Cheat Menu Files:"
echo "  - cheat_menu.py (Python module)"
echo "  - colab/LightGPT_CheatMenu.ipynb (Standalone notebook)"
echo ""
echo "Ready to use in Colab! 🚀"
