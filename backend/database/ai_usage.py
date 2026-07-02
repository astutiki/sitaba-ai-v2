"""
Database Model
AI Usage
AI SINTA
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float,
    Boolean,
    Text,
)

from sqlalchemy.sql import func

from database.database import Base


class AIUsage(Base):

    __tablename__ = "ai_usage"

    id = Column(Integer, primary_key=True, index=True)

    # USER / SESSION
    user_id = Column(Integer, nullable=True, index=True)
    session_id = Column(String(100), nullable=True, index=True)
    history_id = Column(Integer, nullable=True, index=True)
    prompt_log_id = Column(Integer, nullable=True, index=True)

    # REQUEST
    request_id = Column(String(100), nullable=True, index=True)
    intent = Column(String(100), nullable=True)
    source = Column(String(100), nullable=True)

    # MODEL
    provider = Column(String(50), default="Ollama")
    model_name = Column(String(100), nullable=True)
    model_version = Column(String(50), nullable=True)

    # TOKEN
    prompt_tokens = Column(Integer, default=0)
    completion_tokens = Column(Integer, default=0)
    total_tokens = Column(Integer, default=0)

    # PERFORMANCE
    response_time_ms = Column(Float, nullable=True)
    api_time_ms = Column(Float, nullable=True)
    processing_time_ms = Column(Float, nullable=True)

    # COST
    estimated_cost = Column(Float, default=0.0)
    currency = Column(String(10), default="IDR")

    # RESULT
    success = Column(Boolean, default=True)
    error_message = Column(Text, nullable=True)

    # CACHE
    cache_hit = Column(Boolean, default=False)

    # QUALITY
    user_rating = Column(Integer, nullable=True)
    is_liked = Column(Boolean, nullable=True)
    is_disliked = Column(Boolean, nullable=True)

    # CREATED
    created_at = Column(DateTime, server_default=func.now())