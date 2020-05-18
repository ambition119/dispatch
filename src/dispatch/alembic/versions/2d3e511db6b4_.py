"""Adds required or multiple fields to plugin data

Revision ID: 2d3e511db6b4
Revises: 62465f508f69
Create Date: 2020-04-23 15:07:03.996871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2d3e511db6b4"
down_revision = "62465f508f69"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("plugin", sa.Column("multiple", sa.Boolean(), nullable=True))
    op.add_column("plugin", sa.Column("required", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("plugin", "required")
    op.drop_column("plugin", "multiple")
    # ### end Alembic commands ###
