Devpost Assets Checklist

- `demo-lite/Dockerfile` (added) — builds a Valhuntir Lite demo image
- `demo-lite/entrypoint.sh` (added) — scripted demo: `vhir case init`, `vhir case list`, `vhir case status`
- `devpost/DEVPOST.md` (draft) — Devpost submission content
- `devpost/VIDEO_SCRIPT.md` — 90s demo recording script
- `devpost/ASSETS.md` (this file) — asset checklist and screenshot instructions
- `tests/test_demo_smoke.py` — CI smoke test verifying `vhir` commands
- `.github/workflows/ci.yml` — CI job to run tests and build demo image

Suggested screenshots (PNG, 1280x720):
1. `screenshots/01-demo-init.png` — terminal showing `vhir case init` succeeded
2. `screenshots/02-case-list.png` — `vhir case list` output
3. `screenshots/03-case-status.png` — `vhir case status` output

Suggested short description for Devpost header:
"Valhuntir Lite — a portable demo container to showcase Valhuntir's human-in-the-loop forensic CLI for hackathon reviewers without requiring SIFT or OpenSearch."
