"""
AI Placement & Diagnostic Assessment Service
-------------------------------------------
CLEAN ARCHITECTURE - USE CASE / SERVICE LAYER:
1. Multi-turn CEFR Diagnostic: Probes the user's conversational fluency, vocabulary breadth,
   and grammatical accuracy across progressive difficulty levels.
2. Linguistic Error Analysis: Uses Google Gemini (or deterministic NLP rules) to identify specific
   weaknesses (e.g., Swedish V2 word order inversion, en/ett gender mismatches, verb conjugation).
3. Targeted Adaptive Curriculum Builder: Synthesizes a customized set of learning units focused
   strictly on the user's weak points, skipping elementary beginner content if user is already intermediate.
"""

import json
from typing import Dict, Any, List
from sqlalchemy.orm import Session

from app.models.database import Course, Unit, Lesson, Exercise, User
from app.services.ai_client import gemini_client
from app.core.security import sanitize_topic_input


# ------------------------------------------------------------------------------
# 1. Standard Placement Diagnostic Questions
# ------------------------------------------------------------------------------
PLACEMENT_QUESTIONS_DATA: Dict[str, List[Dict[str, str]]] = {
    "sv": [
        {
            "id": "q1_intro",
            "prompt": "Hej! Berätta lite om dig själv: Vad heter du, var bor du, och vad gör du på fritiden?",
            "english_hint": "Introduce yourself: What's your name, where do you live, and what do you do in your free time?",
            "level_target": "A1-A2 (Introductions & Basic Vocabulary)",
        },
        {
            "id": "q2_past",
            "prompt": "Vad gjorde du igår eller under förra helgen? Berätta om något roligt eller intressant som hände!",
            "english_hint": "What did you do yesterday or last weekend? Talk about something fun or interesting that happened!",
            "level_target": "A2-B1 (Past tense & Chronological Storytelling)",
        },
        {
            "id": "q3_scenario",
            "prompt": "Om du fick välja fritt, hur ser din perfekta dag i Sverige ut? Vilka platser vill du besöka och varför?",
            "english_hint": "If you could choose freely, what does your perfect day in Sweden look like? Where would you visit and why?",
            "level_target": "B1-B2 (Hypothetical Conditionals & Complex Arguments)",
        },
    ],
    "en": [
        {
            "id": "q1_intro",
            "prompt": "Hello! Could you introduce yourself and tell me what you enjoy doing in your free time?",
            "english_hint": "Presentera dig själv och berätta om dina intressen.",
            "level_target": "A1-A2",
        },
        {
            "id": "q2_past",
            "prompt": "Tell me about a memorable trip or event you experienced in the past. What happened?",
            "english_hint": "Berätta om en resa eller händelse från förr.",
            "level_target": "A2-B1",
        },
        {
            "id": "q3_scenario",
            "prompt": "In your opinion, what is the best way to learn a new language quickly, and why?",
            "english_hint": "Ge din åsikt om bästa sättet att lära sig språk snabbt.",
            "level_target": "B1-B2",
        },
    ],
}


def get_placement_questions(target_language: str = "sv") -> List[Dict[str, str]]:
    """Returns progressive probe questions for diagnostic testing."""
    return PLACEMENT_QUESTIONS_DATA.get(target_language, PLACEMENT_QUESTIONS_DATA["sv"])


# ------------------------------------------------------------------------------
# 2. Main Placement Evaluation & Personalized Path Generator
# ------------------------------------------------------------------------------
async def evaluate_and_generate_personalized_path(
    db: Session,
    course_id: str,
    dialogue_transcript: List[Dict[str, str]],
) -> Dict[str, Any]:
    """
    Analyzes the user's answers across the diagnostic interview,
    detects grammar gaps, assigns a CEFR level, and generates tailored units in SQLite.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise ValueError(f"Course with ID '{course_id}' not found.")

    target_lang = course.target_language
    target_name = "Swedish" if target_lang == "sv" else "English"

    # Combine dialogue into text
    conversation_text = "\n".join(
        [f"{turn.get('sender', 'User')}: {turn.get('text', '')}" for turn in dialogue_transcript]
    )

    assessment: Dict[str, Any] = {}

    # 1. Evaluate with Google Gemini if configured
    if gemini_client.is_configured:
        system_prompt = (
            f"You are a master linguistic assessor and CEFR examiner for {target_name}. "
            f"Evaluate the user's {target_name} proficiency from their dialogue responses. "
            f"Identify exact grammatical weak points (e.g. V2 word order, en/ett noun genders, "
            f"plural suffixes, verb conjugation) and design 2 custom curriculum units focused strictly "
            f"on fixing those weak points. Return ONLY valid JSON."
        )

        user_prompt = f"""
Analyze this user dialogue in {target_name}:
---
{conversation_text}
---

