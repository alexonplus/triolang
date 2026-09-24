"""
Curriculum Seed Data Module
---------------------------
Language Focus:
- Swedish (Svenska) for English speakers
- English (Engelska) for Swedish speakers
"""

import json
from typing import Any, Dict, List
from sqlalchemy.orm import Session
from app.models.database import Course, Unit, Lesson, Exercise, User

SWEDISH_COURSE_DATA: Dict[str, Any] = {
    "id": "sv-from-en",
    "title": "Swedish",
    "native_title": "Svenska",
    "flag_emoji": "🇸🇪",
    "target_language": "sv",
    "source_language": "en",
    "description": "Learn conversational Swedish, essential vocabulary, Swedish fika culture, and core grammar.",
    "units": [
        {
            "order_index": 1,
            "title": "Unit 1: Basics & Greetings",
            "swedish_title": "Avsnitt 1: Grunder & Hälsningar",
            "description": "Master essential Swedish greetings, introductions, and everyday politeness.",
            "icon_name": "Sparkles",
            "theme_color": "#10B981",
            "lessons": [
                {
                    "order_index": 1,
                    "title": "Lesson 1: Hello & Thanks",
                    "swedish_title": "Lektion 1: Hej och tack",
                    "xp_reward": 20,
                    "exercises": [
                        {
                            "order_index": 1,
                            "exercise_type": "multiple_choice",
                            "prompt_text": "Select the correct Swedish translation for: 'Hello!'",
                            "target_audio_text": "Hej!",
                            "target_language": "sv",
                            "correct_answer": "Hej!",
                            "options": ["Hej!", "Tack!", "Adjö!", "Nej"],
                            "explanation": "'Hej' is the most common Swedish greeting used at any time of day.",
                        },
                        {
                            "order_index": 2,
                            "exercise_type": "word_bank",
                            "prompt_text": "Build the Swedish sentence: 'Thank you very much'",
                            "target_audio_text": "Tack så mycket",
                            "target_language": "sv",
                            "correct_answer": "Tack så mycket",
                            "word_bank": ["Tack", "så", "mycket", "Hej", "God", "natt", "morgon"],
                            "explanation": "'Tack så mycket' literally means 'Thank you so much'.",
                        },
                        {
                            "order_index": 3,
                            "exercise_type": "pair_match",
                            "prompt_text": "Match the Swedish and English words",
                            "target_language": "sv",
                            "correct_answer": "pairs_completed",
                            "pairs": {
                                "Hej": "Hello",
                                "Tack": "Thank you",
                                "Ja": "Yes",
                                "Nej": "No",
                                "Hej då": "Goodbye",
                            },
                            "explanation": "Great job matching core Swedish greetings!",
                        },
                        {
                            "order_index": 4,
                            "exercise_type": "listen_transcribe",
                            "prompt_text": "Listen and select what you hear:",
                            "target_audio_text": "God morgon!",
                            "target_language": "sv",
                            "correct_answer": "God morgon!",
                            "options": ["God morgon!", "God natt!", "Tack så mycket!", "Hej då!"],
                            "explanation": "'God morgon' translates to 'Good morning'.",
                        },
                    ],
                },
                {
                    "order_index": 2,
                    "title": "Lesson 2: Introductions & Pronouns",
                    "swedish_title": "Lektion 2: Presentation & Pronomen",
                    "xp_reward": 25,
                    "exercises": [
                        {
                            "order_index": 1,
                            "exercise_type": "word_bank",
                            "prompt_text": "Translate to Swedish: 'I am a boy'",
                            "target_audio_text": "Jag är en pojke",
                            "target_language": "sv",
                            "correct_answer": "Jag är en pojke",
                            "word_bank": ["Jag", "är", "en", "pojke", "flicka", "kvinna", "du"],
                            "explanation": "Swedish word order is Subject + Verb + Indefinite Article + Noun ('Jag är en pojke').",
                        },
                        {
                            "order_index": 2,
                            "exercise_type": "multiple_choice",
                            "prompt_text": "How do you ask: 'What is your name?' in Swedish?",
                            "target_audio_text": "Vad heter du?",
                            "target_language": "sv",
                            "correct_answer": "Vad heter du?",
                            "options": ["Vad heter du?", "Hur mår du?", "Var bor du?", "Vad gör du?"],
                            "explanation": "'Vad heter du?' uses the verb 'heta' (to be named).",
                        },
                        {
                            "order_index": 3,
                            "exercise_type": "pair_match",
                            "prompt_text": "Match the pronouns and nouns:",
                            "target_language": "sv",
                            "correct_answer": "pairs_completed",
                            "pairs": {
                                "Jag": "I",
                                "Du": "You",
                                "En flicka": "A girl",
                                "En pojke": "A boy",
                                "En kvinna": "A woman",
                            },
                            "explanation": "Well done mastering basic Swedish pronouns and people nouns!",
                        },
                    ],
                },
            ],
        },
        {
            "order_index": 2,
            "title": "Unit 2: Swedish Fika & Food",
            "swedish_title": "Avsnitt 2: Svensk Fika & Mat",
            "description": "Discover Swedish coffee culture ('fika'), bakery treats, and restaurant phrases.",
            "icon_name": "Coffee",
            "theme_color": "#F59E0B",
            "lessons": [
                {
                    "order_index": 1,
                    "title": "Lesson 1: Coffee & Cinnamon Buns",
                    "swedish_title": "Lektion 1: Kaffe och kanelbulle",
                    "xp_reward": 25,
                    "exercises": [
                        {
                            "order_index": 1,
                            "exercise_type": "multiple_choice",
                            "prompt_text": "What is the famous Swedish social coffee break called?",
                            "target_audio_text": "Fika",
                            "target_language": "sv",
                            "correct_answer": "Fika",
                            "options": ["Fika", "Lunch", "Middag", "Frukost"],
                            "explanation": "'Fika' is both a noun and a verb meaning to meet up for coffee and sweet pastries.",
                        },
                        {
                            "order_index": 2,
                            "exercise_type": "word_bank",
                            "prompt_text": "Build the sentence: 'I drink coffee and eat a cinnamon bun'",
                            "target_audio_text": "Jag dricker kaffe och äter en kanelbulle",
                            "target_language": "sv",
                            "correct_answer": "Jag dricker kaffe och äter en kanelbulle",
                            "word_bank": ["Jag", "dricker", "kaffe", "och", "äter", "en", "kanelbulle", "te", "mjölk"],
                            "explanation": "'dricker' = drinks, 'äter' = eats, 'kanelbulle' = cinnamon bun.",
                        },
                        {
                            "order_index": 3,
                            "exercise_type": "pair_match",
                            "prompt_text": "Match Swedish food and drinks:",
                            "target_language": "sv",
                            "correct_answer": "pairs_completed",
                            "pairs": {
                                "Kaffe": "Coffee",
                                "Te": "Tea",
                                "Vatten": "Water",
                                "Mjölk": "Milk",
                                "Bröd": "Bread",
                            },
                            "explanation": "Delicious! You know your Swedish beverages and snacks.",
                        },
                    ],
                },
            ],
        },
        {
            "order_index": 3,
            "title": "Unit 3: Travel & City Life",
            "swedish_title": "Avsnitt 3: Resor & Stadsliv",
            "description": "Navigate Stockholm, Gothenburg, trains, buses, and asking for directions.",
            "icon_name": "Compass",
            "theme_color": "#3B82F6",
            "lessons": [
                {
                    "order_index": 1,
                    "title": "Lesson 1: Transportation & Directions",
                    "swedish_title": "Lektion 1: Transport & Riktningar",
                    "xp_reward": 30,
                    "exercises": [
                        {
                            "order_index": 1,
                            "exercise_type": "multiple_choice",
                            "prompt_text": "How do you say 'Where is the train station?' in Swedish?",
                            "target_audio_text": "Var ligger tågstationen?",
                            "target_language": "sv",
                            "correct_answer": "Var ligger tågstationen?",
                            "options": [
                                "Var ligger tågstationen?",
                                "När går bussen?",
                                "Hur mycket kostar det?",
                                "Var är hotellet?",
                            ],
                            "explanation": "'Var ligger...' is used when asking for the physical location of buildings.",
                        },
                        {
                            "order_index": 2,
                            "exercise_type": "word_bank",
                            "prompt_text": "Translate to Swedish: 'Straight ahead and to the left'",
                            "target_audio_text": "Rakt fram och till vänster",
                            "target_language": "sv",
                            "correct_answer": "Rakt fram och till vänster",
                            "word_bank": ["Rakt", "fram", "och", "till", "vänster", "höger", "där", "här"],
                            "explanation": "'Rakt fram' = Straight ahead, 'till vänster' = to the left, 'till höger' = to the right.",
                        },
                    ],
                },
            ],
        },
    ],
}

