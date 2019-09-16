"""empty message

Revision ID: 52c156027bb2
Revises: 33c64f802480
Create Date: 2019-09-16 14:27:29.231679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52c156027bb2'
down_revision = '33c64f802480'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('type_id', sa.Integer(), nullable=True))
    op.drop_constraint('tickets_ticket_type_fkey', 'tickets', type_='foreignkey')
    op.drop_constraint('tickets_user_id_fkey', 'tickets', type_='foreignkey')
    op.create_foreign_key(None, 'tickets', 'tickettypes', ['type_id'], ['id'])
    op.drop_column('tickets', 'user_id')
    op.drop_column('tickets', 'ticket_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('ticket_type', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tickets', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'tickets', type_='foreignkey')
    op.create_foreign_key('tickets_user_id_fkey', 'tickets', 'users', ['user_id'], ['id'])
    op.create_foreign_key('tickets_ticket_type_fkey', 'tickets', 'tickettypes', ['ticket_type'], ['id'])
    op.drop_column('tickets', 'type_id')
    # ### end Alembic commands ###
