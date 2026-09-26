"""
================================================================================
Swedish CEFR A2 Grammar Topics
================================================================================
Comprehensive, structured A2 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

SWEDISH_A2_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "sv-a2-plural-noun-groups",
        "language": "sv",
        "level": "A2",
        "title": "The 5 Plural Noun Groups",
        "swedish_title": "Substantivens 5 pluralgrupper (-or, -ar, -er, -n, Ø)",
        "summary": "Master the 5 noun declension classes and how each creates indefinite and definite plurals.",
        "rule_explanation": (
            "Swedish nouns are grouped into 5 plural declensions:\n\n"
            "1. Group 1 (-or): en-words ending in -a. (en flicka -> flickor -> flickorna)\n"
            "2. Group 2 (-ar): en-words with 1 syllable or ending in -ing/el/er/en. (en bil -> bilar -> bilarna, en pojke -> pojkar)\n"
            "3. Group 3 (-er): en-words stressed on the final syllable + loanwords + some ett-words. (en katt -> katter -> katterna, en telefon -> telefoner, ett museum -> museer)\n"
            "4. Group 4 (-n): ett-words ending in a vowel. (ett äpple -> äpplen -> äpplena, ett kvitto -> kvitton -> kvittona)\n"
            "5. Group 5 (Zero ending / Ø): ett-words ending in a consonant + en-words ending in -are. (ett hus -> hus -> husen, ett barn -> barn -> barnen, en lärare -> lärare -> lärarna)"
        ),
        "formula": "G1: -or | G2: -ar | G3: -er | G4: -n | G5: Ø (no change in indefinite)",
        "examples": [
            {"swedish": "Två flickor leker i parken.", "english": "Two girls are playing in the park.", "target_highlight": "flickor (G1)"},
            {"swedish": "Tre hundar springer på stranden.", "english": "Three dogs are running on the beach.", "target_highlight": "hundar (G2)"},
            {"swedish": "Fem katter sitter på taket.", "english": "Five cats are sitting on the roof.", "target_highlight": "katter (G3)"},
            {"swedish": "Fyra äpplen ligger i skålen.", "english": "Four apples are in the bowl.", "target_highlight": "äpplen (G4)"},
            {"swedish": "Sex hus byggs i området.", "english": "Six houses are being built in the area.", "target_highlight": "hus (G5)"}
        ],
        "common_pitfalls": [
            "Never add an English '-s' to pluralize Swedish nouns.",
            "Remember that ett-words ending in a consonant (hus, bord, barn, brev) do NOT change in indefinite plural ('ett hus' -> 'tio hus')."
        ],
        "exercises": [
            {
                "id": 201,
                "type": "multiple_choice",
                "prompt": "What is the indefinite plural of 'en klocka' (a watch/clock)?",
                "options": ["klockar", "klockor", "klocker", "klockan"],
                "correct_answer": "klockor",
                "explanation": "Group 1 en-word ending in -a drops -a and adds -or."
            },
            {
                "id": 202,
                "type": "fill_gap",
                "prompt": "Jag ser tre ___ på gatan. (cars - en bil)",
                "options": ["bilar", "bilor", "biler", "bilen"],
                "correct_answer": "bilar",
                "explanation": "'Bil' belongs to Group 2 (-ar)."
            },
            {
                "id": 203,
                "type": "multiple_choice",
                "prompt": "Plural of 'ett barn' (a child -> three children):",
                "options": ["barnar", "barner", "barn", "barnen"],
                "correct_answer": "barn",
                "explanation": "Group 5 neuter noun ending in a consonant has zero ending in indefinite plural."
            },
            {
                "id": 204,
                "type": "fill_gap",
                "prompt": "Vi köpte fem röda ___ i affären. (apples - ett äpple)",
                "options": ["äpplor", "äpplar", "äpplen", "äppler"],
                "correct_answer": "äpplen",
                "explanation": "Group 4 ett-word ending in vowel adds -n."
            },
            {
                "id": 205,
                "type": "multiple_choice",
                "prompt": "Which word belongs to Group 3 (-er)?",
                "options": ["en flicka", "en hund", "en katt", "ett hus"],
                "correct_answer": "en katt",
                "explanation": "'Katt' takes -er -> 'katter'."
            },
            {
                "id": 206,
                "type": "fill_gap",
                "prompt": "Hon talar med flera ___. (teachers - en lärare)",
                "options": ["lärare", "läraror", "läraren", "lärarar"],
                "correct_answer": "lärare",
                "explanation": "En-words ending in -are remain unchanged in indefinite plural."
            },
            {
                "id": 207,
                "type": "multiple_choice",
                "prompt": "What is the definite plural form of 'ett hus' (the houses)?",
                "options": ["husen", "husena", "huserna", "husarna"],
                "correct_answer": "husen",
                "explanation": "Group 5 ett-words form definite plural by adding -en -> 'husen'."
            },
            {
                "id": 208,
                "type": "fill_gap",
                "prompt": "Det finns många ___ i biblioteket. (books - en bok)",
                "options": ["böcker", "bokar", "bokor", "boker"],
                "correct_answer": "böcker",
                "explanation": "Irregular Group 3 noun with vowel change: bok -> böcker."
            },
            {
                "id": 209,
                "type": "multiple_choice",
                "prompt": "Plural form of 'ett frimärke' (a stamp):",
                "options": ["frimärkor", "frimärken", "frimärkar", "frimärker"],
                "correct_answer": "frimärken",
                "explanation": "Group 4: ett-word ending in vowel -> frimärken."
            },
            {
                "id": 210,
                "type": "fill_gap",
                "prompt": "___ leker i trädgården. (The girls - en flicka)",
                "options": ["Flickorna", "Flickarna", "Flickerna", "Flickan"],
                "correct_answer": "Flickorna",
                "explanation": "Definite plural of Group 1 is -orna -> 'Flickorna'."
            }
        ]
    },
    {
        "id": "sv-a2-past-tense-preteritum-supinum",
        "language": "sv",
        "level": "A2",
        "title": "Past Tense (Preteritum vs. Supinum)",
        "swedish_title": "Dåtid: Preteritum och Supinum (har gjort)",
        "summary": "Understand when to use preteritum (-de/-te) for finished moments vs. supinum (-t) with 'har/hade'.",
        "rule_explanation": (
            "Swedish expresses the past through two primary tenses:\n\n"
            "1. Preteritum (Simple Past): Used for finished actions at a specific time in the past (igår, förra veckan, 2018).\n"
            "   • Group 1: -ade (pratade, arbetade)\n"
            "   • Group 2a: -de (ringde, stängde)\n"
            "   • Group 2b (after p, t, k, s): -te (läste, köpte)\n"
            "   • Group 4 (Strong/Irregular): vowel shift (skrev, åt, drack, gick)\n\n"
            "2. Perfekt (har + Supinum): Used for life experience, unfinished time, or present results.\n"
            "   • Regular supinum ends in -t: har pratat, har ringt, har läst, har skrivit, har ätit."
        ),
        "formula": "Preteritum: Verb + -de/-te | Perfekt: har + Supinum (-t / -it)",
        "examples": [
            {"swedish": "Igår pratade jag med min chef.", "english": "Yesterday I spoke with my boss.", "target_highlight": "pratade"},
            {"swedish": "Jag har redan pratat med honom.", "english": "I have already spoken with him.", "target_highlight": "har redan pratat"},
            {"swedish": "Förra året köpte vi ett hus.", "english": "Last year we bought a house.", "target_highlight": "köpte"},
            {"swedish": "Har du ätit lunch ännu?", "english": "Have you eaten lunch yet?", "target_highlight": "Har ... ätit"}
        ],
        "common_pitfalls": [
            "Do NOT confuse the participle form with the supinum. Swedish has a special verbal form called 'supinum' ending in -t (har ätit, har skrivit).",
            "Never use 'har' with a specific finished time: 'Igår har jag ätit' is WRONG -> 'Igår åt jag'."
        ],
        "exercises": [
            {
                "id": 211,
                "type": "multiple_choice",
                "prompt": "Which sentence correctly describes an action yesterday?",
                "options": [
                    "Igår köpte jag en ny dator.",
                    "Igår har jag köpt en ny dator.",
                    "Igår köpt jag en ny dator.",
                    "Igår köpade jag en ny dator."
                ],
                "correct_answer": "Igår köpte jag en ny dator.",
                "explanation": "With 'igår', use Preteritum ('köpte')."
            },
            {
                "id": 212,
                "type": "fill_gap",
                "prompt": "Har du någonsin ___ till Island? (traveled - resa)",
                "options": ["rest", "reste", "resat", "resade"],
                "correct_answer": "rest",
                "explanation": "Supinum of 'resa' is 'rest' (har rest)."
            },
            {
                "id": 213,
                "type": "multiple_choice",
                "prompt": "Preteritum of 'att skriva' (to write):",
                "options": ["skrivade", "skrev", "skrivit", "skrivte"],
                "correct_answer": "skrev",
                "explanation": "Strong verb with vowel change: skriva -> skrev -> skrivit."
            },
            {
                "id": 214,
                "type": "fill_gap",
                "prompt": "I morse ___ jag två koppar te. (drank - dricka)",
                "options": ["drack", "drickade", "druckit", "drickte"],
                "correct_answer": "drack",
                "explanation": "Preteritum of 'dricka' is 'drack'."
            },
            {
                "id": 215,
                "type": "multiple_choice",
                "prompt": "What is the supinum of 'att äta' (to eat)?",
                "options": ["åt", "ätit", "ätat", "ätde"],
                "correct_answer": "ätit",
                "explanation": "Strong verb: äta -> åt -> ätit."
            },
            {
                "id": 216,
                "type": "fill_gap",
                "prompt": "Vi ___ film hela kvällen igår. (watched - titta)",
                "options": ["tittade", "tittat", "titte", "tittar"],
                "correct_answer": "tittade",
                "explanation": "Group 1 preteritum ending is -ade -> 'tittade'."
            },
            {
                "id": 217,
                "type": "multiple_choice",
                "prompt": "Which sentence means 'I have lived in Sweden for two years'?",
                "options": [
                    "Jag har bott i Sverige i två år.",
                    "Jag bodde i Sverige i två år sedan.",
                    "Jag är bott i Sverige i två år.",
                    "Jag har bor i Sverige i två år."
                ],
                "correct_answer": "Jag har bott i Sverige i två år.",
                "explanation": "Use 'har bott' (perfekt) for duration continuing to the present."
            },
            {
                "id": 218,
                "type": "fill_gap",
                "prompt": "Han ___ boken på bordet för en timme sedan. (placed/laid - lägga)",
                "options": ["lade", "lagt", "läggade", "ligger"],
                "correct_answer": "lade",
                "explanation": "Preteritum of 'lägga' is 'lade' (or 'la')."
            },
            {
                "id": 219,
                "type": "multiple_choice",
                "prompt": "Supinum of 'att gå' (to go/walk):",
                "options": ["gick", "gått", "gåat", "gånget"],
                "correct_answer": "gått",
                "explanation": "Gå -> gick -> gått."
            },
            {
                "id": 220,
                "type": "fill_gap",
                "prompt": "De har redan ___ brevet. (sent - skicka)",
                "options": ["skickat", "skickade", "skickte", "skicka"],
                "correct_answer": "skickat",
                "explanation": "Group 1 supinum is -at -> 'skickat'."
            }
        ]
    }
]
