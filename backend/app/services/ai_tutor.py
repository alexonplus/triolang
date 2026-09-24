"""
AI Language Tutor Service
-------------------------
"""

import httpx
from typing import Dict, Any
from app.core.config import settings

LOCAL_TUTOR_KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    "fika": {
        "reply": "🇸🇪 **Fika** is an essential Swedish cultural institution. It is much more than having a cup of coffee; it is a dedicated social break to slow down, converse with friends or colleagues, and enjoy sweet pastries like *kanelbullar* (cinnamon buns) or *chokladbollar*.",
        "suggested_followups": ["What is a kanelbulle?", "How do I order coffee in Swedish?"],
        "swedish_vocabulary": [
            {"word": "en fika", "translation": "a coffee break"},
            {"word": "en kanelbulle", "translation": "a cinnamon bun"},
            {"word": "att fika", "translation": "to have a coffee break (verb)"},
        ],
    },
    "articles": {
        "reply": "🇸🇪 **Swedish Noun Genders (En vs. Ett)**:\nSwedish has two grammatical genders:\n1. **Utrum (En-words)**: ~75% of nouns (e.g., *en flicka* - a girl, *en bil* - a car).\n2. **Neutrum (Ett-words)**: ~25% of nouns (e.g., *ett hus* - a house, *ett äpple* - an apple).\n\n💡 *Tip*: In Swedish, the definite article 'the' is attached to the END of the word:\n- *en katt* (a cat) -> *katten* (the cat)\n- *ett hus* (a house) -> *huset* (the house)",
        "suggested_followups": ["How do plurals work in Swedish?", "Give me 5 common ett-words"],
        "swedish_vocabulary": [
            {"word": "en bok -> boken", "translation": "a book -> the book"},
            {"word": "ett bord -> bordet", "translation": "a table -> the table"},
        ],
    },
    "word_order": {
        "reply": "🇸🇪 **The Swedish V2 Rule (Verb-Second Rule)**:\nIn Swedish main clauses, the finite verb is **always the second element** in the sentence.\n\n- Normal order: *Jag äter frukost nu.* (I eat breakfast now.)\n- If time comes first: *Nu äter jag frukost.* (Now eat I breakfast.)\nNotice how the verb *äter* stayed in position #2!",
        "suggested_followups": ["Why does Swedish invert word order?", "Practice sentences with V2 rule"],
        "swedish_vocabulary": [
            {"word": "idag", "translation": "today"},
            {"word": "nu", "translation": "now"},
            {"word": "alltid", "translation": "always"},
        ],
    },
}


async def ask_ai_tutor(query: str, target_language: str = "sv", context: str = "") -> Dict[str, Any]:
    lower_query = query.lower()

    if settings.GEMINI_API_KEY and settings.GEMINI_API_KEY != "YOUR_GEMINI_API_KEY_HERE":
        system_prompt = (
            "You are 'TrioBot', an encouraging, expert language tutor for Swedish and English in the TrioLang app. "
            "Keep explanations concise, easy to understand, formatted with clear markdown, bullet points, and emoji. "
            "Always include examples in both Swedish and English."
        )
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{settings.GEMINI_MODEL}:generateContent?key={settings.GEMINI_API_KEY}"
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"{system_prompt}\nUser Context: {context}\nUser Question: {query}"}
                    ]
                }
            ]
        }
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(url, json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    ai_text = data["candidates"][0]["content"]["parts"][0]["text"]
                    return {
                        "reply": ai_text,
                        "suggested_followups": ["Explain more examples", "Give me a quick quiz", "How do I pronounce this?"],
                        "swedish_vocabulary": [],
                    }
        except Exception as e:
            print(f"[AI Tutor] Network call failed: {e}. Using local knowledge base.")

    for key, data in LOCAL_TUTOR_KNOWLEDGE_BASE.items():
        if key in lower_query or any(word in lower_query for word in key.split("_")):
            return data

    if "en" in lower_query or "ett" in lower_query or "gender" in lower_query:
        return LOCAL_TUTOR_KNOWLEDGE_BASE["articles"]
    elif "fika" in lower_query or "coffee" in lower_query or "bulle" in lower_query:
        return LOCAL_TUTOR_KNOWLEDGE_BASE["fika"]
    elif "verb" in lower_query or "order" in lower_query or "sentence" in lower_query:
        return LOCAL_TUTOR_KNOWLEDGE_BASE["word_order"]

    return {
        "reply": f"Hej! I am your TrioLang Language Tutor. You asked: *'{query}'*.\n\nIn Swedish, consistency is key! Remember: nouns use either **en** or **ett**, verbs don't conjugate for person (*jag är, du är, vi är*), and the verb is always in the 2nd position in statements.\n\nAsk me about **fika**, **en vs ett articles**, or **Swedish word order**!",
        "suggested_followups": ["Tell me about Swedish Fika", "How do En and Ett work?", "Explain Swedish verb word order"],
        "swedish_vocabulary": [
            {"word": "Välkommen!", "translation": "Welcome!"},
            {"word": "Hur säger man...?", "translation": "How do you say...?"},
            {"word": "Vad betyder...?", "translation": "What does ... mean?"},
        ],
    }
