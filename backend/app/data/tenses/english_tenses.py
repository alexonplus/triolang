"""
================================================================================
Exhaustive English Verb Tenses Dataset (All 12 Tenses)
================================================================================
Provides the full matrix of all 12 English tenses, formulas, signal markers,
timeline placements, concrete examples, common pitfalls, and 10+ drill exercises per tense.
"""

from typing import List, Dict, Any

ENGLISH_TENSES: List[Dict[str, Any]] = [
    # --------------------------------------------------------------------------
    # 1. PRESENT SIMPLE
    # --------------------------------------------------------------------------
    {
        "id": "en-present-simple",
        "language": "en",
        "time_aspect": "present",
        "title": "Present Simple",
        "swedish_title": "Presens enkel",
        "level": "A1",
        "summary": "Habits, universal scientific facts, regular schedules, and permanent situations.",
        "formula": "Positive: Subject + V1 (-s/-es for he/she/it) | Negative: don't/doesn't + V1 | Question: Do/Does + Subject + V1?",
        "signal_words": ["always", "usually", "often", "sometimes", "never", "every day", "on Mondays"],
        "timeline_description": "Repeated regular events across time or permanent general truths.",
        "examples": [
            {"swedish": "Hon dricker kaffe varje morgon.", "english": "She drinks coffee every morning.", "target_highlight": "drinks"},
            {"swedish": "Solen går upp i öster.", "english": "The sun rises in the east.", "target_highlight": "rises"},
            {"swedish": "De bor inte i London.", "english": "They don't live in London.", "target_highlight": "don't live"}
        ],
        "common_pitfalls": ["Forgetting -s with he/she/it ('he work' -> 'he works').", "Using 'does' + verb with -s ('Does he likes?' -> 'Does he like?')."],
        "exercises": [
            {"id": 1101, "type": "fill_gap", "prompt": "My father ___ (work) at a bank in Manchester.", "options": ["works", "work", "is work", "working"], "correct_answer": "works", "explanation": "3rd person singular adds -s."},
            {"id": 1102, "type": "multiple_choice", "prompt": "Which sentence expresses a general fact?", "options": ["Water boils at 100°C.", "Water is boiling right now.", "Water has boiled.", "Water will boil."], "correct_answer": "Water boils at 100°C.", "explanation": "Present Simple describes universal scientific facts."},
            {"id": 1103, "type": "fill_gap", "prompt": "___ you speak French fluently?", "options": ["Do", "Does", "Are", "Have"], "correct_answer": "Do", "explanation": "Subject 'you' takes auxiliary 'Do'."},
            {"id": 1104, "type": "multiple_choice", "prompt": "Correct negative form: 'He ___ like spicy food.'", "options": ["doesn't", "don't", "is not", "not"], "correct_answer": "doesn't", "explanation": "He/she/it takes 'doesn't + base verb'."},
            {"id": 1105, "type": "fill_gap", "prompt": "The train ___ (depart) at 08:30 every weekday.", "options": ["departs", "depart", "is departing", "departed"], "correct_answer": "departs", "explanation": "Fixed timetables use Present Simple."},
            {"id": 1106, "type": "multiple_choice", "prompt": "Choose the correct sentence:", "options": ["She always arrives on time.", "She arrives always on time.", "She is always arrive on time.", "Always she arrives on time."], "correct_answer": "She always arrives on time.", "explanation": "Frequency adverbs go before the main verb."},
            {"id": 1107, "type": "fill_gap", "prompt": "He ___ (watch) television every evening.", "options": ["watches", "watch", "watchs", "is watch"], "correct_answer": "watches", "explanation": "Verbs ending in -ch add -es."},
            {"id": 1108, "type": "multiple_choice", "prompt": "'Do they know the answer?' — 'Yes, they ___.'", "options": ["do", "know", "does", "are"], "correct_answer": "do", "explanation": "Short answer echoes auxiliary 'do'."},
            {"id": 1109, "type": "fill_gap", "prompt": "Cats ___ (hate) water.", "options": ["hate", "hates", "are hating", "hated"], "correct_answer": "hate", "explanation": "Plural subject 'Cats' takes base form 'hate'."},
            {"id": 1110, "type": "multiple_choice", "prompt": "Convert 'I fly' to third person singular:", "options": ["He flies", "He flys", "He flyes", "He is fly"], "correct_answer": "He flies", "explanation": "Consonant + y changes to -ies."}
        ]
    },

    # --------------------------------------------------------------------------
    # 2. PRESENT CONTINUOUS
    # --------------------------------------------------------------------------
    {
        "id": "en-present-continuous",
        "language": "en",
        "time_aspect": "present",
        "title": "Present Continuous (Progressive)",
        "swedish_title": "Presens pågående (håller på att göra)",
        "level": "A1",
        "summary": "Actions happening right now, temporary states, or definite planned future arrangements.",
        "formula": "Subject + am/is/are + Verb-ing",
        "signal_words": ["now", "at the moment", "right now", "currently", "these days", "look!", "listen!"],
        "timeline_description": "An action unfolding actively around the moment of speaking.",
        "examples": [
            {"swedish": "Jag läser en fantastisk bok just nu.", "english": "I am reading a fantastic book right now.", "target_highlight": "am reading"},
            {"swedish": "Titta! Det snöar.", "english": "Look! It is snowing.", "target_highlight": "is snowing"},
            {"swedish": "Vi träffar tandläkaren imorgon bitti.", "english": "We are seeing the dentist tomorrow morning.", "target_highlight": "are seeing"}
        ],
        "common_pitfalls": ["Using continuous with stative verbs ('I am knowing him' -> 'I know him')."],
        "exercises": [
            {"id": 1111, "type": "fill_gap", "prompt": "Please be quiet, the baby ___ (sleep) right now.", "options": ["is sleeping", "sleeps", "sleep", "slept"], "correct_answer": "is sleeping", "explanation": "'Right now' requires Present Continuous."},
            {"id": 1112, "type": "multiple_choice", "prompt": "Which verb is stative and CANNOT be used in continuous form?", "options": ["know", "run", "eat", "write"], "correct_answer": "know", "explanation": "'Know' is a state verb expressing mental state."},
            {"id": 1113, "type": "fill_gap", "prompt": "They ___ (build) a new shopping center in our neighborhood.", "options": ["are building", "build", "is building", "built"], "correct_answer": "are building", "explanation": "Temporary progressive ongoing project."},
            {"id": 1114, "type": "multiple_choice", "prompt": "What are you doing this evening? — I ___ tennis with Mark.", "options": ["am playing", "play", "played", "have played"], "correct_answer": "am playing", "explanation": "Definite planned arrangement in near future."},
            {"id": 1115, "type": "fill_gap", "prompt": "Look outside! It ___ (rain) heavily.", "options": ["is raining", "rains", "rained", "rain"], "correct_answer": "is raining", "explanation": "Action happening at this exact moment."},
            {"id": 1116, "type": "multiple_choice", "prompt": "Choose the correct sentence:", "options": ["I understand the grammar rule.", "I am understanding the grammar rule.", "I understanding the rule.", "I does understand."], "correct_answer": "I understand the grammar rule.", "explanation": "'Understand' is a stative verb."},
            {"id": 1117, "type": "fill_gap", "prompt": "Why ___ you wearing a winter coat in July?", "options": ["are", "do", "is", "have"], "correct_answer": "are", "explanation": "Continuous question: 'Why are you wearing...'."},
            {"id": 1118, "type": "multiple_choice", "prompt": "Spelling of 'swim' + ing:", "options": ["swimming", "swiming", "swimering", "swim"], "correct_answer": "swimming", "explanation": "CVC syllable doubles final consonant: swimming."},
            {"id": 1119, "type": "fill_gap", "prompt": "Listen! Someone ___ (knock) on the front door.", "options": ["is knocking", "knocks", "knocked", "are knocking"], "correct_answer": "is knocking", "explanation": "'Listen!' draws attention to an immediate ongoing event."},
            {"id": 1120, "type": "multiple_choice", "prompt": "Identify the incorrect usage:", "options": ["She is wanting an ice cream.", "She wants an ice cream.", "She is eating an ice cream.", "She eats ice cream."], "correct_answer": "She is wanting an ice cream.", "explanation": "'Want' is stative and cannot be used in continuous form."}
        ]
    },

    # --------------------------------------------------------------------------
    # 3. PRESENT PERFECT SIMPLE
    # --------------------------------------------------------------------------
    {
        "id": "en-present-perfect",
        "language": "en",
        "time_aspect": "present",
        "title": "Present Perfect Simple",
        "swedish_title": "Perfekt enkel (har gjort)",
        "level": "A2",
        "summary": "Actions connected to the present, life experiences, unfinished periods, and recent results.",
        "formula": "Subject + have/has + Past Participle (V3)",
        "signal_words": ["already", "yet", "ever", "never", "just", "so far", "since", "for", "recently"],
        "timeline_description": "An action occurring at an unspecified past time that has direct impact or connection to the present.",
        "examples": [
            {"swedish": "Jag har redan ätit lunch.", "english": "I have already eaten lunch.", "target_highlight": "have already eaten"},
            {"swedish": "Har du någonsin varit i Japan?", "english": "Have you ever been to Japan?", "target_highlight": "Have you ever been"},
            {"swedish": "Hon har bott här i fem år.", "english": "She has lived here for five years.", "target_highlight": "has lived"}
        ],
        "common_pitfalls": ["Never use with specific past time: 'I have seen him yesterday' is WRONG -> 'I saw him yesterday'."],
        "exercises": [
            {"id": 1121, "type": "fill_gap", "prompt": "I have ___ (see) this movie three times.", "options": ["seen", "saw", "see", "seeing"], "correct_answer": "seen", "explanation": "V3 past participle of 'see' is 'seen'."},
            {"id": 1122, "type": "multiple_choice", "prompt": "Select the correct sentence:", "options": ["He has already finished his homework.", "He finished already his homework.", "He has finished his homework yesterday.", "He is finished his homework."], "correct_answer": "He has already finished his homework.", "explanation": "'Already' is placed between auxiliary 'has' and participle 'finished'."},
            {"id": 1123, "type": "fill_gap", "prompt": "Have you sent the email ___? (negative/question marker)", "options": ["yet", "already", "since", "ago"], "correct_answer": "yet", "explanation": "'Yet' goes at the end of questions and negatives."},
            {"id": 1124, "type": "multiple_choice", "prompt": "Choose 'for' or 'since': 'We have been friends ___ 2012.'", "options": ["since", "for", "from", "during"], "correct_answer": "since", "explanation": "'Since' specifies the starting point in time."},
            {"id": 1125, "type": "fill_gap", "prompt": "She ___ (lose) her keys and cannot open her apartment door.", "options": ["has lost", "lost", "is losing", "was lost"], "correct_answer": "has lost", "explanation": "Present result of past action -> Present Perfect."},
            {"id": 1126, "type": "multiple_choice", "prompt": "Which sentence contains an error?", "options": ["I have visited London in 2019.", "I visited London in 2019.", "I have visited London twice.", "I have just arrived in London."], "correct_answer": "I have visited London in 2019.", "explanation": "Specific year 'in 2019' requires Past Simple 'visited'."},
            {"id": 1127, "type": "fill_gap", "prompt": "They ___ (live) in Madrid for ten years now.", "options": ["have lived", "lived", "are living", "were living"], "correct_answer": "have lived", "explanation": "Duration continuing to present requires Present Perfect."},
            {"id": 1128, "type": "multiple_choice", "prompt": "'Has he gone to Berlin?' means:", "options": ["He is in Berlin now or on his way.", "He visited Berlin and has returned home.", "He was born in Berlin.", "He will never go to Berlin."], "correct_answer": "He is in Berlin now or on his way.", "explanation": "'Gone to' means the subject has not yet returned."},
            {"id": 1129, "type": "fill_gap", "prompt": "I ___ never ___ (taste) caviar before.", "options": ["have ... tasted", "had ... tasted", "did ... taste", "am ... tasting"], "correct_answer": "have ... tasted", "explanation": "'Have never tasted' expresses life experience."},
            {"id": 1130, "type": "multiple_choice", "prompt": "Past participle of 'write':", "options": ["written", "wrote", "writed", "writing"], "correct_answer": "written", "explanation": "Write -> wrote -> written."}
        ]
    },

    # --------------------------------------------------------------------------
    # 4. PRESENT PERFECT CONTINUOUS
    # --------------------------------------------------------------------------
    {
        "id": "en-present-perfect-continuous",
        "language": "en",
        "time_aspect": "present",
        "title": "Present Perfect Continuous",
        "swedish_title": "Perfekt pågående (har hållit på att göra)",
        "level": "B1",
        "summary": "Emphasizing the duration or ongoing process of an activity that started in the past and continues into or impacts the present.",
        "formula": "Subject + have/has been + Verb-ing",
        "signal_words": ["for hours", "since morning", "all day", "how long...?", "lately", "recently"],
        "timeline_description": "An action in continuous progress extending up to the present moment.",
        "examples": [
            {"swedish": "Jag har studerat i tre timmar.", "english": "I have been studying for three hours.", "target_highlight": "have been studying"},
            {"swedish": "Gatorna är blöta eftersom det har regnat hela morgonen.", "english": "The streets are wet because it has been raining all morning.", "target_highlight": "has been raining"},
            {"swedish": "Hur länge har du väntat?", "english": "How long have you been waiting?", "target_highlight": "have you been waiting"}
        ],
        "common_pitfalls": ["Do not use with stative verbs ('I have been knowing him for years' -> 'I have known him')."],
        "exercises": [
            {"id": 1131, "type": "fill_gap", "prompt": "She is exhausted because she ___ (run) for an hour.", "options": ["has been running", "has run", "is running", "runs"], "correct_answer": "has been running", "explanation": "Emphasizes the duration of the physical activity."},
            {"id": 1132, "type": "multiple_choice", "prompt": "How long ___ you ___ English?", "options": ["have ... been learning", "are ... learning", "did ... learn", "have ... learned"], "correct_answer": "have ... been learning", "explanation": "'How long' asking about ongoing duration takes Present Perfect Continuous."},
            {"id": 1133, "type": "fill_gap", "prompt": "It ___ (snow) non-stop since yesterday evening.", "options": ["has been snowing", "is snowing", "snowed", "was snowing"], "correct_answer": "has been snowing", "explanation": "Continuous weather event continuing up to now."},
            {"id": 1134, "type": "multiple_choice", "prompt": "Compare: 'I have painted the kitchen' vs 'I have been painting the kitchen':", "options": ["'have painted' means the job is finished; 'have been painting' emphasizes the ongoing activity.", "'have been painting' means it is finished; 'have painted' means ongoing.", "Both mean the kitchen is 100% finished.", "Both are ungrammatical."], "correct_answer": "'have painted' means the job is finished; 'have been painting' emphasizes the ongoing activity.", "explanation": "Simple focuses on completion/result; continuous focuses on the activity duration."},
            {"id": 1135, "type": "fill_gap", "prompt": "My hands are dirty because I ___ (repair) the bicycle.", "options": ["have been repairing", "repaired", "had repaired", "am repair"], "correct_answer": "have been repairing", "explanation": "Present physical evidence resulting from a recent continuous activity."},
            {"id": 1136, "type": "multiple_choice", "prompt": "Choose the correct sentence with stative verb:", "options": ["I have had this car for five years.", "I have been having this car for five years.", "I am having this car for five years.", "I have been having had this car."], "correct_answer": "I have had this car for five years.", "explanation": "Possession 'have' is stative and uses Present Perfect Simple."},
            {"id": 1137, "type": "fill_gap", "prompt": "They ___ (argue) about the decision all afternoon.", "options": ["have been arguing", "are arguing", "argued", "have argued"], "correct_answer": "have been arguing", "explanation": "'All afternoon' duration emphasizing ongoing process."},
            {"id": 1138, "type": "multiple_choice", "prompt": "Which time expression fits best?", "options": ["He has been coughing all morning.", "He has been coughing yesterday.", "He has been coughing in 2020.", "He has been coughing two days ago."], "correct_answer": "He has been coughing all morning.", "explanation": "'All morning' represents an unbroken duration touching the present."},
            {"id": 1139, "type": "fill_gap", "prompt": "We ___ (wait) here for over forty minutes!", "options": ["have been waiting", "wait", "are waiting", "waited"], "correct_answer": "have been waiting", "explanation": "Frustration over prolonged ongoing duration."},
            {"id": 1140, "type": "multiple_choice", "prompt": "Complete: 'Why are your clothes wet?' — 'I ___.'", "options": ["have been washing the dog", "have washed the dog yesterday", "wash the dog", "was wash the dog"], "correct_answer": "have been washing the dog", "explanation": "Explaining immediate physical state via recent continuous activity."}
        ]
    },

    # --------------------------------------------------------------------------
    # 5. PAST SIMPLE
    # --------------------------------------------------------------------------
    {
        "id": "en-past-simple",
        "language": "en",
        "time_aspect": "past",
        "title": "Past Simple",
        "swedish_title": "Preteritum / Dåtid (gjorde)",
        "level": "A2",
        "summary": "Completed events occurring at a definitive, finished time in the past.",
        "formula": "Regular: Verb-ed | Irregular: V2 form | Negative: didn't + V1 | Question: Did + Subject + V1?",
        "signal_words": ["yesterday", "last week", "in 1999", "ago", "when I was young", "at that moment"],
        "timeline_description": "A single or sequential finished point in the past.",
        "examples": [
            {"swedish": "Vi besökte Rom förra året.", "english": "We visited Rome last year.", "target_highlight": "visited"},
            {"swedish": "Han kom inte till mötet igår.", "english": "He didn't come to the meeting yesterday.", "target_highlight": "didn't come"},
            {"swedish": "När köpte du den här datorn?", "english": "When did you buy this computer?", "target_highlight": "did you buy"}
        ],
        "common_pitfalls": ["Adding -ed after 'didn't' ('didn't went' -> 'didn't go')."],
        "exercises": [
            {"id": 1141, "type": "fill_gap", "prompt": "William Shakespeare ___ (write) Hamlet around 1600.", "options": ["wrote", "written", "writes", "has written"], "correct_answer": "wrote", "explanation": "Past Simple V2 of 'write' is 'wrote'."},
            {"id": 1142, "type": "multiple_choice", "prompt": "Select the correct negative question:", "options": ["Why didn't you call me last night?", "Why didn't you called me last night?", "Why you didn't call me last night?", "Why not you called me?"], "correct_answer": "Why didn't you call me last night?", "explanation": "Auxiliary 'didn't' + subject 'you' + bare infinitive 'call'."},
            {"id": 1143, "type": "fill_gap", "prompt": "We ___ (buy) our house three years ago.", "options": ["bought", "buyed", "have bought", "had bought"], "correct_answer": "bought", "explanation": "Irregular past of 'buy' is 'bought'."},
            {"id": 1144, "type": "multiple_choice", "prompt": "Which word indicates Past Simple?", "options": ["ago", "since", "so far", "already"], "correct_answer": "ago", "explanation": "'Ago' always anchors an action to a finished past point in time."},
            {"id": 1145, "type": "fill_gap", "prompt": "She ___ (teach) history at Oxford for twenty years before retiring.", "options": ["taught", "teached", "has taught", "was teach"], "correct_answer": "taught", "explanation": "Completed historical career period."},
            {"id": 1146, "type": "multiple_choice", "prompt": "Convert 'I see him' to Past Simple negative:", "options": ["I didn't see him.", "I didn't saw him.", "I not saw him.", "I hadn't saw him."], "correct_answer": "I didn't see him.", "explanation": "Bare infinitive 'see' follows 'didn't'."},
            {"id": 1147, "type": "fill_gap", "prompt": "What time ___ the concert end last night?", "options": ["did", "was", "does", "had"], "correct_answer": "did", "explanation": "Past simple question uses auxiliary 'did'."},
            {"id": 1148, "type": "multiple_choice", "prompt": "Irregular past of 'catch':", "options": ["caught", "catched", "caughted", "cot"], "correct_answer": "caught", "explanation": "Catch -> caught."},
            {"id": 1149, "type": "fill_gap", "prompt": "Suddenly the lights ___ (go) out.", "options": ["went", "gone", "goed", "was gone"], "correct_answer": "went", "explanation": "Past simple V2 of 'go' is 'went'."},
            {"id": 1150, "type": "multiple_choice", "prompt": "Identify the sequential past narrative:", "options": ["He opened the door, looked around, and entered.", "He was opening the door, has looked, and enters.", "He had opened, is looking, and entered.", "He opens, looked, and had entered."], "correct_answer": "He opened the door, looked around, and entered.", "explanation": "Chain of consecutive completed past actions uses Past Simple."}
        ]
    },

    # --------------------------------------------------------------------------
    # 6. PAST CONTINUOUS
    # --------------------------------------------------------------------------
    {
        "id": "en-past-continuous",
        "language": "en",
        "time_aspect": "past",
        "title": "Past Continuous (Progressive)",
        "swedish_title": "Preteritum pågående (höll på att göra)",
        "level": "A2",
        "summary": "An ongoing backdrop action in progress at a specific past moment, often interrupted by a Past Simple event.",
        "formula": "Subject + was/were + Verb-ing",
        "signal_words": ["while", "as", "at 8 PM last night", "when (for interruption)", "all evening yesterday"],
        "timeline_description": "An action was ongoing in the past when another shorter event intervened.",
        "examples": [
            {"swedish": "Jag lagade mat när telefonen ringde.", "english": "I was cooking dinner when the phone rang.", "target_highlight": "was cooking ... rang"},
            {"swedish": "Medan hon läste, lyssnade han på musik.", "english": "While she was reading, he was listening to music.", "target_highlight": "was reading ... was listening"},
            {"swedish": "Vad gjorde du klockan 20:00 igår?", "english": "What were you doing at 8 PM yesterday?", "target_highlight": "were you doing"}
        ],
        "common_pitfalls": ["Confusing 'while' (continuous background) with 'when' (interruption point)."],
        "exercises": [
            {"id": 1151, "type": "fill_gap", "prompt": "While I ___ (walk) in the park, I found a gold ring.", "options": ["was walking", "walked", "have walked", "am walking"], "correct_answer": "was walking", "explanation": "Continuous background action introduced by 'While'."},
            {"id": 1152, "type": "multiple_choice", "prompt": "Select the correct combination:", "options": ["The lights went out while we were having dinner.", "The lights were going out while we had dinner.", "The lights went out while we had dinner.", "The lights had gone while we were having."], "correct_answer": "The lights went out while we were having dinner.", "explanation": "Interruption (Past Simple) during an ongoing activity (Past Continuous)."},
            {"id": 1153, "type": "fill_gap", "prompt": "At midnight last night, they ___ (drive) through the mountains.", "options": ["were driving", "drove", "had driven", "have driven"], "correct_answer": "were driving", "explanation": "Ongoing action in progress at a precise past timestamp."},
            {"id": 1154, "type": "multiple_choice", "prompt": "Which sentence shows two simultaneous parallel actions?", "options": ["While Tom was cooking, Anna was setting the table.", "While Tom cooked, Anna set the table.", "Tom cooked when Anna set the table.", "Tom was cooking after Anna set the table."], "correct_answer": "While Tom was cooking, Anna was setting the table.", "explanation": "Parallel ongoing past activities both use Past Continuous."},
            {"id": 1155, "type": "fill_gap", "prompt": "He slipped and fell while he ___ (cross) the icy street.", "options": ["was crossing", "crossed", "crosses", "had crossed"], "correct_answer": "was crossing", "explanation": "Action in progress when slipping occurred."},
            {"id": 1156, "type": "multiple_choice", "prompt": "Was/Were choice: 'The children ___ playing in the garden.'", "options": ["were", "was", "are", "been"], "correct_answer": "were", "explanation": "'The children' is plural (they), requiring 'were'."},
            {"id": 1157, "type": "fill_gap", "prompt": "What ___ you ___ (do) when the earthquake struck?", "options": ["were ... doing", "did ... do", "are ... doing", "had ... done"], "correct_answer": "were ... doing", "explanation": "Inquiring about the activity in progress at the moment of interruption."},
            {"id": 1158, "type": "multiple_choice", "prompt": "Identify the INCORRECT sentence:", "options": ["I was knowing the answer when the teacher asked.", "I knew the answer when the teacher asked.", "I was thinking about the answer when she called.", "I was writing the answer."], "correct_answer": "I was knowing the answer when the teacher asked.", "explanation": "'Know' is stative and cannot take continuous form."},
            {"id": 1159, "type": "fill_gap", "prompt": "The wind ___ (blow) fiercely all through the night.", "options": ["was blowing", "blew", "blown", "is blowing"], "correct_answer": "was blowing", "explanation": "Atmospheric backdrop condition in the past."},
            {"id": 1160, "type": "multiple_choice", "prompt": "Structure of Past Continuous negative with 'she':", "options": ["she was not working", "she were not working", "she did not working", "she had not working"], "correct_answer": "she was not working", "explanation": "She was not (wasn't) + V-ing."}
        ]
    },

    # --------------------------------------------------------------------------
    # 7. PAST PERFECT SIMPLE
    # --------------------------------------------------------------------------
    {
        "id": "en-past-perfect",
        "language": "en",
        "time_aspect": "past",
        "title": "Past Perfect Simple",
        "swedish_title": "Pluskvamperfekt enkel (hade gjort)",
        "level": "B1",
        "summary": "An action that occurred before another specified action or point in the past (the 'past before the past').",
        "formula": "Subject + had + Past Participle (V3)",
        "signal_words": ["by the time", "before", "after", "already", "until then", "never before"],
        "timeline_description": "An action finished earlier than another past event.",
        "examples": [
            {"swedish": "När vi kom till stationen hade tåget redan gått.", "english": "When we arrived at the station, the train had already left.", "target_highlight": "arrived ... had already left"},
            {"swedish": "Hon insåg att hon hade glömt sina nycklar.", "english": "She realized that she had forgotten her keys.", "target_highlight": "had forgotten"},
            {"swedish": "Hade du träffat honom före konferensen?", "english": "Had you met him before the conference?", "target_highlight": "Had you met"}
        ],
        "common_pitfalls": ["Overusing Past Perfect when sequence is already obvious with 'before/after'."],
        "exercises": [
            {"id": 1161, "type": "fill_gap", "prompt": "By the time the police arrived, the thieves ___ (escape).", "options": ["had escaped", "escaped", "have escaped", "were escaping"], "correct_answer": "had escaped", "explanation": "The escape happened BEFORE the police arrival."},
            {"id": 1162, "type": "multiple_choice", "prompt": "Which action happened first? 'The film had already started when we entered the cinema.'", "options": ["The film started first.", "We entered the cinema first.", "Both happened simultaneously.", "Neither happened."], "correct_answer": "The film started first.", "explanation": "Past Perfect ('had started') marks the earlier of two past events."},
            {"id": 1163, "type": "fill_gap", "prompt": "He told me he ___ never ___ (see) the ocean before.", "options": ["had ... seen", "has ... seen", "did ... see", "was ... seeing"], "correct_answer": "had ... seen", "explanation": "Past experience before a past moment."},
            {"id": 1164, "type": "multiple_choice", "prompt": "Select the correct combination:", "options": ["After she had graduated, she moved to London.", "After she graduated, she had moved to London.", "After she has graduated, she moved.", "After she was graduating, she moved."], "correct_answer": "After she had graduated, she moved to London.", "explanation": "Graduation (1st past event = had graduated) preceded moving (2nd past event = moved)."},
            {"id": 1165, "type": "fill_gap", "prompt": "I couldn't get into my apartment because I ___ (lose) my key.", "options": ["had lost", "lost", "have lost", "was losing"], "correct_answer": "had lost", "explanation": "The loss happened prior to trying to enter."},
            {"id": 1166, "type": "multiple_choice", "prompt": "Choose the correct negative form:", "options": ["We hadn't finished the exam when the bell rang.", "We didn't had finished the exam.", "We haven't finished the exam when the bell rang.", "We weren't finished."], "correct_answer": "We hadn't finished the exam when the bell rang.", "explanation": "Had + not + V3."},
            {"id": 1167, "type": "fill_gap", "prompt": "She felt confident because she ___ (study) diligently for weeks.", "options": ["had studied", "studied", "has studied", "studies"], "correct_answer": "had studied", "explanation": "Prior preparation explaining past confidence."},
            {"id": 1168, "type": "multiple_choice", "prompt": "Third conditional if-clause uses Past Perfect:", "options": ["If I had known the answer, I would have told you.", "If I knew the answer, I would have told you.", "If I have known the answer, I would tell you.", "If I had knew the answer, I told you."], "correct_answer": "If I had known the answer, I would have told you.", "explanation": "3rd conditional formula: If + Past Perfect, would have + V3."},
            {"id": 1169, "type": "fill_gap", "prompt": "The grass was yellow because it ___ (not / rain) all summer.", "options": ["had not rained", "has not rained", "did not rain", "was not raining"], "correct_answer": "had not rained", "explanation": "Lack of rain preceded the observed yellow grass."},
            {"id": 1170, "type": "multiple_choice", "prompt": "Past participle of 'bring':", "options": ["brought", "brang", "bringed", "broughted"], "correct_answer": "brought", "explanation": "Bring -> brought -> brought."}
        ]
    },

    # --------------------------------------------------------------------------
    # 8. PAST PERFECT CONTINUOUS
    # --------------------------------------------------------------------------
    {
        "id": "en-past-perfect-continuous",
        "language": "en",
        "time_aspect": "past",
        "title": "Past Perfect Continuous",
        "swedish_title": "Pluskvamperfekt pågående (hade hållit på att göra)",
        "level": "B2",
        "summary": "An ongoing activity that had been in continuous progress up to a specific moment in the past, often explaining a past result.",
        "formula": "Subject + had been + Verb-ing",
        "signal_words": ["for hours before", "had been ... when", "all day prior to", "how long had you been...?"],
        "timeline_description": "Continuous activity leading right up to a reference point in the past.",
        "examples": [
            {"swedish": "De hade kört i sex timmar innan de stannade.", "english": "They had been driving for six hours before they stopped.", "target_highlight": "had been driving"},
            {"swedish": "Hennes ögon var röda eftersom hon hade gråtit.", "english": "Her eyes were red because she had been crying.", "target_highlight": "had been crying"},
            {"swedish": "Vi hade väntat i en timme när bussen äntligen dök upp.", "english": "We had been waiting for an hour when the bus finally appeared.", "target_highlight": "had been waiting"}
        ],
        "common_pitfalls": ["Do not confuse with Past Perfect Simple (which emphasizes completion, not ongoing duration)."],
        "exercises": [
            {"id": 1171, "type": "fill_gap", "prompt": "He was out of breath because he ___ (sprint) for the bus.", "options": ["had been sprinting", "had sprinted", "was sprinting", "has been sprinting"], "correct_answer": "had been sprinting", "explanation": "Explains past physical condition via prior ongoing activity."},
            {"id": 1172, "type": "multiple_choice", "prompt": "Select the correct Past Perfect Continuous sentence:", "options": ["We had been living in Paris for three years when the war broke out.", "We were living in Paris for three years when the war broke out.", "We have been living in Paris for three years.", "We had lived in Paris continuous."], "correct_answer": "We had been living in Paris for three years when the war broke out.", "explanation": "Ongoing duration up until a specific past historical event."},
            {"id": 1173, "type": "fill_gap", "prompt": "How long ___ they ___ (work) on the project before it was canceled?", "options": ["had ... been working", "have ... been working", "were ... working", "did ... work"], "correct_answer": "had ... been working", "explanation": "Inquiring about the duration of work prior to cancellation."},
            {"id": 1174, "type": "multiple_choice", "prompt": "The ground was soaked because it ___ all night.", "options": ["had been raining", "had rained", "has been raining", "was raining"], "correct_answer": "had been raining", "explanation": "Emphasizes the continuous duration of the rainfall."},
            {"id": 1175, "type": "fill_gap", "prompt": "She ___ (practice) the violin for ten years before she joined the orchestra.", "options": ["had been practicing", "has been practicing", "was practicing", "practiced"], "correct_answer": "had been practicing", "explanation": "Unbroken prolonged activity leading to the milestone."},
            {"id": 1176, "type": "multiple_choice", "prompt": "Identify the difference: 'He had written three letters' vs 'He had been writing letters all afternoon':", "options": ["Simple emphasizes 3 completed letters; continuous emphasizes the prolonged activity.", "Continuous emphasizes 3 completed letters.", "Both mean 3 letters were written.", "Both are identical."], "correct_answer": "Simple emphasizes 3 completed letters; continuous emphasizes the prolonged activity.", "explanation": "Quantity/completion = Past Perfect Simple; Duration = Past Perfect Continuous."},
            {"id": 1177, "type": "fill_gap", "prompt": "The musician was exhausted because he ___ (rehearse) since dawn.", "options": ["had been rehearsing", "has been rehearsing", "rehearsed", "was rehearsing"], "correct_answer": "had been rehearsing", "explanation": "'Since dawn' with past result 'was exhausted'."},
            {"id": 1178, "type": "multiple_choice", "prompt": "Negative structure with 'I':", "options": ["I had not been sleeping well before the exam.", "I have not been sleeping well before the exam.", "I was not been sleeping.", "I had not sleeping."], "correct_answer": "I had not been sleeping well before the exam.", "explanation": "Had + not + been + V-ing."},
            {"id": 1179, "type": "fill_gap", "prompt": "They ___ (quarrel) for weeks before they finally made peace.", "options": ["had been quarreling", "quarreled", "were quarreling", "have been quarreling"], "correct_answer": "had been quarreling", "explanation": "Ongoing friction preceding reconciliation."},
            {"id": 1180, "type": "multiple_choice", "prompt": "Why is 'She had been belonging to the club' incorrect?", "options": ["'Belong' is a stative verb and cannot be used in continuous tenses.", "'Belong' requires auxiliary 'is'.", "'Club' is singular.", "'She' takes 'have'."], "correct_answer": "'Belong' is a stative verb and cannot be used in continuous tenses.", "explanation": "Stative verbs do not take continuous aspect."}
        ]
    },

    # --------------------------------------------------------------------------
    # 9. FUTURE SIMPLE
    # --------------------------------------------------------------------------
    {
        "id": "en-future-simple",
        "language": "en",
        "time_aspect": "future",
        "title": "Future Simple (will + Verb)",
        "swedish_title": "Futurum enkel (ska / kommer att göra)",
        "level": "A2",
        "summary": "Instant decisions, spontaneous offers, promises, and predictions based on belief.",
        "formula": "Subject + will + base verb | Negative: won't + Verb | Question: Will + Subject + Verb?",
        "signal_words": ["tomorrow", "next year", "in the future", "I think", "I promise", "probably"],
        "timeline_description": "An action projected to occur at a future point in time.",
        "examples": [
            {"swedish": "Jag hjälper dig med dina väskor.", "english": "I will help you with your bags.", "target_highlight": "will help (spontaneous offer)"},
            {"swedish": "Jag lovar att jag inte ska berätta för någon.", "english": "I promise I won't tell anyone.", "target_highlight": "won't tell (promise)"},
            {"swedish": "Tror du att det kommer att regna imorgon?", "english": "Do you think it will rain tomorrow?", "target_highlight": "will rain (prediction)"}
        ],
        "common_pitfalls": ["Do not use 'will' for already confirmed plans/schedules (use 'going to' or Present Continuous)."],
        "exercises": [
            {"id": 1181, "type": "fill_gap", "prompt": "The phone is ringing. — Don't worry, I ___ (answer) it!", "options": ["will answer", "am answering", "answer", "have answered"], "correct_answer": "will answer", "explanation": "Spontaneous instant decision at the moment of speaking uses 'will'."},
            {"id": 1182, "type": "multiple_choice", "prompt": "Which sentence expresses a promise?", "options": ["I will always support you.", "I am supporting you tomorrow.", "I support you.", "I was supporting you."], "correct_answer": "I will always support you.", "explanation": "'Will' is the standard modal for pledges and promises."},
            {"id": 1183, "type": "fill_gap", "prompt": "I think scientists ___ (find) a cure in the near future.", "options": ["will find", "are finding", "find", "found"], "correct_answer": "will find", "explanation": "Predictions based on personal opinion ('I think') use 'will'."},
            {"id": 1184, "type": "multiple_choice", "prompt": "Negative contraction of 'will not':", "options": ["won't", "willn't", "wont", "wouldn't"], "correct_answer": "won't", "explanation": "Will not = won't."},
            {"id": 1185, "type": "fill_gap", "prompt": "___ you please open the window for me?", "options": ["Will", "Do", "Are", "Have"], "correct_answer": "Will", "explanation": "Polite request uses modal 'Will you...'."},
            {"id": 1186, "type": "multiple_choice", "prompt": "First conditional result clause uses:", "options": ["will + base verb", "would + base verb", "is + V-ing", "had + V3"], "correct_answer": "will + base verb", "explanation": "If + Present Simple, WILL + base verb."},
            {"id": 1187, "type": "fill_gap", "prompt": "Don't touch that hot stove or you ___ (burn) yourself!", "options": ["will burn", "are burning", "burn", "burned"], "correct_answer": "will burn", "explanation": "Warning of immediate consequence."},
            {"id": 1188, "type": "multiple_choice", "prompt": "Compare 'will' vs 'be going to': 'Look at those dark clouds! It ___.'", "options": ["is going to rain", "will rain", "rains", "rained"], "correct_answer": "is going to rain", "explanation": "Predictions based on immediate present physical evidence use 'be going to'."},
            {"id": 1189, "type": "fill_gap", "prompt": "We ___ (not / arrive) before midnight due to traffic.", "options": ["won't arrive", "don't arrive", "aren't arrive", "haven't arrive"], "correct_answer": "won't arrive", "explanation": "Future negative prediction: 'won't arrive'."},
            {"id": 1190, "type": "multiple_choice", "prompt": "Formal offer with 'I' / 'We':", "options": ["Shall I carry your coat?", "Will I carry your coat?", "Do I carry your coat?", "Am I carry your coat?"], "correct_answer": "Shall I carry your coat?", "explanation": "In British/formal English, 'Shall I / Shall we' is used for offers."}
        ]
    },

    # --------------------------------------------------------------------------
    # 10. FUTURE CONTINUOUS
    # --------------------------------------------------------------------------
    {
        "id": "en-future-continuous",
        "language": "en",
        "time_aspect": "future",
        "title": "Future Continuous (will be doing)",
        "swedish_title": "Futurum pågående (kommer att hålla på att göra)",
        "level": "B1",
        "summary": "An action that will be actively unfolding at a specific timestamp in the future.",
        "formula": "Subject + will be + Verb-ing",
        "signal_words": ["this time tomorrow", "at 10 AM on Friday", "in five years' time"],
        "timeline_description": "An ongoing activity in active progression at a future reference point.",
        "examples": [
            {"swedish": "Den här tiden imorgon kommer jag att flyga till New York.", "english": "This time tomorrow I will be flying to New York.", "target_highlight": "will be flying"},
            {"swedish": "Ring inte klockan sju, vi kommer att äta middag då.", "english": "Don't call at seven, we will be having dinner then.", "target_highlight": "will be having"},
            {"swedish": "Kommer du att använda bilen imorgon?", "english": "Will you be using the car tomorrow?", "target_highlight": "Will you be using (polite inquiry)"}
        ],
        "common_pitfalls": ["Confusing Future Continuous with Future Simple."],
        "exercises": [
            {"id": 1191, "type": "fill_gap", "prompt": "This time next week, we ___ (sunbathe) in the Caribbean.", "options": ["will be sunbathing", "will sunbathe", "are sunbathed", "sunbathe"], "correct_answer": "will be sunbathing", "explanation": "Action actively unfolding at a specific future moment."},
            {"id": 1192, "type": "multiple_choice", "prompt": "Select the polite inquiry about someone's routine plan:", "options": ["Will you be passing by the supermarket today?", "Will you pass by the supermarket today?", "Do you pass by?", "Are you passed?"], "correct_answer": "Will you be passing by the supermarket today?", "explanation": "Future Continuous is used to ask politely about plans without putting pressure."},
            {"id": 1193, "type": "fill_gap", "prompt": "At 8 PM tonight, I ___ (watch) the championship final.", "options": ["will be watching", "will watch", "watch", "am watch"], "correct_answer": "will be watching", "explanation": "Ongoing activity during the specified time."},
            {"id": 1194, "type": "multiple_choice", "prompt": "Complete: 'Don't visit him at 3 PM because he ___ an exam.'", "options": ["will be taking", "will take", "takes", "has taken"], "correct_answer": "will be taking", "explanation": "The exam will be actively in progress."},
            {"id": 1195, "type": "fill_gap", "prompt": "In ten years, most people ___ (drive) electric vehicles.", "options": ["will be driving", "will drive", "are driven", "drove"], "correct_answer": "will be driving", "explanation": "Projected continuous ongoing state in future society."},
            {"id": 1196, "type": "multiple_choice", "prompt": "Structure for negative Future Continuous:", "options": ["will not be working", "will be not working", "will not working", "won't working"], "correct_answer": "will not be working", "explanation": "Will not (won't) + be + V-ing."},
            {"id": 1197, "type": "fill_gap", "prompt": "She ___ (wait) for you at the airport arrivals hall.", "options": ["will be waiting", "will wait", "waits", "is waited"], "correct_answer": "will be waiting", "explanation": "Anticipated ongoing waiting action."},
            {"id": 1198, "type": "multiple_choice", "prompt": "Choose the best form for parallel future actions:", "options": ["While you are cooking, I will be cleaning the living room.", "While you cook, I clean.", "While you will cook, I will clean.", "While you cooked, I clean."], "correct_answer": "While you are cooking, I will be cleaning the living room.", "explanation": "Time clause uses Present Continuous; main clause uses Future Continuous."},
            {"id": 1199, "type": "fill_gap", "prompt": "Soon we ___ (celebrate) our twentieth wedding anniversary.", "options": ["will be celebrating", "will celebrate", "celebrated", "are celebrate"], "correct_answer": "will be celebrating", "explanation": "Anticipated joyous ongoing milestone."},
            {"id": 1200, "type": "multiple_choice", "prompt": "Question form with 'they':", "options": ["Will they be attending the seminar?", "Will they attend the seminar?", "Do they attending?", "Are they will attend?"], "correct_answer": "Will they be attending the seminar?", "explanation": "Will + Subject + be + V-ing."}
        ]
    },

    # --------------------------------------------------------------------------
    # 11. FUTURE PERFECT SIMPLE
    # --------------------------------------------------------------------------
    {
        "id": "en-future-perfect",
        "language": "en",
        "time_aspect": "future",
        "title": "Future Perfect Simple",
        "swedish_title": "Futurum exaktum / Fullbordad framtid (kommer att ha gjort)",
        "level": "B2",
        "summary": "An action that will be completed prior to a deadline or specified time in the future.",
        "formula": "Subject + will have + Past Participle (V3)",
        "signal_words": ["by next week", "by the time you arrive", "by 2030", "in two months' time"],
        "timeline_description": "Looking back at a completed event from a vantage point in the future.",
        "examples": [
            {"swedish": "Före fredag kommer jag att ha avslutat rapporten.", "english": "By Friday I will have finished the report.", "target_highlight": "will have finished"},
            {"swedish": "Vid år 2030 kommer staden att ha byggt en ny tunnelbana.", "english": "By 2030 the city will have built a new metro line.", "target_highlight": "will have built"},
            {"swedish": "När du kommer hem kommer barnen att ha somnat.", "english": "When you get home, the children will have gone to sleep.", "target_highlight": "will have gone"}
        ],
        "common_pitfalls": ["Using Present Perfect instead of Future Perfect when referring to future deadlines."],
        "exercises": [
            {"id": 1201, "type": "fill_gap", "prompt": "By next December, we ___ (save) enough money for a down payment.", "options": ["will have saved", "will save", "have saved", "save"], "correct_answer": "will have saved", "explanation": "'By next December' sets a future deadline for completion."},
            {"id": 1202, "type": "multiple_choice", "prompt": "Select the correct Future Perfect sentence:", "options": ["By the time you wake up, I will have left for the airport.", "By the time you will wake up, I will leave.", "By the time you wake up, I have left.", "By the time you woke up, I will leave."], "correct_answer": "By the time you wake up, I will have left for the airport.", "explanation": "Time clause in Present Simple ('wake up') + main clause Future Perfect ('will have left')."},
            {"id": 1203, "type": "fill_gap", "prompt": "In six months, she ___ (graduate) from medical school.", "options": ["will have graduated", "will graduate", "graduates", "has graduated"], "correct_answer": "will have graduated", "explanation": "Completion of degree by the six-month milestone."},
            {"id": 1204, "type": "multiple_choice", "prompt": "Which time phrase ALWAYS signals the Future Perfect?", "options": ["By this time next year", "Yesterday evening", "At the moment", "Every Monday"], "correct_answer": "By this time next year", "explanation": "'By + future time' is the quintessential trigger for Future Perfect."},
            {"id": 1205, "type": "fill_gap", "prompt": "The construction crew ___ (complete) the bridge before the winter sets in.", "options": ["will have completed", "will complete", "completes", "has completed"], "correct_answer": "will have completed", "explanation": "Completion prior to future winter onset."},
            {"id": 1206, "type": "multiple_choice", "prompt": "Negative form with 'they':", "options": ["They won't have received the letter by tomorrow.", "They will haven't received.", "They won't receive had.", "They didn't have received."], "correct_answer": "They won't have received the letter by tomorrow.", "explanation": "Won't + have + V3."},
            {"id": 1207, "type": "fill_gap", "prompt": "By 10 PM tonight, the painters ___ (paint) the entire exterior.", "options": ["will have painted", "will paint", "paint", "are painting"], "correct_answer": "will have painted", "explanation": "Deadline 10 PM marks completed status."},
            {"id": 1208, "type": "multiple_choice", "prompt": "Question form:", "options": ["Will you have read the book before the exam?", "Have you will read the book?", "Will you read have the book?", "Do you will have read?"], "correct_answer": "Will you have read the book before the exam?", "explanation": "Will + Subject + have + V3?"},
            {"id": 1209, "type": "fill_gap", "prompt": "By the end of this year, I ___ (teach) over a thousand students.", "options": ["will have taught", "will teach", "have taught", "teach"], "correct_answer": "will have taught", "explanation": "Accumulated count achieved by the year's end."},
            {"id": 1210, "type": "multiple_choice", "prompt": "Past participle of 'drive':", "options": ["driven", "drove", "drived", "driving"], "correct_answer": "driven", "explanation": "Drive -> drove -> driven."}
        ]
    },

    # --------------------------------------------------------------------------
    # 12. FUTURE PERFECT CONTINUOUS
    # --------------------------------------------------------------------------
    {
        "id": "en-future-perfect-continuous",
        "language": "en",
        "time_aspect": "future",
        "title": "Future Perfect Continuous",
        "swedish_title": "Fullbordad framtid pågående (kommer att ha hållit på att göra)",
        "level": "C1",
        "summary": "Projecting ongoing duration forward to a future point, showing how long an activity will have been underway.",
        "formula": "Subject + will have been + Verb-ing",
        "signal_words": ["by next month ... for five years", "by the time he retires ... for decades", "by midnight ... for 12 hours"],
        "timeline_description": "Measuring continuous duration up to a milestone in the future.",
        "examples": [
            {"swedish": "Nästa år kommer jag att ha bott här i tio år.", "english": "Next year I will have been living here for ten years.", "target_highlight": "will have been living"},
            {"swedish": "Vid pensionen kommer hon att ha undervisat i 40 år.", "english": "By the time she retires, she will have been teaching for 40 years.", "target_highlight": "will have been teaching"},
            {"swedish": "Vid midnatt kommer vi att ha kört i 14 timmar.", "english": "By midnight we will have been driving for 14 hours.", "target_highlight": "will have been driving"}
        ],
        "common_pitfalls": ["Avoid with stative verbs (say 'will have had', not 'will have been having')."],
        "exercises": [
            {"id": 1211, "type": "fill_gap", "prompt": "By next month, Dr. Evans ___ (research) this rare disease for twenty years.", "options": ["will have been researching", "will be researching", "will research", "has researched"], "correct_answer": "will have been researching", "explanation": "Measures ongoing continuous research duration up to next month."},
            {"id": 1212, "type": "multiple_choice", "prompt": "Select the correct Future Perfect Continuous sentence:", "options": ["By 2028, I will have been working at this company for a decade.", "By 2028, I will be working at this company for a decade.", "By 2028, I have been working at this company for a decade.", "By 2028, I will have worked continuous."], "correct_answer": "By 2028, I will have been working at this company for a decade.", "explanation": "Formula: will have been + V-ing + duration ('for a decade') + future benchmark ('By 2028')."},
            {"id": 1213, "type": "fill_gap", "prompt": "When the marathon ends, the runners ___ (run) for over four hours.", "options": ["will have been running", "will run", "are running", "have been running"], "correct_answer": "will have been running", "explanation": "Ongoing athletic exertion measured at the marathon finish."},
            {"id": 1214, "type": "multiple_choice", "prompt": "Why is 'By next year I will have been knowing him for 5 years' incorrect?", "options": ["'Know' is stative and must use Future Perfect Simple ('will have known').", "'Know' takes auxiliary 'is'.", "'Next year' requires Past Simple.", "'5 years' is too long."], "correct_answer": "'Know' is stative and must use Future Perfect Simple ('will have known').", "explanation": "Stative verbs do not take continuous aspect."},
            {"id": 1215, "type": "fill_gap", "prompt": "By midnight, the band ___ (perform) on stage for six consecutive hours.", "options": ["will have been performing", "will perform", "has performed", "is performing"], "correct_answer": "will have been performing", "explanation": "Continuous performance measured at midnight."},
            {"id": 1216, "type": "multiple_choice", "prompt": "Structure of question form:", "options": ["How long will you have been studying by the time you take the bar exam?", "How long have you will been studying?", "Will how long you have studying?", "How long will you studying have been?"], "correct_answer": "How long will you have been studying by the time you take the bar exam?", "explanation": "How long + will + subject + have been + V-ing?"},
            {"id": 1217, "type": "fill_gap", "prompt": "In June, my grandparents ___ (live) in their cottage for half a century.", "options": ["will have been living", "will live", "live", "are living"], "correct_answer": "will have been living", "explanation": "50-year ongoing residence milestone."},
            {"id": 1218, "type": "multiple_choice", "prompt": "Negative structure with 'she':", "options": ["She won't have been waiting long when you arrive.", "She will haven't been waiting.", "She hasn't will been waiting.", "She won't been have waiting."], "correct_answer": "She won't have been waiting long when you arrive.", "explanation": "Won't + have been + V-ing."},
            {"id": 1219, "type": "fill_gap", "prompt": "By the end of the shift, the surgeon ___ (operate) for over twelve hours.", "options": ["will have been operating", "will operate", "operates", "has operated"], "correct_answer": "will have been operating", "explanation": "12-hour continuous surgical operation."},
            {"id": 1220, "type": "multiple_choice", "prompt": "Which element is crucial for Future Perfect Continuous?", "options": ["A future time point + a duration phrase (e.g., By 2030 ... for 10 years)", "Only the word yesterday", "A single instant event", "A past finished timestamp"], "correct_answer": "A future time point + a duration phrase (e.g., By 2030 ... for 10 years)", "explanation": "Requires both a future milestone and an ongoing duration indicator."}
        ]
    }
]
