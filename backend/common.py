import requests
import json
from config import GEMINI_API_KEY, GEMINI_MODEL

ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/{GEMINI_MODEL}:generateContent"
HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API_KEY,
}

def call_gemini(prompt: str) -> str:
    body = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(ENDPOINT, headers=HEADERS, data=json.dumps(body))

    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    else:
        return f"❌ Gemini API Error {response.status_code}: {response.text}"
