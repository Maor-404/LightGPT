Param()
# Load environment variables from .env (KEY=VALUE) and run publish_pypi.ps1
if (-not (Test-Path .env)) {
    Write-Error ".env not found — copy .env.template to .env and set TWINE_PASSWORD"
    exit 1
}

Get-Content .env | ForEach-Object {
    if ($_ -match '^[#;]\s*') { return }
    if ($_ -match '^\s*([^=]+)=(.*)$') {
        $name = $matches[1].Trim()
        $val = $matches[2].Trim().Trim('"').Trim("'")
        Set-Item -Path Env:\$name -Value $val
    }
}

if (-not $env:TWINE_PASSWORD) {
    Write-Error "TWINE_PASSWORD not set in .env"
    exit 1
}

./scripts/publish_pypi.ps1
