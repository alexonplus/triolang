"""
================================================================================
English CEFR B1 Grammar Topics
================================================================================
Comprehensive, structured B1 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

ENGLISH_B1_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "en-b1-conditionals-1-and-2",
        "language": "en",
        "level": "B1",
        "title": "Conditionals (First & Second Conditional)",
        "swedish_title": "Villkorssatser: 1:a och 2:a konditionalis",
        "summary": "Master real future possibilities (1st conditional) versus hypothetical or imaginary situations (2nd conditional).",
        "rule_explanation": (
            "1. First Conditional (Real / Possible future situations):\n"
            "   • Structure: If + Present Simple, will + base verb\n"
            "   • 'If it rains tomorrow, we will stay at home.'\n"
            "   • Expresses realistic possibilities in the future.\n\n"
            "2. Second Conditional (Hypothetical / Unreal present or future):\n"
            "   • Structure: If + Past Simple, would + base verb\n"
            "   • 'If I won the lottery, I would travel the world.'\n"
            "   • 'If I were you, I would consult a doctor.' (Notice 'were' is standard for all persons)"
        ),
        "formula": "1st: If + Present Simple, will + Verb | 2nd: If + Past Simple, would + Verb",
        "examples": [
            {"swedish": "Om du studerar hårt, klarar du provet.", "english": "If you study hard, you will pass the exam.", "target_highlight": "study ... will pass"},
            {"swedish": "Om jag hade mer tid, skulle jag lära mig spela gitarr.", "english": "If I had more time, I would learn to play the guitar.", "target_highlight": "had ... would learn"},
            {"swedish": "Vad skulle du göra om du var osynlig?", "english": "What would you do if you were invisible?", "target_highlight": "would you do ... were"}
        ],
        "common_pitfalls": [
            "Never use 'will' or 'would' in the if-clause: say 'If I have time', NOT 'If I will have time'.",
            "Say 'If I were you', not 'If I was you' in formal/written English."
        ],
        "exercises": [
            {
                "id": 801,
                "type": "multiple_choice",
                "prompt": "If it ___ sunny tomorrow, we will go to the beach.",
                "options": ["is", "will be", "was", "would be"],
                "correct_answer": "is",
                "explanation": "First conditional uses Present Simple in the if-clause."
            },
            {
                "id": 802,
                "type": "fill_gap",
                "prompt": "If I ___ (be) in your position, I would accept the job offer.",
                "options": ["were", "am", "will be", "would be"],
                "correct_answer": "were",
                "explanation": "In 2nd conditional, subjunctive 'were' is used for hypothetical advice."
            },
            {
                "id": 803,
                "type": "multiple_choice",
                "prompt": "Which sentence is grammatically correct?",
                "options": [
                    "If she will study, she will pass.",
                    "If she studies, she will pass.",
                    "If she study, she will pass.",
                    "If she studied, she will pass."
                ],
                "correct_answer": "If she studies, she will pass.",
                "explanation": "1st conditional: 'If' + 3rd person singular 'studies' + 'will pass'."
            },
            {
                "id": 804,
                "type": "fill_gap",
                "prompt": "If we had a car, we ___ (travel) much more often.",
                "options": ["would travel", "will travel", "traveled", "have traveled"],
                "correct_answer": "would travel",
                "explanation": "2nd conditional requires 'would + bare infinitive' in the result clause."
            },
            {
                "id": 805,
                "type": "multiple_choice",
                "prompt": "What does this sentence mean? 'If I had a million dollars, I would buy an island.'",
                "options": [
                    "I currently do not have a million dollars (hypothetical situation).",
                    "I definitely expect to get a million dollars tomorrow.",
                    "I bought an island in the past.",
                    "I am required to buy an island."
                ],
                "correct_answer": "I currently do not have a million dollars (hypothetical situation).",
                "explanation": "2nd conditional expresses unreal/hypothetical present situations."
            },
            {
                "id": 806,
                "type": "fill_gap",
                "prompt": "You will miss the train unless you ___ (hurry) now.",
                "options": ["hurry", "will hurry", "hurried", "hurries"],
                "correct_answer": "hurry",
                "explanation": "'Unless' equals 'if not' and takes Present Simple in conditional sentences."
            },
            {
                "id": 807,
                "type": "multiple_choice",
                "prompt": "Choose the correct question form:",
                "options": [
                    "What would you do if you lost your passport?",
                    "What will you do if you lost your passport?",
                    "What did you do if you would lose your passport?",
                    "What would you did if you lost your passport?"
                ],
                "correct_answer": "What would you do if you lost your passport?",
                "explanation": "2nd conditional question: 'What would you do' + 'if you lost'."
            },
            {
                "id": 808,
                "type": "fill_gap",
                "prompt": "If they ___ (offer) you the scholarship, will you move to Boston?",
                "options": ["offer", "offered", "will offer", "would offer"],
                "correct_answer": "offer",
                "explanation": "First conditional with 'will you move' requires Present Simple 'offer'."
            },
            {
                "id": 809,
                "type": "multiple_choice",
                "prompt": "Identify the INCORRECT sentence:",
                "options": [
                    "If I will see Sarah, I will tell her the news.",
                    "If I see Sarah, I will tell her the news.",
                    "If I saw Sarah, I would tell her the news.",
                    "Unless I see Sarah, I won't know the truth."
                ],
                "correct_answer": "If I will see Sarah, I will tell her the news.",
                "explanation": "Never use 'will' in the if-clause."
            },
            {
                "id": 810,
                "type": "fill_gap",
                "prompt": "If he practiced more, he ___ (play) the piano much better.",
                "options": ["would play", "will play", "plays", "played"],
                "correct_answer": "would play",
                "explanation": "2nd conditional: past tense 'practiced' matches 'would play'."
            }
        ]
    }
]
