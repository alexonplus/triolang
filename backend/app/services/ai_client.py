"""
Low-Level AI Client Service (Gemini API Integration)
---------------------------------------------------
"""

import json
from typing import Dict, Any, Optional
import httpx
from app.core.config import settings


class GeminiAPIClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.GEMINI_API_KEY
        self.model = settings.GEMINI_MODEL
        self.timeout = httpx.Timeout(20.0, connect=10.0)

    @property
    def is_configured(self) -> bool:
        return bool(self.api_key and self.api_key != "YOUR_GEMINI_API_KEY_HERE")

    async def generate_json(self, prompt: str, system_instruction: str = "") -> Dict[str, Any]:
        if not self.is_configured:
            raise ValueError("GEMINI_API_KEY is not configured in backend/.env")

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"

        payload: Dict[str, Any] = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ],
            "generationConfig": {
                "response_mime_type": "application/json",
                "temperature": 0.3,
            }
        }

        if system_instruction:
            payload["system_instruction"] = {
                "parts": [{"text": system_instruction}]
            }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(url, json=payload)

            if response.status_code != 200:
                error_detail = response.text
                raise RuntimeError(f"Gemini API Error (HTTP {response.status_code}): {error_detail}")

            data = response.json()
            try:
                candidate_text = data["candidates"][0]["content"]["parts"][0]["text"]
                return json.loads(candidate_text)
            except (KeyError, IndexError, json.JSONDecodeError) as err:
                raise ValueError(f"Failed to parse JSON response from Gemini API: {err}")


gemini_client = GeminiAPIClient()
