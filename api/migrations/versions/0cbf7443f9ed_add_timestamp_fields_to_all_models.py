"""Add timestamp fields to all models

Revision ID: 0cbf7443f9ed
Revises: f5d963a2559b
Create Date: 2020-04-22 19:14:41.508732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cbf7443f9ed'
down_revision = 'f5d963a2559b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin_user', sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False))
    op.add_column('admin_user', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('categories', sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False))
    op.add_column('categories', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('grant_tag', sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False))
    op.add_column('grant_tag', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('grants', sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False))
    op.add_column('grants', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'created_at')
    op.drop_column('grants', 'updated_at')
    op.drop_column('grants', 'created_at')
    op.drop_column('grant_tag', 'updated_at')
    op.drop_column('grant_tag', 'created_at')
    op.drop_column('categories', 'updated_at')
    op.drop_column('categories', 'created_at')
    op.drop_column('admin_user', 'updated_at')
    op.drop_column('admin_user', 'created_at')
    # ### end Alembic commands ###
