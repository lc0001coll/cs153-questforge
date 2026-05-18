# Questforge

A multiplayer AI Dungeon Master for D&D campaigns (Stanford CS153).
This repository currently contains only the project scaffolding — backend +
frontend + Postgres in Docker, wired up end-to-end via a `/health` route.

## Prerequisites

- [`uv`](https://docs.astral.sh/uv/) (Python env + deps)
- Node 20+ and npm
- Docker (for the Postgres container)

## One-time setup

```bash
# 1. Clone and enter the repo
cd questforge

# 2. Copy environment defaults
cp .env.example .env

# 3. Install backend + frontend dependencies
make install
```

## Running the stack locally

In three terminals (or background the first two):

```bash
# Terminal 1 — start Postgres
make up

# Terminal 2 — apply migrations, then start FastAPI on :8000
make migrate
make backend

# Terminal 3 — start the Vite dev server on :5173
make frontend
```

Then open <http://localhost:5173>. The Home page should render
`Backend: ok` and `Database: ok`.

## Verifying the scaffold

```bash
# Backend tests
make test

# Lint (ruff + eslint + prettier)
make lint

# Quick health check
curl http://localhost:8000/api/health
# -> {"status":"ok","db":"ok"}
```

## Layout

```
questforge/
├── backend/      # FastAPI + SQLAlchemy (async) + Alembic, managed by uv
├── frontend/     # Vite + React + TypeScript, React Router
├── docker-compose.yml
└── Makefile
```

## What's next

The following pieces are intentionally **not** in this scaffold and will be
added in later:

- AI Dungeon Master pipeline (Anthropic SDK, prompts, tool use)
- Auth / user accounts / sessions
- WebSocket layer for real-time multiplayer
- `pgvector` extension and RAG over campaign memory
- Persistent world graph (entities, locations, relationships)
- Domain models, schemas, and migrations beyond the empty initial revision
- Production deployment (CI, container builds, hosted DB)
```
