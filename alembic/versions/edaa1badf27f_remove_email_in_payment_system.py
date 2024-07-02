"""remove email in payment system

Revision ID: edaa1badf27f
Revises: 575d48fb13d0
Create Date: 2024-06-21 16:15:25.611362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edaa1badf27f'
down_revision: Union[str, None] = '575d48fb13d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payment', 'email')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    # ### end Alembic commands ###