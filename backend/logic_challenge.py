import requests
import json
from config import GEMINI_API_KEY, GEMINI_MODEL

# Use model and key from config
endpoint = f"https://generativelanguage.googleapis.com/v1/models/{GEMINI_MODEL}:generateContent"
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API_KEY
}

def generate_questions(text):
    prompt = f"""Generate 3 logic- or comprehension-based questions from the document below:\n\n{text}"""
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        content = response.json()['candidates'][0]['content']['parts'][0]['text']
        return [q.strip() for q in content.split("\n") if q.strip()]
    
    return [f"❌ Gemini API Error: {response.status_code} - {response.text}"]

def evaluate_user_answer(text, question, user_answer):
    prompt = f"""Evaluate the following answer based on the document.

Document: {text}

Question: {question}
User Answer: {user_answer}

State whether it is correct or not (✔️ or ❌), provide feedback, and cite the relevant part of the document."""
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    
    return f"❌ Gemini API Error: {response.status_code} - {response.text}"
