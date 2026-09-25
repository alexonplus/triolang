"""
AI Dynamic Lesson Generator Service
-----------------------------------
CLEAN ARCHITECTURE - USE CASE LAYER
"""

import json
from typing import Dict, Any, List
from sqlalchemy.orm import Session

from app.models.database import Course, Unit, Lesson, Exercise
from app.services.ai_client import gemini_client
from app.core.security import sanitize_topic_input

FALLBACK_LESSON_TOPICS: Dict[str, Dict[str, Any]] = {
    "doctor": {
        "unit_title": "At the Doctor (Vårdcentral)",
        "unit_swedish_title": "På vårdcentralen",
        "unit_description": "Learn essential medical vocabulary, describing symptoms, and booking a doctor appointment in Sweden.",
        "icon_name": "Sparkles",
        "theme_color": "#06B6D4",
        "lesson_title": "Describing Symptoms & Booking",
        "lesson_swedish_title": "Beskriva symtom och boka tid",
        "exercises": [
            {
                "exercise_type": "multiple_choice",
                "prompt_text": "How do you say: 'I have a headache' in Swedish?",
                "target_audio_text": "Jag har ont i huvudet",
                "target_language": "sv",
                "correct_answer": "Jag har ont i huvudet",
                "options": ["Jag har ont i huvudet", "Jag är hungrig", "Jag är trött", "Var är doktorn?"],
                "explanation": "'ha ont i...' is the standard Swedish expression for experiencing pain in a body part.",
            },
            {
                "exercise_type": "word_bank",
                "prompt_text": "Build the sentence: 'I need a doctor appointment'",
                "target_audio_text": "Jag behöver en läkartid",
                "target_language": "sv",
                "correct_answer": "Jag behöver en läkartid",
                "word_bank": ["Jag", "behöver", "en", "läkartid", "idag", "medicin", "recept"],
                "explanation": "'behöver' = needs, 'läkartid' = doctor appointment.",
            },
            {
                "exercise_type": "pair_match",
                "prompt_text": "Match medical Swedish and English terms:",
                "target_language": "sv",
                "correct_answer": "pairs_completed",
                "pairs": {
                    "En läkare": "A doctor",
                    "Ett recept": "A prescription",
                    "Medicin": "Medicine",
                    "Feber": "Fever",
                    "Ett apotek": "A pharmacy",
                },
                "explanation": "Great job matching medical vocabulary!",
            },
            {
                "exercise_type": "listen_transcribe",
                "prompt_text": "Listen to the receptionist and choose what you hear:",
                "target_audio_text": "Välkommen till vårdcentralen",
                "target_language": "sv",
                "correct_answer": "Välkommen till vårdcentralen",
                "options": [
                    "Välkommen till vårdcentralen",
                    "Var ligger apoteket?",
                    "Tack för hjälpen",
                    "Hur mår du idag?",
                ],
                "explanation": "'Vårdcentralen' is the Swedish municipal health care center.",
            },
        ],
    },
    "hotel": {
        "unit_title": "Hotel Check-in & Accommodation",
        "unit_swedish_title": "Hotellvistelse och incheckning",
        "unit_description": "Booking hotel rooms, asking for keys, Wi-Fi passwords, and checkout times.",
        "icon_name": "Compass",
        "theme_color": "#8B5CF6",
        "lesson_title": "Checking in at Reception",
        "lesson_swedish_title": "Incheckning i receptionen",
        "exercises": [
            {
                "exercise_type": "multiple_choice",
                "prompt_text": "How do you say: 'I have a room reservation' in Swedish?",
                "target_audio_text": "Jag har en rumsbokning",
                "target_language": "sv",
                "correct_answer": "Jag har en rumsbokning",
                "options": ["Jag har en rumsbokning", "Var är frukosten?", "Jag vill checka ut", "Har ni lediga rum?"],
                "explanation": "'bokning' is booking/reservation, 'rum' is room.",
            },
            {
                "exercise_type": "word_bank",
                "prompt_text": "Translate to Swedish: 'What is the Wi-Fi password?'",
                "target_audio_text": "Vad är lösenordet till wifi?",
                "target_language": "sv",
                "correct_answer": "Vad är lösenordet till wifi?",
                "word_bank": ["Vad", "är", "lösenordet", "till", "wifi", "hotell", "rummet"],
                "explanation": "'lösenord' = password.",
            },
            {
                "exercise_type": "pair_match",
                "prompt_text": "Match hotel terms:",
                "target_language": "sv",
                "correct_answer": "pairs_completed",
                "pairs": {
                    "En nyckel": "A key",
                    "Ett rum": "A room",
                    "Frukost": "Breakfast",
                    "Hiss": "Elevator",
                    "Utcheckning": "Check-out",
                },
                "explanation": "Excellent! You're ready for your hotel stay in Sweden.",
            },
        ],
    },
}


