import streamlit as st
from backend.utils import extract_text
from backend.summarizer import summarize_text
from backend.qa_engine import answer_question
from backend.logic_challenge import generate_questions, evaluate_user_answer

st.set_page_config(page_title="GenAI Smart Assistant", layout="wide")
st.title("📄 GenAI Smart Assistant")

# Upload section
uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("Processing document..."):
        doc_text = extract_text(uploaded_file)
        summary = summarize_text(doc_text)
        st.markdown("### 📌 Document Summary")
        st.info(summary)

        mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

        # ------------------- Ask Anything Mode -------------------
        if mode == "Ask Anything":
            user_question = st.text_input("Ask a question based on the document:")
            if user_question:
                with st.spinner("Thinking..."):
                    answer = answer_question(doc_text, user_question)
                    st.success(answer)

        # ------------------- Challenge Me Mode -------------------
        elif mode == "Challenge Me":
            st.markdown("Click below to test your understanding 👇")

            if "challenge_questions" not in st.session_state:
                st.session_state.challenge_questions = []
                st.session_state.user_answers = []
                st.session_state.evaluations = []

            if st.button("🔁 Generate Logic-Based Questions"):
                st.session_state.challenge_questions = generate_questions(doc_text)
                st.session_state.user_answers = [""] * len(st.session_state.challenge_questions)
                st.session_state.evaluations = [""] * len(st.session_state.challenge_questions)

            if st.session_state.challenge_questions:
                for idx, question in enumerate(st.session_state.challenge_questions):
                    st.markdown(f"**Q{idx+1}: {question}**")
                    st.session_state.user_answers[idx] = st.text_input(
                        f"Your answer to Q{idx+1}", 
                        key=f"user_answer_{idx}"
                    )

                if st.button("✅ Submit Answers"):
                    with st.spinner("Evaluating your responses..."):
                        for idx, question in enumerate(st.session_state.challenge_questions):
                            response = evaluate_user_answer(
                                doc_text,
                                question,
                                st.session_state.user_answers[idx]
                            )
                            st.session_state.evaluations[idx] = response

                # Display feedback
                for idx, feedback in enumerate(st.session_state.evaluations):
                    if feedback:
                        st.markdown(f"**Feedback for Q{idx+1}:**")
                        st.info(feedback)
