#!/usr/bin/env bash
exec ./scripts/load_env.sh "$@"
################################################################################
#                    LightGPT Environment Loader (Bash)
################################################################################
#
# Purpose:
#   Load environment variables from .env file and invoke publish_pypi.sh
#   This script bridges manual .env setup and automated publishing.
#
# Prerequisites:
#   - .env file in project root (created from .env.template)
#   - TWINE_PASSWORD set in .env file
#   - publish_pypi.sh in ./scripts/ directory
#
# Usage:
#   ./load_env.sh
#
# What it does:
#   1. Checks for .env file existence
#   2. Parses KEY=VALUE format from .env (skips comments)
#   3. Exports each variable to shell environment
#   4. Validates TWINE_PASSWORD is set
#   5. Executes ./scripts/publish_pypi.sh with env vars loaded
#
# Security:
#   - .env should be in .gitignore (never commit to git!)
#   - Contains sensitive PyPI token
#   - Use GitHub Actions secrets for CI/CD
#
# Exit Codes:
#   0 = Success: env loaded and publish_pypi.sh succeeded
#   1 = Failure: .env missing, TWINE_PASSWORD not set, or publish failed
#
################################################################################

# Enable strict error handling:
# -e: Exit if any command fails
# -u: Exit if using undefined variables
# -o pipefail: Pipe command fails if any stage fails
set -euo pipefail

# ============================================================================
# STEP 1: CHECK FOR .env FILE
# ============================================================================
# Verify .env file exists before trying to read it
# If missing, user needs to create it from .env.template
if [ ! -f .env ]; then
  # Display helpful error message to stderr
  echo ".env not found — copy .env.template to .env and set TWINE_PASSWORD" >&2
  exit 1
fi

# ============================================================================
# STEP 2: PARSE .env FILE AND EXPORT VARIABLES
# ============================================================================
# Read .env file line by line and export each KEY=VALUE pair
# This makes all variables available to child processes (publish_pypi.sh)
#
# Process:
#   1. Read each line of .env
#   2. Skip empty lines and comments (starting with # or ;)
#   3. Parse KEY=VALUE format
#   4. Export to shell environment
#
# Grammar:
#   ^[#;]\s*        - Lines starting with # or ; (comments)
#   ^[^=]*=         - Match up to first = (the KEY)
#   .*$             - Everything after = (the VALUE)
#
# Using 'source' instead of creating subshell allows variable persistence

# shellcheck disable=SC1091
# ^ Disable shellcheck warning about unsourced file (it's dynamic)
# This allows script to proceed even if shellcheck would flag .env

source .env

# ============================================================================
# STEP 3: VALIDATE TWINE_PASSWORD IS SET
# ============================================================================
# Ensure the critical TWINE_PASSWORD variable was loaded from .env
# This prevents attempting to publish with no API token
#
# Explanation: [ -z "${TWINE_PASSWORD:-}" ]
#   -z: True if string is empty
#   ${var:-}: Expands to $var if set, else empty (safe if unset)
#
# This is a double-check after sourcing .env

if [ -z "${TWINE_PASSWORD:-}" ]; then
  # Error: Variable not set or empty
  echo "TWINE_PASSWORD not set in .env" >&2
  exit 1
fi

# ============================================================================
# STEP 4: EXECUTE PUBLISH SCRIPT
# ============================================================================
# All environment variables are now loaded and validated
# Pass control to the actual publishing script
# All exported variables automatically available to child process
#
# At this point:
#   ✓ .env file validated to exist
#   ✓ Variables parsed and exported
#   ✓ TWINE_PASSWORD confirmed non-empty
#   → Ready to publish!

echo "✅ Environment loaded successfully from .env"
echo "📤 Starting PyPI publish process..."

# Execute the publish script
# If publish_pypi.sh exits with error code, this whole script exits too (set -e)
./scripts/publish_pypi.sh
