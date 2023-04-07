"""Rename zone table

Revision ID: 2d84c4a48d08
Revises: bd687f0e65dd
Create Date: 2023-01-14 19:03:49.673018

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "2d84c4a48d08"
down_revision = "bd687f0e65dd"
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table("zone", "event_zone")


def downgrade():
    op.rename_table("event_zone", "zone")
