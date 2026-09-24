"""
Game Engine & Business Logic Service
------------------------------------
CLEAN ARCHITECTURE - BUSINESS LOGIC LAYER
"""

import string
from datetime import datetime, timezone, timedelta
from typing import Tuple

from app.models.database import Exercise, User
from app.core.config import settings


def normalize_text(text: str) -> str:
    cleaned = text.strip().lower()
    cleaned = cleaned.rstrip(string.punctuation)
    return cleaned


def evaluate_exercise_answer(exercise: Exercise, user_answer: str) -> Tuple[bool, str]:
    if exercise.exercise_type == "pair_match":
        is_correct = user_answer.strip().lower() in ["pairs_completed", "done", "true"]
        explanation = exercise.explanation or "All pairs matched correctly!"
        return is_correct, explanation

    normalized_user = normalize_text(user_answer)
    normalized_correct = normalize_text(exercise.correct_answer)

    is_correct = (normalized_user == normalized_correct)
    explanation = exercise.explanation or f"Correct answer: {exercise.correct_answer}"

    return is_correct, explanation


def update_user_streak(user: User) -> int:
    now = datetime.now(timezone.utc)
    last_active = user.last_active_date

    time_diff = now - last_active.replace(tzinfo=timezone.utc) if last_active.tzinfo is None else now - last_active

    if time_diff.days == 0:
        pass
    elif time_diff.days == 1:
        user.streak_days += 1
    else:
        user.streak_days = 1

    user.last_active_date = now
    return user.streak_days


def award_lesson_rewards(user: User, accuracy: int, base_xp: int = 20) -> dict:
    earned_xp = base_xp + settings.XP_LESSON_COMPLETION_BONUS
    bonus_gems = 5 if accuracy == 100 else 2

    if accuracy == 100:
        earned_xp += 10

    user.total_xp += earned_xp
    user.gems += bonus_gems

    new_streak = update_user_streak(user)

    return {
        "xp_gained": earned_xp,
        "new_total_xp": user.total_xp,
        "new_streak": new_streak,
        "gems_awarded": bonus_gems,
        "message": "Bra jobbat! (Well done!) Perfect lesson!" if accuracy == 100 else "Lesson completed! Keep it up!",
    }
