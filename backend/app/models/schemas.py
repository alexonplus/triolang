"""
Pydantic Schemas & DTO Module
-----------------------------
CLEAN ARCHITECTURE - DTO LAYER
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str
    hearts: int = Field(default=5, ge=0, le=5)
    gems: int = Field(default=100, ge=0)
    total_xp: int = Field(default=0, ge=0)
    streak_days: int = Field(default=1, ge=0)
    active_course_id: str = "sv-from-en"


class UserResponse(UserBase):
    id: int
    model_config = {"from_attributes": True}


class UserUpdateCourseRequest(BaseModel):
    course_id: str


class ExerciseResponse(BaseModel):
    id: int
    lesson_id: int
    order_index: int
    exercise_type: str
    prompt_text: str
    target_audio_text: Optional[str] = None
    target_language: str
    correct_answer: str
    options: Optional[List[str]] = None
    word_bank: Optional[List[str]] = None
    pairs: Optional[Dict[str, str]] = None
    explanation: Optional[str] = None

    model_config = {"from_attributes": True}


class AnswerSubmitRequest(BaseModel):
    exercise_id: int
    user_answer: str


class AnswerSubmitResponse(BaseModel):
    is_correct: bool
    correct_answer: str
    explanation: Optional[str] = None
    xp_earned: int = 0
    hearts_remaining: int = 5
    gems_earned: int = 0


class LessonSummary(BaseModel):
    id: int
    unit_id: int
    order_index: int
    title: str
    swedish_title: str
    xp_reward: int
    is_completed: bool = False
    is_locked: bool = False

    model_config = {"from_attributes": True}


class LessonDetail(LessonSummary):
    exercises: List[ExerciseResponse] = []


class LessonCompleteRequest(BaseModel):
    lesson_id: int
    accuracy_percentage: int = 100


class LessonCompleteResponse(BaseModel):
    lesson_id: int
    xp_gained: int
    new_total_xp: int
    new_streak: int
    gems_awarded: int
    message: str


class UnitResponse(BaseModel):
    id: int
    course_id: str
    order_index: int
    title: str
    swedish_title: str
    description: str
    icon_name: str
    theme_color: str
    lessons: List[LessonSummary] = []

    model_config = {"from_attributes": True}


class CourseResponse(BaseModel):
    id: str
    title: str
    native_title: str
    flag_emoji: str
    target_language: str
    source_language: str
    description: str
    units_count: int = 0
    completed_lessons_count: int = 0

    model_config = {"from_attributes": True}


class AITutorQuestionRequest(BaseModel):
    query: str
    target_language: str = "sv"
    context: Optional[str] = None


class AITutorResponse(BaseModel):
    reply: str
    suggested_followups: List[str] = []
    swedish_vocabulary: List[Dict[str, str]] = []


class GenerateLessonRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=100)
    course_id: str = Field(default="sv-from-en")


class GenerateLessonResponse(BaseModel):
    success: bool
    unit_id: int
    lesson_id: int
    title: str
    swedish_title: str
    exercise_count: int
    source: str


# ------------------------------------------------------------------------------
# Diagnostic Placement Test Schemas
# ------------------------------------------------------------------------------
class PlacementQuestionItem(BaseModel):
    id: str
    prompt: str
    english_hint: str
    level_target: str


class PlacementDialogueTurn(BaseModel):
    sender: str
    text: str


class PlacementEvaluateRequest(BaseModel):
    course_id: str = "sv-from-en"
    dialogue: List[PlacementDialogueTurn]


class PlacementEvaluationResponse(BaseModel):
    cefr_level: str
    level_title: str
    vocabulary_score: str
    strengths: List[str]
    weaknesses: List[str]
    units_generated_count: int
    message: str


# ------------------------------------------------------------------------------
# Grammar Hub & Drill Schemas
# ------------------------------------------------------------------------------
class GrammarExample(BaseModel):
    swedish: str
    english: str
    target_highlight: Optional[str] = None


class GrammarExerciseItem(BaseModel):
    id: int
    type: str
    prompt: str
    options: Optional[List[str]] = None
    correct_answer: str
    explanation: Optional[str] = None


class GrammarTopicSummary(BaseModel):
    id: str
    language: str
    level: str  # A1, A2, B1, B2, C1
    title: str
    swedish_title: str
    summary: str
    formula: str


class GrammarTopicDetail(GrammarTopicSummary):
    rule_explanation: str
    examples: List[GrammarExample] = []
    common_pitfalls: List[str] = []
    exercises_count: int = 0


class GrammarPracticeDrillsResponse(BaseModel):
    topic_id: str
    topic_title: str
    level: str
    exercises: List[GrammarExerciseItem] = []


class GrammarGenerateDrillsRequest(BaseModel):
    custom_prompt: Optional[str] = None


# ------------------------------------------------------------------------------
# Verb Tenses Lab & AI Memory Schemas
# ------------------------------------------------------------------------------
class TenseExample(BaseModel):
    swedish: str
    english: str
    target_highlight: Optional[str] = None


class TenseExerciseItem(BaseModel):
    id: int
    type: str
    prompt: str
    options: Optional[List[str]] = None
    correct_answer: str
    explanation: Optional[str] = None


class TenseSummary(BaseModel):
    id: str
    language: str
    time_aspect: str  # past, present, future
    title: str
    swedish_title: str
    level: str
    summary: str
    formula: str
    signal_words: List[str] = []
    timeline_description: str
    mastery_percentage: int = 0
    attempts_count: int = 0


class TenseDetail(TenseSummary):
    examples: List[TenseExample] = []
    common_pitfalls: List[str] = []
    exercises_count: int = 0


class TenseDrillsResponse(BaseModel):
    tense_id: str
    tense_title: str
    language: str
    time_aspect: str
    exercises: List[TenseExerciseItem] = []


class TenseDrillSubmitRequest(BaseModel):
    exercise_id: int
    user_answer: str


class TenseDrillSubmitResponse(BaseModel):
    is_correct: bool
    correct_answer: str
    explanation: Optional[str] = None
    xp_earned: int = 0
    new_mastery_percentage: int = 0
    ai_memory_feedback: Optional[str] = None


class AIMemoryProfileResponse(BaseModel):
    username: str
    overall_accuracy: int
    detected_strengths: List[str] = []
    detected_weaknesses: List[str] = []
    recommended_focus_tenses: List[str] = []
    total_mistakes_logged: int = 0
    ai_coaching_note: str


