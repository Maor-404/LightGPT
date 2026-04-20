#!/bin/bash
# Push latest changes to GitHub

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo "🔄 Preparing to push changes..."

git add .

if git diff --cached --quiet; then
    echo "✓ No changes to commit"
else
    echo "📝 Committing changes..."
    git commit -m "chore(repo): push latest changes via scripts/push_changes.sh"
    echo "✓ Commit created"
fi

echo "📤 Pushing to GitHub..."
git push -u origin main

echo "✅ Push complete!"

echo ""
echo "🎮 Notes:"
echo "  - Root helper scripts are now centralized in scripts/"
echo "  - Use tests/ for test scripts and scripts/ for repo utilities"
