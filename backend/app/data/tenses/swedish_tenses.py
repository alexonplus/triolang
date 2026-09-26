"""
================================================================================
Exhaustive Swedish Verb Tenses Dataset
================================================================================
Covers the core temporal system of the Swedish language:
Presens, Preteritum, Perfekt (supinum), Pluskvamperfekt, Futurum, and Futurum Preteriti.
"""

from typing import List, Dict, Any

SWEDISH_TENSES: List[Dict[str, Any]] = [
    # --------------------------------------------------------------------------
    # 1. PRESENS (Present)
    # --------------------------------------------------------------------------
    {
        "id": "sv-presens",
        "language": "sv",
        "time_aspect": "present",
        "title": "Presens (Present Tense)",
        "swedish_title": "Presens (-ar, -er, -r)",
        "level": "A1",
        "summary": "Expresses ongoing actions, general facts, habits, and near planned future in Swedish.",
        "formula": "Verb-stam + -ar / -er / -r (No personal conjugation)",
        "signal_words": ["nu", "just nu", "varje dag", "alltid", "ofta", "på måndagar", "imorgon (med tidsadverb)"],
        "timeline_description": "Current moment, recurring habits, or general timeless truths.",
        "examples": [
            {"swedish": "Jag pratar svenska varje dag.", "english": "I speak Swedish every day.", "target_highlight": "pratar"},
            {"swedish": "Vad gör du nu?", "english": "What are you doing now?", "target_highlight": "gör"},
            {"swedish": "Tåget avgår om fem minuter.", "english": "The train departs in five minutes.", "target_highlight": "avgår (presens för framtid)"}
        ],
        "common_pitfalls": ["Do not attempt to construct continuous 'är görande' — 'Jag äter' means both 'I eat' and 'I am eating'."],
        "exercises": [
            {"id": 1301, "type": "fill_gap", "prompt": "Vi ___ (bo) i en lägenhet i Stockholm.", "options": ["bor", "boer", "bo", "bodde"], "correct_answer": "bor", "explanation": "Short vowel verb 'bo' adds -r in present -> 'bor'."},
            {"id": 1302, "type": "multiple_choice", "prompt": "How do you express 'I am reading a book right now' in natural Swedish?", "options": ["Jag läser en bok just nu.", "Jag är läsande en bok.", "Jag är läser en bok.", "Jag läsar en bok."], "correct_answer": "Jag läser en bok just nu.", "explanation": "Swedish uses simple presens 'läser' for both simple and continuous actions."},
            {"id": 1303, "type": "fill_gap", "prompt": "Mormor ___ (baka) kanelbullar varje söndag.", "options": ["bakar", "baker", "baka", "bakat"], "correct_answer": "bakar", "explanation": "Group 1 verb 'baka' -> 'bakar'."},
            {"id": 1304, "type": "multiple_choice", "prompt": "Presens form of 'att skriva':", "options": ["skriver", "skrivar", "skriv", "skrev"], "correct_answer": "skriver", "explanation": "Group 2/4 verb 'skriva' -> 'skriver'."},
            {"id": 1305, "type": "fill_gap", "prompt": "Vad ___ (dricka) du till frukost?", "options": ["dricker", "drickar", "drick", "druckit"], "correct_answer": "dricker", "explanation": "Dricka -> dricker."},
            {"id": 1306, "type": "multiple_choice", "prompt": "Using presens for scheduled near future:", "options": ["Imorgon åker jag till Malmö.", "Imorgon ska jag åkte.", "Imorgon jag åker.", "Imorgon åkt jag."], "correct_answer": "Imorgon åker jag till Malmö.", "explanation": "Presens with a future time marker expresses planned near future with V2 word order."},
            {"id": 1307, "type": "fill_gap", "prompt": "Solen ___ (lysa) på himlen.", "options": ["lyser", "lysar", "lys", "lyste"], "correct_answer": "lyser", "explanation": "Lysa -> lyser."},
            {"id": 1308, "type": "multiple_choice", "prompt": "Irregular presens of 'att gå':", "options": ["går", "gåer", "gåar", "gått"], "correct_answer": "går", "explanation": "Gå -> går."},
            {"id": 1309, "type": "fill_gap", "prompt": "De ___ (köpa) mat på ICA.", "options": ["köper", "köpar", "köp", "köpte"], "correct_answer": "köper", "explanation": "Köpa -> köper."},
            {"id": 1310, "type": "multiple_choice", "prompt": "Presens of 'att veta' (to know):", "options": ["vet", "veter", "vetar", "visste"], "correct_answer": "vet", "explanation": "Irregular verb: veta -> vet."}
        ]
    },

    # --------------------------------------------------------------------------
    # 2. PRETERITUM (Simple Past)
    # --------------------------------------------------------------------------
    {
        "id": "sv-preteritum",
        "language": "sv",
        "time_aspect": "past",
        "title": "Preteritum (Simple Past)",
        "swedish_title": "Preteritum / Imperfekt (-de, -te, vokalväxling)",
        "level": "A2",
        "summary": "Actions finished at a specific past moment in time (yesterday, last year, in 2010).",
        "formula": "G1: -ade | G2a: -de | G2b: -te | G4 (Starka verb): Vokalväxling",
        "signal_words": ["igår", "förra veckan", "i morse", "då", "för tre år sedan", "1995", "när jag var barn"],
        "timeline_description": "A completed moment in past time disconnected from the present.",
        "examples": [
            {"swedish": "Igår ringde jag min mamma.", "english": "Yesterday I called my mother.", "target_highlight": "ringde"},
            {"swedish": "Förra året köpte vi ett sommarställe.", "english": "Last year we bought a summer cottage.", "target_highlight": "köpte"},
            {"swedish": "Han skrev en roman 2018.", "english": "He wrote a novel in 2018.", "target_highlight": "skrev"}
        ],
        "common_pitfalls": ["Do NOT use 'har + supinum' with 'igår' or 'förra veckan'."],
        "exercises": [
            {"id": 1311, "type": "fill_gap", "prompt": "I söndags ___ (titta) vi på fotboll hela kvällen.", "options": ["tittade", "tittat", "titte", "tittar"], "correct_answer": "tittade", "explanation": "Group 1 preteritum ending is -ade -> 'tittade'."},
            {"id": 1312, "type": "multiple_choice", "prompt": "Preteritum of 'att läsa' (to read):", "options": ["läste", "läsade", "läsde", "läst"], "correct_answer": "läste", "explanation": "Group 2b verbs ending in s take -te -> 'läste'."},
            {"id": 1313, "type": "fill_gap", "prompt": "För två timmar sedan ___ (dricka) han en kopp kaffe.", "options": ["drack", "druckit", "drickade", "drickte"], "correct_answer": "drack", "explanation": "Strong verb with vowel shift: dricka -> drack."},
            {"id": 1314, "type": "multiple_choice", "prompt": "Which sentence is grammatically correct for yesterday?", "options": ["Igår åt jag middag klockan sex.", "Igår har jag ätit middag klockan sex.", "Igår äter jag middag.", "Igår ätade jag middag."], "correct_answer": "Igår åt jag middag klockan sex.", "explanation": "Specific finished past time 'igår' requires Preteritum 'åt'."},
            {"id": 1315, "type": "fill_gap", "prompt": "De ___ (resa) till Spanien förra sommaren.", "options": ["reste", "resade", "rest", "reser"], "correct_answer": "reste", "explanation": "Resa -> reste."},
            {"id": 1316, "type": "multiple_choice", "prompt": "Preteritum of irregular 'att göra' (to do):", "options": ["gjorde", "görade", "gjort", "gorde"], "correct_answer": "gjorde", "explanation": "Göra -> gjorde."},
            {"id": 1317, "type": "fill_gap", "prompt": "Vi ___ (få) ett viktigt brev i postlådan igår.", "options": ["fick", "fått", "fådde", "fickte"], "correct_answer": "fick", "explanation": "Få -> fick."},
            {"id": 1318, "type": "multiple_choice", "prompt": "Preteritum of 'att sova' (to sleep):", "options": ["sov", "sovade", "softe", "sovit"], "correct_answer": "sov", "explanation": "Sova -> sov."},
            {"id": 1319, "type": "fill_gap", "prompt": "Hon ___ (hjälpa) mig med läxorna igår.", "options": ["hjälpte", "hjälpade", "hjälpt", "hjalp"], "correct_answer": "hjälpte", "explanation": "Hjälpa (Group 2b after p) takes -te -> 'hjälpte'."},
            {"id": 1320, "type": "multiple_choice", "prompt": "Preteritum of 'att gå':", "options": ["gick", "gådde", "gått", "gickade"], "correct_answer": "gick", "explanation": "Gå -> gick."}
        ]
    },

    # --------------------------------------------------------------------------
    # 3. PERFEKT (Present Perfect with Supinum)
    # --------------------------------------------------------------------------
    {
        "id": "sv-perfekt",
        "language": "sv",
        "time_aspect": "present",
        "title": "Perfekt (har + Supinum)",
        "swedish_title": "Perfekt med supinumform (har gjort)",
        "level": "A2",
        "summary": "Used for life experiences, unfinished time, or past actions whose result is relevant now.",
        "formula": "Subject + har + Supinum (-t / -it)",
        "signal_words": ["redan", "inte ännu", "någonsin", "aldrig", "hittills", "i tre år nu", "nyligen"],
        "timeline_description": "An action occurring in past time that touches or influences the present.",
        "examples": [
            {"swedish": "Jag har redan ätit lunch.", "english": "I have already eaten lunch.", "target_highlight": "har redan ätit"},
            {"swedish": "Har du någonsin besökt Gotland?", "english": "Have you ever visited Gotland?", "target_highlight": "Har ... besökt"},
            {"swedish": "Vi har bott i Sverige i fem år.", "english": "We have lived in Sweden for five years.", "target_highlight": "har bott"}
        ],
        "common_pitfalls": ["Confusing the Supinum (-t, e.g. 'ätit') with the Participle (e.g. 'äten/ätet/ätna')."],
        "exercises": [
            {"id": 1321, "type": "fill_gap", "prompt": "Jag har ___ (läsa) den här boken två gånger.", "options": ["läst", "läste", "läsat", "läser"], "correct_answer": "läst", "explanation": "Supinum of 'läsa' is 'läst'."},
            {"id": 1322, "type": "multiple_choice", "prompt": "What is the supinum of 'att skriva'?", "options": ["skrivit", "skrev", "skrivat", "skrivt"], "correct_answer": "skrivit", "explanation": "Skriva -> skrev -> skrivit."},
            {"id": 1323, "type": "fill_gap", "prompt": "Har du ___ (äta) frukost ännu?", "options": ["ätit", "åt", "ätat", "äter"], "correct_answer": "ätit", "explanation": "Äta -> åt -> ätit."},
            {"id": 1324, "type": "multiple_choice", "prompt": "Select the correct sentence with 'inte':", "options": ["Jag har inte sett den filmen.", "Jag har sett inte den filmen.", "Jag inte har sett den filmen.", "Inte jag har sett den filmen."], "correct_answer": "Jag har inte sett den filmen.", "explanation": "In main clauses, 'inte' comes between auxiliary 'har' and supinum 'sett'."},
            {"id": 1325, "type": "fill_gap", "prompt": "Vi har ___ (bo) i det här huset sedan 2015.", "options": ["bott", "bodde", "bot", "bor"], "correct_answer": "bott", "explanation": "Bo -> bodde -> bott."},
            {"id": 1326, "type": "multiple_choice", "prompt": "Supinum of 'att se' (to see):", "options": ["sett", "såg", "seat", "syns"], "correct_answer": "sett", "explanation": "Se -> såg -> sett."},
            {"id": 1327, "type": "fill_gap", "prompt": "Hon har ___ (köpa) en ny cykel.", "options": ["köpt", "köpte", "köpat", "köptat"], "correct_answer": "köpt", "explanation": "Köpa -> köpte -> köpt."},
            {"id": 1328, "type": "multiple_choice", "prompt": "Which sentence means 'I haven't arrived yet'?", "options": ["Jag har inte kommit fram ännu.", "Jag kom inte fram ännu.", "Jag är inte framme ännu kommit.", "Inte har jag kommit fram."], "correct_answer": "Jag har inte kommit fram ännu.", "explanation": "'Har inte kommit fram ännu'."},
            {"id": 1329, "type": "fill_gap", "prompt": "De har ___ (göra) alla sina läxor.", "options": ["gjort", "gjorde", "görat", "gort"], "correct_answer": "gjort", "explanation": "Göra -> gjorde -> gjort."},
            {"id": 1330, "type": "multiple_choice", "prompt": "Supinum of 'att vara' (to be):", "options": ["varit", "var", "vore", "vart"], "correct_answer": "varit", "explanation": "Vara -> var -> varit."}
        ]
    },

    # --------------------------------------------------------------------------
    # 4. PLUSKVAMPERFEKT (Past Perfect with Supinum)
    # --------------------------------------------------------------------------
    {
        "id": "sv-pluskvamperfekt",
        "language": "sv",
        "time_aspect": "past",
        "title": "Pluskvamperfekt (hade + Supinum)",
        "swedish_title": "Pluskvamperfekt (hade gjort före en annan dåtid)",
        "level": "B1",
        "summary": "Describes an action completed before another past event (dåtidens förflutna).",
        "formula": "Subject + hade + Supinum",
        "signal_words": ["redan när", "innan", "före", "hade redan", "aldrig tidigare"],
        "timeline_description": "An action completed earlier than another specified moment in the past.",
        "examples": [
            {"swedish": "När vi kom fram till stationen hade tåget redan gått.", "english": "When we arrived at the station, the train had already left.", "target_highlight": "hade redan gått"},
            {"swedish": "Hon berättade att hon hade träffat kungen.", "english": "She recounted that she had met the King.", "target_highlight": "hade träffat"},
            {"swedish": "Vi hade aldrig sett något liknande förut.", "english": "We had never seen anything like it before.", "target_highlight": "hade aldrig sett"}
        ],
        "common_pitfalls": ["Confusing 'hade' + supinum with 'har' + supinum."],
        "exercises": [
            {"id": 1331, "type": "fill_gap", "prompt": "När gästerna anlände, ___ kocken redan ___ (laga) maten.", "options": ["hade ... lagat", "har ... lagat", "var ... lagat", "hade ... lagade"], "correct_answer": "hade ... lagat", "explanation": "Action completed before guests arrived -> 'hade lagat'."},
            {"id": 1332, "type": "multiple_choice", "prompt": "Which event happened first? 'Filmen hade redan börjat när vi kom in i biosalongen.'", "options": ["Filmen började först.", "Vi kom in först.", "Båda hände samtidigt.", "Inget hände."], "correct_answer": "Filmen började först.", "explanation": "'Hade börjat' (Pluskvamperfekt) marks the prior past event."},
            {"id": 1333, "type": "fill_gap", "prompt": "Han insåg att han ___ (glömma) sitt pass hemma.", "options": ["hade glömt", "har glömt", "glömde", "hade glömde"], "correct_answer": "hade glömt", "explanation": "Forgetting the passport happened before realizing."},
            {"id": 1334, "type": "multiple_choice", "prompt": "Choose the BIFF rule with pluskvamperfekt: '...eftersom jag ___'", "options": ["...eftersom jag inte hade förstått frågan.", "...eftersom jag hade inte förstått frågan.", "...eftersom inte hade jag förstått.", "...eftersom jag hade förstått inte."], "correct_answer": "...eftersom jag inte hade förstått frågan.", "explanation": "In bisats, 'inte' comes BEFORE auxiliary 'hade'."},
            {"id": 1335, "type": "fill_gap", "prompt": "De ___ (arbeta) hela dagen innan de tog en paus.", "options": ["hade arbetat", "har arbetat", "arbetade", "var arbetat"], "correct_answer": "hade arbetat", "explanation": "Working preceded taking a break."},
            {"id": 1336, "type": "multiple_choice", "prompt": "Third conditional in Swedish: 'Om jag ___ vetat sanningen, hade jag reagerat annorlunda.'", "options": ["hade", "har", "skulle", "blev"], "correct_answer": "hade", "explanation": "Hypothetical condition in past: 'hade vetat'."},
            {"id": 1337, "type": "fill_gap", "prompt": "Hon var lycklig eftersom hon ___ (vinna) första pris.", "options": ["hade vunnit", "har vunnit", "vann", "vinner"], "correct_answer": "hade vunnit", "explanation": "Winning preceded the emotional state 'var lycklig'."},
            {"id": 1338, "type": "multiple_choice", "prompt": "Supinum of 'att försvinna' in pluskvamperfekt:", "options": ["hade försvunnit", "hade försvann", "hade försvunnet", "har försvann"], "correct_answer": "hade försvunnit", "explanation": "Försvinna -> försvann -> försvunnit."},
            {"id": 1339, "type": "fill_gap", "prompt": "Vi ___ (äta) redan när han ringde och bjöd på middag.", "options": ["hade ätit", "har ätit", "åt", "hade ätat"], "correct_answer": "hade ätit", "explanation": "Eating had concluded prior to the phone call."},
            {"id": 1340, "type": "multiple_choice", "prompt": "Transform to inverted C1 condition: 'Om vi hade vetat...' ->", "options": ["Hade vi vetat...", "Vi hade vetat...", "Om hade vi vetat...", "Vetat hade vi..."], "correct_answer": "Hade vi vetat...", "explanation": "Omission of 'om' triggers verb-first inversion."}
        ]
    },

    # --------------------------------------------------------------------------
    # 5. FUTURUM (Future Tense Expressions)
    # --------------------------------------------------------------------------
    {
        "id": "sv-futurum",
        "language": "sv",
        "time_aspect": "future",
        "title": "Futurum (ska / kommer att / tänker)",
        "swedish_title": "Futurum: Ska, Kommer att och Tänker",
        "level": "B1",
        "summary": "Expressing intention (ska), prediction based on facts (kommer att), and plans (tänker + infinitiv).",
        "formula": "1. ska + Infinitiv (Avsikt/Beslut) | 2. kommer att + Infinitiv (Prognos) | 3. tänker + Infinitiv (Plan)",
        "signal_words": ["imorgon", "nästa vecka", "i framtiden", "snart", "om några dagar"],
        "timeline_description": "Events projected forward into future time.",
        "examples": [
            {"swedish": "Jag ska resa till Kiruna nästa vecka.", "english": "I am going to travel to Kiruna next week (intention/decision).", "target_highlight": "ska resa"},
            {"swedish": "Det kommer att regna imorgon enligt prognosen.", "english": "It is going to rain tomorrow according to the forecast.", "target_highlight": "kommer att regna"},
            {"swedish": "Vad tänker du göra efter examen?", "english": "What are you planning/thinking of doing after graduation?", "target_highlight": "tänker du göra"}
        ],
        "common_pitfalls": ["Using 'ska' for weather/uncontrolled predictions (say 'Det kommer att regna', NOT 'Det ska regna' unless conveying rumor/intent)."],
        "exercises": [
            {"id": 1341, "type": "fill_gap", "prompt": "Enligt meteorologen ___ det ___ (regna) i helgen.", "options": ["kommer ... att regna", "ska ... regna", "tänker ... regna", "vill ... regna"], "correct_answer": "kommer ... att regna", "explanation": "Forecast predictions use 'kommer att + infinitiv'."},
            {"id": 1342, "type": "multiple_choice", "prompt": "Which expression denotes personal decision/intention?", "options": ["Jag ska börja gymma på måndag.", "Det kommer att snöa.", "Bilen kommer att gå sönder.", "Solen ska gå upp."], "correct_answer": "Jag ska börja gymma på måndag.", "explanation": "'Ska' expresses subject's own will or commitment."},
            {"id": 1343, "type": "fill_gap", "prompt": "Vad ___ du ___ (köpa) för födelsedagspresent till Anna?", "options": ["ska ... köpa", "kommer ... köpt", "ska ... köpte", "är ... köpa"], "correct_answer": "ska ... köpa", "explanation": "Inquiring about intention: 'Ska du köpa'."},
            {"id": 1344, "type": "multiple_choice", "prompt": "Difference: 'Jag ska studera' vs 'Jag tänker studera':", "options": ["'Ska' is a firmer decision; 'tänker' expresses an internal plan/thought.", "'Tänker' means the action is already finished.", "'Ska' is only for weather.", "They have completely opposite meanings."], "correct_answer": "'Ska' is a firmer decision; 'tänker' expresses an internal plan/thought.", "explanation": "'Tänker' = plans/intends to; 'ska' = decisive intention or requirement."},
            {"id": 1345, "type": "fill_gap", "prompt": "Tror du att priserna ___ stiga nästa år?", "options": ["kommer att", "ska", "tänker", "måste att"], "correct_answer": "kommer att", "explanation": "General objective price trend prediction uses 'kommer att'."},
            {"id": 1346, "type": "multiple_choice", "prompt": "Inverted future with 'Imorgon':", "options": ["Imorgon ska vi träffa vänner.", "Imorgon vi ska träffa vänner.", "Imorgon ska träffa vi vänner.", "Ska imorgon vi träffa."], "correct_answer": "Imorgon ska vi träffa vänner.", "explanation": "V2 rule: Imorgon (1) + ska (2) + vi (3) + träffa (4)."},
            {"id": 1347, "type": "fill_gap", "prompt": "Jag ___ (inte / komma) på festen på fredag.", "options": ["kommer inte att komma", "ska inte komma", "inte kommer att komma", "kommer att inte komma"], "correct_answer": "kommer inte att komma", "explanation": "Main clause negation: 'kommer inte att komma' (or 'ska inte komma')."},
            {"id": 1348, "type": "multiple_choice", "prompt": "Which auxiliary is followed by 'att + infinitiv'?", "options": ["kommer (kommer att göra)", "ska (ska göra)", "vill (vill göra)", "kan (kan göra)"], "correct_answer": "kommer (kommer att göra)", "explanation": "'Kommer' requires the infinitive marker 'att' in standard Swedish."},
            {"id": 1349, "type": "fill_gap", "prompt": "Vi ___ (tänka) sälja bilen och köpa elcyklar.", "options": ["tänker", "ska tänka", "tänkt", "tänkande"], "correct_answer": "tänker", "explanation": "Tänker + bare infinitive 'sälja'."},
            {"id": 1350, "type": "multiple_choice", "prompt": "Negative subordinate clause order with 'ska': '...eftersom jag ___'", "options": ["...eftersom jag inte ska resa.", "...eftersom jag ska inte resa.", "...eftersom inte ska jag resa.", "...eftersom jag ska resa inte."], "correct_answer": "...eftersom jag inte ska resa.", "explanation": "BIFF rule: 'inte' precedes auxiliary verb 'ska'."}
        ]
    }
]
