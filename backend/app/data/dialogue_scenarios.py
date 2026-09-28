"""
================================================================================
TrioLang Conversational Dialogue Scenarios Database
================================================================================
Curated roleplay scenarios for Swedish and English learners with character personas,
context, first-turn AI initiation lines, and suggested vocabulary chips.
"""

from typing import List, Dict, Any

DIALOGUE_SCENARIOS: List[Dict[str, Any]] = [
    # --------------------------------------------------------------------------
    # SWEDISH SCENARIOS (Svenska)
    # --------------------------------------------------------------------------
    {
        "id": "sv-fika-cafe",
        "language": "sv",
        "title": "Fika på Kaféet (Café in Stockholm)",
        "swedish_title": "Fika på kaféet i Stockholm",
        "level": "A1–A2",
        "category": "Daily Life",
        "persona_name": "Linnéa (Barista)",
        "avatar_emoji": "☕",
        "scenario_context": "You are at a cozy café in Gamla Stan, Stockholm. Order a hot drink and traditional Swedish pastries (kanelbulle, kardemummabulle, prinsesstårta) and ask about oat milk or payment.",
        "initial_ai_message": "Hej och varmt välkommen till Kafé Kringlan! Vad får det lov att vara idag?",
        "initial_english_translation": "Hello and a warm welcome to Café Kringlan! What can I get for you today?",
        "suggested_chips": [
            "Hej! Jag vill gärna ha en kaffe och en kanelbulle.",
            "Har ni havremjölk till kaffet?",
            "Vad kostar en kardemummabulle?",
            "Kan jag betala med kort?"
        ],
        "target_grammar": "En/ett nouns, politeness phrases (gärna, tack), presens verbs."
    },
    {
        "id": "sv-bostad-hyra",
        "language": "sv",
        "title": "Bostadsjakt & Hyra Lägenhet (Renting an Apartment)",
        "swedish_title": "Hyra lägenhet i andra hand",
        "level": "B1",
        "category": "Housing & Relocation",
        "persona_name": "Marcus (Hyresvärd)",
        "avatar_emoji": "🏠",
        "scenario_context": "You are inquiring about renting a 2-room apartment in Södermalm. Discuss rent, move-in dates, deposit, and utilities.",
        "initial_ai_message": "Hej! Kul att du är intresserad av lägenheten på Södermalm. Berätta lite om dig själv och när du skulle vilja flytta in?",
        "initial_english_translation": "Hello! Glad that you're interested in the apartment on Södermalm. Tell me a bit about yourself and when you would like to move in?",
        "suggested_chips": [
            "Hej Marcus! Jag jobbar som utvecklare och söker boende från och med nästa månad.",
            "Ingår el, värme och bredband i månadshyran?",
            "Hur stor är depositionen som krävs?",
            "Är det möjligt att komma på en visning i helgen?"
        ],
        "target_grammar": "Subordinate clauses (att, eftersom, när), V2 word order, prepositions."
    },
    {
        "id": "sv-jobbintervju",
        "language": "sv",
        "title": "Jobbintervju (Job Interview)",
        "swedish_title": "Anställningsintervju för ett techbolag",
        "level": "B2",
        "category": "Career & Professional",
        "persona_name": "Helena (Rekryterare)",
        "avatar_emoji": "💼",
        "scenario_context": "You are interviewing for a software development / project role at a Swedish tech startup in Kista. Highlight your experience, team collaboration, and problem-solving skills.",
        "initial_ai_message": "Välkommen hit! Vi är väldigt glada att träffa dig idag. Kan du börja med att berätta kort om din bakgrund och varför du sökte just den här tjänsten?",
        "initial_english_translation": "Welcome here! We are very glad to meet you today. Could you start by briefly telling us about your background and why you applied for this specific role?",
        "suggested_chips": [
            "Tack så mycket! Jag har arbetat med mjukvaruutveckling i fyra år och brinner för Clean Code.",
            "Jag trivs bäst i tvärfunktionella team där man löser komplexa problem tillsammans.",
            "Vilka teknologier och ramverk fokuserar ert team främst på just nu?",
            "Hur ser möjligheterna ut för vidareutbildning och kompetensutveckling hos er?"
        ],
        "target_grammar": "Complex subordinate clauses, s-passive, perfect participle, professional vocabulary."
    },
    {
        "id": "sv-vardcentral",
        "language": "sv",
        "title": "På Vårdcentralen (At the Medical Clinic)",
        "swedish_title": "Läkarbesök och symtombeskrivning",
        "level": "A2–B1",
        "category": "Health & Emergency",
        "persona_name": "Doktor Lindström (Läkare)",
        "avatar_emoji": "🏥",
        "scenario_context": "You are seeing a doctor at the local medical center because you have had a severe fever, sore throat, and cough for several days.",
        "initial_ai_message": "God morgon! Slå dig ner. Vad har du för besvär och hur länge har du känt dig sjuk?",
        "initial_english_translation": "Good morning! Please take a seat. What symptoms are you experiencing and how long have you been feeling unwell?",
        "suggested_chips": [
            "God morgon! Jag har haft hög feber och hosta i tre dagar.",
            "Det gör väldigt ont i halsen när jag sväljer.",
            "Behöver jag ta något receptbelagt läkemedel eller penicillin?",
            "Borde jag stanna hemma från jobbet resten av veckan?"
        ],
        "target_grammar": "Present perfect with duration (har haft i tre dagar), anatomical terms, modal verbs."
    },
    {
        "id": "sv-smaprat-kultur",
        "language": "sv",
        "title": "Småprat om Helgen & Midsommar (Small Talk & Traditions)",
        "swedish_title": "Fredagsfika och helgplaner med kollegan",
        "level": "B1",
        "category": "Social & Cultural",
        "persona_name": "Johan (Kollega)",
        "avatar_emoji": "🇸🇪",
        "scenario_context": "Chat with a Swedish colleague during Friday afternoon fika about weekend plans, weather, and upcoming Swedish holidays.",
        "initial_ai_message": "Äntligen fredag! Har du några roliga planer inför helgen, eller ska du bara ta det lugnt och koppla av?",
        "initial_english_translation": "Finally Friday! Do you have any fun plans for the weekend, or are you just going to take it easy and relax?",
        "suggested_chips": [
            "Ja, äntligen! Jag tänker åka ut i skärgården om vädret tillåter.",
            "Vi ska fira midsommar med några vänner på landet.",
            "Har du något bra tips på sevärdheter eller vandringsleder i närheten?",
            "Vad ska du själv hitta på i helgen?"
        ],
        "target_grammar": "Future expressions (tänker / ska / kommer att), V2 fronted time adverbs."
    },

    # --------------------------------------------------------------------------
    # ENGLISH SCENARIOS
    # --------------------------------------------------------------------------
    {
        "id": "en-restaurant-dinner",
        "language": "en",
        "title": "Dining at a Gourmet Restaurant",
        "swedish_title": "Middag på en fin restaurang",
        "level": "A1–A2",
        "category": "Dining & Food",
        "persona_name": "James (Waiter)",
        "avatar_emoji": "🍽️",
        "scenario_context": "You are having dinner at a top restaurant. Ask for recommendations, specify dietary preferences, and request the bill.",
        "initial_ai_message": "Good evening and welcome to The Garden Bistro! Here are your menus. Would you like to start with something to drink while you look over the specials?",
        "initial_english_translation": "God kväll och välkommen till The Garden Bistro! Här är era menyer. Vill ni börja med något att dricka medan ni tittar på specialrätterna?",
        "suggested_chips": [
            "Good evening! Could we start with some sparkling water with lemon, please?",
            "What do you recommend for the main course tonight?",
            "Is there a vegetarian or gluten-free option available?",
            "Could we please have the bill whenever you have a moment?"
        ],
        "target_grammar": "Polite requests (could/would), continuous while-clauses, food adjectives."
    },
    {
        "id": "en-job-interview-senior",
        "language": "en",
        "title": "Professional Job Interview & Pitch",
        "swedish_title": "Professionell anställningsintervju",
        "level": "B2–C1",
        "category": "Career & Professional",
        "persona_name": "Sarah (Hiring Manager)",
        "avatar_emoji": "💼",
        "scenario_context": "You are interviewing for a senior position. Demonstrate your expertise, leadership philosophy, and handling of complex project deadlines.",
        "initial_ai_message": "Thank you for joining us today! We reviewed your portfolio and were very impressed. Could you walk me through a challenging project where you had to navigate tight deadlines and conflicting stakeholder priorities?",
        "initial_english_translation": "Tack för att du deltar idag! Vi granskade din portfolio och blev mycket imponerade. Kan du berätta om ett utmanande projekt där du navigerade snäva tidsfrister och motstridiga prioriteringar?",
        "suggested_chips": [
            "Thank you, Sarah. In my previous role, I led a cross-functional team through a major product overhaul under a strict quarterly deadline.",
            "I prioritized transparent communication, establishing weekly milestone reviews and agile sprints.",
            "Could you share more about the company's long-term vision and culture for this team?",
            "How does leadership evaluate success and professional development here?"
        ],
        "target_grammar": "Past perfect, participle clauses, sophisticated business English and inversion."
    },
    {
        "id": "en-airport-travel",
        "language": "en",
        "title": "Airport Check-In & Flight Inquiries",
        "swedish_title": "Incheckning och frågor på flygplatsen",
        "level": "A2–B1",
        "category": "Travel & Logistics",
        "persona_name": "Emily (Airline Agent)",
        "avatar_emoji": "✈️",
        "scenario_context": "You are checking in luggage at London Heathrow Airport, inquiring about seat assignments, gate changes, and departure times.",
        "initial_ai_message": "Good afternoon! May I see your passport and flight booking confirmation, please?",
        "initial_english_translation": "God eftermiddag! Får jag be om ditt pass och din bokningsbekräftelse, tack?",
        "suggested_chips": [
            "Good afternoon! Here is my passport and boarding pass on my phone.",
            "I have one suitcase to check in. Is there an extra weight limit?",
            "Is it possible to request a window seat near the front of the aircraft?",
            "Which gate does flight BA-782 depart from and what time is boarding?"
        ],
        "target_grammar": "Modal auxiliaries (may/could/is it possible to), travel vocabulary."
    }
]
