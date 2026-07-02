"""
Database Model
Login Logs
AI SINTA
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    Text,
)

from sqlalchemy.sql import func

from database.database import Base


class LoginLog(Base):
    __tablename__ = "login_logs"

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
        index=True,
        nullable=True
    )

    fullname = Column(
        String(150),
        nullable=True
    )

    email = Column(
        String(150),
        index=True,
        nullable=True
    )

    role = Column(
        String(50),
        nullable=True
    )

    # =====================================================
    # LOGIN
    # =====================================================

    login_method = Column(
        String(50),
        default="password"
    )

    login_status = Column(
        String(30),
        default="SUCCESS"
    )

    failure_reason = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # CLIENT
    # =====================================================

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

    browser_version = Column(
        String(50),
        nullable=True
    )

    operating_system = Column(
        String(100),
        nullable=True
    )

    device_type = Column(
        String(50),
        nullable=True
    )

    hostname = Column(
        String(255),
        nullable=True
    )

    # =====================================================
    # SESSION
    # =====================================================

    session_id = Column(
        String(100),
        nullable=True
    )

    access_token = Column(
        String(255),
        nullable=True
    )

    refresh_token = Column(
        String(255),
        nullable=True
    )

    # =====================================================
    # LOCATION
    # =====================================================

    country = Column(
        String(100),
        nullable=True
    )

    province = Column(
        String(100),
        nullable=True
    )

    city = Column(
        String(100),
        nullable=True
    )

    latitude = Column(
        String(50),
        nullable=True
    )

    longitude = Column(
        String(50),
        nullable=True
    )

    # =====================================================
    # SECURITY
    # =====================================================

    is_vpn = Column(
        Boolean,
        default=False
    )

    is_suspicious = Column(
        Boolean,
        default=False
    )

    two_factor_enabled = Column(
        Boolean,
        default=False
    )

    # =====================================================
    # LOGOUT
    # =====================================================

    logout_time = Column(
        DateTime,
        nullable=True
    )

    session_duration_seconds = Column(
        Integer,
        nullable=True
    )

    # =====================================================
    # CREATED
    # =====================================================

    created_at = Column(
        DateTime,
        server_default=func.now()
    )