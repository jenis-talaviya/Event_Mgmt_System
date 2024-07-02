"""init

Revision ID: 6ea42c9b64e2
Revises: d3741f64a636
Create Date: 2024-06-10 17:34:30.785372

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ea42c9b64e2'
down_revision: Union[str, None] = 'd3741f64a636'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('otp_details', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.drop_column('otp_details', 'is_verified')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('otp_details', sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('otp_details', 'modified_at')
    # ### end Alembic commands ###