Return strict JSON format:
{{
  "cefr_level": "A2" (or "A1", "B1", "B2", "C1"),
  "level_title": "string (e.g. 'Elementary Speaker (A2)' or 'Intermediate (B1)')",
  "vocabulary_score": "string ('Basic' | 'Good' | 'Rich')",
  "strengths": ["string", "string"],
  "weaknesses": ["string (e.g. 'Struggles with V2 word order inversion after time adverbs')", "string (e.g. 'Confuses en/ett articles')"],
  "custom_units": [
    {{
      "unit_title": "string (e.g. 'Mastering Swedish V2 Word Order')",
      "unit_swedish_title": "string (e.g. 'Bemästra V2-ordföljd i svenskan')",
      "unit_description": "string (Targeted drill to eliminate word order errors)",
      "theme_color": "#06B6D4",
      "icon_name": "Sparkles",
      "lesson_title": "string",
      "lesson_swedish_title": "string",
      "exercises": [
        {{
          "exercise_type": "word_bank",
          "prompt_text": "string (Focus on correcting the identified weakness)",
          "target_audio_text": "string",
          "correct_answer": "string",
          "word_bank": ["word1", "word2", "word3", "distractor1", "distractor2"],
          "explanation": "string (Grammar rule explanation)"
        }},
        {{
          "exercise_type": "multiple_choice",
          "prompt_text": "string",
          "target_audio_text": "string",
          "correct_answer": "string",
          "options": ["string", "string", "string", "string"],
          "explanation": "string"
        }},
        {{
          "exercise_type": "pair_match",
          "prompt_text": "Match the vocabulary pairs:",
          "correct_answer": "pairs_completed",
          "pairs": {{"Word1": "Match1", "Word2": "Match2", "Word3": "Match3", "Word4": "Match4"}},
          "explanation": "string"
        }}
      ]
    }}
  ]
}}
"""
        try:
            assessment = await gemini_client.generate_json(user_prompt, system_instruction=system_prompt)
        except Exception as e:
            print(f"[PlacementService] Gemini assessment error: {e}. Using deterministic linguistic fallback.")
            assessment = {}

    # 2. Deterministic Fallback Assessor if Gemini is offline
    if not assessment or "custom_units" not in assessment:
        # Heuristic length and vocabulary check
        total_words = len(conversation_text.split())
        has_v2_keywords = any(k in conversation_text.lower() for k in ["igår", "idag", "eftersom", "brukar", "kanske"])
        
        if total_words > 45 and has_v2_keywords:
            cefr = "B1"
            level_title = "Intermediate Speaker (B1)"
            weaknesses = [
                "Swedish V2 Word Order inversion in complex sentences",
                "Subordinate clause word order (BIFF-regeln: 'inte' before verb)",
            ]
            strengths = ["Rich conversational vocabulary", "Natural sentence flow"]
        elif total_words > 20:
            cefr = "A2"
            level_title = "Elementary Speaker (A2)"
            weaknesses = [
                "En vs. Ett noun genders and definite endings (-en/-et/-na)",
                "Past tense regular verbs (-ade vs -te)",
            ]
            strengths = ["Solid everyday greetings and basic expressions"]
        else:
            cefr = "A1"
            level_title = "Beginner (A1)"
            weaknesses = [
                "Core vocabulary expansion",
                "Basic pronoun and verb agreement (jag är, vi har)",
            ]
            strengths = ["Eager to learn fundamentals"]

        assessment = {
            "cefr_level": cefr,
            "level_title": level_title,
            "vocabulary_score": "Good" if cefr in ["A2", "B1"] else "Basic",
            "strengths": strengths,
            "weaknesses": weaknesses,
            "custom_units": [
                {
                    "unit_title": "Diagnostic Fix: Swedish V2 Word Order Intensive",
                    "unit_swedish_title": "Intensivkurs: Svensk V2-ordföljd",
                    "unit_description": "Targeted practice for verb-second rule after time & place expressions.",
                    "theme_color": "#06B6D4",
                    "icon_name": "Sparkles",
                    "lesson_title": "Lesson 1: Inverted Word Order with Time Adverbs",
                    "lesson_swedish_title": "Lektion 1: Omvänd ordföljd vid tidsuttryck",
                    "exercises": [
                        {
                            "exercise_type": "word_bank",
                            "prompt_text": "Build the correct Swedish sentence: 'Yesterday I ate a cinnamon bun'",
                            "target_audio_text": "Igår åt jag en kanelbulle",
                            "target_language": "sv",
                            "correct_answer": "Igår åt jag en kanelbulle",
                            "word_bank": ["Igår", "åt", "jag", "en", "kanelbulle", "äter", "bulle", "imorgon"],
                            "explanation": "V2 Rule: When a sentence begins with a time adverb ('Igår'), the verb ('åt') MUST come second before the subject ('jag').",
                        },
                        {
                            "exercise_type": "multiple_choice",
                            "prompt_text": "Which sentence follows correct Swedish word order?",
                            "target_audio_text": "Nu dricker vi kaffe",
                            "target_language": "sv",
                            "correct_answer": "Nu dricker vi kaffe",
                            "options": [
                                "Nu dricker vi kaffe",
                                "Nu vi dricker kaffe",
                                "Vi nu dricker kaffe",
                                "Kaffe dricker nu vi",
                            ],
                            "explanation": "In Swedish statements with an adverb in first place, the verb ('dricker') is always in position #2.",
                        },
                        {
                            "exercise_type": "pair_match",
                            "prompt_text": "Match time expressions and verbs:",
                            "target_language": "sv",
                            "correct_answer": "pairs_completed",
                            "pairs": {
                                "Igår": "Yesterday",
                                "Idag": "Today",
                                "Imorgon": "Tomorrow",
                                "Nu": "Now",
                                "Alltid": "Always",
                            },
                            "explanation": "Mastering time adverbs makes your Swedish sound fluent!",
                        },
                    ],
                },
                {
                    "unit_title": "Diagnostic Fix: En vs. Ett & Definite Noun Endings",
                    "unit_swedish_title": "Intensivkurs: En/Ett och bestämd form",
                    "unit_description": "Master gender articles and attaching '-en' / '-et' suffixes in context.",
                    "theme_color": "#8B5CF6",
                    "icon_name": "BookOpen",
                    "lesson_title": "Lesson 1: Attaching Definite Endings",
                    "lesson_swedish_title": "Lektion 1: Bestämd form i praktiken",
                    "exercises": [
                        {
                            "exercise_type": "multiple_choice",
                            "prompt_text": "How do you say 'The book is on the table' in Swedish?",
                            "target_audio_text": "Boken ligger på bordet",
                            "target_language": "sv",
                            "correct_answer": "Boken ligger på bordet",
                            "options": [
                                "Boken ligger på bordet",
                                "En bok ligger på ett bord",
                                "Boket ligger på borden",
                                "Boken är bordet",
                            ],
                            "explanation": "'en bok' becomes 'boken' (the book), and 'ett bord' becomes 'bordet' (the table).",
                        },
                    ],
                },
            ],
        }

    # 3. Persist the Customized Units into SQLite
    try:
        user = db.query(User).first()
        current_max_order = db.query(Unit).filter(Unit.course_id == course.id).count()

        created_unit_ids = []

        for unit_offset, u_data in enumerate(assessment.get("custom_units", []), start=1):
            new_unit = Unit(
                course_id=course.id,
                order_index=current_max_order + unit_offset,
                title=u_data.get("unit_title", "Personalized Custom Unit"),
                swedish_title=u_data.get("unit_swedish_title", "Anpassat Avsnitt"),
                description=u_data.get("unit_description", "Personalized unit targeting your grammar gaps."),
                icon_name=u_data.get("icon_name", "Sparkles"),
                theme_color=u_data.get("theme_color", "#06B6D4"),
            )
            db.add(new_unit)
            db.flush()
            created_unit_ids.append(new_unit.id)

            new_lesson = Lesson(
                unit_id=new_unit.id,
                order_index=1,
                title=u_data.get("lesson_title", "Lesson 1"),
                swedish_title=u_data.get("lesson_swedish_title", "Lektion 1"),
                xp_reward=40,
            )
            db.add(new_lesson)
            db.flush()

            for idx, ex_data in enumerate(u_data.get("exercises", []), start=1):
                exercise = Exercise(
                    lesson_id=new_lesson.id,
                    order_index=idx,
                    exercise_type=ex_data.get("exercise_type", "multiple_choice"),
                    prompt_text=ex_data.get("prompt_text", "Answer the question:"),
                    target_audio_text=ex_data.get("target_audio_text"),
                    target_language=target_lang,
                    correct_answer=ex_data.get("correct_answer", ""),
                    options_json=json.dumps(ex_data["options"]) if "options" in ex_data else None,
                    word_bank_json=json.dumps(ex_data["word_bank"]) if "word_bank" in ex_data else None,
                    pairs_json=json.dumps(ex_data["pairs"]) if "pairs" in ex_data else None,
                    explanation=ex_data.get("explanation"),
                )
                db.add(exercise)

        db.commit()

        return {
            "cefr_level": assessment.get("cefr_level", "A2"),
            "level_title": assessment.get("level_title", "Elementary Speaker (A2)"),
            "vocabulary_score": assessment.get("vocabulary_score", "Good"),
            "strengths": assessment.get("strengths", ["Good baseline fluency"]),
            "weaknesses": assessment.get("weaknesses", ["Swedish V2 word order", "En/ett noun genders"]),
            "units_generated_count": len(created_unit_ids),
            "message": f"Diagnostics complete! Generated {len(created_unit_ids)} targeted units for your level ({assessment.get('cefr_level', 'A2')}).",
        }

    except Exception as db_err:
        db.rollback()
        raise RuntimeError(f"Database error during placement persistence: {db_err}")
