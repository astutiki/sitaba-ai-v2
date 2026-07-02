"""
Database Model
Suggested Questions
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


class SuggestedQuestion(Base):

    __tablename__ = "suggested_questions"

    # =====================================================
    # PRIMARY KEY
    # =====================================================

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # =====================================================
    # CATEGORY
    # =====================================================

    category = Column(
        String(100),
        nullable=False,
        index=True
    )

    sub_category = Column(
        String(100),
        nullable=True
    )

    intent = Column(
        String(100),
        nullable=True
    )

    # =====================================================
    # QUESTION
    # =====================================================

    title = Column(
        String(255),
        nullable=False
    )

    question = Column(
        Text,
        nullable=False
    )

    answer = Column(
        Text,
        nullable=True
    )

    description = Column(
        Text,
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

    # =====================================================
    # AI
    # =====================================================

    source = Column(
        String(100),
        default="SITABA"
    )

    ai_model = Column(
        String(100),
        nullable=True
    )

    # =====================================================
    # POPULARITY
    # =====================================================

    total_clicked = Column(
        Integer,
        default=0
    )

    total_used = Column(
        Integer,
        default=0
    )

    popularity_score = Column(
        Integer,
        default=0
    )

    # =====================================================
    # DISPLAY
    # =====================================================

    display_order = Column(
        Integer,
        default=1
    )

    icon = Column(
        String(100),
        nullable=True
    )

    color = Column(
        String(50),
        nullable=True
    )

    # =====================================================
    # STATUS
    # =====================================================

    is_featured = Column(
        Boolean,
        default=False
    )

    is_active = Column(
        Boolean,
        default=True
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