"""Trying to fid bug

Revision ID: 7da4367c6937
Revises: 64568605d624
Create Date: 2017-10-16 15:26:23.043747

"""

# revision identifiers, used by Alembic.
revision = '7da4367c6937'
down_revision = '64568605d624'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('survey_answers_id', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('primary_programming_language_used_at_work', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('years_of_pro_exp', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('jobs', sa.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('tech_role', sa.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###
