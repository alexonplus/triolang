"""
================================================================================
TrioLang Grammar Data Store (CEFR A1 -> C1)
================================================================================
Provides a comprehensive, curated curriculum of Swedish and English grammar
rules, formula breakdowns, concrete examples with audio cues, common learner
pitfalls, and built-in interactive practice exercises.
"""

from typing import Dict, List, Any

# Structure of Grammar Topics database categorized by Language and CEFR level.
GRAMMAR_TOPICS: List[Dict[str, Any]] = [
    # --------------------------------------------------------------------------
    # SWEDISH (Svenska) — A1 to C1
    # --------------------------------------------------------------------------
    {
        "id": "sv-a1-articles",
        "language": "sv",
        "level": "A1",
        "title": "Articles & Gender (En vs Ett)",
        "swedish_title": "Obestämd och bestämd artikel (En och Ett)",
        "summary": "Mastering the fundamental two genders of Swedish nouns and their definite suffix forms.",
        "rule_explanation": (
            "Swedish has two grammatical genders: Utrum ('en'-words, ~75% of nouns) and Neutrum ('ett'-words, ~25% of nouns).\n\n"
            "• Indefinite article: 'en hund' (a dog), 'ett hus' (a house).\n"
            "• Definite form: Swedish attaches the article as an ending to the noun: 'hunden' (the dog), 'huset' (the house).\n"
            "• Words ending in a vowel simply add -n or -t: 'en flicka' -> 'flickan', 'ett äpple' -> 'äpplet'."
        ),
        "formula": "Indefinite: en/ett + Noun  |  Definite: Noun + -(e)n / -(e)t",
        "examples": [
            {"swedish": "En katt sover på soffan.", "english": "A cat sleeps on the sofa.", "target_highlight": "En katt"},
            {"swedish": "Katten är mycket söt.", "english": "The cat is very cute.", "target_highlight": "Katten"},
            {"swedish": "Ett brev ligger på bordet.", "english": "A letter is on the table.", "target_highlight": "Ett brev"},
            {"swedish": "Brevet är från Maria.", "english": "The letter is from Maria.", "target_highlight": "Brevet"}
        ],
        "common_pitfalls": [
            "Do not say 'den katt' for 'the cat' — use the definite suffix 'katten'.",
            "Memorize nouns together with their article (e.g., 'ett hus', not just 'hus')."
        ],
        "exercises": [
            {
                "id": 1,
                "type": "multiple_choice",
                "prompt": "Choose the correct definite form for 'ett äpple' (the apple):",
                "options": ["äpplen", "äpplet", "äpplenet", "äppleten"],
                "correct_answer": "äpplet",
                "explanation": "For neuter nouns ('ett'), the definite ending is -t (or -et)."
            },
            {
                "id": 2,
                "type": "fill_gap",
                "prompt": "Hon läser ___ intressant bok varje kväll. (a / an)",
                "options": ["en", "ett", "den", "det"],
                "correct_answer": "en",
                "explanation": "'Bok' is an utrum noun ('en bok')."
            }
        ]
    },
    {
        "id": "sv-a1-present-tense",
        "language": "sv",
        "level": "A1",
        "title": "Present Tense Verbs (Presens)",
        "swedish_title": "Verb i presens (-ar, -er, -r)",
        "summary": "Swedish verbs do not conjugate for person or number (I work, you work, they work use the exact same form!).",
        "rule_explanation": (
            "In Swedish, verbs do NOT change by subject (jag, du, han, vi, ni, de all use the same form).\n\n"
            "Present tense is formed primarily in 3 groups:\n"
            "• Group 1 (Infinitives ending in -a): add -r -> tala (to speak) -> talar, arbeta -> arbetar.\n"
            "• Group 2 (Consonant stem): add -er -> läsa (to read) -> läser, skriva -> skriver.\n"
            "• Short verbs (ending in stressed vowel): add -r -> bo (to live) -> bor, gå (to walk) -> går."
        ),
        "formula": "Subject + Verb-presens (-ar / -er / -r) + Object",
        "examples": [
            {"swedish": "Jag pratar svenska varje dag.", "english": "I speak Swedish every day.", "target_highlight": "pratar"},
            {"swedish": "De bor i Stockholm nu.", "english": "They live in Stockholm now.", "target_highlight": "bor"},
            {"swedish": "Vi läser en god bok.", "english": "We are reading a good book.", "target_highlight": "läser"}
        ],
        "common_pitfalls": [
            "There is no continuous '-ing' form in Swedish. 'Jag läser' means both 'I read' and 'I am reading'."
        ],
        "exercises": [
            {
                "id": 3,
                "type": "multiple_choice",
                "prompt": "How do you say 'We are living in Sweden'?",
                "options": ["Vi är boende i Sverige", "Vi bor i Sverige", "Vi bo i Sverige", "Vi borer i Sverige"],
                "correct_answer": "Vi bor i Sverige",
                "explanation": "'Bo' is a short vowel verb and forms presens as 'bor'."
            }
        ]
    },
    {
        "id": "sv-a2-plural-groups",
        "language": "sv",
        "level": "A2",
        "title": "Plural Noun Groups (1 to 5)",
        "swedish_title": "Substantivens pluralgrupper (1–5)",
        "summary": "Mastering the 5 plural endings in Swedish: -or, -ar, -er, -n, and zero ending.",
        "rule_explanation": (
            "Swedish nouns form plural according to 5 declension groups:\n"
            "1. Group 1 (-or): Most 'en' words ending in -a (en flicka -> flickor).\n"
            "2. Group 2 (-ar): Many 'en' words (en bil -> bilar, en hund -> hundar).\n"
            "3. Group 3 (-er): Many 'en' words and foreign words (en katt -> katter, en telefon -> telefoner).\n"
            "4. Group 4 (-n): 'ett' words ending in a vowel (ett äpple -> äpplen, ett kvitto -> kvitton).\n"
            "5. Group 5 (no change / zero ending): 'ett' words ending in a consonant (ett hus -> hus, ett barn -> barn)."
        ),
        "formula": "Group 1: -or | Group 2: -ar | Group 3: -er | Group 4: -n | Group 5: Ø",
        "examples": [
            {"swedish": "Tre flickor cyklar till skolan.", "english": "Three girls are cycling to school.", "target_highlight": "flickor"},
            {"swedish": "Jag har fem bilar i garaget.", "english": "I have five cars in the garage.", "target_highlight": "bilar"},
            {"swedish": "Två hus står vid sjön.", "english": "Two houses stand by the lake.", "target_highlight": "hus"}
        ],
        "common_pitfalls": [
            "Do not add -s for Swedish plurals! (Except for very rare loanwords).",
            "Group 5 words ('ett hus', 'ett barn') stay unchanged in plural: 'ett hus' -> 'två hus'."
        ],
        "exercises": [
            {
                "id": 4,
                "type": "fill_gap",
                "prompt": "En katt -> tre ___ (plural)",
                "options": ["kattor", "kattar", "katter", "kattn"],
                "correct_answer": "katter",
                "explanation": "'Katt' belongs to Group 3 (-er)."
            }
        ]
    },
    {
        "id": "sv-b1-v2-rule",
        "language": "sv",
        "level": "B1",
        "title": "The Fundamental V2 Word Order Rule",
        "swedish_title": "V2-regeln (Verbet på andra plats)",
        "summary": "In main clauses, the finite verb MUST always occupy the second grammatical position.",
        "rule_explanation": (
            "The V2 rule is the cornerstone of Scandinavian syntax.\n"
            "In any main clause (huvudsats), the finite verb MUST be the second element.\n\n"
            "• Standard SVO: 'Jag (1) köpte (2) en cykel igår.'\n"
            "• Fronted Time/Place (Inversion): 'Igår (1) köpte (2) jag (3) en cykel.'\n"
            "Notice how the subject 'jag' moves after the verb so that the verb stays in position 2!"
        ),
        "formula": "[Fronted Element (Time/Place/Object)] + [Finite Verb] + [Subject] + ...",
        "examples": [
            {"swedish": "Imorgon åker vi till Göteborg.", "english": "Tomorrow we go to Gothenburg.", "target_highlight": "åker vi"},
            {"swedish": "I Sverige pratar man mycket svenska.", "english": "In Sweden people speak a lot of Swedish.", "target_highlight": "pratar man"},
            {"swedish": "Därför vill jag lära mig språket.", "english": "Therefore I want to learn the language.", "target_highlight": "vill jag"}
        ],
        "common_pitfalls": [
            "NEVER say 'Igår jag åkte...' — this is the most frequent mistake by English speakers.",
            "Always invert: 'Igår åkte jag...'."
        ],
        "exercises": [
            {
                "id": 5,
                "type": "multiple_choice",
                "prompt": "Which sentence follows the correct Swedish V2 word order?",
                "options": [
                    "På måndag jag ska börja jobba.",
                    "På måndag ska jag börja jobba.",
                    "På måndag ska börja jag jobba.",
                    "Ska på måndag jag börja jobba."
                ],
                "correct_answer": "På måndag ska jag börja jobba.",
                "explanation": "Because 'På måndag' is in position 1, the verb 'ska' must be in position 2, followed by subject 'jag'."
            }
        ]
    },
    {
        "id": "sv-b1-biff-rule",
        "language": "sv",
        "level": "B1",
        "title": "The BIFF Rule in Subordinate Clauses",
        "swedish_title": "BIFF-regeln (I Bisats kommer 'Inte' Före Finita verbet)",
        "summary": "BIFF: 'I Bisats kommer Inte Före Finita verbet' — positioning sentence adverbs in subordinate clauses.",
        "rule_explanation": (
            "BIFF is a famous Swedish mnemonic:\n"
            "• B = Bisats (subordinate clause introduced by 'eftersom', 'att', 'när', 'om', etc.)\n"
            "• I = Inte (or other sentence adverbs like 'alltid', 'aldrig')\n"
            "• F = Före (before)\n"
            "• F = Finita verbet (the finite verb)\n\n"
            "Compare:\n"
            "• Main clause: 'Han kommer inte idag.' (inte comes AFTER the verb)\n"
            "• Subordinate clause: '...eftersom han inte kommer idag.' (inte comes BEFORE the verb!)"
        ),
        "formula": "Subjunction (eftersom/att/om) + Subject + Inte/Alltid + Finite Verb",
        "examples": [
            {"swedish": "Jag vet att du inte tycker om sill.", "english": "I know that you do not like herring.", "target_highlight": "inte tycker"},
            {"swedish": "Hon stannar hemma om det inte slutar regna.", "english": "She stays home if it does not stop raining.", "target_highlight": "inte slutar"},
            {"swedish": "Han sa att han alltid äter frukost.", "english": "He said that he always eats breakfast.", "target_highlight": "alltid äter"}
        ],
        "common_pitfalls": [
            "Do not use main clause word order inside a subordinate clause: say 'eftersom jag inte förstår', NOT 'eftersom jag förstår inte'."
        ],
        "exercises": [
            {
                "id": 6,
                "type": "fill_gap",
                "prompt": "Jag stannar hemma eftersom jag ___ mår bra idag.",
                "options": ["inte", "mår inte", "är inte", "inte mår"],
                "correct_answer": "inte",
                "explanation": "In a subordinate clause ('eftersom...'), 'inte' precedes the verb 'mår'."
            }
        ]
    },
    {
        "id": "sv-b2-s-passive",
        "language": "sv",
        "level": "B2",
        "title": "Passive Voice with -s Suffix",
        "swedish_title": "S-passiv och Bli-passiv",
        "summary": "Forming the synthetic -s passive used extensively in official signs, recipes, and Swedish media.",
        "rule_explanation": (
            "Swedish has a very elegant morphological passive formed by simply adding '-s' to the verb.\n\n"
            "• Present: 'sälja' -> 'säljs' / 'säljes' (is sold), 'öppna' -> 'öppnas' (is opened).\n"
            "• Past: 'byggde' -> 'byggdes' (was built), 'skrev' -> 'skrevs' (was written).\n"
            "• Supinum: 'har byggt' -> 'har byggts' (has been built).\n\n"
            "Swedish also has the 'bli-passiv' for progressive events: 'Bilen blev reparerad av mekanikern.'"
        ),
        "formula": "Active Verb Ending + -s",
        "examples": [
            {"swedish": "Dörren öppnas automatiskt.", "english": "The door is opened automatically.", "target_highlight": "öppnas"},
            {"swedish": "Boken skrevs av Astrid Lindgren 1945.", "english": "The book was written by Astrid Lindgren in 1945.", "target_highlight": "skrevs"},
            {"swedish": "Svenska talas i både Sverige och Finland.", "english": "Swedish is spoken in both Sweden and Finland.", "target_highlight": "talas"}
        ],
        "common_pitfalls": [
            "Do not confuse S-passiv with reciprocal verbs ('vi ses' = we see each other) or deponent verbs ('hoppas' = to hope)."
        ],
        "exercises": [
            {
                "id": 7,
                "type": "multiple_choice",
                "prompt": "How do you say 'The house was built in 1920' using s-passive?",
                "options": [
                    "Huset byggdes 1920.",
                    "Huset byggdes av 1920.",
                    "Huset var byggde 1920.",
                    "Huset byggs 1920."
                ],
                "correct_answer": "Huset byggdes 1920.",
                "explanation": "'Byggdes' is preteritum s-passive of 'bygga'."
            }
        ]
    },
    {
        "id": "sv-c1-stylistic-inversion",
        "language": "sv",
        "level": "C1",
        "title": "Conditional Inversion without 'Om'",
        "swedish_title": "Villkorsbisats med omvänd ordföljd utan 'om'",
        "summary": "Advanced stylistic syntax replacing 'om' with verb-first inversion in hypothetical conditional clauses.",
        "rule_explanation": (
            "In high-register, academic, and literary Swedish, hypothetical conditional clauses frequently omit the subjunction 'om' (if) and invert the clause by placing the auxiliary or finite verb first.\n\n"
            "• Standard: 'Om jag hade vetat detta, skulle jag ha agerat annorlunda.'\n"
            "• C1 Inverted: 'Hade jag vetat detta, skulle jag ha agerat annorlunda.' (Had I known this...)\n"
            "• Present conditional: 'Skulle du behöva hjälp, säg bara till.' (Should you need help...)"
        ),
        "formula": "[Auxiliary / Finite Verb] + [Subject] + [Object/Participle], [Main Clause with Skulle/Vore...]",
        "examples": [
            {"swedish": "Vore det inte för dig, hade vi missat tåget.", "english": "Were it not for you, we would have missed the train.", "target_highlight": "Vore det inte"},
            {"swedish": "Skulle problem uppstå, kontakta supporten.", "english": "Should problems arise, contact support.", "target_highlight": "Skulle problem uppstå"}
        ],
        "common_pitfalls": [
            "Ensure the main clause that follows still respects the V2 rule."
        ],
        "exercises": [
            {
                "id": 8,
                "type": "multiple_choice",
                "prompt": "Transform 'Om du vill veta mer, ring oss' into high-register inverted C1 Swedish:",
                "options": [
                    "Vill du veta mer, ring oss.",
                    "Du vill veta mer, ring oss.",
                    "Om vill du veta mer, ring oss.",
                    "Veta mer du vill, ring oss."
                ],
                "correct_answer": "Vill du veta mer, ring oss.",
                "explanation": "Omitting 'om' triggers verb-initial position ('Vill du veta mer...')."
            }
        ]
    },

    # --------------------------------------------------------------------------
    # ENGLISH — A1 to C1
    # --------------------------------------------------------------------------
    {
        "id": "en-a1-present-simple",
        "language": "en",
        "level": "A1",
        "title": "Present Simple & 3rd Person -s",
        "swedish_title": "Presens och 3:e person -s",
        "summary": "Expressing habits, general truths, and the crucial 3rd person singular 'he/she/it' -s rule.",
        "rule_explanation": (
            "Use the Present Simple for routines, permanent states, and general facts.\n\n"
            "• I / You / We / They + base verb (I work in an office).\n"
            "• He / She / It + verb + -s / -es (She works in a bank, He watches TV).\n"
            "• Negative: don't / doesn't + base verb (He doesn't like tea).\n"
            "• Question: Do / Does + subject + base verb? (Does she live here?)"
        ),
        "formula": "Subject (He/She/It) + Verb-s / -es",
        "examples": [
            {"swedish": "Hon pratar tre språk flytande.", "english": "She speaks three languages fluently.", "target_highlight": "speaks"},
            {"swedish": "Han gillar inte kallt väder.", "english": "He doesn't like cold weather.", "target_highlight": "doesn't like"}
        ],
        "common_pitfalls": [
            "Forgetting the -s for third person singular (say 'He plays', not 'He play').",
            "Do NOT add -s after 'does': say 'Does he know?', not 'Does he knows?'."
        ],
        "exercises": [
            {
                "id": 9,
                "type": "fill_gap",
                "prompt": "My brother ___ (live) in London.",
                "options": ["live", "lives", "is live", "living"],
                "correct_answer": "lives",
                "explanation": "'My brother' is 3rd person singular (he), requiring '-s'."
            }
        ]
    },
    {
        "id": "en-a2-present-perfect-vs-past",
        "language": "en",
        "level": "A2",
        "title": "Present Perfect vs. Past Simple",
        "swedish_title": "Present Perfect vs. Past Simple (Dåtid vs Fullbordat)",
        "summary": "Distinguishing between finished past moments (yesterday, in 2010) and life experience / unfinished time.",
        "rule_explanation": (
            "• Past Simple (V2 / -ed): Used with specific, finished time markers (yesterday, last week, in 2020, when I was young).\n"
            "  Example: 'I visited Paris in 2019.'\n\n"
            "• Present Perfect (have/has + V3 past participle): Used for life experiences, unfinished periods, or actions with a direct result in the present (already, yet, ever, never, since, for).\n"
            "  Example: 'I have visited Paris three times.' (in my life so far)"
        ),
        "formula": "Past Simple: Verb-ed (Finished time)  |  Present Perfect: have/has + V3 (Connected to now)",
        "examples": [
            {"swedish": "Jag såg den filmen igår.", "english": "I saw that movie yesterday.", "target_highlight": "saw ... yesterday"},
            {"swedish": "Jag har redan sett den filmen.", "english": "I have already seen that movie.", "target_highlight": "have already seen"}
        ],
        "common_pitfalls": [
            "Never use Present Perfect with a specific past time: 'I have seen him yesterday' is WRONG -> 'I saw him yesterday'."
        ],
        "exercises": [
            {
                "id": 10,
                "type": "multiple_choice",
                "prompt": "Select the correct sentence:",
                "options": [
                    "I have finished my homework two hours ago.",
                    "I finished my homework two hours ago.",
                    "I was finished my homework two hours ago.",
                    "I have finish my homework two hours ago."
                ],
                "correct_answer": "I finished my homework two hours ago.",
                "explanation": "'Two hours ago' is a specific finished past time, requiring Past Simple."
            }
        ]
    },
    {
        "id": "en-b1-conditionals",
        "language": "en",
        "level": "B1",
        "title": "First & Second Conditionals",
        "swedish_title": "Första och andra konditionalis (If-satser)",
        "summary": "Mastering real future possibilities (1st conditional) vs. hypothetical dreams/unreal situations (2nd conditional).",
        "rule_explanation": (
            "• First Conditional (Real / Likely future):\n"
            "  If + Present Simple, will + base verb.\n"
            "  'If it rains tomorrow, we will stay at home.'\n\n"
            "• Second Conditional (Hypothetical / Unreal present/future):\n"
            "  If + Past Simple, would + base verb.\n"
            "  'If I won the lottery, I would travel around the world.'"
        ),
        "formula": "1st: If + Pres, will + V  |  2nd: If + Past, would + V",
        "examples": [
            {"swedish": "Om du studerar hårt, kommer du att klara provet.", "english": "If you study hard, you will pass the exam.", "target_highlight": "study ... will pass"},
            {"swedish": "Om jag hade mer tid, skulle jag läsa fler böcker.", "english": "If I had more time, I would read more books.", "target_highlight": "had ... would read"}
        ],
        "common_pitfalls": [
            "Do NOT put 'will' or 'would' in the if-clause! (Say 'If I have time', not 'If I will have time')."
        ],
        "exercises": [
            {
                "id": 11,
                "type": "fill_gap",
                "prompt": "If I ___ (be) you, I would accept the job offer.",
                "options": ["am", "were", "will be", "would be"],
                "correct_answer": "were",
                "explanation": "In 2nd conditional, 'were' is preferred for all subjects ('If I were you')."
            }
        ]
    },
    {
        "id": "en-b2-third-conditional-mixed",
        "language": "en",
        "level": "B2",
        "title": "Third & Mixed Conditionals",
        "swedish_title": "Tredje och blandad konditionalis",
        "summary": "Expressing past regrets and counterfactual history: what would have happened if things had been different.",
        "rule_explanation": (
            "• Third Conditional (Past unreal situation & past result):\n"
            "  If + Past Perfect (had + V3), would have + V3.\n"
            "  'If I had set my alarm, I would not have missed my flight.'\n\n"
            "• Mixed Conditional (Past event with present result):\n"
            "  If + had + V3, would + base verb.\n"
            "  'If I had taken that job in 2020, I would be living in London today.'"
        ),
        "formula": "If + had + V3, would have + V3",
        "examples": [
            {"swedish": "Om vi hade åkt tidigare, skulle vi inte ha fastnat i trafiken.", "english": "If we had left earlier, we wouldn't have been stuck in traffic.", "target_highlight": "had left ... wouldn't have been"}
        ],
        "common_pitfalls": [
            "Avoid saying 'If I would have known' — use 'If I had known'."
        ],
        "exercises": [
            {
                "id": 12,
                "type": "multiple_choice",
                "prompt": "Complete: 'If you had warned me, I ___ the contract.'",
                "options": [
                    "would not sign",
                    "would not have signed",
                    "had not signed",
                    "did not sign"
                ],
                "correct_answer": "would not have signed",
                "explanation": "Third conditional requires 'would have + past participle' in the main clause."
            }
        ]
    },
    {
        "id": "en-c1-inversion-emphasis",
        "language": "en",
        "level": "C1",
        "title": "Negative Inversion for Rhetorical Emphasis",
        "swedish_title": "Negativ inversion för stilistisk emfas",
        "summary": "Using fronted negative adverbs (Rarely, Seldom, Not only, Under no circumstances) with subject-auxiliary inversion.",
        "rule_explanation": (
            "In formal and literary English, when a negative or restrictive adverb begins a sentence, the subject and auxiliary verb invert (just like in questions).\n\n"
            "• Standard: 'I have rarely seen such dedication.'\n"
            "• C1 Inversion: 'Rarely have I seen such dedication.'\n"
            "• Standard: 'He did not know what would happen next.'\n"
            "• C1 Inversion: 'Little did he know what would happen next.'\n"
            "• 'Under no circumstances should you open this door.'"
        ),
        "formula": "[Negative Adverb] + [Auxiliary Verb (have/do/is/should)] + [Subject] + [Main Verb]",
        "examples": [
            {"swedish": "Sällan har jag bevittnat en sådan prestation.", "english": "Seldom have I witnessed such a remarkable achievement.", "target_highlight": "Seldom have I witnessed"},
            {"swedish": "Inte förrän igår fick vi reda på sanningen.", "english": "Not until yesterday did we discover the truth.", "target_highlight": "Not until yesterday did we discover"}
        ],
        "common_pitfalls": [
            "Remember that dummy auxiliary 'do/did' must be supplied if no auxiliary was present: 'Never did she imagine...'."
        ],
        "exercises": [
            {
                "id": 13,
                "type": "multiple_choice",
                "prompt": "Which sentence has correct negative inversion?",
                "options": [
                    "Hardly had we arrived when the storm began.",
                    "Hardly we had arrived when the storm began.",
                    "Hardly did we arrived when the storm began.",
                    "Hardly we arrived when the storm began."
                ],
                "correct_answer": "Hardly had we arrived when the storm began.",
                "explanation": "Negative adverb 'Hardly' triggers auxiliary inversion 'had we arrived'."
            }
        ]
    }
]
