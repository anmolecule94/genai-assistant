import requests
import json
from config import GEMINI_API_KEY, GEMINI_MODEL

# Gemini endpoint using model from config
ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/{GEMINI_MODEL}:generateContent"

HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API_KEY
}

def answer_question(text, question):
    prompt = f"""
You are a smart assistant helping to extract answers from a document that may contain unstructured or semi-structured information such as tables, mark sheets, or paragraph descriptions.

Document:
{text}

User Question:
{question}

Instructions:
- Carefully look for tabular or list-like patterns in the document.
- If the document includes semester results or subject marks, extract subject names and corresponding marks.
- Answer directly and accurately. Be brief and only include what's asked.
- If the document doesn’t contain relevant data, respond with: "The document does not include this information."

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
