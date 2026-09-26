"""
================================================================================
TrioLang Grammar Service
================================================================================
CLEAN ARCHITECTURE - DOMAIN SERVICE LAYER
Provides business logic for grammar topic retrieval, rule breakdowns,
built-in exercise drills, and on-demand Gemini AI exercise generation.
"""

import json
import logging
from typing import List, Optional, Dict, Any

from app.core.config import settings
from app.data.grammar_data import GRAMMAR_TOPICS
from app.models.schemas import (
    GrammarTopicSummary,
    GrammarTopicDetail,
    GrammarPracticeDrillsResponse,
    GrammarExerciseItem,
)

logger = logging.getLogger(__name__)


class GrammarService:
    """
    Domain service responsible for grammar curriculum queries and AI drill generation.
    """

    @staticmethod
    def get_topics(
        language: Optional[str] = None,
        level: Optional[str] = None
    ) -> List[GrammarTopicSummary]:
        """
        Filter grammar topics by target language and CEFR level (A1 -> C1).
        """
        filtered = GRAMMAR_TOPICS
        if language:
            filtered = [t for t in filtered if t["language"] == language.lower()]
        if level:
            filtered = [t for t in filtered if t["level"].upper() == level.upper()]

        return [
            GrammarTopicSummary(
                id=t["id"],
                language=t["language"],
                level=t["level"],
                title=t["title"],
                swedish_title=t["swedish_title"],
                summary=t["summary"],
                formula=t["formula"],
            )
            for t in filtered
        ]

    @staticmethod
    def get_topic_detail(topic_id: str) -> Optional[GrammarTopicDetail]:
        """
        Fetch complete theoretical rule explanation, formulas, examples, and pitfalls.
        """
        topic = next((t for t in GRAMMAR_TOPICS if t["id"] == topic_id), None)
        if not topic:
            return None

        return GrammarTopicDetail(
            id=topic["id"],
            language=topic["language"],
            level=topic["level"],
            title=topic["title"],
            swedish_title=topic["swedish_title"],
            summary=topic["summary"],
            formula=topic["formula"],
            rule_explanation=topic["rule_explanation"],
            examples=topic.get("examples", []),
            common_pitfalls=topic.get("common_pitfalls", []),
            exercises_count=len(topic.get("exercises", [])),
        )

    @staticmethod
    def get_practice_drills(topic_id: str) -> Optional[GrammarPracticeDrillsResponse]:
        """
        Get built-in interactive drill exercises for a specific grammar rule.
        """
        topic = next((t for t in GRAMMAR_TOPICS if t["id"] == topic_id), None)
        if not topic:
            return None

        exercises = [
            GrammarExerciseItem(
                id=ex["id"],
                type=ex["type"],
                prompt=ex["prompt"],
                options=ex.get("options"),
                correct_answer=ex["correct_answer"],
                explanation=ex.get("explanation"),
            )
            for ex in topic.get("exercises", [])
        ]

        return GrammarPracticeDrillsResponse(
            topic_id=topic["id"],
            topic_title=topic["title"],
            level=topic["level"],
            exercises=exercises,
        )

    @classmethod
    def generate_ai_drills(
        cls,
        topic_id: str,
        custom_focus: Optional[str] = None
    ) -> Optional[GrammarPracticeDrillsResponse]:
        """
        Dynamically generate targeted practice exercises for a grammar topic using Gemini AI.
        Falls back to curated extension templates if API key is not supplied.
        """
        topic = next((t for t in GRAMMAR_TOPICS if t["id"] == topic_id), None)
        if not topic:
            return None

        # Check if Gemini API is available
        if settings.GEMINI_API_KEY and settings.GEMINI_API_KEY != "your-gemini-api-key-here":
            try:
                import google.generativeai as genai

                genai.configure(api_key=settings.GEMINI_API_KEY)
                model = genai.GenerativeModel("gemini-1.5-flash")

                prompt = (
                    f"You are a master language teacher specializing in CEFR language pedagogy.\n"
                    f"Topic: {topic['title']} ({topic['swedish_title']})\n"
                    f"Language: {topic['language']} (Level: {topic['level']})\n"
                    f"Rule: {topic['rule_explanation']}\n"
                    f"Optional Focus: {custom_focus or 'General mastery and common pitfalls'}\n\n"
                    f"Generate 3 brand-new interactive grammar exercises targeting this exact rule.\n"
                    f"Respond ONLY with valid JSON in this structure (no markdown fences):\n"
                    f"{{\n"
                    f'  "exercises": [\n'
                    f'    {{\n'
                    f'      "id": 101,\n'
                    f'      "type": "multiple_choice",\n'
                    f'      "prompt": "Choose the correct sentence...",\n'
                    f'      "options": ["Option A", "Option B", "Option C", "Option D"],\n'
                    f'      "correct_answer": "Option B",\n'
                    f'      "explanation": "Clear grammatical reasoning explaining why."\n'
                    f'    }}\n'
                    f'  ]\n'
                    f"}}"
                )

                response = model.generate_content(prompt)
                raw_text = response.text.strip()
                if raw_text.startswith("```json"):
                    raw_text = raw_text[7:]
                if raw_text.startswith("```"):
                    raw_text = raw_text[3:]
                if raw_text.endswith("```"):
                    raw_text = raw_text[:-3]

                data = json.loads(raw_text.strip())
                generated_items = [
                    GrammarExerciseItem(
                        id=ex.get("id", i + 100),
                        type=ex.get("type", "multiple_choice"),
                        prompt=ex["prompt"],
                        options=ex.get("options", []),
                        correct_answer=ex["correct_answer"],
                        explanation=ex.get("explanation"),
                    )
                    for i, ex in enumerate(data.get("exercises", []))
                ]

                return GrammarPracticeDrillsResponse(
                    topic_id=topic["id"],
                    topic_title=f"{topic['title']} (AI Generated)",
                    level=topic["level"],
                    exercises=generated_items,
                )
            except Exception as err:
                logger.warning(f"AI drill generation fallback triggered: {err}")

        # Fallback drill generation
        base_drills = cls.get_practice_drills(topic_id)
        return base_drills
