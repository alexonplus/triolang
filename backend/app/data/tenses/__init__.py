"""
================================================================================
TrioLang Tenses Registry Package
================================================================================
Aggregates comprehensive English and Swedish verb tense curriculum.
"""

from typing import List, Dict, Any

from app.data.tenses.english_tenses import ENGLISH_TENSES
from app.data.tenses.swedish_tenses import SWEDISH_TENSES

ALL_TENSES: List[Dict[str, Any]] = ENGLISH_TENSES + SWEDISH_TENSES