ENGLISH_COURSE_DATA: Dict[str, Any] = {
    "id": "en-from-sv",
    "title": "English",
    "native_title": "Engelska",
    "flag_emoji": "🇬🇧",
    "target_language": "en",
    "source_language": "sv",
    "description": "Lär dig praktisk engelska för resor, arbete och vardagliga samtal.",
    "units": [
        {
            "order_index": 1,
            "title": "Unit 1: Basic English Conversations",
            "swedish_title": "Avsnitt 1: Grundläggande samtal",
            "description": "Hälsningsfraser, artighetsuttryck och presentation på engelska.",
            "icon_name": "Sparkles",
            "theme_color": "#6366F1",
            "lessons": [
                {
                    "order_index": 1,
                    "title": "Lesson 1: Greetings & Small Talk",
                    "swedish_title": "Lektion 1: Hälsningar och vardagsprat",
                    "xp_reward": 20,
                    "exercises": [
                        {
                            "order_index": 1,
                            "exercise_type": "multiple_choice",
                            "prompt_text": "Välj rätt engelsk översättning för: 'Hur mår du?'",
                            "target_audio_text": "How are you doing?",
                            "target_language": "en",
                            "correct_answer": "How are you doing?",
                            "options": [
                                "How are you doing?",
                                "What is your name?",
                                "Where are you going?",
                                "Nice to meet you",
                            ],
                            "explanation": "'How are you doing?' eller 'How are you?' är den vanligaste hälsningen.",
                        },
                        {
                            "order_index": 2,
                            "exercise_type": "word_bank",
                            "prompt_text": "Bygg meningen: 'Nice to meet you'",
                            "target_audio_text": "Nice to meet you",
                            "target_language": "en",
                            "correct_answer": "Nice to meet you",
                            "word_bank": ["Nice", "to", "meet", "you", "too", "Good", "morning"],
                            "explanation": "'Nice to meet you' betyder 'Trevligt att träffas'.",
                        },
                        {
                            "order_index": 3,
                            "exercise_type": "pair_match",
                            "prompt_text": "Para ihop engelska och svenska ord:",
                            "target_language": "en",
                            "correct_answer": "pairs_completed",
                            "pairs": {
                                "Hello": "Hej",
                                "Please": "Snälla / Tack",
                                "Thank you": "Tack",
                                "Excuse me": "Ursäkta mig",
                                "Goodbye": "Hej då",
                            },
                            "explanation": "Bra jobbat med de engelska grundorden!",
                        },
                    ],
                },
            ],
        },
    ],
}


