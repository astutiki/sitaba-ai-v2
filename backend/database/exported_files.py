"""
Database Model
Exported Files
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


class ExportedFile(Base):

    __tablename__ = "exported_files"

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

    fullname = Column(
        String(150),
        nullable=True
    )

    email = Column(
        String(150),
        nullable=True
    )

    # =====================================================
    # FILE
    # =====================================================

    file_name = Column(
        String(255),
        nullable=False
    )

    original_name = Column(
        String(255),
        nullable=True
    )

    file_path = Column(
        Text,
        nullable=False
    )

    file_url = Column(
        Text,
        nullable=True
    )

    file_extension = Column(
        String(20),
        nullable=True
    )

    mime_type = Column(
        String(100),
        nullable=True
    )

    file_size = Column(
        Float,
        nullable=True
    )

    # =====================================================
    # EXPORT
    # =====================================================

    export_type = Column(
        String(50),
        nullable=False
    )

    export_source = Column(
        String(100),
        nullable=True
    )

    export_title = Column(
        String(255),
        nullable=True
    )

    description = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # CHAT
    # =====================================================

    question = Column(
        Text,
        nullable=True
    )

    answer = Column(
        Text,
        nullable=True
    )

    intent = Column(
        String(100),
        nullable=True
    )

    ai_model = Column(
        String(100),
        nullable=True
    )

    # =====================================================
   