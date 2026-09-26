"""
================================================================================
Swedish CEFR C1 Grammar Topics
================================================================================
Comprehensive, structured C1 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

SWEDISH_C1_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "sv-c1-conditional-inversion",
        "language": "sv",
        "level": "C1",
        "title": "Stylistic Conditional Inversion (Villkorsinversion)",
        "swedish_title": "Omvänd ordföljd i villkorssatser (Utan 'om')",
        "summary": "Master high-register, academic, and literary conditional structures that omit the subjunction 'om'.",
        "rule_explanation": (
            "In advanced, formal, legal, and literary Swedish, hypothetical and conditional clauses often omit the subjunction 'om' (if) and invert the word order by placing the finite verb in the initial position.\n\n"
            "• Standard B1/B2 form (with 'om'):\n"
            "  'Om jag hade vetat detta tidigare, skulle jag inte ha godkänt förslaget.'\n\n"
            "• Advanced C1 Inverted form (without 'om'):\n"
            "  'Hade jag vetat detta tidigare, skulle jag inte ha godkänt förslaget.'\n\n"
            "• Present / Future Conditional:\n"
            "  'Skulle du behöva ytterligare information, står vi gärna till tjänst.' (Should you need...)\n\n"
            "• Subjunctive form with 'vore':\n"
            "  'Vore det inte för din insats, hade projektet havererat.' (Were it not for...)"
        ),
        "formula": "[Finite / Auxiliary Verb] + [Subject] + [Rest of Condition], [Main Clause with Inversion: Modal/Aux + Subject + ...]",
        "examples": [
            {"swedish": "Hade vi anlänt i tid, hade vi hunnit med flyget.", "english": "Had we arrived on time, we would have caught the flight.", "target_highlight": "Hade vi anlänt"},
            {"swedish": "Skulle problem uppstå, var god kontakta ledningen.", "english": "Should problems arise, please contact management.", "target_highlight": "Skulle problem uppstå"},
            {"swedish": "Vore jag i dina kläder, skulle jag tacka ja direkt.", "english": "Were I in your shoes, I would accept immediately.", "target_highlight": "Vore jag"},
            {"swedish": "Finge jag önska fritt, valde jag detta alternativ.", "english": "Could I wish freely, I would choose this option.", "target_highlight": "Finge jag"}
        ],
        "common_pitfalls": [
            "Do NOT write 'Om hade jag vetat...' (combining 'om' and inversion is ungrammatical).",
            "Ensure the main clause following the inverted condition still obeys the V2 rule."
        ],
        "exercises": [
            {
                "id": 501,
                "type": "multiple_choice",
                "prompt": "Transform 'Om du vill veta mer, ring oss' into formal C1 inverted Swedish:",
                "options": [
                    "Vill du veta mer, ring oss.",
                    "Du vill veta mer, ring oss.",
                    "Om vill du veta mer, ring oss.",
                    "Veta mer vill du, ring oss."
                ],
                "correct_answer": "Vill du veta mer, ring oss.",
                "explanation": "Omitting 'om' triggers verb-first positioning ('Vill du veta mer...')."
            },
            {
                "id": 502,
                "type": "fill_gap",
                "prompt": "___ det inte för regnet, hade vi haft picknick. (Were it not - Vore)",
                "options": ["Vore", "Om vore", "Var", "Hade varit"],
                "correct_answer": "Vore",
                "explanation": "'Vore det inte...' is the subjunctive conditional inversion of 'att vara'."
            },
            {
                "id": 503,
                "type": "multiple_choice",
                "prompt": "Which sentence demonstrates proper C1 conditional inversion?",
                "options": [
                    "Hade jag haft mer resurser, skulle jag ha expanderat verksamheten.",
                    "Hade jag hade mer resurser, skulle jag expanderat verksamheten.",
                    "Om hade jag haft mer resurser, skulle jag ha expanderat verksamheten.",
                    "Jag hade haft mer resurser, skulle jag ha expanderat verksamheten."
                ],
                "correct_answer": "Hade jag haft mer resurser, skulle jag ha expanderat verksamheten.",
                "explanation": "Past perfect conditional inversion: 'Hade jag haft...'."
            },
            {
                "id": 504,
                "type": "fill_gap",
                "prompt": "___ du ha några frågor, tveka inte att höra av dig. (Should you have - Skulle)",
                "options": ["Skulle", "Om skulle", "Vill", "Måste"],
                "correct_answer": "Skulle",
                "explanation": "'Skulle du ha...' translates to formal 'Should you have...'."
            },
            {
                "id": 505,
                "type": "multiple_choice",
                "prompt": "What does 'Finge jag bestämma...' express in Swedish?",
                "options": [
                    "Hypothetical wish / conditional (If I were allowed to decide...)",
                    "A factual statement about past decisions",
                    "A direct imperative command",
                    "A future prediction"
                ],
                "correct_answer": "Hypothetical wish / conditional (If I were allowed to decide...)",
                "explanation": "'Finge' is the archaic/formal subjunctive of 'få' used in hypothetical conditions."
            },
            {
                "id": 506,
                "type": "fill_gap",
                "prompt": "Visste jag svaret, ___ jag berätta det för dig. (would - skulle)",
                "options": ["skulle", "jag skulle", "vill", "kunde jag inte"],
                "correct_answer": "skulle",
                "explanation": "Main clause following the inverted conditional clause places auxiliary 'skulle' in position 2."
            },
            {
                "id": 507,
                "type": "multiple_choice",
                "prompt": "Identify the ungrammatical sentence:",
                "options": [
                    "Om hade vi förstått konsekvenserna, hade vi agerat annorlunda.",
                    "Hade vi förstått konsekvenserna, hade vi agerat annorlunda.",
                    "Skulle situationen förvärras, måste åtgärder vidtas.",
                    "Vore det möjligt, skulle alla delta."
                ],
                "correct_answer": "Om hade vi förstått konsekvenserna, hade vi agerat annorlunda.",
                "explanation": "'Om' cannot be used together with inverted word order."
            },
            {
                "id": 508,
                "type": "fill_gap",
                "prompt": "___ omständigheterna annorlunda, skulle resultatet bli ett annat. (Were - Vore)",
                "options": ["Vore", "Om vore", "Blev", "Är"],
                "correct_answer": "Vore",
                "explanation": "Subjunctive inversion: 'Vore omständigheterna annorlunda...'."
            },
            {
                "id": 509,
                "type": "multiple_choice",
                "prompt": "How is 'Had she known the truth, she would have left' correctly phrased in C1 Swedish?",
                "options": [
                    "Hade hon vetat sanningen, hade hon gett sig av.",
                    "Hon hade vetat sanningen, hon hade gett sig av.",
                    "Om hon visste sanningen, gav hon sig av.",
                    "Hade hon visste sanningen, skulle hon gett sig av."
                ],
                "correct_answer": "Hade hon vetat sanningen, hade hon gett sig av.",
                "explanation": "'Hade hon vetat...' (inversion) + 'hade hon gett sig av' (main clause inversion)."
            },
            {
                "id": 510,
                "type": "fill_gap",
                "prompt": "Har du lust, ___ du gärna följa med på lunchen. (can/are welcome to - kan)",
                "options": ["kan", "du kan", "måste du", "vill du"],
                "correct_answer": "kan",
                "explanation": "Inverted conditional clause acts as fundament, requiring verb 'kan' in position 2 of main clause."
            }
        ]
    },
    {
        "id": "sv-c1-satsflata",
        "language": "sv",
        "level": "C1",
        "title": "Clause Intertwining (Satsfläta & Complex Extraction)",
        "swedish_title": "Satsfläta (Syntaktisk utbrytning och extraktion)",
        "summary": "Master the native Scandinavian syntactic phenomenon of extracting constituents across subordinate clause boundaries.",
        "rule_explanation": (
            "A 'satsfläta' (intertwined clause) occurs when a phrase belonging semantically to a subordinate clause is fronted to the beginning of the matrix main clause.\n\n"
            "• Underlying structure:\n"
            "  'Jag tror [att den här boken är bäst].'\n"
            "• Satsfläta transformation (extracting 'Den här boken'):\n"
            "  'Den här boken tror jag [att _ är bäst].'\n\n"
            "• Question extraction:\n"
            "  'Vem tror du [att han pratade med _]?' (Who do you think he was talking to?)\n"
            "  'Vad sa du [att det kostade _]?' (What did you say it cost?)"
        ),
        "formula": "[Extracted Constituent] + [Matrix Finite Verb] + [Matrix Subject] + [att-bisats with gap]",
        "examples": [
            {"swedish": "Henne tror jag inte att du känner.", "english": "Her I don't think that you know.", "target_highlight": "Henne tror jag inte"},
            {"swedish": "Vad menar du att vi ska göra nu?", "english": "What do you mean that we should do now?", "target_highlight": "Vad menar du att"},
            {"swedish": "Den filmen tycker han att alla borde se.", "english": "That movie he thinks that everyone ought to see.", "target_highlight": "Den filmen tycker han"}
        ],
        "common_pitfalls": [
            "Ensure that the matrix verb stays in position 2 directly after the extracted element."
        ],
        "exercises": [
            {
                "id": 511,
                "type": "multiple_choice",
                "prompt": "Which sentence contains a correct Swedish satsfläta?",
                "options": [
                    "Det här förslaget tror jag att styrelsen kommer att gilla.",
                    "Det här förslaget jag tror att styrelsen kommer att gilla.",
                    "Det här förslaget tror jag att gilla styrelsen kommer.",
                    "Tror jag det här förslaget att styrelsen kommer att gilla."
                ],
                "correct_answer": "Det här förslaget tror jag att styrelsen kommer att gilla.",
                "explanation": "Extracted object 'Det här förslaget' (1) + matrix verb 'tror' (2) + subject 'jag' (3)."
            },
            {
                "id": 512,
                "type": "fill_gap",
                "prompt": "Vem sa du att ___ vann tävlingen? (who - som)",
                "options": ["som", "att", "när", "därför"],
                "correct_answer": "som",
                "explanation": "When subject is extracted, relative connective 'som' is required: 'Vem sa du att som vann...' (or 'Vem sa du vann...')."
            },
            {
                "id": 513,
                "type": "multiple_choice",
                "prompt": "Extract 'Stockholm' from 'Hon tycker att Stockholm är vackrast':",
                "options": [
                    "Stockholm tycker hon att är vackrast.",
                    "Stockholm hon tycker att är vackrast.",
                    "Är vackrast Stockholm tycker hon.",
                    "Stockholm tycker att hon är vackrast."
                ],
                "correct_answer": "Stockholm tycker hon att är vackrast.",
                "explanation": "Satsfläta with fronted topic 'Stockholm' and V2 matrix clause."
            },
            {
                "id": 514,
                "type": "fill_gap",
                "prompt": "Vad ___ du att vi borde göra? (think - anser)",
                "options": ["anser", "du anser", "anses", "anse"],
                "correct_answer": "anser",
                "explanation": "Wh-word 'Vad' (1) requires verb 'anser' in position 2."
            },
            {
                "id": 515,
                "type": "multiple_choice",
                "prompt": "Choose the most natural advanced Swedish sentence:",
                "options": [
                    "Den tavlan vet jag att min farfar målade.",
                    "Den tavlan jag vet att min farfar målade.",
                    "Att min farfar målade den tavlan jag vet.",
                    "Vet jag att den tavlan min farfar målade."
                ],
                "correct_answer": "Den tavlan vet jag att min farfar målade.",
                "explanation": "Natural Swedish stylistic extraction (satsfläta)."
            },
            {
                "id": 516,
                "type": "fill_gap",
                "prompt": "Honom ___ jag aldrig trott att jag skulle träffa igen. (have - har)",
                "options": ["har", "hade", "är", "skulle"],
                "correct_answer": "har",
                "explanation": "Fronted object 'Honom' (1) + auxiliary 'har' (2) + subject 'jag' (3)."
            },
            {
                "id": 517,
                "type": "multiple_choice",
                "prompt": "Why is satsfläta considered an advanced stylistic tool in Swedish?",
                "options": [
                    "It allows natural topicalization of emphasized elements across clause boundaries.",
                    "It eliminates the need for verbs.",
                    "It replaces all punctuation marks.",
                    "It is only used in medieval poetry."
                ],
                "correct_answer": "It allows natural topicalization of emphasized elements across clause boundaries.",
                "explanation": "Satsfläta enables flexible focus and topicalization in sophisticated Scandinavian prose."
            },
            {
                "id": 518,
                "type": "fill_gap",
                "prompt": "Vilken bok ___ du att jag borde läsa först? (recommend - rekommenderar)",
                "options": ["rekommenderar", "du rekommenderar", "rekommenderade du", "rekommendera"],
                "correct_answer": "rekommenderar",
                "explanation": "Question interrogative constituent 'Vilken bok' (1) + verb 'rekommenderar' (2)."
            },
            {
                "id": 519,
                "type": "multiple_choice",
                "prompt": "Identify the grammatical satsfläta:",
                "options": [
                    "Den här rapporten verkar det som att alla har missförstått.",
                    "Den här rapporten det verkar som att alla har missförstått.",
                    "Verkar det den här rapporten som att alla har missförstått.",
                    "Den här rapporten verkar som alla har missförstått det."
                ],
                "correct_answer": "Den här rapporten verkar det som att alla har missförstått.",
                "explanation": "Fronting object 'Den här rapporten' with dummy subject 'det' in matrix clause."
            },
            {
                "id": 520,
                "type": "fill_gap",
                "prompt": "Det målet ___ vi fast beslutna att nå. (are - är)",
                "options": ["är", "vi är", "blir", "varit"],
                "correct_answer": "är",
                "explanation": "Fronted complement 'Det målet' (1) + verb 'är' (2) + subject 'vi' (3)."
            }
        ]
    }
]
