import requests
import json
from config import GEMINI_API_KEY, GEMINI_MODEL

# Correct Gemini endpoint using model from config
ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/{GEMINI_MODEL}:generateContent"

HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API_KEY
}

def answer_question(text, question):
    prompt = f"""You are a smart assistant. Use the document below to answer the user's question. Reference the paragraph or section when possible.

Document:
{text}

Question:
{question}

Answer:"""

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(ENDPOINT, headers=HEADERS, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text'].strip()
    else:
        return f"❌ Gemini API Error: {response.status_code} - {response.text}"
