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
        v2_resp = client.get("/api/grammar/topics/sv-b1-v2-rule")
        assert v2_resp.status_code == 200
        v2_data = v2_resp.json()
        assert "V2" in v2_data["title"]
        assert len(v2_data["examples"]) >= 1
        assert len(v2_data["common_pitfalls"]) >= 1

        # 3. Get practice drills for V2 rule
        drills_resp = client.get("/api/grammar/topics/sv-b1-v2-rule/drills")
        assert drills_resp.status_code == 200
        drills = drills_resp.json()
        assert len(drills["exercises"]) >= 1

        # 4. Test English C1 inversion topic
        c1_resp = client.get("/api/grammar/topics/en-c1-inversion-emphasis")
        assert c1_resp.status_code == 200
        assert c1_resp.json()["level"] == "C1"

