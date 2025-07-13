"""
backend/logic_challenge.py
–––––––––––––––––––––––––––
Generates logic‑based questions and evaluates answers.
• If the uploaded text looks like a mark‑sheet table, we:
  – extract subject → marks using regex,
  – auto‑generate three “marks” questions,
  – evaluate answers locally.
• Otherwise we delegate both tasks to Gemini.
"""

import re
import random
import json
import requests
from config import GEMINI_API_KEY, GEMINI_MODEL

# ------------------------------------------------------------------ #
#                   Gemini REST helper (fallback mode)               #
# ------------------------------------------------------------------ #
ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/{GEMINI_MODEL}:generateContent"
HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API_KEY,
}

def call_gemini(prompt: str) -> str:
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    r = requests.post(ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    if r.status_code == 200:
        return r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    return f"❌ Gemini API Error {r.status_code}: {r.text}"

# ------------------------------------------------------------------ #
#                Simple mark‑sheet parser (regex based)              #
# ------------------------------------------------------------------ #
def parse_marks(text: str) -> dict:
    """
    Returns a dict {Subject: int_mark} if subject‑mark lines are detected, else {}.
    Recognises separators :, -, or whitespace.
    """
    pattern = re.compile(
        r"^\s*([A-Za-z][A-Za-z\s&\-]+?)\s*[:\-\s]\s*(\d{1,3})\s*$",
        re.IGNORECASE | re.MULTILINE,
    )
    marks = {subj.strip().title(): int(mark) for subj, mark in pattern.findall(text)}
    return marks

# ------------------------------------------------------------------ #
#                    Question generation function                    #
# ------------------------------------------------------------------ #
def generate_questions(text: str):
    marks = parse_marks(text)

    # If we have at least three subjects, create “marks” questions locally.
    if len(marks) >= 3:
        subjects = random.sample(list(marks.keys()), 3)
        return [f"What is the marks of {subj}?" for subj in subjects]

    # Fallback: ask Gemini to create questions.
    prompt = (
        "Generate 3 logic‑ or comprehension‑based questions from the document below:\n\n"
        f"{text}"
    )
    out = call_gemini(prompt)
    return [q.strip() for q in out.split("\n") if q.strip()]

# ------------------------------------------------------------------ #
#                    Answer evaluation function                      #
# ------------------------------------------------------------------ #
def evaluate_user_answer(text: str, question: str, user_answer: str):
    marks = parse_marks(text)

    # If the question matches our “marks” pattern and subject exists, evaluate locally.
    m = re.match(r"What\s+is\s+the\s+marks?\s+of\s+(.+?)\s*\??$", question, re.IGNORECASE)
    if m and marks:
        subject = m.group(1).strip().title()
        if subject in marks:
            correct = marks[subject]
            # Extract first integer from the user answer
            found = re.search(r"\d{1,3}", user_answer)
            if found:
                given = int(found.group())
                if given == correct:
                    return f"✔️ Correct! {subject}: {correct}."
                return f"❌ Incorrect. {subject} has {correct} marks."
            return "❌ Please provide a numeric mark in your answer."

    # Fallback: let Gemini evaluate.
    prompt = (
        "Evaluate the following answer based on the document.\n\n"
        f"Document:\n{text}\n\n"
        f"Question:\n{question}\n"
        f"User Answer:\n{user_answer}\n\n"
        "Respond with ✔️ or ❌, give feedback, and cite supporting text."
    )
    return call_gemini(prompt)
