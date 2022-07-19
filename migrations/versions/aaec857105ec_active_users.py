"""active_users

Revision ID: aaec857105ec
Revises: 
Create Date: 2022-06-07 10:39:48.011600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "aaec857105ec"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    print("Creating active_patients table")
    op.create_table(
        "active_patients",
        sa.Column("year_week", sa.String(), nullable=False),
        sa.Column("product_name", sa.String(), nullable=False),
        sa.Column("trust", sa.String(), nullable=False),
        sa.Column("count", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("year_week", "product_name", "trust"),
    )
    op.create_index(
        op.f("ix_active_patients_year_week"),
        "active_patients",
        ["year_week"],
        unique=False,
    )
    op.create_index(
        op.f("ix_active_patients_product_name"),
        "active_patients",
        ["product_name"],
        unique=False,
    )
    op.create_index(
        op.f("ix_active_patients_trust"), "active_patients", ["trust"], unique=False
    )

    print("Creating created_patients table")
    op.create_table(
        "created_patients",
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("product_name", sa.String(), nullable=False),
        sa.Column("trust", sa.String(), nullable=False),
        sa.Column("count", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("date", "product_name", "trust"),
    )
    op.create_index(
        op.f("ix_created_patients_year_week"),
        "created_patients",
        ["date"],
        unique=False,
    )
    op.create_index(
        op.f("ix_created_patients_product_name"),
        "created_patients",
        ["product_name"],
        unique=False,
    )
    op.create_index(
        op.f("ix_created_patients_trust"), "created_patients", ["trust"], unique=False
    )


def downgrade():
    print("Dropping active_patients table")
    op.drop_table("active_patients")

    print("Dropping created_patients table")
    op.drop_table("created_patients")
