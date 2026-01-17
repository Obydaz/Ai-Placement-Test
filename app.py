import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Placement Test", layout="centered")

st.title("AI Placement Test")
st.write("This app evaluates English level using AI.")

# Input
student_text = st.text_area(
    "Write 80–120 words about your daily routine:",
    height=200
)

# Button
if st.button("Evaluate"):
    if len(student_text.strip()) < 40:
        st.error("Please write more text so AI can evaluate your level.")
    else:
        st.info("Evaluating...")

        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

prompt = f"""
You are an English placement examiner.

Evaluate the student's writing and give:
- Grammar score (0–5)
- Vocabulary score (0–5)
- Coherence score (0–5)
- Overall level (A1, A2, B1, B2, or C1)

Student text:
{student_text}
"""

