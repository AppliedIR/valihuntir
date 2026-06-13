#!/usr/bin/env bash
set -euo pipefail

echo "Starting Valhuntir Lite demo container"

# Create a temp cases dir
CASES_DIR="/tmp/vhir-cases"
mkdir -p "$CASES_DIR"

echo "Initializing demo case..."
vhir case init "demo-case" --cases-dir "$CASES_DIR" || true

echo
echo "Listing cases (should show demo-case):"
vhir case list --cases-dir "$CASES_DIR" || true

echo
echo "Show active case status (if any):"
vhir case status --cases-dir "$CASES_DIR" || true

echo
echo "Demo complete. To explore interactively, run a shell in the container."
exec /bin/bash
