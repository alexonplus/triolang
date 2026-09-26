"""
================================================================================
English CEFR B2 Grammar Topics
================================================================================
Comprehensive, structured B2 grammar modules with progressive drill exercises.
"""

from typing import List, Dict, Any

ENGLISH_B2_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "en-b2-third-and-mixed-conditionals",
        "language": "en",
        "level": "B2",
        "title": "Third & Mixed Conditionals",
        "swedish_title": "Tredje och blandad konditionalis",
        "summary": "Express counterfactual past regrets (Third Conditional) and connect past decisions to present realities (Mixed Conditionals).",
        "rule_explanation": (
            "1. Third Conditional (Past unreal situation & past outcome):\n"
            "   • Structure: If + Past Perfect (had + V3), would have + Past Participle (V3)\n"
            "   • 'If I had set my alarm, I would not have missed my flight.'\n"
            "   • Used for regrets, missed opportunities, and historical counterfactuals.\n\n"
            "2. Mixed Conditionals (Past action with present result):\n"
            "   • Structure: If + Past Perfect (had + V3), would + base verb (now)\n"
            "   • 'If I had accepted that job offer in 2020, I would be living in London today.'\n"
            "   • (Present condition with past result):\n"
            "   • 'If I were more organised, I wouldn't have forgotten my passport yesterday.'"
        ),
        "formula": "3rd: If + had + V3, would have + V3 | Mixed: If + had + V3, would + Verb (now)",
        "examples": [
            {"swedish": "Om vi hade åkt tidigare, skulle vi inte ha missat tåget.", "english": "If we had left earlier, we would not have missed the train.", "target_highlight": "had left ... would not have missed"},
            {"swedish": "Om jag hade pluggat medicin, skulle jag vara läkare idag.", "english": "If I had studied medicine, I would be a doctor today.", "target_highlight": "had studied ... would be"},
            {"swedish": "Om hon inte hade hjälpt mig, hade jag misslyckats.", "english": "Had she not helped me, I would have failed.", "target_highlight": "Had she not helped"}
        ],
        "common_pitfalls": [
            "Never say 'If I would have known' — use 'If I had known'.",
            "Ensure the result clause uses 'would have + V3' for past results, and 'would + base verb' for present results."
        ],
        "exercises": [
            {
                "id": 901,
                "type": "multiple_choice",
                "prompt": "Complete the 3rd conditional: 'If you had warned me, I ___ the contract.'",
                "options": [
                    "would not have signed",
                    "would not sign",
                    "had not signed",
                    "didn't sign"
                ],
                "correct_answer": "would not have signed",
                "explanation": "3rd conditional requires 'would have + past participle' in the main clause."
            },
            {
                "id": 902,
                "type": "fill_gap",
                "prompt": "If he had taken the earlier train, he ___ (arrive) on time for the interview.",
                "options": ["would have arrived", "would arrive", "had arrived", "arrived"],
                "correct_answer": "would have arrived",
                "explanation": "Unreal past situation and past outcome -> 'would have arrived'."
            },
            {
                "id": 903,
                "type": "multiple_choice",
                "prompt": "Identify the MIXED conditional (past cause, present result):",
                "options": [
                    "If I had won the lottery yesterday, I would be rich today.",
                    "If I had won the lottery yesterday, I would have bought a yacht.",
                    "If I win the lottery, I will buy a yacht.",
                    "If I won the lottery, I would travel."
                ],
                "correct_answer": "If I had won the lottery yesterday, I would be rich today.",
                "explanation": "Past condition ('had won yesterday') affecting present state ('would be rich today')."
            },
            {
                "id": 904,
                "type": "fill_gap",
                "prompt": "We would have gone swimming if the weather ___ (be) warmer.",
                "options": ["had been", "would have been", "was", "were"],
                "correct_answer": "had been",
                "explanation": "3rd conditional if-clause requires Past Perfect ('had been')."
            },
            {
                "id": 905,
                "type": "multiple_choice",
                "prompt": "Which sentence contains an error?",
                "options": [
                    "If I would have known about the traffic, I would have taken the metro.",
                    "If I had known about the traffic, I would have taken the metro.",
                    "Had I known about the traffic, I would have taken the metro.",
                    "If we had left earlier, we wouldn't be late now."
                ],
                "correct_answer": "If I would have known about the traffic, I would have taken the metro.",
                "explanation": "Error: 'would have' cannot be used in the if-clause."
            },
            {
                "id": 906,
                "type": "fill_gap",
                "prompt": "If she ___ (not / study) German in college, she wouldn't be working in Berlin now.",
                "options": ["had not studied", "did not study", "would not study", "has not studied"],
                "correct_answer": "had not studied",
                "explanation": "Mixed conditional past condition: 'had not studied'."
            },
            {
                "id": 907,
                "type": "multiple_choice",
                "prompt": "Complete: 'If they had played better defense, they ___ the championship.'",
                "options": [
                    "might have won",
                    "will win",
                    "win",
                    "would won"
                ],
                "correct_answer": "might have won",
                "explanation": "Modal conditional possibility in the past: 'might have won'."
            },
            {
                "id": 908,
                "type": "fill_gap",
                "prompt": "___ you told me earlier, I would have helped you. (Inversion - Had)",
                "options": ["Had", "If had", "Were", "Did"],
                "correct_answer": "Had",
                "explanation": "Formal inverted 3rd conditional: 'Had you told me...'."
            },
            {
                "id": 909,
                "type": "multiple_choice",
                "prompt": "Transform 'Because I didn't learn Spanish as a child, I don't speak it fluently now':",
                "options": [
                    "If I had learned Spanish as a child, I would speak it fluently now.",
                    "If I learned Spanish as a child, I would have spoken it fluently now.",
                    "If I would have learned Spanish, I will speak it.",
                    "If I had learned Spanish, I would have spoken it now."
                ],
                "correct_answer": "If I had learned Spanish as a child, I would speak it fluently now.",
                "explanation": "Mixed conditional connecting past childhood event to present fluency."
            },
            {
                "id": 910,
                "type": "fill_gap",
                "prompt": "If you had followed the instructions, the machine ___ (not / break).",
                "options": ["would not have broken", "would not break", "had not broken", "did not break"],
                "correct_answer": "would not have broken",
                "explanation": "3rd conditional main clause: 'would not have broken'."
            }
        ]
    }
]
