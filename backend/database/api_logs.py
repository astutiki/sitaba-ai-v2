"""
Database Model
API Logs
AI SINTA
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Boolean,
    Float,
)

from sqlalchemy.sql import func

from database.database import Base


class ApiLog(Base):

    __tablename__ = "api_logs"

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

    session_id = Column(
        String(100),
        nullable=True,
        index=True
    )

    # =====================================================
    # REQUEST
    # =====================================================

    request_id = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    endpoint = Column(
        String(255),
        nullable=False
    )

    method = Column(
        String(20),
        nullable=False
    )

    query_params = Column(
        Text,
        nullable=True
    )

    request_headers = Column(
        Text,
        nullable=True
    )

    request_body = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # RESPONSE
    # =====================================================

    status_code = Column(
        Integer,
        nullable=True
    )

    response_headers = Column(
        Text,
        nullable=True
    )

    response_body = Column(
        Text,
        nullable=True
    )

    response_size = Column(
        Integer,
        nullable=True
    )

    # =====================================================
    # PERFORMANCE
    # =====================================================

    response_time_ms = Column(
        Float,
        nullable=True
    )

    processing_time_ms = Column(
        Float,
        nullable=True
    )

    retry_count = Column(
        Integer,
        default=0
    )

    # =====================================================
    # SOURCE
    # =====================================================

    service_name = Column(
        String(100),
        nullable=True
    )

    api_name = Column(
        String(100),
        nullable=True
    )

    api_version = Column(
        String(30),
        nullable=True
    )

    api_key_name = Column(
        String(100),
        nullable=True
    )

    # =====================================================
    # NETWORK
    # =====================================================

    client_ip = Column(
        String(100),
        nullable=True
    )

    user_agent = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # RESULT
    # =====================================================

    success = Column(
        Boolean,
        default=True
    )

    error_message = Column(
        Text,
        nullable=True
    )

    stack_trace = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # CACHE
    # =====================================================

    cache_hit = Column(
        Boolean,
        default=False
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
    # CREATED
    # =====================================================

    created_at = Column(
        DateTime,
        server_default=func.now()
    )