"""empty message

Revision ID: cb8b51145b50
Revises: 2cc2c8ab3952
Create Date: 2023-06-17 20:57:57.691586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb8b51145b50'
down_revision = '2cc2c8ab3952'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('journal_entries',
    sa.Column('entry_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('mood', sa.String(length=255), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('entry_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journal_entries')
    # ### end Alembic commands ###
