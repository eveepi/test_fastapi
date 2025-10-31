# test_fastapi

A minimal FastAPI example project.

## Overview

This repository contains a small FastAPI application (under `src/api_v1`) used for demos and development.

Key points

- The FastAPI documentation: https://fastapi.tiangolo.com/
- Devcontainer / VS Code Remote - Containers docs: https://code.visualstudio.com/docs/devcontainers/containers

All project dependencies are declared in `src/pyproject.toml`.

## Quick start (local)

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies using your preferred tool. The dependency list is in `src/pyproject.toml` — install with Poetry, pip, or your tool of choice. Example using pip (PEP 517/518):

```bash
pip install .
```

3. Run the app with Uvicorn (from the repository root):

```bash
cd src
uvicorn api_v1.main:app --reload --port 8000
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. The interactive API docs are available at `/docs` (Swagger UI) and `/redoc`.

## Quick start (Docker / docker-compose)

If you prefer containers, there is a `Dockerfile` and `docker-compose.yml` in the repo root. Build and run with:

```bash
docker-compose up --build
```

This will build the image and start the service (check `docker-compose.yml` for ports).

## Using the Devcontainer (VS Code)

This project includes a devcontainer configuration (in `.devcontainer/`) to provide a ready-to-code environment in VS Code.

To use it:

1. Install the "Remote - Containers" / "Dev Containers" extension in VS Code.
2. Open this repository in VS Code.
3. From the Command Palette (F1) choose "Remote-Containers: Reopen in Container" (or "Dev Containers: Reopen in Container").

The devcontainer will build and provide an environment with the configured Python toolchain and extensions. Once inside the container you can run the same commands above (install deps, run uvicorn, run tests) without installing tools on your host.

## Tests

Run tests from the repository root (ensures virtualenv activated or inside devcontainer):

```bash
pytest -q
```
