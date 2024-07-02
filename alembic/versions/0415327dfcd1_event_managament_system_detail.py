"""event managament system  detail

Revision ID: 0415327dfcd1
Revises: bc0264a34168
Create Date: 2024-06-17 11:00:50.653629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0415327dfcd1'
down_revision: Union[str, None] = 'bc0264a34168'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('audio_visual', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('audio_visual', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('audio_visual', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('audio_visual', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('catering', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('catering', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('catering', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('catering', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('decoandfloral', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('decoandfloral', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('decoandfloral', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('decoandfloral', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('entertainment', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('entertainment', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('entertainment', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('entertainment', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('photo_video_graphy', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('photo_video_graphy', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('photo_video_graphy', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('photo_video_graphy', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('status', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('status', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('status', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('status', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('transportation', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('transportation', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('transportation', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('transportation', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('venue', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('venue', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('venue', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('venue', sa.Column('modified_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'modified_at')
    op.drop_column('venue', 'created_at')
    op.drop_column('venue', 'is_active')
    op.drop_column('venue', 'is_deleted')
    op.drop_column('transportation', 'modified_at')
    op.drop_column('transportation', 'created_at')
    op.drop_column('transportation', 'is_active')
    op.drop_column('transportation', 'is_deleted')
    op.drop_column('status', 'modified_at')
    op.drop_column('status', 'created_at')
    op.drop_column('status', 'is_active')
    op.drop_column('status', 'is_deleted')
    op.drop_column('photo_video_graphy', 'modified_at')
    op.drop_column('photo_video_graphy', 'created_at')
    op.drop_column('photo_video_graphy', 'is_active')
    op.drop_column('photo_video_graphy', 'is_deleted')
    op.drop_column('entertainment', 'modified_at')
    op.drop_column('entertainment', 'created_at')
    op.drop_column('entertainment', 'is_active')
    op.drop_column('entertainment', 'is_deleted')
    op.drop_column('decoandfloral', 'modified_at')
    op.drop_column('decoandfloral', 'created_at')
    op.drop_column('decoandfloral', 'is_active')
    op.drop_column('decoandfloral', 'is_deleted')
    op.drop_column('catering', 'modified_at')
    op.drop_column('catering', 'created_at')
    op.drop_column('catering', 'is_active')
    op.drop_column('catering', 'is_deleted')
    op.drop_column('audio_visual', 'modified_at')
    op.drop_column('audio_visual', 'created_at')
    op.drop_column('audio_visual', 'is_active')
    op.drop_column('audio_visual', 'is_deleted')
    # ### end Alembic commands ###