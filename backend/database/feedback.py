"""
Database Model
Feedback AI SINTA
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


class Feedback(Base):

    __tablename__ = "feedback"

    # =====================================================
    # PRIMARY KEY
    # =====================================================

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # =====================================================
    # RELASI
    # =====================================================

    user_id = Column(
        Integer,
        index=True,
        nullable=True
    )

    session_id = Column(
        String(100),
        index=True,
        nullable=True
    )

    history_id = Column(
        Integer,
        index=True,
        nullable=True
    )

    # =====================================================
    # PERTANYAAN & JAWABAN
    # =====================================================

    question = Column(
        Text,
        nullable=False
    )

    answer = Column(
        Text,
        nullable=False
    )

    # =====================================================
    # AI
    # =====================================================

    intent = Column(
        String(100),
        nullable=True
    )

    source = Column(
        String(100),
        nullable=True
    )

    model_name = Column(
        String(100),
        nullable=True
    )

    # =====================================================
    # FEEDBACK
    # =====================================================

    rating = Column(
        Integer,
        nullable=True
    )

    is_like = Column(
        Boolean,
        default=False
    )

    is_dislike = Column(
        Boolean,
        default=False
    )

    feedback_type = Column(
        String(50),
        nullable=True
    )

    comment = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # STATUS
    # =====================================================

    is_reviewed = Column(
        Boolean,
        default=False
    )

    reviewed_by = Column(
        String(100),
        nullable=True
    )

    review_note = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # WAKTU
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