"""empty message

Revision ID: dbce5a9b3eb7
Revises: 8a49cf1470cc
Create Date: 2023-06-18 00:52:03.061913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbce5a9b3eb7'
down_revision = '8a49cf1470cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('journal_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.String(length=255), nullable=False))
        batch_op.drop_column('date_string')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('journal_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_string', sa.DATE(), autoincrement=False, nullable=False))
        batch_op.drop_column('date')

    # ### end Alembic commands ###
