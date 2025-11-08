#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
TOKEN_FILE="${PROJECT_ROOT}/pypi-token.txt"
DIST_DIR="${PROJECT_ROOT}/dist"

if ! command -v twine >/dev/null 2>&1; then
    echo "Error: twine is not installed. Install it with 'pip install twine'." >&2
    exit 1
fi

if [ ! -f "${TOKEN_FILE}" ]; then
    echo "Error: PyPI token file not found at ${TOKEN_FILE}." >&2
    exit 1
fi

if [ ! -d "${DIST_DIR}" ] || [ -z "$(ls -A "${DIST_DIR}" 2>/dev/null)" ]; then
    echo "Error: dist directory is missing or empty. Build the distribution first (e.g. 'python -m build')." >&2
    exit 1
fi

PYPI_TOKEN="$(<"${TOKEN_FILE}")"

twine upload --non-interactive -u __token__ -p "${PYPI_TOKEN}" "${DIST_DIR}"/*
