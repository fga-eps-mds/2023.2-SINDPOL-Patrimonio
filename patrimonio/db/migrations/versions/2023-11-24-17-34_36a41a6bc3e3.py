"""empty message

Revision ID: 36a41a6bc3e3
Revises: 
Create Date: 2023-11-24 17:34:20.457718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36a41a6bc3e3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "patrimony",
        sa.Column("id", sa.String(length=200), primary_key=True, nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(length=200), nullable=False),
        sa.Column("items_description", sa.String(length=200), nullable=False),
        sa.Column("acquisition_date", sa.Date, nullable=False),
        sa.Column("local", sa.String(length=200), nullable=False),
        sa.Column("serial_number", sa.Integer, nullable=False),
        sa.Column("patrimony_type", sa.String(length=200), nullable=False),
        sa.Column("patrimony_value", sa.Float, nullable=False),
        sa.Column("items_value", sa.Float, nullable=False),
        sa.Column("sector", sa.String(length=200), nullable=False),
        sa.Column("conservation_state", sa.Integer, nullable=False),
        sa.Column("invoice_number", sa.Integer, nullable=False),
        sa.Column("brand", sa.String(length=200), nullable=False),
        sa.Column("manufacturer", sa.String(length=200), nullable=False),
        sa.Column("model", sa.String(length=200), nullable=False),
        sa.Column("depreciation_value", sa.Float, nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        schema="public",
    )


def downgrade() -> None:
    op.drop_table("patrimony")
