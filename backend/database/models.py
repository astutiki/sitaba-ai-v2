"""
Database Models
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy.sql import func

from database.database import Base


# =====================================================
# USER
# =====================================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    fullname = Column(String(100))

    email = Column(String(100), unique=True)

    password = Column(String(255))

    role = Column(String(20), default="user")

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())


# =====================================================
# CHAT HISTORY
# =====================================================

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True)

    session_id = Column(String(100))

    user_id = Column(Integer)

    question = Column(Text)

    answer = Column(Text)

    intent = Column(String(50))

    source = Column(String(100))

    created_at = Column(DateTime, server_default=func.now())


# =====================================================
# FEEDBACK
# =====================================================

class Feedback(Base):

    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    question = Column(Text)

    answer = Column(Text)

    rating = Column(Integer)

    comment = Column(Text)

    created_at = Column(DateTime, server_default=func.now())