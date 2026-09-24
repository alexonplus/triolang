"""
Database Models & ORM Setup Module
----------------------------------
CLEAN ARCHITECTURE - DOMAIN & PERSISTENCE LAYER
"""

from datetime import datetime, timezone
from typing import Generator, List, Optional
import json

from sqlalchemy import (
    create_engine,
    String,
    Integer,
    Boolean,
    DateTime,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
    Session,
)

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {},
    echo=False,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, default="VikingLearner")
    hearts: Mapped[int] = mapped_column(Integer, default=5)
    gems: Mapped[int] = mapped_column(Integer, default=100)
    total_xp: Mapped[int] = mapped_column(Integer, default=0)
    streak_days: Mapped[int] = mapped_column(Integer, default=1)
    last_active_date: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    active_course_id: Mapped[str] = mapped_column(String(20), default="sv-from-en")

    progress_records: Mapped[List["UserLessonProgress"]] = relationship(
        "UserLessonProgress", back_populates="user", cascade="all, delete-orphan"
    )


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    native_title: Mapped[str] = mapped_column(String(100))
    flag_emoji: Mapped[str] = mapped_column(String(10))
    target_language: Mapped[str] = mapped_column(String(10))
    source_language: Mapped[str] = mapped_column(String(10))
    description: Mapped[str] = mapped_column(Text)

    units: Mapped[List["Unit"]] = relationship(
        "Unit", back_populates="course", cascade="all, delete-orphan", order_by="Unit.order_index"
    )


class Unit(Base):
    __tablename__ = "units"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    course_id: Mapped[str] = mapped_column(String(20), ForeignKey("courses.id"), index=True)
    order_index: Mapped[int] = mapped_column(Integer, default=1)
    title: Mapped[str] = mapped_column(String(150))
    swedish_title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(Text)
    icon_name: Mapped[str] = mapped_column(String(50), default="Sparkles")
    theme_color: Mapped[str] = mapped_column(String(30), default="#10B981")

    course: Mapped["Course"] = relationship("Course", back_populates="units")
    lessons: Mapped[List["Lesson"]] = relationship(
        "Lesson", back_populates="unit", cascade="all, delete-orphan", order_by="Lesson.order_index"
    )


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    unit_id: Mapped[int] = mapped_column(Integer, ForeignKey("units.id"), index=True)
    order_index: Mapped[int] = mapped_column(Integer, default=1)
    title: Mapped[str] = mapped_column(String(150))
    swedish_title: Mapped[str] = mapped_column(String(150))
    xp_reward: Mapped[int] = mapped_column(Integer, default=20)

    unit: Mapped["Unit"] = relationship("Unit", back_populates="lessons")
    exercises: Mapped[List["Exercise"]] = relationship(
        "Exercise", back_populates="lesson", cascade="all, delete-orphan", order_by="Exercise.order_index"
    )


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lesson_id: Mapped[int] = mapped_column(Integer, ForeignKey("lessons.id"), index=True)
    order_index: Mapped[int] = mapped_column(Integer, default=1)
    exercise_type: Mapped[str] = mapped_column(String(30))
    prompt_text: Mapped[str] = mapped_column(Text)
    target_audio_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    target_language: Mapped[str] = mapped_column(String(10), default="sv")
    correct_answer: Mapped[str] = mapped_column(Text)
    options_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    word_bank_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    pairs_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    explanation: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="exercises")


class UserLessonProgress(Base):
    __tablename__ = "user_lesson_progress"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), index=True)
    lesson_id: Mapped[int] = mapped_column(Integer, ForeignKey("lessons.id"), index=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    accuracy_percentage: Mapped[int] = mapped_column(Integer, default=100)
    completed_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )

    user: Mapped["User"] = relationship("User", back_populates="progress_records")


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
