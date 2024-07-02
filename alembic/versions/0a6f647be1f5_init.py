"""init

Revision ID: 0a6f647be1f5
Revises: 6df1fe0e1d39
Create Date: 2024-06-06 17:41:56.735445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a6f647be1f5'
down_revision: Union[str, None] = '6df1fe0e1d39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('mobile_no', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'mobile_no')
    # ### end Alembic commands ###
