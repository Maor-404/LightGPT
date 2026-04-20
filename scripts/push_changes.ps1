# Push latest changes to GitHub (PowerShell)

$repoPath = Resolve-Path "$(Split-Path -Parent $MyInvocation.MyCommand.Path)\.."
Set-Location $repoPath

Write-Host "🔄 Preparing to push changes..." -ForegroundColor Cyan

git add .

$status = git status --porcelain
if ($status) {
    Write-Host "📝 Committing changes..." -ForegroundColor Yellow
    git commit -m "chore(repo): push latest changes via scripts/push_changes.ps1"
    Write-Host "✓ Commit created" -ForegroundColor Green
} else {
    Write-Host "✓ No changes to commit" -ForegroundColor Green
}

Write-Host "📤 Pushing to GitHub..." -ForegroundColor Cyan
git push -u origin main

Write-Host "✅ Push complete!" -ForegroundColor Green
Write-Host ""
Write-Host "🎮 Notes:" -ForegroundColor Magenta
Write-Host "  - Root helper scripts are now centralized in scripts/" -ForegroundColor White
Write-Host "  - Use tests/ for test scripts and scripts/ for repo utilities" -ForegroundColor White
