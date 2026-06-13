# FIND EVIL! — Valhuntir + Protocol SIFT (Demo)

Project: Valhuntir Lite — Rapid demo of Valhuntir CLI for Protocol SIFT hackathon

Deadline: Jun 16, 2026

Summary
-------
Valhuntir Lite provides a minimal, reproducible container to demo Valhuntir's `vhir` CLI for hackathon judges. It installs the CLI from the repository in editable mode and runs a scripted demo that initializes a case and shows basic case management commands. This allows judges to explore the human-in-the-loop workflow without requiring SIFT, OpenSearch, or additional VMs.

Key Features
------------
- Reproducible Docker demo that installs the repository and exercises the `vhir` CLI.
- Demo script that initializes a case, lists cases, and shows case status.
- Clear instructions for building and running the container locally.

How it maps to Protocol SIFT
----------------------------
This demo highlights Valhuntir's human-in-the-loop case management and approval workflow in a minimal environment, making it easier to showcase the platform during the hackathon even when judges cannot run full SIFT VMs.

How to build and run (for judges / reviewers)
--------------------------------------------
From the repository root:

```bash
cd demo-lite
docker build -t valhuntir-lite:latest -f Dockerfile ..
docker run --rm -it valhuntir-lite:latest
```

Notes for maintainers
---------------------
- The demo intentionally avoids running SIFT or OpenSearch; it is a minimal, portable showcase to help judges quickly validate functionality.
- Next steps: add automated smoke tests, create a GitHub Action to publish a demo image, and record short screencast.

CI
--
This repository includes a GitHub Actions workflow (`.github/workflows/ci.yml`) which:

- Installs `vhir` and dev dependencies
- Runs the test suite (including the demo smoke test)
- Builds the `demo-lite` Docker image (without pushing it)

This helps ensure the demo is reproducible for reviewers and provides an automated validation path for hackathon submissions.
