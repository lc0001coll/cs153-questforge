.PHONY: help up down migrate backend frontend test lint install

help:
	@echo "Common targets:"
	@echo "  make install   - install backend (uv sync) and frontend (npm install) deps"
	@echo "  make up        - start Postgres via docker compose"
	@echo "  make down      - stop Postgres"
	@echo "  make migrate   - run alembic upgrade head"
	@echo "  make backend   - run the FastAPI dev server on :8000"
	@echo "  make frontend  - run the Vite dev server on :5173"
	@echo "  make test      - run backend pytest"
	@echo "  make lint      - run ruff and eslint"

install:
	cd backend && uv sync
	cd frontend && npm install

up:
	docker compose up -d

down:
	docker compose down

migrate:
	cd backend && uv run alembic upgrade head

backend:
	cd backend && uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend:
	cd frontend && npm run dev

test:
	cd backend && uv run pytest

lint:
	cd backend && uv run ruff check . && uv run ruff format --check .
	cd frontend && npm run lint
