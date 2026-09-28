"""
Backend Unit & Integration Tests Module
---------------------------------------
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.database import init_db, SessionLocal
from app.data.curriculum import seed_curriculum_if_empty


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    init_db()
    db = SessionLocal()
    try:
        seed_curriculum_if_empty(db)
    finally:
        db.close()


def test_root_health_check():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "online"
        assert "Swedish (sv)" in data["languages_supported"]


def test_get_user_profile():
    with TestClient(app) as client:
        response = client.get("/api/user")
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "VikingLearner"
        assert data["hearts"] >= 0
        assert "active_course_id" in data


def test_list_courses():
    with TestClient(app) as client:
        response = client.get("/api/courses")
        assert response.status_code == 200
        courses = response.json()
        assert len(courses) >= 2
        course_ids = [c["id"] for c in courses]
        assert "sv-from-en" in course_ids
        assert "en-from-sv" in course_ids


def test_get_swedish_units():
    with TestClient(app) as client:
        response = client.get("/api/courses/sv-from-en/units")
        assert response.status_code == 200
        units = response.json()
        assert len(units) >= 1
        unit_1 = units[0]
        assert "Basics & Greetings" in unit_1["title"] or "Grunder" in unit_1["swedish_title"]
        assert len(unit_1["lessons"]) >= 1


def test_submit_exercise_answer():
    with TestClient(app) as client:
        lesson_resp = client.get("/api/lessons/1")
        assert lesson_resp.status_code == 200
        lesson = lesson_resp.json()
        assert len(lesson["exercises"]) >= 1

        first_ex = lesson["exercises"][0]
        submit_resp = client.post(
            "/api/exercises/submit",
            json={"exercise_id": first_ex["id"], "user_answer": first_ex["correct_answer"]}
        )
        assert submit_resp.status_code == 200
        submit_data = submit_resp.json()
        assert submit_data["is_correct"] is True
        assert submit_data["xp_earned"] > 0


def test_ai_tutor_endpoint():
    with TestClient(app) as client:
        response = client.post(
            "/api/ai/tutor",
            json={"query": "What is fika in Sweden?", "target_language": "sv"}
        )
        assert response.status_code == 200
        tutor_data = response.json()
        assert "Fika" in tutor_data["reply"] or "fika" in tutor_data["reply"].lower()


def test_generate_ai_lesson_endpoint():
    with TestClient(app) as client:
        response = client.post(
            "/api/ai/generate-lesson",
            json={"topic": "At the Doctor", "course_id": "sv-from-en"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["exercise_count"] >= 1


def test_diagnostic_placement_endpoint():
    with TestClient(app) as client:
        # 1. Test probe questions
        q_resp = client.get("/api/ai/placement-questions?course_id=sv-from-en")
        assert q_resp.status_code == 200
        questions = q_resp.json()
        assert len(questions) >= 3

        # 2. Test diagnostic evaluation
        eval_resp = client.post(
            "/api/ai/diagnostic-evaluate",
            json={
                "course_id": "sv-from-en",
                "dialogue": [
                    {"sender": "AI", "text": "Hej! Berätta lite om dig själv"},
                    {"sender": "User", "text": "Jag heter Alex och bor i Stockholm. Jag gillar att programmera och dricka kaffe."},
                    {"sender": "AI", "text": "Vad gjorde du igår?"},
                    {"sender": "User", "text": "Igår jag åt en god pizza och tittade på film med mina vänner."},
                ]
            }
        )
        assert eval_resp.status_code == 200
        data = eval_resp.json()
        assert "cefr_level" in data
        assert data["units_generated_count"] >= 1


def test_grammar_hub_endpoints():
    with TestClient(app) as client:
        # 1. List all Swedish topics
        resp = client.get("/api/grammar/topics?language=sv")
        assert resp.status_code == 200
        topics = resp.json()
        assert len(topics) >= 5
        levels = {t["level"] for t in topics}
        assert "A1" in levels
        assert "B1" in levels

        # 2. Get details for Swedish V2 rule
        v2_resp = client.get("/api/grammar/topics/sv-b1-v2-inversion")
        assert v2_resp.status_code == 200
        v2_data = v2_resp.json()
        assert "V2" in v2_data["title"]
        assert len(v2_data["examples"]) >= 1
        assert len(v2_data["common_pitfalls"]) >= 1
        assert v2_data["exercises_count"] >= 10

        # 3. Get practice drills for V2 rule (verifying 10+ exercises!)
        drills_resp = client.get("/api/grammar/topics/sv-b1-v2-inversion/drills")
        assert drills_resp.status_code == 200
        drills = drills_resp.json()
        assert len(drills["exercises"]) >= 10

        # 4. Test English C1 inversion topic (verifying 10+ exercises!)
        c1_resp = client.get("/api/grammar/topics/en-c1-negative-inversion")
        assert c1_resp.status_code == 200
        assert c1_resp.json()["level"] == "C1"
        assert c1_resp.json()["exercises_count"] >= 10


def test_tenses_and_ai_memory_endpoints():
    with TestClient(app) as client:
        # 1. Verify all 12 English tenses are returned
        resp = client.get("/api/tenses?language=en")
        assert resp.status_code == 200
        en_tenses = resp.json()
        assert len(en_tenses) == 12
        tense_ids = [t["id"] for t in en_tenses]
        assert "en-present-simple" in tense_ids
        assert "en-present-perfect-continuous" in tense_ids
        assert "en-past-perfect-continuous" in tense_ids
        assert "en-future-perfect-continuous" in tense_ids

        # 2. Verify Swedish tenses
        sv_resp = client.get("/api/tenses?language=sv")
        assert sv_resp.status_code == 200
        assert len(sv_resp.json()) >= 5

        # 3. Get drills for Past Perfect Continuous (10+ exercises)
        drills_resp = client.get("/api/tenses/en-past-perfect-continuous/drills")
        assert drills_resp.status_code == 200
        drills = drills_resp.json()
        assert len(drills["exercises"]) >= 10

        first_ex = drills["exercises"][0]

        # 4. Submit correct drill answer and check SQLite mastery update
        submit_resp = client.post(
            "/api/tenses/en-past-perfect-continuous/submit",
            json={"exercise_id": first_ex["id"], "user_answer": first_ex["correct_answer"]},
        )
        assert submit_resp.status_code == 200
        data = submit_resp.json()
        assert data["is_correct"] is True
        assert data["new_mastery_percentage"] > 0

        # 5. Submit incorrect answer and verify AI Memory logging
        bad_submit = client.post(
            "/api/tenses/en-past-perfect-continuous/submit",
            json={"exercise_id": first_ex["id"], "user_answer": "wrong-verb-form-test"},
        )
        assert bad_submit.status_code == 200
        bad_data = bad_submit.json()
        assert bad_data["is_correct"] is False
        assert "AI Memory logged" in bad_data["ai_memory_feedback"]

        # 6. Query AI Memory Profile
        profile_resp = client.get("/api/ai/memory-profile")
        assert profile_resp.status_code == 200
        profile = profile_resp.json()
        assert profile["total_mistakes_logged"] >= 1
        assert len(profile["ai_coaching_note"]) > 0


def test_dialogue_simulator_and_grammar_correction():
    with TestClient(app) as client:
        # 1. List Swedish and English scenarios
        scenarios_resp = client.get("/api/dialogues/scenarios?language=sv")
        assert scenarios_resp.status_code == 200
        scenarios = scenarios_resp.json()
        assert len(scenarios) >= 4
        scenario_ids = [s["id"] for s in scenarios]
        assert "sv-fika-cafe" in scenario_ids

        # 2. Initiate scenario (computer speaks first)
        start_resp = client.post(
            "/api/dialogues/start",
            json={"scenario_id": "sv-fika-cafe", "language": "sv"},
        )
        assert start_resp.status_code == 200
        start_data = start_resp.json()
        assert start_data["persona_name"] == "Linnéa (Barista)"
        assert start_data["initial_message"]["sender"] == "AI"
        assert len(start_data["initial_message"]["text"]) > 0
        assert len(start_data["suggested_chips"]) >= 3

        # 3. User responds with an intentional V2 mistake ("Igår jag åt...")
        turn_resp = client.post(
            "/api/dialogues/turn",
            json={
                "scenario_id": "sv-fika-cafe",
                "language": "sv",
                "user_message": "Igår jag drack kaffe och idag vill jag ha en kanelbulle.",
                "history": [start_data["initial_message"]],
            },
        )
        assert turn_resp.status_code == 200
        turn_data = turn_resp.json()
        assert turn_data["ai_reply"]["sender"] == "AI"
        assert len(turn_data["ai_reply"]["text"]) > 0

        # 4. Verify grammar correction detected V2 inversion error
        assert turn_data["correction_feedback"] is not None
        assert turn_data["correction_feedback"]["has_errors"] is True
        assert "V2" in turn_data["correction_feedback"]["grammar_rule_explanation"] or "V2" in turn_data["correction_feedback"]["highlighted_issues"][0]
        assert "Igår drack jag" in turn_data["correction_feedback"]["corrected_text"]




