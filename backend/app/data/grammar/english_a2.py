"""
================================================================================
English CEFR A2 Grammar Topics
================================================================================
Comprehensive, structured A2 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

ENGLISH_A2_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "en-a2-present-perfect-vs-past-simple",
        "language": "en",
        "level": "A2",
        "title": "Present Perfect vs. Past Simple",
        "swedish_title": "Perfekt vs. Dåtid (Present Perfect vs. Past Simple)",
        "summary": "Differentiate between finished historical time (yesterday, in 2019) and life experiences or unfinished time (ever, already, since).",
        "rule_explanation": (
            "Choosing between the Past Simple and the Present Perfect is one of the most critical skills in English grammar:\n\n"
            "1. Past Simple (Verb-ed / V2):\n"
            "   Use when the action took place at a specific, finished time in the past.\n"
            "   • Time markers: yesterday, last night, two days ago, in 2015, when I was at university.\n"
            "   • 'I visited Rome in 2021.'\n\n"
            "2. Present Perfect (have / has + Past Participle / V3):\n"
            "   Use when the time is unfinished, unspecified, or the result is relevant right now.\n"
            "   • Time markers: already, yet, ever, never, just, so far, since 2010, for 5 years.\n"
            "   • 'I have visited Rome three times.' (in my life experience so far)"
        ),
        "formula": "Past Simple: Verb-ed / V2 (Finished time) | Present Perfect: have/has + V3 (Connected to present)",
        "examples": [
            {"swedish": "Jag tappade mina nycklar igår.", "english": "I lost my keys yesterday.", "target_highlight": "lost ... yesterday"},
            {"swedish": "Jag har tappat mina nycklar! (Jag kan inte öppna dörren nu)", "english": "I have lost my keys! (I cannot open the door now)", "target_highlight": "have lost"},
            {"swedish": "Har du någonsin sett norrsken?", "english": "Have you ever seen the Northern Lights?", "target_highlight": "Have you ever seen"},
            {"swedish": "Vi flyttade till London 2018.", "english": "We moved to London in 2018.", "target_highlight": "moved ... in 2018"}
        ],
        "common_pitfalls": [
            "NEVER use Present Perfect with a specific past time: 'I have seen him yesterday' is WRONG -> 'I saw him yesterday'.",
            "Do not confuse 'for' (duration: for 3 years) with 'since' (starting point: since 2020)."
        ],
        "exercises": [
            {
                "id": 701,
                "type": "multiple_choice",
                "prompt": "Select the grammatically correct sentence:",
                "options": [
                    "I have finished the report two hours ago.",
                    "I finished the report two hours ago.",
                    "I was finished the report two hours ago.",
                    "I have finish the report two hours ago."
                ],
                "correct_answer": "I finished the report two hours ago.",
                "explanation": "'Two hours ago' is a specific finished past time marker requiring Past Simple."
            },
            {
                "id": 702,
                "type": "fill_gap",
                "prompt": "___ you ever eaten Swedish meatballs?",
                "options": ["Have", "Did", "Were", "Are"],
                "correct_answer": "Have",
                "explanation": "Life experience question uses 'Have you ever + V3'."
            },
            {
                "id": 703,
                "type": "multiple_choice",
                "prompt": "Complete: 'She ___ in Stockholm since 2015.'",
                "options": [
                    "has lived",
                    "lived",
                    "lives",
                    "was living"
                ],
                "correct_answer": "has lived",
                "explanation": "Actions that started in the past and continue to now with 'since' require Present Perfect."
            },
            {
                "id": 704,
                "type": "fill_gap",
                "prompt": "Last weekend we ___ (go) hiking in the mountains.",
                "options": ["went", "have gone", "go", "gone"],
                "correct_answer": "went",
                "explanation": "'Last weekend' specifies a finished past time -> Past Simple 'went'."
            },
            {
                "id": 705,
                "type": "multiple_choice",
                "prompt": "Choose between 'for' and 'since': 'They have known each other ___ ten years.'",
                "options": ["for", "since", "from", "during"],
                "correct_answer": "for",
                "explanation": "'For' is used for a period or duration of time."
            },
            {
                "id": 706,
                "type": "fill_gap",
                "prompt": "I haven't received the package ___ (yet / already).",
                "options": ["yet", "already", "since", "ago"],
                "correct_answer": "yet",
                "explanation": "'Yet' is used in negative sentences and questions at the end of a clause."
            },
            {
                "id": 707,
                "type": "multiple_choice",
                "prompt": "Which sentence is INCORRECT?",
                "options": [
                    "When did you buy this car?",
                    "When have you bought this car?",
                    "I have already seen that movie.",
                    "He lived in Berlin for two years before moving to Paris."
                ],
                "correct_answer": "When have you bought this car?",
                "explanation": "Questions asking 'When...' refer to a specific point in time and must use Past Simple ('When did you buy...')."
            },
            {
                "id": 708,
                "type": "fill_gap",
                "prompt": "Mozart ___ (write) more than 600 pieces of music.",
                "options": ["wrote", "has written", "writes", "was written"],
                "correct_answer": "wrote",
                "explanation": "Mozart's life is a finished past period, so Past Simple 'wrote' is required."
            },
            {
                "id": 709,
                "type": "multiple_choice",
                "prompt": "'He has gone to Italy' vs. 'He has been to Italy':",
                "options": [
                    "'has gone' means he is in Italy now; 'has been' means he visited and returned.",
                    "'has been' means he is in Italy now; 'has gone' means he returned.",
                    "Both mean the exact same thing.",
                    "Both are ungrammatical."
                ],
                "correct_answer": "'has gone' means he is in Italy now; 'has been' means he visited and returned.",
                "explanation": "'Been to' indicates a completed round-trip experience; 'gone to' indicates the person has not yet returned."
            },
            {
                "id": 710,
                "type": "fill_gap",
                "prompt": "Look! Someone ___ (break) the window.",
                "options": ["has broken", "broke", "breaked", "was broken"],
                "correct_answer": "has broken",
                "explanation": "Present result of a recent action requires Present Perfect ('has broken')."
            }
        ]
    }
]
