#!/usr/bin/env bash
set -euo pipefail

echo "Starting Valhuntir Lite demo container"


# Create a temp cases dir and export VHIR_CASES_DIR so `vhir` picks it up
CASES_DIR="/tmp/vhir-cases"
mkdir -p "$CASES_DIR"
export VHIR_CASES_DIR="$CASES_DIR"

echo "Initializing demo case..."
vhir case init "demo-case" || true

echo
echo "Listing cases (should show demo-case):"
vhir case list || true

echo
echo "Show active case status (if any):"
vhir case status || true

echo
echo "Demo complete. To explore interactively, run a shell in the container."
exec /bin/bash
