"""add email verification fields

Revision ID: beffcd5c8abd
Revises: c29facfe716b
Create Date: 2025-11-02 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "beffcd5c8abd"
down_revision: Union[str, None] = "c29facfe716b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add email_verified column with server_default False
    op.add_column("user", sa.Column("email_verified", sa.Boolean(), nullable=True, server_default=sa.false()))
    # Add email_verification_token column
    op.add_column("user", sa.Column("email_verification_token", sa.String(), nullable=True))

    # Update existing users to have email_verified=False (for safety)
    op.execute("UPDATE user SET email_verified = FALSE WHERE email_verified IS NULL")

    # Make email_verified non-nullable after setting defaults
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.alter_column("email_verified", nullable=False)


def downgrade() -> None:
    op.drop_column("user", "email_verified")
    op.drop_column("user", "email_verification_token")
