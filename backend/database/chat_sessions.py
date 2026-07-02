"""
Database Model
Chat Sessions - AI SINTA
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.sql import func

from database.database import Base


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(String(100), unique=True, index=True, nullable=False)

    user_id = Column(Integer, index=True, nullable=True)

    title = Column(String(255), nullable=True)

    description = Column(Text, nullable=True)

    is_active = Column(Boolean, default=True)

    is_pinned = Column(Boolean, default=False)

    created_at = Column(DateTime, server_default=func.now())

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )