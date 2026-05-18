from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.main import app


class _FakeResult:
    def scalar(self) -> int:
        return 1


class _FakeSession:
    """Minimal stand-in for AsyncSession so /health can run without a real DB."""

    async def execute(self, _statement: object) -> _FakeResult:
        return _FakeResult()


async def _override_session() -> AsyncIterator[AsyncSession]:
    yield _FakeSession()  # type: ignore[misc]


@pytest.fixture(autouse=True)
def _patch_session():
    app.dependency_overrides[get_session] = _override_session
    yield
    app.dependency_overrides.clear()


async def test_health_ok() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "db": "ok"}
