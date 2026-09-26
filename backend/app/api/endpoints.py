"""
API Router & Endpoints Module
-----------------------------
CLEAN ARCHITECTURE - PRESENTATION LAYER
"""

import json
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.database import get_db, Course, Unit, Lesson, Exercise, User, UserLessonProgress
from app.models.schemas import (
    UserResponse,
    UserUpdateCourseRequest,
    CourseResponse,
    UnitResponse,
    LessonDetail,
    AnswerSubmitRequest,
    AnswerSubmitResponse,
    LessonCompleteRequest,
    LessonCompleteResponse,
    AITutorQuestionRequest,
    AITutorResponse,
    GenerateLessonRequest,
    GenerateLessonResponse,
    PlacementQuestionItem,
    PlacementEvaluateRequest,
    PlacementEvaluationResponse,
)
from app.services.game_engine import evaluate_exercise_answer, award_lesson_rewards
from app.services.ai_tutor import ask_ai_tutor
from app.services.lesson_generator import generate_and_save_ai_lesson
from app.services.placement_service import get_placement_questions, evaluate_and_generate_personalized_path
from app.core.config import settings

router = APIRouter()


@router.get("/user", response_model=UserResponse, summary="Get current user stats & profile")
def get_user_profile(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User profile not found.")
    return user


@router.post("/user/active-course", response_model=UserResponse, summary="Switch active learning course")
def switch_active_course(payload: UserUpdateCourseRequest, db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    course = db.query(Course).filter(Course.id == payload.course_id).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course '{payload.course_id}' not found.")

    user.active_course_id = payload.course_id
    db.commit()
    db.refresh(user)
    return user


@router.post("/user/refill-hearts", response_model=UserResponse, summary="Refill user hearts to 5")
def refill_hearts(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    user.hearts = 5
    db.commit()
    db.refresh(user)
    return user


@router.get("/courses", response_model=List[CourseResponse], summary="List available courses")
def list_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    response_list = []
    for c in courses:
        units_count = db.query(Unit).filter(Unit.course_id == c.id).count()
        response_list.append(
            CourseResponse(
                id=c.id,
                title=c.title,
                native_title=c.native_title,
                flag_emoji=c.flag_emoji,
                target_language=c.target_language,
                source_language=c.source_language,
                description=c.description,
                units_count=units_count,
            )
        )
    return response_list


@router.get("/courses/{course_id}/units", response_model=List[UnitResponse], summary="Get units & learning path")
def get_course_units(course_id: str, db: Session = Depends(get_db)):
    user = db.query(User).first()
    completed_lesson_ids = set()
    if user:
        completed_records = db.query(UserLessonProgress).filter(
            UserLessonProgress.user_id == user.id,
            UserLessonProgress.is_completed == True
        ).all()
        completed_lesson_ids = {r.lesson_id for r in completed_records}

    units = db.query(Unit).filter(Unit.course_id == course_id).order_by(Unit.order_index).all()
    
    result = []
    for unit in units:
        lessons_data = []
        for lesson in unit.lessons:
            is_completed = lesson.id in completed_lesson_ids
            lessons_data.append({
                "id": lesson.id,
                "unit_id": lesson.unit_id,
                "order_index": lesson.order_index,
                "title": lesson.title,
                "swedish_title": lesson.swedish_title,
                "xp_reward": lesson.xp_reward,
                "is_completed": is_completed,
                "is_locked": False,
            })
        
        result.append(
            UnitResponse(
                id=unit.id,
                course_id=unit.course_id,
                order_index=unit.order_index,
                title=unit.title,
                swedish_title=unit.swedish_title,
                description=unit.description,
                icon_name=unit.icon_name,
                theme_color=unit.theme_color,
                lessons=lessons_data,
            )
        )
    return result


@router.get("/lessons/{lesson_id}", response_model=LessonDetail, summary="Get full lesson exercises")
def get_lesson_detail(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found.")

    formatted_exercises = []
    for ex in lesson.exercises:
        formatted_exercises.append({
            "id": ex.id,
            "lesson_id": ex.lesson_id,
            "order_index": ex.order_index,
            "exercise_type": ex.exercise_type,
            "prompt_text": ex.prompt_text,
            "target_audio_text": ex.target_audio_text,
            "target_language": ex.target_language,
            "correct_answer": ex.correct_answer,
            "options": json.loads(ex.options_json) if ex.options_json else None,
            "word_bank": json.loads(ex.word_bank_json) if ex.word_bank_json else None,
            "pairs": json.loads(ex.pairs_json) if ex.pairs_json else None,
            "explanation": ex.explanation,
        })

    return LessonDetail(
        id=lesson.id,
        unit_id=lesson.unit_id,
        order_index=lesson.order_index,
        title=lesson.title,
        swedish_title=lesson.swedish_title,
        xp_reward=lesson.xp_reward,
        is_completed=False,
        is_locked=False,
        exercises=formatted_exercises,
    )


@router.post("/exercises/submit", response_model=AnswerSubmitResponse, summary="Check exercise answer")
def submit_exercise_answer(payload: AnswerSubmitRequest, db: Session = Depends(get_db)):
    user = db.query(User).first()
    exercise = db.query(Exercise).filter(Exercise.id == payload.exercise_id).first()
    if not exercise or not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise or User not found.")

    is_correct, explanation = evaluate_exercise_answer(exercise, payload.user_answer)

    xp_earned = 0
    gems_earned = 0

    if is_correct:
        xp_earned = settings.XP_PER_CORRECT_ANSWER
        user.total_xp += xp_earned
    else:
        if user.hearts > 0:
            user.hearts -= 1

    db.commit()
    db.refresh(user)

    return AnswerSubmitResponse(
        is_correct=is_correct,
        correct_answer=exercise.correct_answer,
        explanation=explanation,
        xp_earned=xp_earned,
        hearts_remaining=user.hearts,
        gems_earned=gems_earned,
    )


@router.post("/lessons/complete", response_model=LessonCompleteResponse, summary="Finalize completed lesson")
def complete_lesson(payload: LessonCompleteRequest, db: Session = Depends(get_db)):
    user = db.query(User).first()
    lesson = db.query(Lesson).filter(Lesson.id == payload.lesson_id).first()
    if not user or not lesson:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User or Lesson not found.")

    progress = db.query(UserLessonProgress).filter(
        UserLessonProgress.user_id == user.id,
        UserLessonProgress.lesson_id == payload.lesson_id
    ).first()

    if not progress:
        progress = UserLessonProgress(
            user_id=user.id,
            lesson_id=payload.lesson_id,
            is_completed=True,
            accuracy_percentage=payload.accuracy_percentage
        )
        db.add(progress)
    else:
        progress.is_completed = True
        progress.accuracy_percentage = max(progress.accuracy_percentage, payload.accuracy_percentage)

    reward_data = award_lesson_rewards(user, payload.accuracy_percentage, lesson.xp_reward)

    db.commit()
    db.refresh(user)

    return LessonCompleteResponse(
        lesson_id=lesson.id,
        xp_gained=reward_data["xp_gained"],
        new_total_xp=reward_data["new_total_xp"],
        new_streak=reward_data["new_streak"],
        gems_awarded=reward_data["gems_awarded"],
        message=reward_data["message"],
    )


# ------------------------------------------------------------------------------
# 4. AI Grammar Tutor & Dynamic Lesson Generator Endpoints
# ------------------------------------------------------------------------------
@router.post("/ai/tutor", response_model=AITutorResponse, summary="Ask AI Tutor for grammar help")
async def ask_tutor_endpoint(payload: AITutorQuestionRequest):
    tutor_data = await ask_ai_tutor(
        query=payload.query,
        target_language=payload.target_language,
        context=payload.context or ""
    )
    return AITutorResponse(**tutor_data)


@router.post("/ai/generate-lesson", response_model=GenerateLessonResponse, summary="Generate dynamic AI lesson")
async def generate_lesson_endpoint(
    payload: GenerateLessonRequest,
    db: Session = Depends(get_db),
):
    try:
        result = await generate_and_save_ai_lesson(
            db=db,
            course_id=payload.course_id,
            raw_topic=payload.topic,
        )
        return GenerateLessonResponse(**result)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Lesson generation failed: {str(err)}",
        )


# ------------------------------------------------------------------------------
# 5. Diagnostic Placement Test Endpoints
# ------------------------------------------------------------------------------
@router.get("/ai/placement-questions", response_model=List[PlacementQuestionItem], summary="Get placement probe questions")
def get_placement_questions_endpoint(course_id: str = "sv-from-en", db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    target_lang = course.target_language if course else "sv"
    questions = get_placement_questions(target_lang)
    return [PlacementQuestionItem(**q) for q in questions]


@router.post("/ai/diagnostic-evaluate", response_model=PlacementEvaluationResponse, summary="Evaluate diagnostic test & generate custom path")
async def evaluate_diagnostic_endpoint(
    payload: PlacementEvaluateRequest,
    db: Session = Depends(get_db),
):
    try:
        transcript = [{"sender": turn.sender, "text": turn.text} for turn in payload.dialogue]
        result = await evaluate_and_generate_personalized_path(
            db=db,
            course_id=payload.course_id,
            dialogue_transcript=transcript,
        )
        return PlacementEvaluationResponse(**result)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Diagnostic evaluation failed: {str(err)}",
        )
