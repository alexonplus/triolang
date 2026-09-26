"""
================================================================================
TrioLang Tenses Domain Service
================================================================================
CLEAN ARCHITECTURE - DOMAIN SERVICE LAYER
Provides business logic for verb tense curriculum queries, drill execution,
SQLite progress persistence, and integration with AI Memory.
"""

import json
import logging
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.core.config import settings
from app.data.tenses import ALL_TENSES
from app.models.database import User, UserTenseProgress
from app.models.schemas import (
    TenseSummary,
    TenseDetail,
    TenseDrillsResponse,
    TenseExerciseItem,
    TenseDrillSubmitResponse,
)
from app.services.ai_memory_service import AIMemoryService

logger = logging.getLogger(__name__)


class TensesService:
    """
    Domain service managing grammatical tenses curriculum and drill evaluations.
    """

    @staticmethod
    def get_tenses(
        db: Session,
        user_id: int,
        language: Optional[str] = None,
        time_aspect: Optional[str] = None,
    ) -> List[TenseSummary]:
        """
        List tenses filtered by language and aspect, enriched with user mastery from DB.
        """
        filtered = ALL_TENSES
        if language:
            filtered = [t for t in filtered if t["language"] == language.lower()]
        if time_aspect and time_aspect.lower() != "all":
            filtered = [t for t in filtered if t["time_aspect"] == time_aspect.lower()]

        # Query user progress map
        progress_records = db.query(UserTenseProgress).filter(UserTenseProgress.user_id == user_id).all()
        progress_map = {p.tense_id: p for p in progress_records}

        result = []
        for t in filtered:
            prog = progress_map.get(t["id"])
            mastery = prog.mastery_percentage if prog else 0
            attempts = prog.attempts_count if prog else 0

            result.append(
                TenseSummary(
                    id=t["id"],
                    language=t["language"],
                    time_aspect=t["time_aspect"],
                    title=t["title"],
                    swedish_title=t["swedish_title"],
                    level=t["level"],
                    summary=t["summary"],
                    formula=t["formula"],
                    signal_words=t.get("signal_words", []),
                    timeline_description=t.get("timeline_description", ""),
                    mastery_percentage=mastery,
                    attempts_count=attempts,
                )
            )
        return result

    @staticmethod
    def get_tense_detail(db: Session, user_id: int, tense_id: str) -> Optional[TenseDetail]:
        """
        Fetch full tense explanation, timeline, examples, pitfalls, and user mastery.
        """
        tense = next((t for t in ALL_TENSES if t["id"] == tense_id), None)
        if not tense:
            return None

        prog = (
            db.query(UserTenseProgress)
            .filter(UserTenseProgress.user_id == user_id, UserTenseProgress.tense_id == tense_id)
            .first()
        )
        mastery = prog.mastery_percentage if prog else 0
        attempts = prog.attempts_count if prog else 0

        return TenseDetail(
            id=tense["id"],
            language=tense["language"],
            time_aspect=tense["time_aspect"],
            title=tense["title"],
            swedish_title=tense["swedish_title"],
            level=tense["level"],
            summary=tense["summary"],
            formula=tense["formula"],
            signal_words=tense.get("signal_words", []),
            timeline_description=tense.get("timeline_description", ""),
            examples=tense.get("examples", []),
            common_pitfalls=tense.get("common_pitfalls", []),
            exercises_count=len(tense.get("exercises", [])),
            mastery_percentage=mastery,
            attempts_count=attempts,
        )

    @staticmethod
    def get_drills(tense_id: str) -> Optional[TenseDrillsResponse]:
        """
        Retrieve built-in interactive exercises for a specific tense.
        """
        tense = next((t for t in ALL_TENSES if t["id"] == tense_id), None)
        if not tense:
            return None

        exercises = [
            TenseExerciseItem(
                id=ex["id"],
                type=ex["type"],
                prompt=ex["prompt"],
                options=ex.get("options"),
                correct_answer=ex["correct_answer"],
                explanation=ex.get("explanation"),
            )
            for ex in tense.get("exercises", [])
        ]

        return TenseDrillsResponse(
            tense_id=tense["id"],
            tense_title=tense["title"],
            language=tense["language"],
            time_aspect=tense["time_aspect"],
            exercises=exercises,
        )

    @classmethod
    def submit_drill_answer(
        cls,
        db: Session,
        user_id: int,
        tense_id: str,
        exercise_id: int,
        user_answer: str,
    ) -> TenseDrillSubmitResponse:
        """
        Evaluate answer, update SQLite user progress, log mistake if incorrect, and compute AI feedback.
        """
        user = db.query(User).filter(User.id == user_id).first()
        tense = next((t for t in ALL_TENSES if t["id"] == tense_id), None)

        if not tense or not user:
            raise ValueError("Invalid tense or user.")

        # Find exercise
        exercise = next((ex for ex in tense.get("exercises", []) if ex["id"] == exercise_id), None)
        if not exercise:
            # Fallback check across all tenses
            for t in ALL_TENSES:
                ex = next((e for e in t.get("exercises", []) if e["id"] == exercise_id), None)
                if ex:
                    exercise = ex
                    break

        if not exercise:
            raise ValueError(f"Exercise {exercise_id} not found.")

        is_correct = user_answer.strip().lower() == exercise["correct_answer"].strip().lower()
        xp_earned = settings.XP_PER_CORRECT_ANSWER if is_correct else 0

        # Update or create progress record
        prog = (
            db.query(UserTenseProgress)
            .filter(UserTenseProgress.user_id == user_id, UserTenseProgress.tense_id == tense_id)
            .first()
        )

        if not prog:
            prog = UserTenseProgress(
                user_id=user_id,
                tense_id=tense_id,
                language=tense["language"],
                attempts_count=1,
                correct_count=1 if is_correct else 0,
                mastery_percentage=100 if is_correct else 0,
                last_practiced_at=datetime.now(timezone.utc),
            )
            db.add(prog)
        else:
            prog.attempts_count += 1
            if is_correct:
                prog.correct_count += 1
            prog.mastery_percentage = round((prog.correct_count / prog.attempts_count) * 100)
            prog.last_practiced_at = datetime.now(timezone.utc)

        if is_correct:
            user.total_xp += xp_earned
        else:
            # Log mistake into AI memory
            AIMemoryService.log_mistake(
                db=db,
                user_id=user_id,
                topic_or_tense_id=tense_id,
                language=tense["language"],
                prompt_text=exercise["prompt"],
                user_answer=user_answer,
                correct_answer=exercise["correct_answer"],
                explanation=exercise.get("explanation"),
            )

        db.commit()
        db.refresh(prog)
        db.refresh(user)

        ai_feedback = None
        if not is_correct:
            ai_feedback = f"AI Memory logged this mistake. Current mastery for {tense['title']}: {prog.mastery_percentage}%."

        return TenseDrillSubmitResponse(
            is_correct=is_correct,
            correct_answer=exercise["correct_answer"],
            explanation=exercise.get("explanation"),
            xp_earned=xp_earned,
            new_mastery_percentage=prog.mastery_percentage,
            ai_memory_feedback=ai_feedback,
        )
