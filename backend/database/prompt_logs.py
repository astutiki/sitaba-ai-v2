"""
Database Model
Prompt Logs
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


class PromptLog(Base):

    __tablename__ = "prompt_logs"

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

    history_id = Column(
        Integer,
        nullable=True,
        index=True
    )

    # =====================================================
    # USER QUESTION
    # =====================================================

    user_question = Column(
        Text,
        nullable=False
    )

    normalized_question = Column(
        Text,
        nullable=True
    )

    language = Column(
        String(30),
        default="id"
    )

    # =====================================================
    # INTENT
    # =====================================================

    intent = Column(
        String(100),
        nullable=True
    )

    category = Column(
        String(100),
        nullable=True
    )

    source = Column(
        String(100),
        nullable=True
    )

    confidence = Column(
        Float,
        nullable=True
    )

    # =====================================================
    # PROMPT
    # =====================================================

    system_prompt = Column(
        Text,
        nullable=True
    )

    user_prompt = Column(
        Text,
        nullable=True
    )

    final_prompt = Column(
        Text,
        nullable=True
    )

    context = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # MODEL
    # =====================================================

    provider = Column(
        String(50),
        default="Ollama"
    )

    model_name = Column(
        String(100),
        nullable=True
    )

    model_version = Column(
        String(50),
        nullable=True
    )

    temperature = Column(
        Float,
        nullable=True
    )

    top_p = Column(
        Float,
        nullable=True
    )

    max_tokens = Column(
        Integer,
        nullable=True
    )

    # =====================================================
    # RESPONSE
    # =====================================================

    ai_response = Column(
        Text,
        nullable=True
    )

    finish_reason = Column(
        String(50),
        nullable=True
    )

    # =====================================================
    # TOKEN
    # =====================================================

    prompt_tokens = Column(
        Integer,
        default=0
    )

    completion_tokens = Column(
        Integer,
        default=0
    )

    total_tokens = Column(
        Integer,
        default=0
    )

    # =====================================================
    # PERFORMANCE
    # =====================================================

    response_time_ms = Column(
        Float,
        nullable=True
    )

    api_time_ms = Column(
        Float,
        nullable=True
    )

    processing_time_ms = Column(
        Float,
        nullable=True
    )

    # =====================================================
    # STATUS
    # =====================================================

    success = Column(
        Boolean,
        default=True
    )

    cache_hit = Column(
        Boolean,
        default=False
    )

    hallucination = Column(
        Boolean,
        default=False
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
    # FEEDBACK
    # =====================================================

    user_rating = Column(
        Integer,
        nullable=True
    )

    user_feedback = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # CREATED
    # =====================================================

    created_at = Column(
        DateTime,
        server_default=func.now()
    )