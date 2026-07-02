"""
Database Model
Bookmarked Questions
AI SINTA
"""

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func

from database.database import Base


class BookmarkedQuestion(Base):
    __tablename__ = "bookmarked_questions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=True, index=True)

    session_id = Column(String(100), nullable=True, index=True)

    history_id = Column(Integer, nullable=True, index=True)

    question = Column(Text, nullable=False)

    answer = Column(Text, nullable=True)

    intent = Column(String(100), nullable=True)

    source = Column(String(100), nullable=True)

    category = Column(String(100), nullable=True)

    title = Column(String(255), nullable=True)

    note = Column(Text, nullable=True)

    tags = Column(Text, nullable=True)

    is_favorite = Column(Boolean, default=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )