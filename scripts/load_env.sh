#!/usr/bin/env bash
set -euo pipefail

# Load environment variables from .env and run the POSIX publish script
if [ ! -f .env ]; then
  echo ".env not found — copy .env.template to .env and set TWINE_PASSWORD" >&2
  exit 1
fi

# shellcheck disable=SC1091
source .env

if [ -z "${TWINE_PASSWORD:-}" ]; then
  echo "TWINE_PASSWORD not set in .env" >&2
  exit 1
fi

./scripts/publish_pypi.sh
