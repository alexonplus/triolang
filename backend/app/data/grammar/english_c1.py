"""
================================================================================
English CEFR C1 Grammar Topics
================================================================================
Comprehensive, structured C1 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

ENGLISH_C1_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "en-c1-negative-inversion",
        "language": "en",
        "level": "C1",
        "title": "Negative & Restrictive Inversion for Rhetorical Emphasis",
        "swedish_title": "Negativ inversion för stilistisk emfas",
        "summary": "Master formal stylistic inversion triggered by fronted negative and restrictive adverbs.",
        "rule_explanation": (
            "In formal, literary, or rhetorical English, when a negative, restrictive, or limiting adverbial expression begins a sentence, the subject and auxiliary verb invert (taking question word order).\n\n"
            "Key triggers:\n"
            "• Rarely / Seldom / Scarcely / Hardly / Barely\n"
            "• Never / Under no circumstances / On no account / In no way\n"
            "• Not only ... but also / Not until / Not since\n"
            "• Little / Only after / Only by / Only when\n\n"
            "Transformation patterns:\n"
            "• Standard: 'I have rarely seen such dedication.'\n"
            "• C1 Inversion: 'Rarely have I seen such dedication.'\n"
            "• Standard: 'He little realized the danger.'\n"
            "• C1 Inversion: 'Little did he realize the danger.'\n"
            "• Standard: 'You should under no circumstances open this door.'\n"
            "• C1 Inversion: 'Under no circumstances should you open this door.'"
        ),
        "formula": "[Negative Adverb] + [Auxiliary Verb (have/do/be/should)] + [Subject] + [Main Verb]",
        "examples": [
            {"swedish": "Sällan har jag bevittnat en sådan hängivenhet.", "english": "Rarely have I witnessed such extraordinary dedication.", "target_highlight": "Rarely have I witnessed"},
            {"swedish": "Inte bara vann hon tävlingen, utan hon slog också världsrekord.", "english": "Not only did she win the race, but she also broke the world record.", "target_highlight": "Not only did she win"},
            {"swedish": "Under inga omständigheter får dörren lämnas olåst.", "english": "Under no circumstances should the door be left unlocked.", "target_highlight": "Under no circumstances should"},
            {"swedish": "Knappt hade vi anlänt förrän stormen bröt ut.", "english": "Hardly had we arrived when the tempest erupted.", "target_highlight": "Hardly had we arrived"}
        ],
        "common_pitfalls": [
            "Always introduce dummy auxiliary 'do/does/did' if the original sentence had no auxiliary verb ('Little did he know', NOT 'Little knew he').",
            "In 'Not until...' clauses, the inversion occurs in the MAIN clause, not the time clause: 'Not until I arrived DID I REALIZE the truth'."
        ],
        "exercises": [
            {
                "id": 1001,
                "type": "multiple_choice",
                "prompt": "Which sentence has grammatically correct negative inversion?",
                "options": [
                    "Hardly had we sat down when the phone rang.",
                    "Hardly we had sat down when the phone rang.",
                    "Hardly did we sat down when the phone rang.",
                    "Hardly we sat down when the phone rang."
                ],
                "correct_answer": "Hardly had we sat down when the phone rang.",
                "explanation": "Fronted 'Hardly' triggers auxiliary inversion 'had we sat down'."
            },
            {
                "id": 1002,
                "type": "fill_gap",
                "prompt": "Seldom ___ I experienced such genuine hospitality. (have)",
                "options": ["have", "did", "had", "was"],
                "correct_answer": "have",
                "explanation": "Present perfect inversion: 'Seldom have I experienced'."
            },
            {
                "id": 1003,
                "type": "multiple_choice",
                "prompt": "Invert: 'He little suspected that his life was about to change':",
                "options": [
                    "Little did he suspect that his life was about to change.",
                    "Little he suspected that his life was about to change.",
                    "Little had he suspected that his life was about to change.",
                    "Little was he suspected that his life was about to change."
                ],
                "correct_answer": "Little did he suspect that his life was about to change.",
                "explanation": "Past simple without auxiliary requires dummy 'did': 'Little did he suspect'."
            },
            {
                "id": 1004,
                "type": "fill_gap",
                "prompt": "Under no circumstances ___ staff members discuss confidential data. (may/should)",
                "options": ["should", "they should", "did", "are to"],
                "correct_answer": "should",
                "explanation": "Modal inversion: 'Under no circumstances should staff members...'."
            },
            {
                "id": 1005,
                "type": "multiple_choice",
                "prompt": "Complete: 'Not only ___ an outstanding researcher, but she is also a brilliant lecturer.'",
                "options": [
                    "is she",
                    "she is",
                    "does she",
                    "was she"
                ],
                "correct_answer": "is she",
                "explanation": "Inversion with verb 'to be': 'Not only is she...'."
            },
            {
                "id": 1006,
                "type": "fill_gap",
                "prompt": "Not until yesterday ___ I find out about the merger. (did)",
                "options": ["did", "have", "had", "was"],
                "correct_answer": "did",
                "explanation": "In 'Not until...' constructions, the main clause inverts with dummy past auxiliary 'did'."
            },
            {
                "id": 1007,
                "type": "multiple_choice",
                "prompt": "Identify the INCORRECT sentence:",
                "options": [
                    "Rarely we see such profound changes in consumer behavior.",
                    "Rarely do we see such profound changes in consumer behavior.",
                    "Only after the investigation did the truth emerge.",
                    "No sooner had the keynote finished than the applause erupted."
                ],
                "correct_answer": "Rarely we see such profound changes in consumer behavior.",
                "explanation": "Uninverted order after 'Rarely' is ungrammatical in formal English (must be 'Rarely do we see...')."
            },
            {
                "id": 1008,
                "type": "fill_gap",
                "prompt": "No sooner had the plane landed ___ the passengers stood up. (than/when)",
                "options": ["than", "when", "that", "then"],
                "correct_answer": "than",
                "explanation": "'No sooner had ... THAN' is the standard comparative correlative pair."
            },
            {
                "id": 1009,
                "type": "multiple_choice",
                "prompt": "Transform 'You will only understand the nuance by reading the original text':",
                "options": [
                    "Only by reading the original text will you understand the nuance.",
                    "Only by reading the original text you will understand the nuance.",
                    "Only by reading the original text understand you will the nuance.",
                    "By reading the original text will only you understand the nuance."
                ],
                "correct_answer": "Only by reading the original text will you understand the nuance.",
                "explanation": "'Only by...' fronting triggers modal auxiliary inversion 'will you understand'."
            },
            {
                "id": 1010,
                "type": "fill_gap",
                "prompt": "Scarcely ___ the announcement been made when protests started. (had)",
                "options": ["had", "has", "did", "was"],
                "correct_answer": "had",
                "explanation": "'Scarcely had the announcement been made when...'."
            }
        ]
    }
]
