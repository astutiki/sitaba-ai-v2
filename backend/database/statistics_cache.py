"""
Database Model
Statistics Cache
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


class StatisticsCache(Base):

    __tablename__ = "statistics_cache"

    # =====================================================
    # PRIMARY KEY
    # =====================================================

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # =====================================================
    # CACHE KEY
    # =====================================================

    cache_key = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    query = Column(
        Text,
        nullable=False
    )

    intent = Column(
        String(100),
        nullable=True
    )

    # =====================================================
    # FILTER
    # =====================================================

    province = Column(
        String(100),
        nullable=True
    )

    city = Column(
        String(100),
        nullable=True
    )

    disaster_type = Column(
        String(100),
        nullable=True
    )

    year = Column(
        Integer,
        nullable=True
    )

    month = Column(
        Integer,
        nullable=True
    )

    # =====================================================
    # RESPONSE
    # =====================================================

    total_disaster = Column(
        Integer,
        nullable=True
    )

    total_province = Column(
        Integer,
        nullable=True
    )

    total_city = Column(
        Integer,
        nullable=True
    )

    statistics_json = Column(
        Text,
        nullable=False
    )

    # =====================================================
    # SOURCE
    # =====================================================

    source = Column(
        String(100),
        default="SITABA API"
    )

    endpoint = Column(
        String(255),
        nullable=True
    )

    api_version = Column(
        String(50),
        nullable=True
    )

    # =====================================================
    # CACHE
    # =====================================================

    cache_hit = Column(
        Integer,
        default=0
    )

    ttl_seconds = Column(
        Integer,
        default=600
    )

    is_active = Column(
        Boolean,
        default=True
    )

    is_expired = Column(
        Boolean,
        default=False
    )

    # =====================================================
    # TIME
    # =====================================================

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    expired_at = Column(
        DateTime,
        nullable=True
    )