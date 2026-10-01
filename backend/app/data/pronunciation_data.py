"""
================================================================================
TrioLang Pronunciation & Phonetics Dataset
================================================================================
Comprehensive phonetic guides, minimal pairs, soft/hard vowel rules,
and pitch accent contrast pairs for Swedish and English.
"""

from typing import Dict, List, Any

PRONUNCIATION_DATA: Dict[str, Any] = {
    "sv": {
        "vowel_length_rule": {
            "title": "Vokallängd: Lång vs. Kort Vokal",
            "description": "I svenskan är betonade vokaler antingen långa eller korta. Regeln är enkel: Följs vokalen av EN konsonant är den LÅNG. Följs den av TVÅ eller fler konsonanter är den KORT.",
            "formula": "1 konsonant = Lång vokal [V:]  |  2+ konsonanter = Kort vokal [V]",
            "minimal_pairs": [
                {
                    "pair_id": "mat-matt",
                    "long_word": "mat",
                    "long_ipa": "[ma:t]",
                    "long_translation": "food",
                    "long_audio_text": "mat",
                    "short_word": "matt",
                    "short_ipa": "[mat:]",
                    "short_translation": "faint / exhausted / carpet",
                    "short_audio_text": "matt",
                    "explanation": "'Mat' har en konsonant (t) -> långt a. 'Matt' har dubbelkonsonant (tt) -> kort a.",
                },
                {
                    "pair_id": "glas-glass",
                    "long_word": "glas",
                    "long_ipa": "[gla:s]",
                    "long_translation": "glass (cup/pane)",
                    "long_audio_text": "glas",
                    "short_word": "glass",
                    "short_ipa": "[glas:]",
                    "short_translation": "ice cream",
                    "short_audio_text": "glass",
                    "explanation": "'Glas' = dricksglas med långt a. 'Glass' = ätbar glass med kort a och dubbel-s.",
                },
                {
                    "pair_id": "tak-tack",
                    "long_word": "tak",
                    "long_ipa": "[ta:k]",
                    "long_translation": "roof / ceiling",
                    "long_audio_text": "tak",
                    "short_word": "tack",
                    "short_ipa": "[tak:]",
                    "short_translation": "thank you",
                    "short_audio_text": "tack",
                    "explanation": "'Tak' har långt a. 'Tack' följs av 'ck' som räknas som dubbelkonsonant -> kort a.",
                },
                {
                    "pair_id": "ful-full",
                    "long_word": "ful",
                    "long_ipa": "[fʉ:l]",
                    "long_translation": "ugly",
                    "long_audio_text": "ful",
                    "short_word": "full",
                    "short_ipa": "[fɵl:]",
                    "short_translation": "drunk / full",
                    "short_audio_text": "full",
                    "explanation": "'Ful' har det unika svenska långa u-ljudet [ʉ:]. 'Full' har kort u [ɵ].",
                },
                {
                    "pair_id": "sil-sill",
                    "long_word": "sil",
                    "long_ipa": "[si:l]",
                    "long_translation": "strainer / sieve",
                    "long_audio_text": "sil",
                    "short_word": "sill",
                    "short_ipa": "[sɪl:]",
                    "short_translation": "herring (traditional Swedish fish)",
                    "short_audio_text": "sill",
                    "explanation": "'Sil' har långt i. 'Sill' har kort i och dubbel-l.",
                },
            ],
        },
        "vowel_groups": {
            "hard_vowels": {
                "title": "Hårda Vokaler (A, O, U, Å)",
                "vowels": ["A", "O", "U", "Å"],
                "rule": "Framför hårda vokaler uttalas K, G och SK med sina hårda standardljud [k], [g], [sk].",
                "examples": [
                    {"word": "kaka", "pronunciation": "[kaka]", "translation": "cake / cookie"},
                    {"word": "gata", "pronunciation": "[gata]", "translation": "street"},
                    {"word": "skola", "pronunciation": "[skula]", "translation": "school"},
                ],
            },
            "soft_vowels": {
                "title": "Mjuka Vokaler (E, I, Y, Ä, Ö)",
                "vowels": ["E", "I", "Y", "Ä", "Ö"],
                "rule": "Framför mjuka vokaler mjuknar konsonanterna: K blir [tj/ɕ] (t.ex. kök, kyrka), G blir [j] (t.ex. göra, gilla), och SK blir sje-ljudet [ɧ] (t.ex. sked, skjorta).",
                "examples": [
                    {"word": "kyrka", "pronunciation": "[ɕʏrka] (tj-ljud)", "translation": "church"},
                    {"word": "göra", "pronunciation": "[jœ:ra] (j-ljud)", "translation": "to do / make"},
                    {"word": "sked", "pronunciation": "[ɧe:d] (sje-ljud)", "translation": "spoon"},
                ],
            },
        },
        "pitch_accents": {
            "title": "Svensk Tonaccent: Accent 1 (Akut) vs. Accent 2 (Grav)",
            "description": "Svenskan är ett tonalt språk med två melodiska accenter som kan ändra ordets betydelse helt.",
            "pairs": [
                {
                    "word_1": "anden",
                    "accent_1": "Accent 1 (Akut)",
                    "meaning_1": "anden = the duck (från 'and')",
                    "audio_text_1": "anden",
                    "word_2": "anden",
                    "accent_2": "Accent 2 (Grav)",
                    "meaning_2": "anden = the spirit / ghost (från 'ande')",
                    "audio_text_2": "anden",
                },
                {
                    "word_1": "tomten",
                    "accent_1": "Accent 1 (Akut)",
                    "meaning_1": "tomten = the building plot / yard (från 'tomt')",
                    "audio_text_1": "tomten",
                    "word_2": "tomten",
                    "accent_2": "Accent 2 (Grav)",
                    "meaning_2": "tomten = Santa Claus / the gnome (från 'tomte')",
                    "audio_text_2": "tomten",
                },
            ],
        },
        "listening_quiz": [
            {
                "id": 1,
                "prompt": "Lyssna noga: Är vokalen lång eller kort?",
                "target_word": "glass",
                "audio_text": "glass",
                "options": ["Glas (långt a - dricksglas)", "Glass (kort a - ätbar glass)"],
                "correct_answer": "Glass (kort a - ätbar glass)",
                "explanation": "Ordet uttalades med kort a följt av långt konsonantljud [glas:], vilket betyder 'glass' (ice cream).",
            },
            {
                "id": 2,
                "prompt": "Vilket ord uttalas?",
                "target_word": "tak",
                "audio_text": "tak",
                "options": ["Tak (långt a - yttertak)", "Tack (kort a - tack så mycket)"],
                "correct_answer": "Tak (långt a - yttertak)",
                "explanation": "Det långa utdragna vokalljudet [ta:k] betyder 'tak' (roof).",
            },
            {
                "id": 3,
                "prompt": "Hur uttalas begynnelsebokstaven i ordet 'kyrka'?",
                "target_word": "kyrka",
                "audio_text": "kyrka",
                "options": ["Hårt k-ljud som i 'kaka'", "Mjukt tj-ljud [ɕ] eftersom 'y' är en mjuk vokal"],
                "correct_answer": "Mjukt tj-ljud [ɕ] eftersom 'y' är en mjuk vokal",
                "explanation": "Bokstaven 'Y' är en mjuk vokal, vilket mjukar upp K till tj-ljudet [ɕʏrka].",
            },
        ],
    }
}
