FROM python:3.12-slim

WORKDIR /app

# System deps for building/installing
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential git \
    && rm -rf /var/lib/apt/lists/*

# Copy repo into image (build from repo root)
COPY . /app

# Install package in editable mode with dev deps for a usable demo
RUN python -m pip install --upgrade pip setuptools wheel \
    && python -m pip install -e ".[dev]" \
    && python -m pip cache purge || true

COPY entrypoint.sh /app/demo-lite/entrypoint.sh
RUN chmod +x /app/demo-lite/entrypoint.sh

ENTRYPOINT ["/app/demo-lite/entrypoint.sh"]
