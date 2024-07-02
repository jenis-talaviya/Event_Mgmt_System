"""event managament system  detail

Revision ID: a0b0eac39fad
Revises: 7ff1a4691130
Create Date: 2024-06-14 20:31:00.272708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0b0eac39fad'
down_revision: Union[str, None] = '7ff1a4691130'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audio_visual',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('contact_number', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('cost', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('catering',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('contact_number', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('cost', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('decoandfloral',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('contact_number', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('cost', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('entertainment',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('contact_number', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('cost', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('logistic',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('setup_breakdown', sa.String(length=50), nullable=False),
    sa.Column('staffing_volunteers', sa.String(length=50), nullable=False),
    sa.Column('security_safety', sa.String(length=50), nullable=False),
    sa.Column('transportation_parking', sa.String(length=50), nullable=False),
    sa.Column('signage_directions', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('manager',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('contact_no', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photo_video_graphy',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('contact_number', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('cost', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transportation',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('contact_number', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('cost', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('Event_id', sa.String(length=50), nullable=True),
    sa.Column('E_name', sa.String(length=50), nullable=False),
    sa.Column('E_venue', sa.String(length=50), nullable=False),
    sa.Column('E_date', sa.Date(), nullable=False),
    sa.Column('E_time', sa.Time(), nullable=False),
    sa.Column('E_location', sa.String(length=250), nullable=False),
    sa.Column('E_description', sa.String(length=250), nullable=False),
    sa.Column('E_guest_size', sa.Integer(), nullable=False),
    sa.Column('E_price', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['Event_id'], ['manager.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.String(length=50), nullable=False),
    sa.Column('event_id', sa.String(length=50), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('payment_status', sa.String(length=50), nullable=False),
    sa.Column('transaction_id', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('event_id', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venue',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('event_id', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('contact_number', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('cost', sa.String(length=50), nullable=False),
    sa.Column('facility', sa.String(length=999), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue')
    op.drop_table('status')
    op.drop_table('payment')
    op.drop_table('event')
    op.drop_table('transportation')
    op.drop_table('photo_video_graphy')
    op.drop_table('manager')
    op.drop_table('logistic')
    op.drop_table('entertainment')
    op.drop_table('decoandfloral')
    op.drop_table('catering')
    op.drop_table('audio_visual')
    # ### end Alembic commands ###
