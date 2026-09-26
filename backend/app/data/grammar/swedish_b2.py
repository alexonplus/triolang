"""
================================================================================
Swedish CEFR B2 Grammar Topics
================================================================================
Comprehensive, structured B2 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

SWEDISH_B2_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "sv-b2-passive-voice",
        "language": "sv",
        "level": "B2",
        "title": "Passive Voice (S-passiv & Bli-passiv)",
        "swedish_title": "Passiv form: S-passiv och Bli-passiv",
        "summary": "Master the morphological s-passive and periphrastic bli-passive used in news, regulations, and formal Swedish.",
        "rule_explanation": (
            "Swedish offers two main passive constructions:\n\n"
            "1. S-passiv (Morphological suffix -s):\n"
            "   Formed by attaching '-s' directly to the verb stem/ending:\n"
            "   • Presens: säljer -> säljs / säljes (is sold), öppnar -> öppnas (is opened)\n"
            "   • Preteritum: byggde -> byggdes (was built), skrev -> skrevs (was written)\n"
            "   • Supinum: har byggt -> har byggts (has been built)\n"
            "   • Infinitiv: att renovera -> att renoveras (to be renovated)\n\n"
            "2. Bli-passiv (bli + Perfekt Particip):\n"
            "   Used when emphasizing dynamic events, changes of state, or personal impact:\n"
            "   • 'Bilen blev reparerad av en mekaniker.'\n"
            "   • 'Patienten blev inlagd på sjukhuset.'"
        ),
        "formula": "S-passiv: Verb + -s  |  Bli-passiv: bli/blev + Perfekt Particip (-d/-t/-da)",
        "examples": [
            {"swedish": "Dörrarna öppnas automatiskt.", "english": "The doors are opened automatically.", "target_highlight": "öppnas"},
            {"swedish": "Bron byggdes på 1800-talet.", "english": "The bridge was built in the 19th century.", "target_highlight": "byggdes"},
            {"swedish": "Många hus har förstörts i branden.", "english": "Many houses have been destroyed in the fire.", "target_highlight": "har förstörts"},
            {"swedish": "Han blev vald till ordförande.", "english": "He was elected chairman.", "target_highlight": "blev vald"}
        ],
        "common_pitfalls": [
            "Do not confuse S-passive with deponent verbs ('hoppas', 'andas', 'minnas') which end in -s but have active meaning.",
            "Do not confuse with reciprocal verbs ('vi ses' = we see each other, 'vi hörs' = we'll hear from each other)."
        ],
        "exercises": [
            {
                "id": 401,
                "type": "multiple_choice",
                "prompt": "Convert to s-passive: 'Astrid Lindgren skrev boken 1945' -> 'Boken ___ 1945 av Astrid Lindgren.'",
                "options": [
                    "skrevs",
                    "skrivs",
                    "blev skriva",
                    "skrev"
                ],
                "correct_answer": "skrevs",
                "explanation": "Preteritum s-passive of 'skriva' is 'skrevs'."
            },
            {
                "id": 402,
                "type": "fill_gap",
                "prompt": "Svenska ___ i både Sverige och Finland. (is spoken - tala)",
                "options": ["talas", "talar", "blev talat", "talades"],
                "correct_answer": "talas",
                "explanation": "Present tense s-passive of 'tala' is 'talas'."
            },
            {
                "id": 403,
                "type": "multiple_choice",
                "prompt": "What is the supinum passive form for 'att bygga' (has been built)?",
                "options": ["har byggts", "har byggtsade", "har blivit bygg", "har byggdes"],
                "correct_answer": "har byggts",
                "explanation": "Supinum 'byggt' + 's' -> 'har byggts'."
            },
            {
                "id": 404,
                "type": "fill_gap",
                "prompt": "Huset ___ av en berömd arkitekt 1920. (was designed - rita)",
                "options": ["ritades", "ritas", "ritar", "blev rita"],
                "correct_answer": "ritades",
                "explanation": "Past tense passive of 'rita' is 'ritades'."
            },
            {
                "id": 405,
                "type": "multiple_choice",
                "prompt": "Which sentence uses 'bli-passiv' correctly?",
                "options": [
                    "Bilen blev stulen under natten.",
                    "Bilen blev stjäla under natten.",
                    "Bilen blev stulit under natten.",
                    "Bilen blev stals under natten."
                ],
                "correct_answer": "Bilen blev stulen under natten.",
                "explanation": "'Stulen' agrees with en-word 'bilen' (en bil -> stulen)."
            },
            {
                "id": 406,
                "type": "fill_gap",
                "prompt": "Affären ___ klockan 20:00 varje kväll. (is closed - stänga)",
                "options": ["stängs", "stängdes", "stänger", "blir stäng"],
                "correct_answer": "stängs",
                "explanation": "Present passive of 'stänga' is 'stängs'."
            },
            {
                "id": 407,
                "type": "multiple_choice",
                "prompt": "Identify the deponent verb (looks passive with -s, but is active in meaning):",
                "options": ["säljs", "hoppas", "byggdes", "skrivs"],
                "correct_answer": "hoppas",
                "explanation": "'Hoppas' (to hope) is a deponent verb with active meaning."
            },
            {
                "id": 408,
                "type": "fill_gap",
                "prompt": "Rapporten måste ___ före fredag. (be submitted - lämna in)",
                "options": ["lämnas in", "lämnade in", "lämnar in", "bli lämna in"],
                "correct_answer": "lämnas in",
                "explanation": "Infinitive passive with modal 'måste': 'lämnas in'."
            },
            {
                "id": 409,
                "type": "multiple_choice",
                "prompt": "Convert 'Man måste betala skatt' into passive:",
                "options": [
                    "Skatt måste betalas.",
                    "Skatt måste betala.",
                    "Skatt blir betalade.",
                    "Skatt har betalats."
                ],
                "correct_answer": "Skatt måste betalas.",
                "explanation": "Infinitive passive: 'betalas'."
            },
            {
                "id": 410,
                "type": "fill_gap",
                "prompt": "Beslutet ___ av styrelsen igår. (was made - fatta)",
                "options": ["fattades", "fattas", "fatta", "har fattats"],
                "correct_answer": "fattades",
                "explanation": "Preteritum passive of 'fatta' is 'fattades'."
            }
        ]
    },
    {
        "id": "sv-b2-partikelverb",
        "language": "sv",
        "level": "B2",
        "title": "Particle Verbs (Partikelverb & Stress)",
        "swedish_title": "Partikelverb och betoningsregler",
        "summary": "Learn the vital distinction between prepositional verbs and particle verbs where the stress falls on the particle.",
        "rule_explanation": (
            "Swedish particle verbs (partikelverb) consist of a verb + a stressed particle (adverb/preposition).\n\n"
            "• Pronunciation Rule: In a particle verb, the STRESS ALWAYS falls on the particle, NOT the verb!\n"
            "  - 'tycker OM' (to like) vs. 'TYCKER om' (to have an opinion about)\n"
            "  - 'håller MED' (to agree) vs. 'HÅLLER med' (to hold with)\n"
            "  - 'lägger AV' (to quit/stop) vs. 'LÄGGER av' (to lay off)\n"
            "  - 'ger UPP' (to give up)\n\n"
            "• Word Order: The particle generally stays right next to the verb in main and subordinate clauses."
        ),
        "formula": "Verb + STRESSED PARTICLE (om / upp / av / på / till / ut / in / igen)",
        "examples": [
            {"swedish": "Jag tycker mycket om svensk musik.", "english": "I like Swedish music very much.", "target_highlight": "tycker om"},
            {"swedish": "Hon gav inte upp trots svårigheterna.", "english": "She did not give up despite the difficulties.", "target_highlight": "gav upp"},
            {"swedish": "Vi måste ställa in mötet imorgon.", "english": "We have to cancel the meeting tomorrow.", "target_highlight": "ställa in (cancel)"},
            {"swedish": "Han känner igen sin gamla lärare.", "english": "He recognizes his old teacher.", "target_highlight": "känner igen"}
        ],
        "common_pitfalls": [
            "Do not confuse 'ställa in' (to cancel) with 'ställa om' (to adjust/switch) or 'ställa upp' (to participate/help).",
            "Remember that stressing the wrong word completely alters the meaning."
        ],
        "exercises": [
            {
                "id": 411,
                "type": "multiple_choice",
                "prompt": "Which particle verb means 'to cancel a meeting'?",
                "options": ["ställa upp", "ställa in", "ställa om", "ställa av"],
                "correct_answer": "ställa in",
                "explanation": "'Ställa in' means to cancel."
            },
            {
                "id": 412,
                "type": "fill_gap",
                "prompt": "Jag håller ___ med dig fullständigt. (agree with you - med)",
                "options": ["med", "om", "på", "av"],
                "correct_answer": "med",
                "explanation": "'Hålla med' means to agree with someone."
            },
            {
                "id": 413,
                "type": "multiple_choice",
                "prompt": "What does 'att ge upp' mean?",
                "options": ["to give up / surrender", "to give away", "to give back", "to invent"],
                "correct_answer": "to give up / surrender",
                "explanation": "'Ge upp' means to surrender or abandon efforts."
            },
            {
                "id": 414,
                "type": "fill_gap",
                "prompt": "Kan du stänga ___ teven, tack? (turn off - av)",
                "options": ["av", "på", "ut", "om"],
                "correct_answer": "av",
                "explanation": "'Stänga av' means to switch/turn off."
            },
            {
                "id": 415,
                "type": "multiple_choice",
                "prompt": "In the sentence 'Jag tycker om kaffe', where is the phonetic stress?",
                "options": ["On 'om'", "On 'tycker'", "On 'jag'", "On 'kaffe' only"],
                "correct_answer": "On 'om'",
                "explanation": "In particle verbs, the stress is always placed on the particle ('om')."
            },
            {
                "id": 416,
                "type": "fill_gap",
                "prompt": "När går tåget ___? (leaves/departs - iväg)",
                "options": ["iväg", "av", "om", "till"],
                "correct_answer": "iväg",
                "explanation": "'Gå iväg' means to leave or depart."
            },
            {
                "id": 417,
                "type": "multiple_choice",
                "prompt": "'Att känna igen någon' means:",
                "options": [
                    "To recognize someone",
                    "To feel sorry for someone",
                    "To ignore someone",
                    "To introduce someone"
                ],
                "correct_answer": "To recognize someone",
                "explanation": "'Känna igen' is the particle verb for recognizing someone/something."
            },
            {
                "id": 418,
                "type": "fill_gap",
                "prompt": "Hon kom ___ en lysande idé! (came up with - på)",
                "options": ["på", "om", "upp", "in"],
                "correct_answer": "på",
                "explanation": "'Komma på' means to come up with or remember an idea."
            },
            {
                "id": 419,
                "type": "multiple_choice",
                "prompt": "What does 'att gå under' mean in Swedish?",
                "options": [
                    "To perish / collapse / sink",
                    "To take a walk below",
                    "To succeed",
                    "To continue"
                ],
                "correct_answer": "To perish / collapse / sink",
                "explanation": "'Gå under' means to collapse, perish, or sink."
            },
            {
                "id": 420,
                "type": "fill_gap",
                "prompt": "Vi måste se ___ för hala vägar. (watch out for - upp)",
                "options": ["upp", "ut", "på", "om"],
                "correct_answer": "upp",
                "explanation": "'Se upp' means watch out / beware."
            }
        ]
    }
]
