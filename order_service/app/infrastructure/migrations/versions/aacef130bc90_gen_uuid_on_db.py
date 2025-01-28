"""gen uuid on db

Revision ID: aacef130bc90
Revises: 73aeb5b42d19
Create Date: 2025-01-28 17:33:45.469600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aacef130bc90'
down_revision: Union[str, None] = '73aeb5b42d19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'products',
        'product_id',
        server_default=sa.text('gen_random_uuid()'),
        existing_type=sa.dialects.postgresql.UUID(as_uuid=True),
    )
    op.alter_column(
        'orders',
        'order_id',
        server_default=sa.text('gen_random_uuid()'),
        existing_type=sa.dialects.postgresql.UUID(as_uuid=True),
    )
    op.alter_column(
        'order_products',
        'id',
        server_default=sa.text('gen_random_uuid()'),
        existing_type=sa.dialects.postgresql.UUID(as_uuid=True),
    )


def downgrade() -> None:
    op.alter_column(
        'products',
        'product_id',
        server_default=sa.text('gen_random_uuid()'),
        existing_type=sa.dialects.postgresql.UUID(as_uuid=True),
    )
    op.alter_column(
        'orders',
        'order_id',
        server_default=sa.text('gen_random_uuid()'),
        existing_type=sa.dialects.postgresql.UUID(as_uuid=True),
    )
    op.alter_column(
        'order_products',
        'id',
        server_default=sa.text('gen_random_uuid()'),
        existing_type=sa.dialects.postgresql.UUID(as_uuid=True),
    )
