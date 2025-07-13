📄 GenAI Smart Assistant
An AI-powered assistant that reads research papers or technical documents (PDF/TXT), summarizes them, answers questions with contextual references, and tests users using logic-based questions.

✅ Powered by Gemini Flash (1.5) via REST API
✅ Built with Streamlit
✅ No need to paste API keys manually – uses config.py

🚀 Features
📄 Upload PDF/TXT: Accepts research papers, manuals, etc.

🧠 Auto Summary: Generates a 150-word summary instantly.

💬 Ask Anything: Ask free-form questions; assistant answers using document context.

🧩 Challenge Me: Auto-generates 3 logic/comprehension questions. Evaluates your answers with justification.

✅ All answers grounded in the uploaded document.

🔒 No hallucinations or fabrications.

🛠 Setup Instructions
1. Clone this repo
bash
Copy
Edit
git clone https://github.com/yourusername/genai-assistant.git
cd genai-assistant
2. Create virtual environment and install dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install streamlit requests PyPDF2
3. Add your Gemini API Key
Create a file config.py in the root directory:

python
Copy
Edit
GEMINI_API_KEY = "your_actual_api_key"
GEMINI_MODEL = "gemini-1.5-flash"  # or gemini-pro or gemini-2.0-flash
⚠️ This file is ignored in .gitignore for safety.

4. Run the App
bash
Copy
Edit
streamlit run app.py
🧠 Architecture & Reasoning Flow
plaintext
Copy
Edit
📂 genai-assistant/
│
├── app.py                     # Main Streamlit UI
├── config.py                  # Stores Gemini API key & model
├── backend/
│   ├── common.py              # Shared Gemini API call logic
│   ├── summarizer.py          # Summarizes full doc
│   ├── qa_engine.py           # Handles free-form Q&A
│   ├── logic_challenge.py     # Generates + evaluates logic questions
│   └── utils.py               # PDF/TXT parsing
Reasoning Flow:

User uploads a document.

summarizer.py generates concise summary using Gemini.

Two modes:

Ask Anything: qa_engine.py generates answer with reference.

Challenge Me: logic_challenge.py creates 3 logic questions and evaluates user responses.

All interactions are powered by Gemini REST API via a unified function in common.py.