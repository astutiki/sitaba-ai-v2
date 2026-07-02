"""
Database Model
Knowledge Cache
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


class KnowledgeCache(Base):

    __tablename__ = "knowledge_cache"

    id = Column(Integer, primary_key=True, index=True)

    # CACHE KEY
    cache_key = Column(String(255), unique=True, nullable=False, index=True)

    # QUERY
    query = Column(Text, nullable=False)
    normalized_query = Column(Text, nullable=True)
    intent = Column(String(100), nullable=True)
    category = Column(String(100), nullable=True)

    # KNOWLEDGE SOURCE
    knowledge_module = Column(String(100), nullable=True)
    knowledge_function = Column(String(150), nullable=True)
    source = Column(String(100), default="Knowledge Base")

    # RESPONSE
    answer = Column(Text, nullable=False)
    answer_summary = Column(Text, nullable=True)

    # METADATA
    language = Column(String(20), default="id")
    tags = Column(Text, nullable=True)

    # CACHE
    cache_hit = Column(Integer, default=0)
    ttl_seconds = Column(Integer, default=3600)
    is_active = Column(Boolean, default=True)
    is_expired = Column(Boolean, default=False)

    # QUALITY
    rating_average = Column(Integer, nullable=True)
    total_liked = Column(Integer, default=0)
    total_disliked = Column(Integer, default=0)

    # TIME
    created_at = Column(DateTime, server_default=func.now())

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    expired_at = Column(DateTime, nullable=True)