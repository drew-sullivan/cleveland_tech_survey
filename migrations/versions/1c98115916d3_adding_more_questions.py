"""Adding more questions

Revision ID: 1c98115916d3
Revises: 1b42576891e0
Create Date: 2017-10-16 19:47:06.292841

"""

# revision identifiers, used by Alembic.
revision = '1c98115916d3'
down_revision = '1b42576891e0'

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
    op.drop_column('users', 'favorite_cleveland_hangout_area')
    op.drop_column('users', 'favorite_cleveland_activity')
    # ### end Alembic commands ###
