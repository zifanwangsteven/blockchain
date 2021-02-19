"""empty message

Revision ID: d3b4a26af6ed
Revises: d66f086b258
Create Date: 2021-02-19 18:56:46.482964

"""

# revision identifiers, used by Alembic.
revision = 'd3b4a26af6ed'
down_revision = 'd66f086b258'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('algorand_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_address', sa.String(length=64), nullable=True),
    sa.Column('account_val', sa.Float(), nullable=True),
    sa.Column('active_since', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_address')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('algorand_accounts')
    # ### end Alembic commands ###