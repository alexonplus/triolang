"""
================================================================================
TrioLang AI Memory Engine
================================================================================
CLEAN ARCHITECTURE - AI MEMORY DOMAIN SERVICE
Maintains persistent learner state across sessions in SQLite:
analyzes historical mistake logs, tracks tense mastery levels, and generates
personalized diagnostic memory profiles.
"""

import json
import logging
from typing import Dict, List, Any
from sqlalchemy.orm import Session

from app.models.database import User, UserTenseProgress, UserMistakeLog, UserAIMemoryProfile
from app.models.schemas import AIMemoryProfileResponse
from app.core.config import settings

logger = logging.getLogger(__name__)


class AIMemoryService:
    """
    Persistent AI learner memory service managing diagnostic analytics and error profiling.
    """

    @classmethod
    def get_or_create_profile(cls, db: Session, user_id: int) -> UserAIMemoryProfile:
        """
        Fetch existing user memory profile or create a fresh initial record.
        """
        profile = db.query(UserAIMemoryProfile).filter(UserAIMemoryProfile.user_id == user_id).first()
        if not profile:
            profile = UserAIMemoryProfile(
                user_id=user_id,
                detected_strengths_json=json.dumps([]),
                detected_weaknesses_json=json.dumps([]),
                recommended_focus_json=json.dumps([]),
                overall_tense_accuracy=100,
                ai_tutor_summary_notes="Initial baseline learner profile established.",
            )
            db.add(profile)
            db.commit()
            db.refresh(profile)
        return profile

    @classmethod
    def log_mistake(
        cls,
        db: Session,
        user_id: int,
        topic_or_tense_id: str,
        language: str,
        prompt_text: str,
        user_answer: str,
        correct_answer: str,
        explanation: str = None,
    ) -> None:
        """
        Permanently record an erroneous drill response for AI memory analysis.
        """
        mistake = UserMistakeLog(
            user_id=user_id,
            topic_or_tense_id=topic_or_tense_id,
            language=language,
            prompt_text=prompt_text,
            user_answer=user_answer,
            correct_answer=correct_answer,
            explanation=explanation,
        )
        db.add(mistake)
        db.commit()

        # Re-compute and refresh the memory profile
        cls.recalculate_memory_profile(db, user_id)

    @classmethod
    def recalculate_memory_profile(cls, db: Session, user_id: int) -> AIMemoryProfileResponse:
        """
        Recalculate mastery statistics, detect patterns in mistake logs, and update profile.
        """
        user = db.query(User).filter(User.id == user_id).first()
        username = user.username if user else "Learner"

        # Query all tense progress records
        progress_records = db.query(UserTenseProgress).filter(UserTenseProgress.user_id == user_id).all()
        mistakes_count = db.query(UserMistakeLog).filter(UserMistakeLog.user_id == user_id).count()

        strengths: List[str] = []
        weaknesses: List[str] = []
        recommended: List[str] = []

        total_attempts = 0
        total_correct = 0

        for p in progress_records:
            total_attempts += p.attempts_count
            total_correct += p.correct_count

            if p.attempts_count >= 3:
                if p.mastery_percentage >= 75:
                    strengths.append(f"{p.tense_id} ({p.mastery_percentage}% mastery)")
                elif p.mastery_percentage < 60:
                    weaknesses.append(f"{p.tense_id} ({p.mastery_percentage}% mastery)")
                    recommended.append(p.tense_id)

        # Recent mistake analysis
        recent_mistakes = (
            db.query(UserMistakeLog)
            .filter(UserMistakeLog.user_id == user_id)
            .order_by(UserMistakeLog.created_at.desc())
            .limit(10)
            .all()
        )

        mistake_tense_frequency: Dict[str, int] = {}
        for m in recent_mistakes:
            mistake_tense_frequency[m.topic_or_tense_id] = (
                mistake_tense_frequency.get(m.topic_or_tense_id, 0) + 1
            )

        for tense_id, count in mistake_tense_frequency.items():
            if count >= 2 and tense_id not in recommended:
                weaknesses.append(f"{tense_id} ({count} recent mistakes)")
                recommended.append(tense_id)

        overall_accuracy = (
            round((total_correct / total_attempts) * 100) if total_attempts > 0 else 100
        )

        # AI Coaching note synthesis
        if weaknesses:
            coaching_note = (
                f"TrioBot Memory Notice: We observed recurring difficulties with {', '.join(recommended[:2])}. "
                f"We recommend focused drill practice to reinforce these temporal patterns."
            )
        elif strengths:
            coaching_note = (
                f"TrioBot Memory Notice: Excellent consistency in {', '.join(strengths[:2])}! "
                f"Ready to advance to higher CEFR tense nuances."
            )
        else:
            coaching_note = "TrioBot Memory: Baseline active. Practice tense drills to calibrate your AI mastery profile."

        # Save to DB
        profile = cls.get_or_create_profile(db, user_id)
        profile.detected_strengths_json = json.dumps(strengths)
        profile.detected_weaknesses_json = json.dumps(weaknesses)
        profile.recommended_focus_json = json.dumps(recommended)
        profile.overall_tense_accuracy = overall_accuracy
        profile.ai_tutor_summary_notes = coaching_note
        db.commit()

        return AIMemoryProfileResponse(
            username=username,
            overall_accuracy=overall_accuracy,
            detected_strengths=strengths,
            detected_weaknesses=weaknesses,
            recommended_focus_tenses=recommended,
            total_mistakes_logged=mistakes_count,
            ai_coaching_note=coaching_note,
        )
