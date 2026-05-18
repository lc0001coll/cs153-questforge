from typing import Annotated, Literal

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session

router = APIRouter(tags=["health"])

SessionDep = Annotated[AsyncSession, Depends(get_session)]


class HealthResponse(BaseModel):
    status: Literal["ok"]
    db: Literal["ok", "error"]


@router.get("/health", response_model=HealthResponse)
async def health(session: SessionDep) -> HealthResponse:
    try:
        result = await session.execute(text("SELECT 1"))
        db_status: Literal["ok", "error"] = "ok" if result.scalar() == 1 else "error"
    except Exception:
        db_status = "error"
    return HealthResponse(status="ok", db=db_status)
