"""
================================================================================
Swedish CEFR B1 Grammar Topics
================================================================================
Comprehensive, structured B1 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

SWEDISH_B1_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "sv-b1-v2-inversion",
        "language": "sv",
        "level": "B1",
        "title": "V2 Word Order & Fronted Inversion",
        "swedish_title": "V2-regeln och omvänd ordföljd (Inversion)",
        "summary": "The fundamental law of Scandinavian syntax: the finite verb is ALWAYS the 2nd grammatical constituent in main clauses.",
        "rule_explanation": (
            "In Swedish main clauses (huvudsats), the finite verb MUST be in position 2.\n\n"
            "1. Normal SVO order:\n"
            "   [Subject (1)] + [Verb (2)] + [Object/Time (3)]\n"
            "   'Jag (1) köpte (2) en bil igår.'\n\n"
            "2. Inverted order (Spetsställning / Fronting):\n"
            "   When any element other than the subject begins the sentence (Time, Place, Object, Adverb), the subject moves immediately AFTER the verb to preserve position 2 for the verb:\n"
            "   [Fundament/Fronted element (1)] + [Verb (2)] + [Subject (3)] + ...\n"
            "   'Igår (1) köpte (2) jag (3) en bil.'\n"
            "   'I Sverige (1) dricker (2) man (3) mycket kaffe.'\n"
            "   'Den där boken (1) har (2) jag (3) redan läst.'"
        ),
        "formula": "[Fundament / Time / Place (1)] + [Finite Verb (2)] + [Subject (3)] + [Satsadverbial] + [Infinite Verb] + [Object]",
        "examples": [
            {"swedish": "På måndag börjar jag min nya kurs.", "english": "On Monday I start my new course.", "target_highlight": "börjar jag"},
            {"swedish": "Ibland dricker vi te på eftermiddagen.", "english": "Sometimes we drink tea in the afternoon.", "target_highlight": "dricker vi"},
            {"swedish": "Efter jobbet åkte han hem.", "english": "After work he went home.", "target_highlight": "åkte han"},
            {"swedish": "Tyvärr kan vi inte komma ikväll.", "english": "Unfortunately we cannot come tonight.", "target_highlight": "kan vi inte"}
        ],
        "common_pitfalls": [
            "NEVER say 'På måndag jag börjar...' or 'Igår jag åt...' (direct English calque).",
            "Sentence adverbs ('inte', 'kanske', 'alltid') in main clauses follow the subject in inverted sentences: 'Igår åt jag inte frukost'."
        ],
        "exercises": [
            {
                "id": 301,
                "type": "multiple_choice",
                "prompt": "Which sentence correctly demonstrates the Swedish V2 rule?",
                "options": [
                    "Förra veckan vi reste till Malmö.",
                    "Förra veckan reste vi till Malmö.",
                    "Förra veckan reste till Malmö vi.",
                    "Vi förra veckan reste till Malmö."
                ],
                "correct_answer": "Förra veckan reste vi till Malmö.",
                "explanation": "Because 'Förra veckan' occupies position 1, verb 'reste' must be in position 2, followed by subject 'vi'."
            },
            {
                "id": 302,
                "type": "fill_gap",
                "prompt": "Imorgon ___ vi på bio. (are going - gå)",
                "options": ["går", "vi går", "är gående", "gångar"],
                "correct_answer": "går",
                "explanation": "'Imorgon' (1) + 'går' (2) + 'vi' (3)."
            },
            {
                "id": 303,
                "type": "multiple_choice",
                "prompt": "Arrange: 'I Stockholm / bor / min bror' starting with the place adverbial:",
                "options": [
                    "I Stockholm bor min bror.",
                    "I Stockholm min bror bor.",
                    "Min bror i Stockholm bor.",
                    "Bor i Stockholm min bror."
                ],
                "correct_answer": "I Stockholm bor min bror.",
                "explanation": "Place fundament triggers V2 inversion: 'I Stockholm' (1) + 'bor' (2) + 'min bror' (3)."
            },
            {
                "id": 304,
                "type": "fill_gap",
                "prompt": "Nu ___ jag trött. (am - vara)",
                "options": ["är", "jag är", "vara", "blir"],
                "correct_answer": "är",
                "explanation": "'Nu' (1) + 'är' (2) + 'jag' (3)."
            },
            {
                "id": 305,
                "type": "multiple_choice",
                "prompt": "Where does 'inte' go in the inverted sentence: 'Igår drack [1] Erik [2] kaffe [3]'?",
                "options": [
                    "Position 2 (Igår drack Erik inte kaffe)",
                    "Position 1 (Igår inte drack Erik kaffe)",
                    "Position 3 (Igår drack Erik kaffe inte)",
                    "Before Igår (Inte igår drack Erik kaffe)"
                ],
                "correct_answer": "Position 2 (Igår drack Erik inte kaffe)",
                "explanation": "In inverted main clauses, 'inte' is placed after the subject: Verb + Subject + Satsadverbial."
            },
            {
                "id": 306,
                "type": "fill_gap",
                "prompt": "Därför ___ hon inte i mötet. (participated - delta)",
                "options": ["deltog", "hon deltog", "deltog hon", "har deltagit"],
                "correct_answer": "deltog",
                "explanation": "Fronted 'Därför' (1) requires verb 'deltog' in position 2."
            },
            {
                "id": 307,
                "type": "multiple_choice",
                "prompt": "Identify the INCORRECT sentence:",
                "options": [
                    "Plötsligt började det regna.",
                    "Klockan fem slutar jag arbeta.",
                    "Ibland jag glömmer mina nycklar.",
                    "Här trivs vi väldigt bra."
                ],
                "correct_answer": "Ibland jag glömmer mina nycklar.",
                "explanation": "Incorrect V2 order! It must be 'Ibland glömmer jag mina nycklar'."
            },
            {
                "id": 308,
                "type": "fill_gap",
                "prompt": "Om två timmar ___ tåget. (arrives - ankomma)",
                "options": ["ankommer", "tåget ankommer", "ankommer tåget", "ska ankomma"],
                "correct_answer": "ankommer",
                "explanation": "Time phrase occupies fundament (1), so 'ankommer' is in position 2."
            },
            {
                "id": 309,
                "type": "multiple_choice",
                "prompt": "Which sentence has correct word order with a modal verb?",
                "options": [
                    "Ikväll kan vi titta på film.",
                    "Ikväll vi kan titta på film.",
                    "Ikväll kan titta vi på film.",
                    "Kan ikväll vi titta på film."
                ],
                "correct_answer": "Ikväll kan vi titta på film.",
                "explanation": "Fronted 'Ikväll' (1) + modal verb 'kan' (2) + subject 'vi' (3) + main verb 'titta' (4)."
            },
            {
                "id": 310,
                "type": "fill_gap",
                "prompt": "På sommaren ___ många turister till Gotland. (travel - resa)",
                "options": ["reser", "många reser", "reser många", "reste"],
                "correct_answer": "reser",
                "explanation": "Fundament 'På sommaren' (1) + verb 'reser' (2) + subject 'många turister' (3)."
            }
        ]
    },
    {
        "id": "sv-b1-biff-subordinate-clauses",
        "language": "sv",
        "level": "B1",
        "title": "The BIFF Rule (Bisatsordföljd)",
        "swedish_title": "BIFF-regeln (I Bisats kommer Inte Före Finita verbet)",
        "summary": "Master the placement of negation and adverbs (inte, alltid, aldrig) in Swedish subordinate clauses.",
        "rule_explanation": (
            "The BIFF rule is the most famous Swedish grammar acronym:\n"
            "• B = Bisats (Subordinate clause starting with att, eftersom, när, om, medan, fastän...)\n"
            "• I = Inte (or other sentence adverbs like alltid, aldrig, ofta, kanske)\n"
            "• F = Före (Before)\n"
            "• F = Finita verbet (The finite verb)\n\n"
            "Compare the syntax:\n"
            "1. Huvudsats (Main clause): Verb comes BEFORE 'inte':\n"
            "   'Han kommer inte idag.'\n"
            "2. Bisats (Subordinate clause): 'inte' comes BEFORE the verb:\n"
            "   '...eftersom han inte kommer idag.'\n"
            "   'Jag vet att hon alltid dricker te.'"
        ),
        "formula": "[Subjunktion (att/eftersom/om/när)] + [Subject] + [INTE / SATSADVERBIAL] + [Finite Verb] + [Rest]",
        "examples": [
            {"swedish": "Jag stannar hemma eftersom jag inte mår bra.", "english": "I stay home because I don't feel well.", "target_highlight": "inte mår"},
            {"swedish": "Hon undrar om han alltid är så punktlig.", "english": "She wonders if he is always so punctual.", "target_highlight": "alltid är"},
            {"swedish": "Vi visste att de aldrig hade varit i Norge.", "english": "We knew that they had never been to Norway.", "target_highlight": "aldrig hade varit"},
            {"swedish": "Om du inte vill följa med, behöver du inte.", "english": "If you don't want to come along, you don't have to.", "target_highlight": "inte vill"}
        ],
        "common_pitfalls": [
            "Never use main clause word order inside a subordinate clause: say 'eftersom jag inte förstår', NOT 'eftersom jag förstår inte'.",
            "When the subordinate clause is placed FIRST, the following main clause MUST invert by V2: 'Eftersom det regnar (1), stannar (2) vi (3) hemma'."
        ],
        "exercises": [
            {
                "id": 311,
                "type": "multiple_choice",
                "prompt": "Which subordinate clause follows the BIFF rule?",
                "options": [
                    "...eftersom jag kan inte simma.",
                    "...eftersom jag inte kan simma.",
                    "...eftersom kan jag inte simma.",
                    "...eftersom inte jag kan simma."
                ],
                "correct_answer": "...eftersom jag inte kan simma.",
                "explanation": "BIFF rule: in a bisats, 'inte' must come BEFORE the finite verb 'kan'."
            },
            {
                "id": 312,
                "type": "fill_gap",
                "prompt": "Jag vet att hon ___ kaffe. (never drinks - aldrig dricker)",
                "options": ["aldrig dricker", "dricker aldrig", "inte dricker aldrig", "dricker inte"],
                "correct_answer": "aldrig dricker",
                "explanation": "In bisats ('att...'), adverb 'aldrig' precedes finite verb 'dricker'."
            },
            {
                "id": 313,
                "type": "multiple_choice",
                "prompt": "Complete the sentence with correct main clause order after a bisats: 'Eftersom bussen var sen, ___ för sent till jobbet.'",
                "options": [
                    "jag kom",
                    "kom jag",
                    "jag har kommit",
                    "kommit jag"
                ],
                "correct_answer": "kom jag",
                "explanation": "The introductory subordinate clause acts as fundament (position 1), so main clause inverts: 'kom' (2) + 'jag' (3)."
            },
            {
                "id": 314,
                "type": "fill_gap",
                "prompt": "Han frågade om vi ___ tid imorgon. (don't have - inte har)",
                "options": ["inte har", "har inte", "har", "inte hade"],
                "correct_answer": "inte har",
                "explanation": "BIFF: 'om' + 'vi' + 'inte' + 'har'."
            },
            {
                "id": 315,
                "type": "multiple_choice",
                "prompt": "Transform to subordinate clause: 'De bor inte här' -> 'Jag tror att...'",
                "options": [
                    "Jag tror att de inte bor här.",
                    "Jag tror att de bor inte här.",
                    "Jag tror att inte de bor här.",
                    "Jag tror att bor de inte här."
                ],
                "correct_answer": "Jag tror att de inte bor här.",
                "explanation": "Subject 'de' + 'inte' + verb 'bor'."
            },
            {
                "id": 316,
                "type": "fill_gap",
                "prompt": "Hon stannar inne när det ___ snöar. (not - inte)",
                "options": ["inte", "snöar inte", "är inte", "inte snöar"],
                "correct_answer": "inte",
                "explanation": "'När det inte snöar' satisfies the BIFF rule."
            },
            {
                "id": 317,
                "type": "multiple_choice",
                "prompt": "Which sentence contains an error?",
                "options": [
                    "Jag vet att du alltid hjälper mig.",
                    "Hon sa att han förstår inte frågan.",
                    "Om du inte ringer, blir jag orolig.",
                    "Vi stannar eftersom vi gärna vill prata."
                ],
                "correct_answer": "Hon sa att han förstår inte frågan.",
                "explanation": "BIFF violation! It must be 'att han inte förstår frågan'."
            },
            {
                "id": 318,
                "type": "fill_gap",
                "prompt": "Vi undrar varför ni ___ på festen igår. (were not - inte var)",
                "options": ["inte var", "var inte", "vore inte", "inte vore"],
                "correct_answer": "inte var",
                "explanation": "Interrogative bisats: 'varför ni inte var...'."
            },
            {
                "id": 319,
                "type": "multiple_choice",
                "prompt": "Choose the correct sentence with 'alltid':",
                "options": [
                    "Hon berättade att hon alltid stiger upp tidigt.",
                    "Hon berättade att hon stiger alltid upp tidigt.",
                    "Hon berättade alltid att hon stiger upp tidigt.",
                    "Hon berättade att alltid hon stiger upp tidigt."
                ],
                "correct_answer": "Hon berättade att hon alltid stiger upp tidigt.",
                "explanation": "In bisats, 'alltid' comes before finite verb 'stiger'."
            },
            {
                "id": 320,
                "type": "fill_gap",
                "prompt": "När vi ___ hungriga längre, går vi ut. (are not - inte är)",
                "options": ["inte är", "är inte", "var inte", "blir inte"],
                "correct_answer": "inte är",
                "explanation": "BIFF in time clause: 'när vi inte är hungriga'."
            }
        ]
    }
]
