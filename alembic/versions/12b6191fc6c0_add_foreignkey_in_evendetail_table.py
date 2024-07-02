"""add foreignkey in evendetail table

Revision ID: 12b6191fc6c0
Revises: edaa1badf27f
Create Date: 2024-07-01 16:40:29.232156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12b6191fc6c0'
down_revision: Union[str, None] = 'edaa1badf27f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('E_venue_id', sa.String(length=50), nullable=True))
    op.add_column('event', sa.Column('E_catering_id', sa.String(length=50), nullable=True))
    op.add_column('event', sa.Column('E_decoandfloral_id', sa.String(length=50), nullable=True))
    op.add_column('event', sa.Column('E_audiovisual_id', sa.String(length=50), nullable=True))
    op.add_column('event', sa.Column('E_entertainment_id', sa.String(length=50), nullable=True))
    op.add_column('event', sa.Column('E_photoandvideography_id', sa.String(length=50), nullable=True))
    op.add_column('event', sa.Column('E_transportation_id', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'event', 'entertainment', ['E_entertainment_id'], ['id'])
    op.create_foreign_key(None, 'event', 'audio_visual', ['E_audiovisual_id'], ['id'])
    op.create_foreign_key(None, 'event', 'photo_video_graphy', ['E_photoandvideography_id'], ['id'])
    op.create_foreign_key(None, 'event', 'transportation', ['E_transportation_id'], ['id'])
    op.create_foreign_key(None, 'event', 'venue', ['E_venue_id'], ['id'])
    op.create_foreign_key(None, 'event', 'decoandfloral', ['E_decoandfloral_id'], ['id'])
    op.create_foreign_key(None, 'event', 'catering', ['E_catering_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_column('event', 'E_transportation_id')
    op.drop_column('event', 'E_photoandvideography_id')
    op.drop_column('event', 'E_entertainment_id')
    op.drop_column('event', 'E_audiovisual_id')
    op.drop_column('event', 'E_decoandfloral_id')
    op.drop_column('event', 'E_catering_id')
    op.drop_column('event', 'E_venue_id')
    # ### end Alembic commands ###