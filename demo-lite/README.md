# Valhuntir Lite demo (Docker)

This demo builds a lightweight container that installs the Valhuntir CLI and runs a small scripted demo: initialize a case, list cases, and show status. It's intended for hackathon demos when the host system does not have SIFT or OpenSearch available.

Build:

```bash
cd demo-lite
docker build -t valhuntir-lite:latest ..
```

Run:

```bash
docker run --rm -it valhuntir-lite:latest
```

Notes:
- The image installs the repository in editable mode with dev dependencies to ensure the `vhir` CLI entrypoint is available.
- This is a local demo for the CLI only and does not run SIFT or other MCP backends.
