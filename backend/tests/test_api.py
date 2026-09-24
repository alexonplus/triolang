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
