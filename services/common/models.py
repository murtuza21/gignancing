from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class UserRole(str, Enum):
    ADMIN = "Admin"
    UNDERWRITER = "Underwriter"
    SUPPORT = "Support"
    USER = "User"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    phone: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    role: Mapped[str] = mapped_column(String(20), default=UserRole.USER.value)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    connections: Mapped[list[PlatformConnection]] = relationship(
        "PlatformConnection", back_populates="user"
    )
    loans: Mapped[list[Loan]] = relationship("Loan", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"


class PlatformConnection(Base):
    __tablename__ = "platform_connections"
    __table_args__ = (UniqueConstraint("user_id", "platform"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    platform: Mapped[str] = mapped_column(String(50))
    external_id: Mapped[str] = mapped_column(String(100))
    connected_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped[User] = relationship("User", back_populates="connections")

    def __repr__(self) -> str:
        return (
            f"PlatformConnection(id={self.id!r}, user_id={self.user_id!r},"
            f" platform={self.platform!r})"
        )


class Earning(Base):
    __tablename__ = "earnings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    connection_id: Mapped[int] = mapped_column(ForeignKey("platform_connections.id"))
    amount: Mapped[Numeric] = mapped_column(Numeric(10, 2))
    recorded_at: Mapped[datetime] = mapped_column(DateTime)

    connection: Mapped[PlatformConnection] = relationship("PlatformConnection")

    def __repr__(self) -> str:
        return (
            f"Earning(id={self.id!r}, connection_id={self.connection_id!r},"
            f" amount={self.amount!r})"
        )


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    principal: Mapped[Numeric] = mapped_column(Numeric(10, 2))
    interest_rate: Mapped[Numeric] = mapped_column(Numeric(5, 2))
    term_months: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    status: Mapped[str] = mapped_column(String(20), default="pending")

    user: Mapped[User] = relationship("User", back_populates="loans")
    repayments: Mapped[list[Repayment]] = relationship(
        "Repayment", back_populates="loan"
    )

    def __repr__(self) -> str:
        return f"Loan(id={self.id!r}, user_id={self.user_id!r}, principal={self.principal!r})"


class Repayment(Base):
    __tablename__ = "repayments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    loan_id: Mapped[int] = mapped_column(ForeignKey("loans.id"))
    amount: Mapped[Numeric] = mapped_column(Numeric(10, 2))
    due_date: Mapped[datetime] = mapped_column(DateTime)
    paid_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    loan: Mapped[Loan] = relationship("Loan", back_populates="repayments")

    def __repr__(self) -> str:
        return f"Repayment(id={self.id!r}, loan_id={self.loan_id!r}, amount={self.amount!r})"


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    message: Mapped[str] = mapped_column(Text)
    sent_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    read: Mapped[bool] = mapped_column(Boolean, default=False)
    read_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    user: Mapped[User] = relationship("User")

    def __repr__(self) -> str:
        return f"Notification(id={self.id!r}, user_id={self.user_id!r}, read={self.read!r})"


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id"), nullable=True
    )
    action: Mapped[str] = mapped_column(String(100))
    metadata: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ip_address: Mapped[Optional[str]] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped[Optional[User]] = relationship("User")

    def __repr__(self) -> str:
        return f"AuditLog(id={self.id!r}, action={self.action!r})"


class Consent(Base):
    __tablename__ = "consents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    consent_type: Mapped[str] = mapped_column(String(50))
    granted_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    revoked_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    user: Mapped[User] = relationship("User")

    def __repr__(self) -> str:
        return f"Consent(id={self.id!r}, user_id={self.user_id!r}, type={self.consent_type!r})"