async def generate_and_save_ai_lesson(
    db: Session,
    course_id: str,
    raw_topic: str,
) -> Dict[str, Any]:
    topic = sanitize_topic_input(raw_topic)
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise ValueError(f"Course with ID '{course_id}' not found.")

    target_lang = course.target_language
    target_name = "Swedish" if target_lang == "sv" else "English"
    source_name = "English" if target_lang == "sv" else "Swedish"

    unit_data: Dict[str, Any] = {}

    if gemini_client.is_configured:
        system_prompt = (
            f"You are an expert language curriculum designer for TrioLang (a gamified language app). "
            f"You create interactive {target_name} lessons for {source_name} speakers. "
            f"Return ONLY valid, structured JSON without any markdown code formatting."
        )

        user_prompt = f"""
Generate a complete learning unit on the topic: '{topic}' for {target_name} learners.

JSON format must strictly follow:
{{
  "unit_title": "string",
  "unit_swedish_title": "string",
  "unit_description": "string",
  "theme_color": "string (hex color)",
  "icon_name": "string ('Sparkles' | 'Coffee' | 'Compass' | 'BookOpen')",
  "lesson_title": "string",
  "lesson_swedish_title": "string",
  "exercises": [
    {{
      "exercise_type": "multiple_choice",
      "prompt_text": "string",
      "target_audio_text": "string",
      "correct_answer": "string",
      "options": ["string", "string", "string", "string"],
      "explanation": "string"
    }},
    {{
      "exercise_type": "word_bank",
      "prompt_text": "string",
      "target_audio_text": "string",
      "correct_answer": "string",
      "word_bank": ["word1", "word2", "word3", "distractor1", "distractor2", "distractor3"],
      "explanation": "string"
    }},
    {{
      "exercise_type": "pair_match",
      "prompt_text": "Match the words",
      "correct_answer": "pairs_completed",
      "pairs": {{
        "Word 1": "Match 1",
        "Word 2": "Match 2",
        "Word 3": "Match 3",
        "Word 4": "Match 4"
      }},
      "explanation": "string"
    }},
    {{
      "exercise_type": "listen_transcribe",
      "prompt_text": "Listen and select the correct answer:",
      "target_audio_text": "string",
      "correct_answer": "string",
      "options": ["string", "string", "string", "string"],
      "explanation": "string"
    }}
  ]
}}
"""
        try:
            unit_data = await gemini_client.generate_json(user_prompt, system_instruction=system_prompt)
        except Exception as e:
            print(f"[LessonGenerator] Gemini API generation error: {e}. Falling back to template generator.")
            unit_data = {}

    if not unit_data or "exercises" not in unit_data:
        topic_lower = topic.lower()
        if "hotel" in topic_lower or "room" in topic_lower:
            unit_data = FALLBACK_LESSON_TOPICS["hotel"]
        else:
            unit_data = FALLBACK_LESSON_TOPICS["doctor"]
            unit_data["unit_title"] = f"AI Custom: {topic.title()}"
            unit_data["unit_swedish_title"] = f"AI Anpassad: {topic.title()}"

    try:
        current_max_order = db.query(Unit).filter(Unit.course_id == course.id).count()

        new_unit = Unit(
            course_id=course.id,
            order_index=current_max_order + 1,
            title=unit_data.get("unit_title", f"AI Unit: {topic}"),
            swedish_title=unit_data.get("unit_swedish_title", f"AI Avsnitt: {topic}"),
            description=unit_data.get("unit_description", f"Custom AI-generated lesson on {topic}"),
            icon_name=unit_data.get("icon_name", "Sparkles"),
            theme_color=unit_data.get("theme_color", "#8B5CF6"),
        )
        db.add(new_unit)
        db.flush()

        new_lesson = Lesson(
            unit_id=new_unit.id,
            order_index=1,
            title=unit_data.get("lesson_title", f"Lesson: {topic}"),
            swedish_title=unit_data.get("lesson_swedish_title", f"Lektion: {topic}"),
            xp_reward=35,
        )
        db.add(new_lesson)
        db.flush()

        for idx, ex_data in enumerate(unit_data.get("exercises", []), start=1):
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
            "success": True,
            "unit_id": new_unit.id,
            "lesson_id": new_lesson.id,
            "title": new_unit.title,
            "swedish_title": new_unit.swedish_title,
            "exercise_count": len(unit_data.get("exercises", [])),
            "source": "Google Gemini AI" if gemini_client.is_configured else "Smart AI Template Generator",
        }

    except Exception as db_err:
        db.rollback()
        raise RuntimeError(f"Database error while saving generated lesson: {db_err}")
