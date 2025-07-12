## 📄 GenAI Smart Assistant (Built with Gemini Flash & Streamlit)

An AI-powered smart assistant that can **summarize** research documents, **answer user questions**, and **generate logic-based challenges** – all grounded in your uploaded content.

> 🚀 Powered by **Google Gemini Flash (1.5)**
> 🎯 Built with **Streamlit**
> 🔒 API Key is securely handled via `config.py`

---

### 🔍 Features

* ✅ **PDF/TXT Upload** – drag & drop your own files.
* ✅ **Auto Summarization** – 150-word concise summaries using Gemini.
* ✅ **Ask Anything** – get answers with references from your uploaded content.
* ✅ **Challenge Me Mode** – auto-generates logic-based questions and gives feedback on your answers.

---

### 🛠 Setup Instructions

#### 1. Clone the repository

```bash
git clone https://github.com/anmolecule94/genai-assistant.git
cd genai-assistant
```

#### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On macOS/Linux: source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Add your Gemini API Key

Create a file named `config.py` in the project root:

```python
# config.py
GEMINI_API_KEY = "your_actual_gemini_api_key"
GEMINI_MODEL = "gemini-1.5-flash"
```

> 🔐 This file is already excluded from Git using `.gitignore`.

#### 5. Run the app

```bash
streamlit run app.py
```

---

### 🧠 Architecture

```
genai-assistant/
├── app.py                 # Streamlit frontend
├── config.py              # Gemini key + model
├── README.md
├── requirements.txt
├── .gitignore
└── backend/
    ├── common.py              # API logic (unified Gemini call)
    ├── summarizer.py          # 150-word summarization
    ├── qa_engine.py           # Free-form Q&A with reference
    ├── logic_challenge.py     # Question generation + answer evaluation
    └── utils.py               # PDF/TXT extractor
```

---

### 🧪 How It Works (Logic Flow)

1. **Document Upload**

   * PDF or TXT is parsed with `PyPDF2` or plain decoding.
2. **Summary Mode**

   * Sends full text to Gemini with a prompt for 150-word summarization.
3. **Ask Anything**

   * Sends question + full context to Gemini with reference-style prompts.
4. **Challenge Me**

   * Generates 3 questions → User answers → Gemini evaluates them.

---

### 📄 License

This project is under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use and build on it!

---

### 💡 Credits

Built with 💙 by [Anmol Singh](https://github.com/anmolecule94)
API powered by **Google Gemini Flash**

---
