# TrioLang (Svenska & English) 🦉

[![Python 3.14](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React 19](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)

**TrioLang** is a standalone, gamified language learning web application inspired by Duolingo, built specifically for learning **Swedish (Svenska)** and **English (Engelska)**.

It features interactive sentence-building word tiles, multiple-choice cards, vocabulary pair matching, audio listening comprehension with native text-to-speech, streak tracking, hearts/lives, XP rewards, victory confetti, and an integrated **TrioBot AI Language Tutor** & **AI Dynamic Lesson Builder**.

---

## 🇸🇪 Svenska Sammanfattning (Swedish Overview)
**TrioLang** är en modern språkinlärningsapp för svenska och engelska med Duolingo-liknande spelupplevelse:
- 🗺 **Kurskarta**: Följ lektionsstigen med enheter som *Grunder & Hälsningar*, *Svensk Fika & Mat*, och *Resor & Stadsliv*.
- 🎮 **Interaktiva övningar**: Bygg meningar med ordbrickor, para ihop ord, flervalsfrågor och lyssna på uttal.
- 🔊 **Uttal & Ljud**: Talsyntes för både svenska (`sv-SE`) och engelska (`en-US`) samt ljudeffekter.
- 🤖 **TrioBot AI**: Fråga om svensk grammatik (*en/ett*, *V2-regeln*) och generera dynamiska lektioner med Gemini AI.

---

## 🐍 Python Learner's Guide (How to Learn Python from this Codebase)

The backend code in `backend/` has been documented with in-depth educational comments to help you master modern Python:

| File | Core Python Concepts Taught |
| :--- | :--- |
| [`backend/app/core/config.py`](file:///c:/triolang/backend/app/core/config.py) | `@dataclass`, `pathlib.Path`, Type hinting (`str`, `list[str]`), `os.getenv` |
| [`backend/app/core/security.py`](file:///c:/triolang/backend/app/core/security.py) | Input sanitization, regex filters, defense against injection |
| [`backend/app/models/database.py`](file:///c:/triolang/backend/app/models/database.py) | SQLAlchemy 2.0 ORM, `DeclarativeBase`, `Mapped[]`, Relationships, Generators & `yield` for Dependency Injection |
| [`backend/app/models/schemas.py`](file:///c:/triolang/backend/app/models/schemas.py) | Pydantic v2 `BaseModel`, DTO pattern, field validation, `model_config = {"from_attributes": True}` |
| [`backend/app/data/curriculum.py`](file:///c:/triolang/backend/app/data/curriculum.py) | Python dictionaries (`dict`), nested data structures, JSON serialization, database seeding |
| [`backend/app/services/game_engine.py`](file:///c:/triolang/backend/app/services/game_engine.py) | Business logic separation, string normalization (`string.punctuation`), `datetime` & `timedelta` arithmetic |
| [`backend/app/services/ai_client.py`](file:///c:/triolang/backend/app/services/ai_client.py) | Asynchronous Python (`async` / `await`), `httpx.AsyncClient`, Google Gemini API client |
| [`backend/app/services/lesson_generator.py`](file:///c:/triolang/backend/app/services/lesson_generator.py) | Dynamic lesson generation with LLM prompt templates and SQLite transactional persistence |
| [`backend/app/services/ai_tutor.py`](file:///c:/triolang/backend/app/services/ai_tutor.py) | AI Grammar Tutor, offline knowledge base fallback |
| [`backend/app/api/endpoints.py`](file:///c:/triolang/backend/app/api/endpoints.py) | FastAPI `APIRouter`, Dependency Injection (`Depends(get_db)`), HTTP status codes, error handling |
| [`backend/app/main.py`](file:///c:/triolang/backend/app/main.py) | FastAPI application setup, `@asynccontextmanager` lifespan events, CORS middleware |
| [`backend/tests/test_api.py`](file:///c:/triolang/backend/tests/test_api.py) | `pytest`, `@pytest.fixture(autouse=True)`, `TestClient` context managers, `assert` statements |

---

## 🚀 Quick Start Instructions

### 1. Start the Python FastAPI Backend

Open a terminal and run:

```bash
cd c:\triolang\backend

# Create virtual environment (if not created yet)
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Start backend development server
uvicorn app.main:app --reload --port 8000
```

* **API Healthcheck:** `http://127.0.0.1:8000/`
* **Interactive Swagger UI Documentation:** `http://127.0.0.1:8000/docs`

---

### 2. Start the React Frontend

Open a second terminal and run:

```bash
cd c:\triolang\frontend

# Install dependencies (if not installed yet)
npm install

# Start frontend development server
npm run dev
```

* **Frontend Web App:** `http://localhost:5173`

---

### 3. Run Automated Tests

```bash
cd c:\triolang\backend
.\venv\Scripts\pytest -v
```
