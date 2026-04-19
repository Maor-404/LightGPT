# Push latest changes to GitHub (PowerShell)

$repoPath = "C:\path\to\LightGPT"  # Update this to your repo path

Push-Location $repoPath

Write-Host "🔄 Preparing to push changes..." -ForegroundColor Cyan

# Stage all changes
git add .

# Check if there are changes to commit
$status = git status --porcelain
if ($status) {
    Write-Host "📝 Committing changes..." -ForegroundColor Yellow
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
    
    Write-Host "✓ Commit created" -ForegroundColor Green
} else {
    Write-Host "✓ No changes to commit" -ForegroundColor Green
}

Write-Host "📤 Pushing to GitHub..." -ForegroundColor Cyan
git push -u origin main

Write-Host "✅ Push complete!" -ForegroundColor Green
Write-Host ""
Write-Host "🎮 Cheat Menu Files:" -ForegroundColor Magenta
Write-Host "  - cheat_menu.py (Python module)" -ForegroundColor White
Write-Host "  - colab/LightGPT_CheatMenu.ipynb (Standalone notebook)" -ForegroundColor White
Write-Host ""
Write-Host "Ready to use in Colab! 🚀" -ForegroundColor Cyan

Pop-Location
