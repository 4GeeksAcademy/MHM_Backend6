"""empty message

Revision ID: 8a49cf1470cc
Revises: 185b5f308ae7
Create Date: 2023-06-18 00:47:52.133970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a49cf1470cc'
down_revision = '185b5f308ae7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('journal_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_string', sa.Date(), nullable=False))
        batch_op.drop_column('date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('journal_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DATE(), autoincrement=False, nullable=False))
        batch_op.drop_column('date_string')

    # ### end Alembic commands ###