"""
================================================================================
TrioLang Dialogue Service & Real-Time Grammar Correction Engine
================================================================================
CLEAN ARCHITECTURE - CONVERSATIONAL ROLEPLAY LAYER
Manages multi-turn roleplay conversations, AI first-turn initiation,
real-time grammatical error detection, native rephrasing, and SQLite mistake logging.
"""

import json
import re
import logging
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session

from app.core.config import settings
from app.data.dialogue_scenarios import DIALOGUE_SCENARIOS
from app.models.schemas import (
    DialogueScenarioSummary,
    DialogueTurnMessage,
    GrammarCorrectionFeedback,
    DialogueStartResponse,
    DialogueTurnResponse,
)
from app.services.ai_memory_service import AIMemoryService

logger = logging.getLogger(__name__)


class DialogueService:
    """
    Domain service handling conversational simulations and real-time grammar feedback.
    """

    @staticmethod
    def get_scenarios(language: Optional[str] = None) -> List[DialogueScenarioSummary]:
        """
        List all available dialogue roleplay scenarios filtered by language.
        """
        filtered = DIALOGUE_SCENARIOS
        if language:
            filtered = [s for s in filtered if s["language"] == language.lower()]

        return [
            DialogueScenarioSummary(
                id=s["id"],
                language=s["language"],
                title=s["title"],
                swedish_title=s["swedish_title"],
                level=s["level"],
                category=s["category"],
                persona_name=s["persona_name"],
                avatar_emoji=s["avatar_emoji"],
                scenario_context=s["scenario_context"],
                suggested_chips=s.get("suggested_chips", []),
                target_grammar=s.get("target_grammar", ""),
            )
            for s in filtered
        ]

    @classmethod
    def start_dialogue(
        cls,
        scenario_id: str,
        custom_topic: Optional[str] = None,
        language: str = "sv",
    ) -> DialogueStartResponse:
        """
        Initiate a dialogue simulation: computer speaks first.
        """
        scenario = next((s for s in DIALOGUE_SCENARIOS if s["id"] == scenario_id), None)

        if scenario:
            initial_turn = DialogueTurnMessage(
                sender="AI",
                text=scenario["initial_ai_message"],
                translation=scenario.get("initial_english_translation"),
            )
            return DialogueStartResponse(
                scenario_id=scenario["id"],
                persona_name=scenario["persona_name"],
                avatar_emoji=scenario["avatar_emoji"],
                scenario_title=scenario["title"],
                initial_message=initial_turn,
                suggested_chips=scenario.get("suggested_chips", []),
            )

        # Custom user-defined scenario fallback
        is_sv = language == "sv"
        title = custom_topic or ("Custom Dialogue" if not is_sv else "Eget samtalsämne")
        persona = "TrioBot Conversationalist"
        avatar = "🤖"
        opening = (
            f"Hej! Jag ser fram emot att prata om '{title}'. Hur vill du att vi börjar?"
            if is_sv
            else f"Hello! I look forward to chatting about '{title}'. How would you like to start?"
        )
        chips = (
            ["Hej! Låt oss börja.", "Vad tycker du om det här ämnet?", "Kan du berätta mer?"]
            if is_sv
            else ["Hello! Let's get started.", "What do you think about this topic?", "Tell me more."]
        )

        return DialogueStartResponse(
            scenario_id="custom",
            persona_name=persona,
            avatar_emoji=avatar,
            scenario_title=title,
            initial_message=DialogueTurnMessage(sender="AI", text=opening),
            suggested_chips=chips,
        )

    @classmethod
    async def process_turn(
        cls,
        db: Session,
        user_id: int,
        scenario_id: str,
        user_message: str,
        language: str = "sv",
        history: List[DialogueTurnMessage] = None,
        custom_topic: Optional[str] = None,
    ) -> DialogueTurnResponse:
        """
        Process a learner reply: generates in-character reply and checks for grammatical errors.
        """
        scenario = next((s for s in DIALOGUE_SCENARIOS if s["id"] == scenario_id), None)
        scenario_title = scenario["title"] if scenario else (custom_topic or "Roleplay Dialogue")
        persona = scenario["persona_name"] if scenario else "TrioBot AI"

        # Check if Gemini API is configured
        if settings.GEMINI_API_KEY and settings.GEMINI_API_KEY != "your-gemini-api-key-here":
            try:
                ai_response = await cls._generate_gemini_turn(
                    scenario_title=scenario_title,
                    persona=persona,
                    language=language,
                    user_message=user_message,
                    history=history or [],
                )
                if ai_response:
                    # Log mistake into DB if grammar errors were flagged
                    if ai_response.correction_feedback and ai_response.correction_feedback.has_errors:
                        AIMemoryService.log_mistake(
                            db=db,
                            user_id=user_id,
                            topic_or_tense_id=scenario_id,
                            language=language,
                            prompt_text=f"Dialogue context: {scenario_title}",
                            user_answer=user_message,
                            correct_answer=ai_response.correction_feedback.corrected_text or "",
                            explanation=ai_response.correction_feedback.grammar_rule_explanation,
                        )
                    return ai_response
            except Exception as err:
                logger.warning(f"Gemini conversational turn error: {err}")

        # Fallback offline linguistic heuristic engine
        fallback_response = cls._generate_fallback_turn(
            scenario=scenario,
            scenario_title=scenario_title,
            persona=persona,
            language=language,
            user_message=user_message,
            history=history or [],
        )

        if fallback_response.correction_feedback and fallback_response.correction_feedback.has_errors:
            AIMemoryService.log_mistake(
                db=db,
                user_id=user_id,
                topic_or_tense_id=scenario_id,
                language=language,
                prompt_text=f"Dialogue context: {scenario_title}",
                user_answer=user_message,
                correct_answer=fallback_response.correction_feedback.corrected_text or "",
                explanation=fallback_response.correction_feedback.grammar_rule_explanation,
            )

        return fallback_response

    @classmethod
    async def _generate_gemini_turn(
        cls,
        scenario_title: str,
        persona: str,
        language: str,
        user_message: str,
        history: List[DialogueTurnMessage],
    ) -> Optional[DialogueTurnResponse]:
        """
        Invoke Google Gemini API for simultaneous roleplay continuation and pedagogical grammar analysis.
        """
        import google.generativeai as genai

        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")

        history_text = "\n".join(
            [f"{turn.sender}: {turn.text}" for turn in history[-6:]]
        )

        prompt = (
            f"You are roleplaying as {persona} in the scenario: '{scenario_title}'.\n"
            f"Target Language: {language} (Swedish if 'sv', English if 'en').\n\n"
            f"Recent Dialogue History:\n{history_text}\n"
            f"User just said: \"{user_message}\"\n\n"
            f"Instructions:\n"
            f"1. Respond IN CHARACTER naturally in {language} as {persona}.\n"
            f"2. Carefully analyze the user's message for any grammatical, word order, spelling, or article mistakes.\n"
            f"3. Suggest 2-3 short, natural follow-up response phrases in {language} for the user.\n\n"
            f"Respond ONLY with valid JSON in this exact structure (no markdown fences):\n"
            f"{{\n"
            f'  "ai_reply_text": "In-character reply...",\n'
            f'  "ai_reply_translation": "English translation...",\n'
            f'  "has_errors": false,\n'
            f'  "corrected_text": "Corrected sentence if has_errors is true, else null",\n'
            f'  "grammar_rule_explanation": "Explanation of the grammar rule if errors found, else null",\n'
            f'  "improved_native_alternative": "More natural phrasing if applicable",\n'
            f'  "highlighted_issues": ["Issue 1", "Issue 2"],\n'
            f'  "suggested_next_chips": ["Option 1", "Option 2", "Option 3"]\n'
            f"}}"
        )

        response = model.generate_content(prompt)
        raw_text = response.text.strip()
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]

        data = json.loads(raw_text.strip())

        correction = None
        if data.get("has_errors") or data.get("grammar_rule_explanation"):
            correction = GrammarCorrectionFeedback(
                has_errors=data.get("has_errors", False),
                original_text=user_message,
                corrected_text=data.get("corrected_text"),
                grammar_rule_explanation=data.get("grammar_rule_explanation"),
                improved_native_alternative=data.get("improved_native_alternative"),
                highlighted_issues=data.get("highlighted_issues", []),
            )

        ai_turn = DialogueTurnMessage(
            sender="AI",
            text=data.get("ai_reply_text", "Tack för ditt svar!"),
            translation=data.get("ai_reply_translation"),
            correction_feedback=correction,
        )

        return DialogueTurnResponse(
            ai_reply=ai_turn,
            correction_feedback=correction,
            suggested_next_chips=data.get("suggested_next_chips", []),
        )

    @classmethod
    def _generate_fallback_turn(
        cls,
        scenario: Optional[Dict[str, Any]],
        scenario_title: str,
        persona: str,
        language: str,
        user_message: str,
        history: List[DialogueTurnMessage],
    ) -> DialogueTurnResponse:
        """
        Intelligent offline heuristic correction engine & conversational generator.
        Detects V2 inversion errors, gender/article agreement, and common grammar traps.
        """
        user_lower = user_message.lower().strip()
        has_error = False
        corrected_text = None
        rule_explanation = None
        improved_alt = None
        issues: List[str] = []

        # ----------------------------------------------------------------------
        # Swedish Grammar Heuristic Analysis
        # ----------------------------------------------------------------------
        if language == "sv":
            # 1. V2 word order check after fronted time/place adverbs
            v2_triggers = ["igår", "idag", "imorgon", "nu", "på måndag", "därför", "ibland", "förra veckan", "i sverige"]
            for trigger in v2_triggers:
                # Match e.g. "igår jag åkte" or "nu vi ska"
                pattern = rf"\b({re.escape(trigger)})\s+(jag|du|han|hon|vi|ni|de)\s+([a-zåäö]+)"
                match = re.search(pattern, user_message, flags=re.IGNORECASE)
                if match:
                    matched_trigger = match.group(1)
                    pronoun = match.group(2)
                    verb = match.group(3)
                    has_error = True
                    issues.append("V2-ordföljd (Inversion)")
                    corrected_text = (
                        user_message[:match.start()]
                        + f"{matched_trigger} {verb} {pronoun}"
                        + user_message[match.end():]
                    )
                    rule_explanation = (
                        f"V2-regeln: När en mening inleds med ett tids- eller rumsadverb ('{matched_trigger}'), "
                        f"måste det finita verbet ('{verb}') komma före subjektet ('{pronoun}')."
                    )
                    improved_alt = f"{matched_trigger} {verb} {pronoun}..."
                    break

            # 2. En vs Ett article errors
            if not has_error:
                if "ett kaffe" in user_lower:
                    has_error = True
                    issues.append("Genusfel (En kaffe)")
                    corrected_text = user_message.replace("ett kaffe", "en kaffe").replace("Ett kaffe", "En kaffe")
                    rule_explanation = "Kaffe beställs som utrum substantiv ('en kaffe' = en kopp kaffe)."
                elif "en hus" in user_lower:
                    has_error = True
                    issues.append("Genusfel (Ett hus)")
                    corrected_text = user_message.replace("en hus", "ett hus")
                    rule_explanation = "'Hus' är ett neutrumord ('ett hus')."
                elif "en bord" in user_lower:
                    has_error = True
                    issues.append("Genusfel (Ett bord)")
                    corrected_text = user_message.replace("en bord", "ett bord")
                    rule_explanation = "'Bord' är ett neutrumord ('ett bord')."

            # Conversational reply generation for Swedish scenarios
            if "fika" in (scenario.get("id") if scenario else "") or "kaffe" in user_lower:
                ai_text = "Javisst, det ordnar jag direkt! Vill du sitta här eller ta med i farten?"
                ai_trans = "Certainly, I'll get that for you right away! Would you like to sit here or take away?"
                next_chips = ["Jag vill sitta här, tack.", "Ta med, tack!", "Kan jag få kvittot?"]
            elif "hyra" in user_lower or "lägenhet" in user_lower or "bostad" in (scenario.get("id") if scenario else ""):
                ai_text = "Det låter utmärkt! Lägenheten är ledig från första november och vi kan boka in en visning på söndag. Passar det?"
                ai_trans = "That sounds great! The apartment is available from November 1st and we can schedule a viewing on Sunday. Does that suit you?"
                next_chips = ["Ja, söndag klockan 14 passar perfekt.", "Finns det parkeringsplats tillgänglig?", "Hur lång är uppsägningstiden?"]
            elif "intervju" in (scenario.get("id") if scenario else "") or "erfarenhet" in user_lower or "jobb" in user_lower:
                ai_text = "Mycket intressant! Hur hanterar du situationer där prioriteringar plötsligt förändras under en sprint?"
                ai_trans = "Very interesting! How do you handle situations where priorities suddenly change during a sprint?"
                next_chips = ["Jag fokuserar på tydlig kommunikation med produktägaren och teamet.", "Vi omvärderar kraven och anpassar backloggen.", "Jag behåller lugnet och prioriterar de viktigaste leverablerna."]
            elif "ont" in user_lower or "feber" in user_lower or "läkare" in user_lower:
                ai_text = "Jag förstår. Låt mig ta en titt i halsen och lyssna på dina lungor. Har du tagit någon febernedsättande medicin som Alvedon?"
                ai_trans = "I understand. Let me examine your throat and listen to your lungs. Have you taken any fever-reducing medication like Paracetamol?"
                next_chips = ["Ja, jag tog en Alvedon i morse.", "Nej, jag har inte tagit någon medicin ännu.", "Hur länge smittar det här?"]
            else:
                ai_text = "Tack för ditt svar! Det låter mycket bra. Vad tänker du om nästa steg?"
                ai_trans = "Thank you for your reply! That sounds very good. What are your thoughts on the next step?"
                next_chips = ["Jag håller helt med.", "Kan du berätta lite mer om detaljerna?", "Tack för hjälpen!"]

        # ----------------------------------------------------------------------
        # English Grammar Heuristic Analysis
        # ----------------------------------------------------------------------
        else:
            if "didn't went" in user_lower:
                has_error = True
                issues.append("Past Simple with Auxiliary")
                corrected_text = user_message.replace("didn't went", "didn't go")
                rule_explanation = "After auxiliary 'didn't', always use the bare infinitive ('didn't go', not 'didn't went')."
            elif "he don't" in user_lower:
                has_error = True
                issues.append("3rd Person Singular Agreement")
                corrected_text = user_message.replace("he don't", "he doesn't")
                rule_explanation = "Third person singular (he/she/it) requires 'doesn't', not 'don't'."
            elif "i have saw" in user_lower:
                has_error = True
                issues.append("Past Participle V3")
                corrected_text = user_message.replace("I have saw", "I have seen").replace("i have saw", "i have seen")
                rule_explanation = "Present perfect uses the V3 past participle ('have seen', not 'have saw')."

            if "menu" in user_lower or "drink" in user_lower or "water" in user_lower or "recommend" in user_lower:
                ai_text = "Certainly! Tonight our chef's special is grilled sea bass with herbs. Would you like a starter as well?"
                ai_trans = "Självklart! Ikväll är kockens specialitet grillad havsabborre med örter. Önskar ni en förrätt också?"
                next_chips = ["Yes, we would love to start with the soup.", "Just the main course for now, please.", "Do you have any gluten-free desserts?"]
            else:
                ai_text = "That sounds wonderful. Tell me more about your thoughts on this!"
                ai_trans = "Det låter underbart. Berätta mer om dina tankar kring detta!"
                next_chips = ["I completely agree.", "Could you elaborate on that?", "Thank you for the recommendation."]

        correction = None
        if has_error:
            correction = GrammarCorrectionFeedback(
                has_errors=True,
                original_text=user_message,
                corrected_text=corrected_text or user_message,
                grammar_rule_explanation=rule_explanation,
                improved_native_alternative=improved_alt,
                highlighted_issues=issues,
            )

        ai_turn = DialogueTurnMessage(
            sender="AI",
            text=ai_text,
            translation=ai_trans,
            correction_feedback=correction,
        )

        return DialogueTurnResponse(
            ai_reply=ai_turn,
            correction_feedback=correction,
            suggested_next_chips=next_chips,
        )
