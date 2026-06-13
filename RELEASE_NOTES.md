# Release Notes — Hackathon demo additions

Summary of changes made for the FIND EVIL! hackathon:

- Added `demo-lite/` directory with a `Dockerfile` and `entrypoint.sh` to provide a lightweight, reproducible Valhuntir CLI demo.
- Added `devpost/DEVPOST.md`, `devpost/VIDEO_SCRIPT.md`, and `devpost/ASSETS.md` to prepare submission assets and a short demo script.
- Added a pytest smoke test `tests/test_demo_smoke.py` to verify basic CLI functionality.
- Added CI workflow `.github/workflows/ci.yml` to run tests and build the demo image in GitHub Actions.

Next steps:

1. Push branch to a fork and open a PR for review.
2. Build the demo image locally (or let CI build it). Capture screenshots and record the 90s demo.
3. Optionally configure a registry and add publish step to CI.
