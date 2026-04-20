#!/usr/bin/env bash
################################################################################
#                    LightGPT PyPI Publisher (Bash)
################################################################################
#
# Purpose:
#   Build and publish the LightGPT package to PyPI (Python Package Index)
#   This script automates the entire build and upload process.
#
# Prerequisites:
#   - Python 3.7+ installed
#   - PyPI account with API token generated
#   - TWINE_PASSWORD environment variable set
#
# Usage:
#   export TWINE_PASSWORD=<your-pypi-api-token>
#   ./scripts/publish_pypi.sh
#
# Example:
#   export TWINE_PASSWORD=pypi-AgEIcHlwaS5vcmc...
#   ./scripts/publish_pypi.sh
#
# Security Notes:
#   - NEVER commit TWINE_PASSWORD to git (use .gitignore)
#   - Use GitHub Actions secrets for CI/CD publishing
#   - API tokens should be repo-scoped, not user account wide
#
# Exit Codes:
#   0 = Success: package published to PyPI
#   1 = Failure: TWINE_PASSWORD not set or build/upload error
#
################################################################################

# Enable strict error handling:
# -e: Exit immediately if any command exits with non-zero status
# -u: Treat unset variables as errors
# -o pipefail: Pipe fails if any command in pipeline fails
set -euo pipefail

# ============================================================================
# STEP 1: INSTALL BUILD TOOLS
# ============================================================================
# Install/upgrade the 'build' package (PEP 517/518 build backend)
# and 'twine' (PyPI upload tool)
# The --upgrade flag ensures we have the latest versions
echo "📦 Installing build tools (build, twine)..."
python -m pip install --upgrade build twine

# ============================================================================
# STEP 2: BUILD THE PACKAGE
# ============================================================================
# Use the 'build' module to create distribution files
# This reads pyproject.toml and creates:
#   - .whl file (wheel distribution: binary package)
#   - .tar.gz file (source distribution: for source installs)
# Output goes to ./dist/ directory
echo "🔨 Building LightGPT package..."
python -m build

# ============================================================================
# STEP 3: VALIDATE TWINE_PASSWORD
# ============================================================================
# Check if TWINE_PASSWORD environment variable is set
# 
# Explanation of the syntax:
#   [ -z "${TWINE_PASSWORD:-}" ]
#   - -z: Returns true if string is empty
#   - ${var:-}: Expands to $var if set, otherwise empty string
#   - :- prefix allows checking even if variable is unset (no error)
#
# If not set, print error and exit
if [ -z "${TWINE_PASSWORD:-}" ]; then
  # Send error message to stderr (>&2 means redirect to stderr)
  echo "❌ TWINE_PASSWORD not set. Create a PyPI API token and set TWINE_PASSWORD environment variable." >&2
  exit 1
fi

# ============================================================================
# STEP 4: UPLOAD TO PyPI
# ============================================================================
# Use twine to upload the package distribution files to PyPI
#
# Key points:
#   • --non-interactive: Don't prompt for password interactively
#   • -u __token__: PyPI requires username to be literal '__token__'
#   • -p "$TWINE_PASSWORD": API token from environment variable
#   • dist/*: Upload all files in dist/ directory
#
# What happens:
#   - Twine reads .whl and .tar.gz files from ./dist/
#   - Uploads metadata to PyPI
#   - Creates/updates package page on PyPI
#   - Package becomes installable via: pip install lightgpt
#
echo "📤 Uploading to PyPI..."
python -m twine upload --non-interactive -u __token__ -p "$TWINE_PASSWORD" dist/*

# ============================================================================
# SUCCESS
# ============================================================================
# If we get here, everything succeeded
echo "✅ Package successfully published to PyPI!"
echo "🎉 LightGPT is now available via: pip install lightgpt"
