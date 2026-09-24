"""
Security & Input Sanitization Module
------------------------------------
CLEAN ARCHITECTURE - SECURITY LAYER
"""

import re


def sanitize_topic_input(topic: str, max_length: int = 100) -> str:
    """
    Sanitizes user-submitted lesson topics to prevent prompt injection or abuse.
    """
    if not topic:
        return "General Conversation"

    cleaned = topic.strip()[:max_length]
    cleaned = re.sub(r"[^\w\s\-(),.!?'åäöÅÄÖ]", "", cleaned, flags=re.UNICODE)
    return cleaned if cleaned else "General Conversation"
