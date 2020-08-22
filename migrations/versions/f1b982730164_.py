"""empty message

Revision ID: f1b982730164
Revises: 
Create Date: 2020-08-22 17:28:08.365889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1b982730164'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=1000), nullable=False),
    sa.Column('price', sa.Float(asdecimal=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vendor_name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('longitude', sa.String(length=16), nullable=False),
    sa.Column('latitude', sa.String(length=16), nullable=False),
    sa.Column('vendor_id', sa.Integer(), nullable=False),
    sa.Column('is_open', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('started_at', sa.DateTime(), nullable=False),
    sa.Column('cancel_order', sa.DateTime(), nullable=True),
    sa.Column('closed_at', sa.DateTime(), nullable=False),
    sa.Column('expected_pickup', sa.DateTime(), nullable=False),
    sa.Column('vendor_id', sa.Integer(), nullable=False),
    sa.Column('sub_total_price', sa.Float(asdecimal=True), nullable=False),
    sa.Column('total_price', sa.Float(asdecimal=True), nullable=False),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendor.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('order_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Float(asdecimal=True), nullable=False),
    sa.Column('special_instructions', sa.String(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Float(asdecimal=True), nullable=False),
    sa.Column('payment_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('payment_type', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    op.drop_table('order_item')
    op.drop_table('order')
    op.drop_table('location')
    op.drop_table('vendor')
    op.drop_table('product')
    # ### end Alembic commands ###
