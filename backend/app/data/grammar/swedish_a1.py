"""
================================================================================
Swedish CEFR A1 Grammar Topics
================================================================================
Comprehensive, structured A1 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

SWEDISH_A1_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "sv-a1-en-ett-articles",
        "language": "sv",
        "level": "A1",
        "title": "Articles & Noun Gender (En vs. Ett)",
        "swedish_title": "Obestämd och bestämd form (En och Ett)",
        "summary": "Learn to distinguish Utrum (en) and Neutrum (ett) nouns and form the definite suffix (-en, -et, -n, -t).",
        "rule_explanation": (
            "Swedish nouns belong to two genders:\n"
            "1. Utrum ('en'-words) — ~75% of all nouns (en hund, en bil, en katt).\n"
            "2. Neutrum ('ett'-words) — ~25% of all nouns (ett hus, ett barn, ett bord).\n\n"
            "In English, the definite article 'the' is placed before the noun. In Swedish, it is attached as an ending:\n"
            "• en hund -> hunden (the dog)\n"
            "• ett hus -> huset (the house)\n"
            "• en flicka (ends in vowel) -> flickan (the girl)\n"
            "• ett äpple (ends in vowel) -> äpplet (the apple)"
        ),
        "formula": "Indefinite: en/ett + Noun  |  Definite: Noun + -(e)n / -(e)t",
        "examples": [
            {"swedish": "En man dricker kaffe.", "english": "A man drinks coffee.", "target_highlight": "En man"},
            {"swedish": "Mannen dricker kaffet.", "english": "The man drinks the coffee.", "target_highlight": "Mannen ... kaffet"},
            {"swedish": "Ett tåg kommer nu.", "english": "A train is arriving now.", "target_highlight": "Ett tåg"},
            {"swedish": "Tåget är försenat.", "english": "The train is delayed.", "target_highlight": "Tåget"}
        ],
        "common_pitfalls": [
            "Never say 'den hund' for 'the dog' — the definite article is the suffix 'hunden'.",
            "Always learn new words with their article ('ett bord', not just 'bord')."
        ],
        "exercises": [
            {
                "id": 101,
                "type": "multiple_choice",
                "prompt": "What is the correct definite form of 'ett fönster' (the window)?",
                "options": ["fönstren", "fönstret", "fönsterna", "fönsteret"],
                "correct_answer": "fönstret",
                "explanation": "Nouns of neuter gender ('ett') take the definite ending -et / -t."
            },
            {
                "id": 102,
                "type": "fill_gap",
                "prompt": "Jag har ___ katt som heter Misse. (a/an)",
                "options": ["en", "ett", "den", "det"],
                "correct_answer": "en",
                "explanation": "'Katt' is an utrum noun ('en katt')."
            },
            {
                "id": 103,
                "type": "multiple_choice",
                "prompt": "Convert 'en stol' (a chair) to 'the chair':",
                "options": ["stolen", "stolet", "stolarna", "den stol"],
                "correct_answer": "stolen",
                "explanation": "For en-words ending in a consonant, add '-en'."
            },
            {
                "id": 104,
                "type": "fill_gap",
                "prompt": "Var ligger ___? (the hospital - ett sjukhus)",
                "options": ["sjukhusen", "sjukhuset", "sjukhus", "sjukhusar"],
                "correct_answer": "sjukhuset",
                "explanation": "'Sjukhus' is an ett-word, so definite singular is 'sjukhuset'."
            },
            {
                "id": 105,
                "type": "multiple_choice",
                "prompt": "Which pair is grammatically correct?",
                "options": [
                    "en kvinna – kvinnan",
                    "ett kvinna – kvinnat",
                    "en bord – borden",
                    "ett katt – kattet"
                ],
                "correct_answer": "en kvinna – kvinnan",
                "explanation": "'Kvinna' is an en-word ending in -a, so definite is 'kvinnan'."
            },
            {
                "id": 106,
                "type": "fill_gap",
                "prompt": "Hon dricker ___ glas vatten. (a)",
                "options": ["en", "ett", "den", "det"],
                "correct_answer": "ett",
                "explanation": "'Glas' is a neutrum noun ('ett glas')."
            },
            {
                "id": 107,
                "type": "multiple_choice",
                "prompt": "What is the definite form of 'en tidning' (the newspaper)?",
                "options": ["tidninget", "tidningen", "tidningar", "tidning"],
                "correct_answer": "tidningen",
                "explanation": "Add -en to 'tidning' -> 'tidningen'."
            },
            {
                "id": 108,
                "type": "fill_gap",
                "prompt": "___ sover på mattan. (The dog - en hund)",
                "options": ["Hund", "Hunden", "Hundet", "Hundar"],
                "correct_answer": "Hunden",
                "explanation": "Definite form of 'en hund' is 'hunden'."
            },
            {
                "id": 109,
                "type": "multiple_choice",
                "prompt": "Which of the following is an 'ett'-word?",
                "options": ["bil", "bok", "hus", "flicka"],
                "correct_answer": "hus",
                "explanation": "'Ett hus' is neuter; 'bil', 'bok', 'flicka' are all 'en'-words."
            },
            {
                "id": 110,
                "type": "fill_gap",
                "prompt": "Jag köpte ___ ny jacka. (a)",
                "options": ["en", "ett", "den", "det"],
                "correct_answer": "en",
                "explanation": "'Jacka' is an en-word ('en jacka')."
            }
        ]
    },
    {
        "id": "sv-a1-present-tense-verbs",
        "language": "sv",
        "level": "A1",
        "title": "Present Tense Verbs (Presens)",
        "swedish_title": "Verb i presens (-ar, -er, -r)",
        "summary": "Learn how Swedish verbs work in the present tense: no conjugation by person, just 3 simple patterns.",
        "rule_explanation": (
            "Swedish verbs are refreshingly simple: they DO NOT change by person (jag, du, han, hon, vi, ni, de all share the identical verb form).\n\n"
            "Present tense is formed in three main ways:\n"
            "• Group 1 (-ar): Verbs with infinitive in -a add -r -> tala (to speak) -> talar, fika -> fikar.\n"
            "• Group 2 (-er): Verbs drop -a and add -er -> läsa (to read) -> läser, skriva -> skriver, stänga -> stänger.\n"
            "• Group 3 / Short verbs (-r): Verbs ending in a stressed vowel add -r -> bo (to live) -> bor, gå (to go) -> går, tro (to believe) -> tror."
        ),
        "formula": "Subject + Verb-presens (-ar / -er / -r) + Object",
        "examples": [
            {"swedish": "Jag talar svenska och engelska.", "english": "I speak Swedish and English.", "target_highlight": "talar"},
            {"swedish": "Vi bor i Uppsala nu.", "english": "We live in Uppsala now.", "target_highlight": "bor"},
            {"swedish": "Hon läser en spännande roman.", "english": "She is reading an exciting novel.", "target_highlight": "läser"},
            {"swedish": "De dricker kaffe varje morgon.", "english": "They drink coffee every morning.", "target_highlight": "dricker"}
        ],
        "common_pitfalls": [
            "There is no 'am doing' in Swedish. 'Jag äter' means BOTH 'I eat' and 'I am eating'.",
            "Do not try to conjugate for 'he/she' with an extra -s."
        ],
        "exercises": [
            {
                "id": 111,
                "type": "multiple_choice",
                "prompt": "What is the present tense of 'att arbeta' (to work)?",
                "options": ["arbetar", "arbeter", "arbet", "arbetande"],
                "correct_answer": "arbetar",
                "explanation": "Group 1 verb: arbeta -> arbetar."
            },
            {
                "id": 112,
                "type": "fill_gap",
                "prompt": "Maria ___ i en lägenhet i Göteborg. (lives - bo)",
                "options": ["boer", "bor", "bot", "bo"],
                "correct_answer": "bor",
                "explanation": "Short vowel verb 'bo' adds -r in present -> 'bor'."
            },
            {
                "id": 113,
                "type": "multiple_choice",
                "prompt": "How do you say 'We are writing a letter'?",
                "options": [
                    "Vi är skrivande ett brev",
                    "Vi skriver ett brev",
                    "Vi skrivar ett brev",
                    "Vi skriv ett brev"
                ],
                "correct_answer": "Vi skriver ett brev",
                "explanation": "'Skriva' is Group 2 -> 'skriver'. Swedish doesn't use auxiliary 'är' for continuous action."
            },
            {
                "id": 114,
                "type": "fill_gap",
                "prompt": "Barnen ___ fotboll efter skolan. (play - spela)",
                "options": ["spelar", "speler", "spela", "spelt"],
                "correct_answer": "spelar",
                "explanation": "'Spela' is a Group 1 verb -> 'spelar'."
            },
            {
                "id": 115,
                "type": "multiple_choice",
                "prompt": "Select the correct form for 'De ___ kaffe' (drink - dricka):",
                "options": ["drickar", "dricker", "drick", "drickt"],
                "correct_answer": "dricker",
                "explanation": "'Dricka' takes -er in present -> 'dricker'."
            },
            {
                "id": 116,
                "type": "fill_gap",
                "prompt": "Vad ___ du på helgerna? (do - göra)",
                "options": ["gör", "görar", "görer", "göra"],
                "correct_answer": "gör",
                "explanation": "Present tense of irregular 'göra' is 'gör'."
            },
            {
                "id": 117,
                "type": "multiple_choice",
                "prompt": "Which sentence means 'She understands Swedish'?",
                "options": [
                    "Hon förstår svenska.",
                    "Hon förstå svenska.",
                    "Hon förstårande svenska.",
                    "Hon är förstå svenska."
                ],
                "correct_answer": "Hon förstår svenska.",
                "explanation": "'Förstå' -> 'förstår'."
            },
            {
                "id": 118,
                "type": "fill_gap",
                "prompt": "Tåget ___ klockan åtta. (leaves - avgå)",
                "options": ["avgår", "avgåer", "avgåar", "avgått"],
                "correct_answer": "avgår",
                "explanation": "Compound of 'gå' -> 'avgår'."
            },
            {
                "id": 119,
                "type": "multiple_choice",
                "prompt": "Choose the correct sentence:",
                "options": [
                    "Han lyssnar på musik.",
                    "Han lyssner på musik.",
                    "Han är lyssna på musik.",
                    "Han lyssna på musik."
                ],
                "correct_answer": "Han lyssnar på musik.",
                "explanation": "'Lyssna' is Group 1 -> 'lyssnar'."
            },
            {
                "id": 120,
                "type": "fill_gap",
                "prompt": "Jag ___ kaffe utan socker. (want/like - vill ha)",
                "options": ["vill ha", "villar ha", "vill", "ville ha"],
                "correct_answer": "vill ha",
                "explanation": "'Vill ha' expresses 'want to have'."
            }
        ]
    }
]
