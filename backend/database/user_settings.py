"""
Database Model
User Settings
AI SINTA
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
)

from sqlalchemy.sql import func

from database.database import Base


class UserSetting(Base):

    __tablename__ = "user_settings"

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
        unique=True,
        nullable=False,
        index=True
    )

    # =====================================================
    # APPEARANCE
    # =====================================================

    theme = Column(
        String(30),
        default="light"
    )

    accent_color = Column(
        String(30),
        default="blue"
    )

    font_size = Column(
        String(20),
        default="medium"
    )

    compact_mode = Column(
        Boolean,
        default=False
    )

    # =====================================================
    # LANGUAGE
    # =====================================================

    language = Column(
        String(20),
        default="id"
    )

    timezone = Column(
        String(100),
        default="Asia/Jakarta"
    )

    # =====================================================
    # AI
    # =====================================================

    default_ai_model = Column(
        String(100),
        default="gemma3:4b"
    )

    ai_temperature = Column(
        String(20),
        default="0.2"
    )

    enable_ai_memory = Column(
        Boolean,
        default=True
    )

    auto_suggest = Column(
        Boolean,
        default=True
    )

    show_source = Column(
        Boolean,
        default=True
    )

    # =====================================================
    # CHAT
    # =====================================================

    show_timestamp = Column(
        Boolean,
        default=True
    )

    show_typing_effect = Column(
        Boolean,
        default=True
    )

    save_chat_history = Column(
        Boolean,
        default=True
    )

    auto_scroll = Column(
        Boolean,
        default=True
    )

    # =====================================================
    # EXPORT
    # =====================================================

    default_export_format = Column(
        String(20),
        default="pdf"
    )

    include_logo = Column(
        Boolean,
        default=True
    )

    include_timestamp = Column(
        Boolean,
        default=True
    )

    # =====================================================
    # NOTIFICATION
    # =====================================================

    enable_notification = Column(
        Boolean,
        default=True
    )

    sound_notification = Column(
        Boolean,
        default=False
    )

    # =====================================================
    # LOCATION
    # =====================================================

    default_province = Column(
        String(100),
        nullable=True
    )

    default_city = Column(
        String(100),
        nullable=True
    )

    # =====================================================
    # ACCESSIBILITY
    # =====================================================

    high_contrast = Column(
        Boolean,
        default=False
    )

    text_to_speech = Column(
        Boolean,
        default=False
    )

    voice_input = Column(
        Boolean,
        default=False
    )

    # =====================================================
    # STATUS
    # =====================================================

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