def seed_curriculum_if_empty(db: Session) -> None:
    default_user = db.query(User).first()
    if not default_user:
        default_user = User(
            username="VikingLearner",
            hearts=5,
            gems=150,
            total_xp=0,
            streak_days=1,
            active_course_id="sv-from-en",
        )
        db.add(default_user)
        db.commit()

    courses_to_seed = [SWEDISH_COURSE_DATA, ENGLISH_COURSE_DATA]

    for course_data in courses_to_seed:
        existing_course = db.query(Course).filter(Course.id == course_data["id"]).first()
        if existing_course:
            continue

        course = Course(
            id=course_data["id"],
            title=course_data["title"],
            native_title=course_data["native_title"],
            flag_emoji=course_data["flag_emoji"],
            target_language=course_data["target_language"],
            source_language=course_data["source_language"],
            description=course_data["description"],
        )
        db.add(course)
        db.flush()

        for u_data in course_data["units"]:
            unit = Unit(
                course_id=course.id,
                order_index=u_data["order_index"],
                title=u_data["title"],
                swedish_title=u_data["swedish_title"],
                description=u_data["description"],
                icon_name=u_data.get("icon_name", "Sparkles"),
                theme_color=u_data.get("theme_color", "#10B981"),
            )
            db.add(unit)
            db.flush()

            for l_data in u_data["lessons"]:
                lesson = Lesson(
                    unit_id=unit.id,
                    order_index=l_data["order_index"],
                    title=l_data["title"],
                    swedish_title=l_data["swedish_title"],
                    xp_reward=l_data.get("xp_reward", 20),
                )
                db.add(lesson)
                db.flush()

                for e_data in l_data["exercises"]:
                    exercise = Exercise(
                        lesson_id=lesson.id,
                        order_index=e_data["order_index"],
                        exercise_type=e_data["exercise_type"],
                        prompt_text=e_data["prompt_text"],
                        target_audio_text=e_data.get("target_audio_text"),
                        target_language=e_data.get("target_language", "sv"),
                        correct_answer=e_data["correct_answer"],
                        options_json=json.dumps(e_data["options"]) if "options" in e_data else None,
                        word_bank_json=json.dumps(e_data["word_bank"]) if "word_bank" in e_data else None,
                        pairs_json=json.dumps(e_data["pairs"]) if "pairs" in e_data else None,
                        explanation=e_data.get("explanation"),
                    )
                    db.add(exercise)

    db.commit()
