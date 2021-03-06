"""empty message

Revision ID: 6708b4ef6bf9
Revises: 0cbf7443f9ed
Create Date: 2020-04-22 20:03:25.304089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6708b4ef6bf9'
down_revision = '0cbf7443f9ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('procuct_categories',
    sa.Column('product_category_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_category_id'], ['product_category.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('product_category_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('procuct_categories')
    op.drop_table('product_category')
    # ### end Alembic commands ###
