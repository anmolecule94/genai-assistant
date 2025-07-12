import requests
import json
from config import GEMINI_API_KEY, GEMINI_MODEL

# ✅ Use correct v1 endpoint
ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/{GEMINI_MODEL}:generateContent"

HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API_KEY
}

def summarize_text(text):
    prompt = f"Summarize the following document in under 150 words:\n\n{text}"

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(ENDPOINT, headers=HEADERS, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text'].strip()
    else:
        return f"❌ Gemini API Error: {response.status_code} - {response.text}"
