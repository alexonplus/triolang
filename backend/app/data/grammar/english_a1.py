"""
================================================================================
English CEFR A1 Grammar Topics
================================================================================
Comprehensive, structured A1 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

ENGLISH_A1_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "en-a1-present-simple-3rd-person",
        "language": "en",
        "level": "A1",
        "title": "Present Simple & 3rd Person Singular (-s/-es)",
        "swedish_title": "Presens enkel och 3:e person singular (-s/-es)",
        "summary": "Mastering routines, habitual facts, and the essential 3rd person singular 'he/she/it' -s rule.",
        "rule_explanation": (
            "The Present Simple tense is used to describe habits, regular routines, and universal facts.\n\n"
            "• I / You / We / They + base verb (I work, they play, we eat).\n"
            "• He / She / It + base verb + -s / -es (He works, she watches, it rains).\n\n"
            "• Negatives:\n"
            "  - I/you/we/they + do not (don't) + base verb\n"
            "  - He/she/it + does not (doesn't) + base verb (no -s on main verb!)\n\n"
            "• Questions:\n"
            "  - Do + I/you/we/they + base verb?\n"
            "  - Does + he/she/it + base verb?"
        ),
        "formula": "Subject (He/She/It) + Verb-s / -es | Negative: doesn't + Verb | Question: Does + Subject + Verb?",
        "examples": [
            {"swedish": "Hon bor i London.", "english": "She lives in London.", "target_highlight": "lives"},
            {"swedish": "Han gillar inte fisk.", "english": "He doesn't like fish.", "target_highlight": "doesn't like"},
            {"swedish": "Jobbar hon på ett sjukhus?", "english": "Does she work at a hospital?", "target_highlight": "Does she work"},
            {"swedish": "Tåget avgår klockan 09:00.", "english": "The train leaves at 09:00.", "target_highlight": "leaves"}
        ],
        "common_pitfalls": [
            "Never add -s after 'does' or 'doesn't': say 'Does he like?', NOT 'Does he likes?'.",
            "Don't forget the -s for third person singular (say 'My brother speaks', not 'My brother speak')."
        ],
        "exercises": [
            {
                "id": 601,
                "type": "fill_gap",
                "prompt": "My sister ___ (teach) English at a high school.",
                "options": ["teaches", "teach", "is teach", "teaching"],
                "correct_answer": "teaches",
                "explanation": "'My sister' is 3rd person singular (she), adding -es to verbs ending in -ch."
            },
            {
                "id": 602,
                "type": "multiple_choice",
                "prompt": "Choose the correct negative sentence:",
                "options": [
                    "He doesn't likes spicy food.",
                    "He doesn't like spicy food.",
                    "He don't likes spicy food.",
                    "He not likes spicy food."
                ],
                "correct_answer": "He doesn't like spicy food.",
                "explanation": "After auxiliary 'doesn't', the main verb remains in bare infinitive form ('like')."
            },
            {
                "id": 603,
                "type": "fill_gap",
                "prompt": "___ (Do/Does) David play tennis on Sundays?",
                "options": ["Does", "Do", "Is", "Has"],
                "correct_answer": "Does",
                "explanation": "Subject 'David' is 3rd person singular -> 'Does'."
            },
            {
                "id": 604,
                "type": "multiple_choice",
                "prompt": "Convert 'They study hard' to subject 'Emily':",
                "options": [
                    "Emily studies hard.",
                    "Emily studys hard.",
                    "Emily study hard.",
                    "Emily is study hard."
                ],
                "correct_answer": "Emily studies hard.",
                "explanation": "Verbs ending in consonant + y change y to -ies -> 'studies'."
            },
            {
                "id": 605,
                "type": "fill_gap",
                "prompt": "Water ___ (boil) at 100 degrees Celsius.",
                "options": ["boils", "boil", "is boil", "boiling"],
                "correct_answer": "boils",
                "explanation": "General scientific fact with uncountable singular subject 'Water' -> 'boils'."
            },
            {
                "id": 606,
                "type": "multiple_choice",
                "prompt": "Which sentence is correct?",
                "options": [
                    "Where does your parents live?",
                    "Where do your parents live?",
                    "Where are your parents live?",
                    "Where does your parents lives?"
                ],
                "correct_answer": "Where do your parents live?",
                "explanation": "'Your parents' is plural (they), requiring auxiliary 'do'."
            },
            {
                "id": 607,
                "type": "fill_gap",
                "prompt": "He always ___ (wash) his car on Saturday mornings.",
                "options": ["washes", "wash", "washing", "washs"],
                "correct_answer": "washes",
                "explanation": "Verbs ending in -sh add -es in third person singular."
            },
            {
                "id": 608,
                "type": "multiple_choice",
                "prompt": "Identify the INCORRECT sentence:",
                "options": [
                    "She has two brothers.",
                    "He goes to the gym every day.",
                    "My mother don't drive.",
                    "The sun rises in the east."
                ],
                "correct_answer": "My mother don't drive.",
                "explanation": "Incorrect auxiliary! It must be 'My mother doesn't drive'."
            },
            {
                "id": 609,
                "type": "fill_gap",
                "prompt": "What time ___ the bank open in the morning?",
                "options": ["does", "do", "is", "has"],
                "correct_answer": "does",
                "explanation": "'The bank' is singular (it), taking auxiliary 'does'."
            },
            {
                "id": 610,
                "type": "multiple_choice",
                "prompt": "Select the correct present simple form for 'fly':",
                "options": ["He flys", "He flies", "He is fly", "He flyes"],
                "correct_answer": "He flies",
                "explanation": "Consonant + y changes to -ies: fly -> flies."
            }
        ]
    }
]
