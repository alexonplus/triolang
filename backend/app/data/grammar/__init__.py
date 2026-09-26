"""
================================================================================
TrioLang Grammar Registry Package
================================================================================
Aggregates modular CEFR A1-C1 grammar topics for Swedish and English.
"""

from typing import List, Dict, Any

from app.data.grammar.swedish_a1 import SWEDISH_A1_TOPICS
from app.data.grammar.swedish_a2 import SWEDISH_A2_TOPICS
from app.data.grammar.swedish_b1 import SWEDISH_B1_TOPICS
from app.data.grammar.swedish_b2 import SWEDISH_B2_TOPICS
from app.data.grammar.swedish_c1 import SWEDISH_C1_TOPICS

from app.data.grammar.english_a1 import ENGLISH_A1_TOPICS
from app.data.grammar.english_a2 import ENGLISH_A2_TOPICS
from app.data.grammar.english_b1 import ENGLISH_B1_TOPICS
from app.data.grammar.english_b2 import ENGLISH_B2_TOPICS
from app.data.grammar.english_c1 import ENGLISH_C1_TOPICS

GRAMMAR_TOPICS: List[Dict[str, Any]] = (
    SWEDISH_A1_TOPICS
    + SWEDISH_A2_TOPICS
    + SWEDISH_B1_TOPICS
    + SWEDISH_B2_TOPICS
    + SWEDISH_C1_TOPICS
    + ENGLISH_A1_TOPICS
    + ENGLISH_A2_TOPICS
    + ENGLISH_B1_TOPICS
    + ENGLISH_B2_TOPICS
    + ENGLISH_C1_TOPICS
)
