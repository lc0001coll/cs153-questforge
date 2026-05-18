"""initial empty migration

Revision ID: 0001_initial
Revises:
Create Date: 2026-05-17

Establishes the migration chain. No schema changes yet — tables will be added
in subsequent migrations as models land.
"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "0001_initial"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
