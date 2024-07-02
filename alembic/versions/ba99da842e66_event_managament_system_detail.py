"""event managament system  detail

Revision ID: ba99da842e66
Revises: 0415327dfcd1
Create Date: 2024-06-17 16:51:15.139811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba99da842e66'
down_revision: Union[str, None] = '0415327dfcd1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('logistic', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('logistic', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('logistic', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('logistic', sa.Column('modified_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('logistic', 'modified_at')
    op.drop_column('logistic', 'created_at')
    op.drop_column('logistic', 'is_active')
    op.drop_column('logistic', 'is_deleted')
    # ### end Alembic commands ###