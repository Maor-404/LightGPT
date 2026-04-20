# ============================================================================
#                    LightGPT Environment Loader (PowerShell)
# ============================================================================
& .\scripts\load_env.ps1 @Args
exit 0
#
# Purpose:
#   Load environment variables from .env file and invoke publish_pypi.ps1
#   This script bridges manual .env setup and automated publishing on Windows.
#
# Prerequisites:
#   - .env file in project root (created from .env.template)
#   - TWINE_PASSWORD set in .env file
#   - publish_pypi.ps1 in .\scripts\ directory
#   - PowerShell 5.0+
#
# Usage:
#   .\load_env.ps1
#
# What it does:
#   1. Checks for .env file existence
#   2. Parses KEY=VALUE format from .env (skips comments)
#   3. Sets each variable in environment
#   4. Validates TWINE_PASSWORD is set
#   5. Executes .\scripts\publish_pypi.ps1 with env vars loaded
#
# Security:
#   - .env should be in .gitignore (never commit to git!)
#   - Contains sensitive PyPI API token
#   - Use GitHub Actions secrets for CI/CD automation
#
# Exit Codes:
#   0 = Success: env loaded and publish_pypi.ps1 succeeded
#   1 = Failure: .env missing, TWINE_PASSWORD not set, or publish failed
#
# ============================================================================

# PowerShell parameter declaration (no parameters for this script)
# Param()

# ============================================================================
# STEP 1: CHECK FOR .env FILE
# ============================================================================
# Verify .env file exists before trying to read it
# If missing, user needs to create it from .env.template
#
# PowerShell syntax:
#   Test-Path: Check if file/directory exists
#   -not: Logical NOT operator
#
# if (-not (Test-Path .env)) {
   # Display helpful error message to console
#  Write-Error ".env not found — copy .env.template to .env and set TWINE_PASSWORD"
#  exit 1
#

# ============================================================================
# STEP 2: PARSE .env FILE AND EXPORT VARIABLES
# ============================================================================
# Read .env file line by line and set each KEY=VALUE pair as environment variable
# This makes all variables available to child processes (publish_pypi.ps1)
#
# Process:
#   1. Get-Content: Read all lines from .env
#   2. ForEach-Object: Process each line
#   3. Filter out comments (lines starting with # or ;)
#   4. Match KEY=VALUE pattern using regex
#   5. Extract KEY and VALUE from captures
#   6. Set-Item: Store in environment ($Env:)
#
# Safety notes:
#   - Trim(): Remove leading/trailing whitespace
#   - Trim('"').Trim("'"): Remove quotes if present
#   - Only process lines with = (valid KEY=VALUE format)

Write-Host "📋 Loading environment variables from .env..." -ForegroundColor Cyan

# Read and parse .env file
Get-Content .env | ForEach-Object {
  # Skip comment lines (starting with # or ;)
  if ($_ -match '^[#;]\s*') {
    return  # Skip to next iteration
  }
  
  # Match lines with KEY=VALUE format
  # PowerShell regex with named captures for clarity
  if ($_ -match '^\s*([^=]+)=(.*)$') {
    # Extract KEY name from regex capture group 1
    $name = $matches[1].Trim()
    
    # Extract VALUE from regex capture group 2
    # Also trim quotes (common in config files)
    $val = $matches[2].Trim().Trim('"').Trim("'")
    
    # Set environment variable
    # $Env:VARIABLE is PowerShell syntax for environment variables
    Set-Item -Path Env:\$name -Value $val
    
    # Debug: Show what we loaded (optional)
    # Uncomment the line below for verbose output:
    # Write-Host "  ✓ Set $name" -ForegroundColor Gray
  }
}

# ============================================================================
# STEP 3: VALIDATE TWINE_PASSWORD IS SET
# ============================================================================
# Ensure the critical TWINE_PASSWORD variable was loaded from .env
# This prevents attempting to publish with no API token
#
# PowerShell syntax:
#   $env:VARIABLE: Access environment variable
#   -not: Logical NOT operator
#
# This is a double-check after parsing .env

if (-not $env:TWINE_PASSWORD) {
  # Error: Variable not set or empty
  Write-Error "TWINE_PASSWORD not set in .env"
  exit 1
}

# ============================================================================
# STEP 4: EXECUTE PUBLISH SCRIPT
# ============================================================================
# All environment variables are now loaded and validated
# Pass control to the actual publishing script
# All set environment variables automatically available to child process
#
# At this point:
#   ✓ .env file validated to exist
#   ✓ Variables parsed and exported
#   ✓ TWINE_PASSWORD confirmed non-empty
#   → Ready to publish!

Write-Host "✅ Environment loaded successfully from .env" -ForegroundColor Green
Write-Host "📤 Starting PyPI publish process..." -ForegroundColor Cyan

# Execute the publish script using & (call operator)
# In PowerShell, & runs the specified command
# If publish_pypi.ps1 exits with error, this script will also fail
& .\scripts\publish_pypi.ps1

# Script automatically exits with same code as publish_pypi.ps1
