Param()
# PowerShell script to build and publish to PyPI
# Usage: $env:TWINE_PASSWORD = '<token>'; .\scripts\publish_pypi.ps1
python -m pip install --upgrade build twine
python -m build
if (-not $env:TWINE_PASSWORD) {
  Write-Error "TWINE_PASSWORD not set. Create a PyPI API token and set TWINE_PASSWORD environment variable."
  exit 1
}
python -m twine upload --non-interactive -u __token__ -p $env:TWINE_PASSWORD dist/*
