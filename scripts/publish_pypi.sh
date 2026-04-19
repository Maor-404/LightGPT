#!/usr/bin/env bash
set -euo pipefail

# Build and publish to PyPI using TWINE_PASSWORD env var (PyPI API token)
# Usage: export TWINE_PASSWORD=<pypi-token>; ./scripts/publish_pypi.sh
python -m pip install --upgrade build twine
python -m build
# TWINE_USERNAME must be '__token__' and TWINE_PASSWORD the token
if [ -z "${TWINE_PASSWORD:-}" ]; then
  echo "TWINE_PASSWORD not set. Create a PyPI API token and set TWINE_PASSWORD environment variable." >&2
  exit 1
fi
python -m twine upload --non-interactive -u __token__ -p "$TWINE_PASSWORD" dist/*
