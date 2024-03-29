"""Add index to event by provider_id

Revision ID: 414add6a298a
Revises: 2d84c4a48d08
Create Date: 2023-04-07 19:49:14.046359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '414add6a298a'
down_revision = '2d84c4a48d08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('event_provider_id_index', 'event', ['provider_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('event_provider_id_index', table_name='event')
    # ### end Alembic commands ###
