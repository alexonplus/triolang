"""
Application Configuration & Settings Module
-------------------------------------------
CLEAN ARCHITECTURE - CORE LAYER
"""

import os
from dataclasses import dataclass, field
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
ENV_FILE: Path = BASE_DIR / ".env"

if ENV_FILE.exists():
    load_dotenv(dotenv_path=ENV_FILE)
else:
    load_dotenv()


@dataclass
class Settings:
    PROJECT_NAME: str = "TrioLang API"
    PROJECT_VERSION: str = "1.0.0"
    DESCRIPTION: str = "REST API for TrioLang language learning application (Swedish & English)."

    DATABASE_PATH: Path = BASE_DIR / "triolang.db"
    DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite:///{DATABASE_PATH}")

    CORS_ORIGINS: list[str] = field(
        default_factory=lambda: [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "*",
        ]
    )

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    INITIAL_HEARTS: int = 5
    XP_PER_CORRECT_ANSWER: int = 10
    XP_LESSON_COMPLETION_BONUS: int = 25
    HEART_REGEN_MINUTES: int = 15


settings = Settings()
