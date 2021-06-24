"""empty message

Revision ID: abcf1e6d0fd6
Revises: 77a68bf2c58b
Create Date: 2021-04-28 17:42:12.055775

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'abcf1e6d0fd6'
down_revision = '77a68bf2c58b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('second_table_with_timezone2',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('method', sa.String(), nullable=False),
    sa.Column('json_body', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('xml_body', sa.TEXT(), nullable=True),
    sa.Column('ip', postgresql.INET(), nullable=True),
    sa.Column('content_type', sa.String(), nullable=True),
    sa.Column('login', sa.VARCHAR(), nullable=True),
    sa.Column('password', sa.VARCHAR(), nullable=True),
    sa.Column('user_agent', sa.VARCHAR(), nullable=True),
    sa.Column('date', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('second_table_with_timezone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('second_table_with_timezone',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('method', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('json_body', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('xml_body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('ip', postgresql.INET(), autoincrement=False, nullable=True),
    sa.Column('content_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('login', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('user_agent', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='second_table_with_timezone_pkey')
    )
    op.drop_table('second_table_with_timezone2')
    # ### end Alembic commands ###
