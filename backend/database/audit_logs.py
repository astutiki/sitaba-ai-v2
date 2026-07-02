"""
Database Model
Audit Logs
AI SINTA
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Boolean,
)

from sqlalchemy.sql import func

from database.database import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    # =====================================================
    # PRIMARY KEY
    # =====================================================

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # =====================================================
    # USER
    # =====================================================

    user_id = Column(
        Integer,
        nullable=True,
        index=True
    )

    fullname = Column(
        String(150),
        nullable=True
    )

    email = Column(
        String(150),
        nullable=True,
        index=True
    )

    role = Column(
        String(50),
        nullable=True
    )

    session_id = Column(
        String(100),
        nullable=True,
        index=True
    )

    # =====================================================
    # ACTIVITY
    # =====================================================

    module = Column(
        String(100),
        nullable=False
    )

    action = Column(
        String(100),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # OBJECT
    # =====================================================

    object_type = Column(
        String(100),
        nullable=True
    )

    object_id = Column(
        String(100),
        nullable=True
    )

    # =====================================================
    # BEFORE & AFTER
    # =====================================================

    old_value = Column(
        Text,
        nullable=True
    )

    new_value = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # REQUEST
    # =====================================================

    endpoint = Column(
        String(255),
        nullable=True
    )

    http_method = Column(
        String(20),
        nullable=True
    )

    ip_address = Column(
        String(100),
        nullable=True
    )

    user_agent = Column(
        Text,
        nullable=True
    )

    browser = Column(
        String(100),
        nullable=True
    )

    operating_system = Column(
        String(100),
        nullable=True
    )

    device = Column(
        String(100),
        nullable=True
    )

    # =====================================================
    # RESULT
    # =====================================================

    status = Column(
        String(30),
        default="SUCCESS"
    )

    success = Column(
        Boolean,
        default=True
    )

    error_message = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # AI
    # =====================================================

    ai_model = Column(
        String(100),
        nullable=True
    )

    intent = Column(
        String(100),
        nullable=True
    )

    source = Column(
        String(100),
        nullable=True
    )

    # =====================================================
    # EXTRA
    # =====================================================

    remarks = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # TIME
    # =====================================================

    created_at = Column(
        DateTime,
        server_default=func.now()
    )