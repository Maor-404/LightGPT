# ============================================================================
#                    LightGPT PyPI Publisher (PowerShell)
# ============================================================================
#
# Purpose:
#   Build and publish the LightGPT package to PyPI (Python Package Index)
#   This script automates the entire build and upload process on Windows.
#
# Prerequisites:
#   - Python 3.7+ installed and in PATH
#   - PowerShell 5.0+ (or core)
#   - PyPI account with API token generated
#   - TWINE_PASSWORD environment variable set
#
# Usage:
#   $env:TWINE_PASSWORD = '<your-pypi-api-token>'
#   .\scripts\publish_pypi.ps1
#
# Example:
#   $env:TWINE_PASSWORD = 'pypi-AgEIcHlwaS5vcmc...'
#   .\scripts\publish_pypi.ps1
#
# Security Notes:
#   - NEVER store TWINE_PASSWORD in plaintext in scripts
#   - Use GitHub Actions secrets for automated publishing
#   - API tokens should be narrowly scoped (repo-specific)
#
# Exit Codes:
#   0 = Success: package published to PyPI
#   1 = Failure: TWINE_PASSWORD not set or build/upload error
#
# ============================================================================

# PowerShell parameter declaration (no required parameters for this script)
#Param()

# ============================================================================
# STEP 1: INSTALL BUILD TOOLS
# ============================================================================
# Install/upgrade the 'build' package (PEP 517/518 build backend)
# and 'twine' (PyPI upload tool)
# The --upgrade flag ensures we have the latest versions
#Write-Host "📦 Installing build tools (build, twine)..." -ForegroundColor Cyan
#python -m pip install --upgrade build twine

# ============================================================================
# STEP 2: BUILD THE PACKAGE
# ============================================================================
# Use the 'build' module to create distribution files
# This reads pyproject.toml and creates:
#   - .whl file (wheel distribution: compiled/binary package)
#   - .tar.gz file (source distribution: for source installs)
# Output goes to .\dist\ directory
#Write-Host "🔨 Building LightGPT package..." -ForegroundColor Cyan
#python -m build

# ============================================================================
# STEP 3: VALIDATE TWINE_PASSWORD
# ============================================================================
# Check if TWINE_PASSWORD environment variable is set
#
# PowerShell syntax explanation:
#   (-not $env:TWINE_PASSWORD)
#   - Checks if environment variable is empty/null
#   - -not is PowerShell's NOT operator (equivalent to ! in bash)
#
# If not set, print error and exit
#if (-not $env:TWINE_PASSWORD) {
  # Write-Error outputs formatted error message to host
  Write-Error "❌ TWINE_PASSWORD not set. Create a PyPI API token and set TWINE_PASSWORD environment variable."
  # Exit with error code 1
  exit 1
}

# ============================================================================
# STEP 4: UPLOAD TO PyPI
# ============================================================================
# Use twine to upload the package distribution files to PyPI
#
# Key points:
#   • --non-interactive: Don't prompt for password interactively
#   • -u __token__: PyPI requires username to be literal '__token__'
#   • -p $env:TWINE_PASSWORD: API token from environment variable (PowerShell syntax)
#   • dist/*: Upload all files in dist\ directory (PowerShell glob)
#
# What happens:
#   - Twine reads .whl and .tar.gz files from .\dist\
#   - Uploads metadata and package to PyPI
#   - Creates/updates package page on PyPI website
#   - Package becomes installable via: pip install lightgpt
#
Write-Host "📤 Uploading to PyPI..." -ForegroundColor Cyan
python -m twine upload --non-interactive -u __token__ -p $env:TWINE_PASSWORD dist/*

# ============================================================================
# SUCCESS
# ============================================================================
# If we get here, everything succeeded without errors
Write-Host "✅ Package successfully published to PyPI!" -ForegroundColor Green
Write-Host "🎉 LightGPT is now available via: pip install lightgpt" -ForegroundColor Green
