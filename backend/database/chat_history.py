"""
Database Model
Chat History - AI SINTA
"""

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func

from database.database import Base


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(String(100), index=True, nullable=False)

    user_id = Column(Integer, index=True, nullable=True)

    question = Column(Text, nullable=False)

    answer = Column(Text, nullable=False)

    intent = Column(String(100), nullable=True)

    source = Column(String(100), nullable=True)

    model_name = Column(String(100), nullable=True)

    response_time_ms = Column(Integer, nullable=True)

    is_liked = Column(Boolean, nullable=True)

    is_bookmarked = Column(Boolean, default=False)

    created_at = Column(DateTime, server_default=func.now())