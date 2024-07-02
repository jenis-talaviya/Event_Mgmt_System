"""remove event id in venuemanagement

Revision ID: 84907787134a
Revises: 12b6191fc6c0
Create Date: 2024-07-02 10:23:50.282404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84907787134a'
down_revision: Union[str, None] = '12b6191fc6c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('venue_event_id_fkey', 'venue', type_='foreignkey')
    op.drop_column('venue', 'event_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('event_id', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.create_foreign_key('venue_event_id_fkey', 'venue', 'event', ['event_id'], ['id'])
    # ### end Alembic commands ###