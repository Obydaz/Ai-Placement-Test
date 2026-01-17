import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Placement Test", layout="centered")
st.title("AI Placement Test (MCQ)")

QUESTIONS = [
    {
        "q": "Choose the correct sentence:",
        "options": ["She go to school every day.", "She goes to school every day.", "She going to school every day."],
        "answer": "She goes to school every day.",
        "skill": "Present Simple / S-V agreement",
        "level": "A1-A2"
    },
    {
        "q": "I ______ English right now.",
        "options": ["study", "am studying", "studies"],
        "answer": "am studying",
        "skill": "Present Continuous",
        "level": "A2"
    },
    {
        "q": "If I had time, I ______ travel more.",
        "options": ["will", "would", "am"],
        "answer": "would",
        "skill": "Second Conditional",
        "level": "B1-B2"
    },
    {
        "q": "By the time we arrived, the movie ______ .",
        "options": ["started", "had started", "has started"],
        "answer": "had started",
        "skill": "Past Perfect",
        "level": "B1"
    },
    {
        "q": "Choose the best word: This book is very ______.",
        "options": ["interested", "interesting", "interest"],
        "answer": "interesting",
        "skill": "Adjectives (-ed / -ing)",
        "level": "A2-B1"
    },
]

st.subheader("Answer the questions")

user_answers = []
for i, item in enumerate(QUESTIONS, start=1):
    choice = st.radio(f"Q{i}. {item['q']}", item["options"], key=f"q{i}")
    user_answers.append(choice)

def cefr_from_score(score, total):
    pct = score / total
    if pct < 0.35: return "A1"
    if pct < 0.55: return "A2"
    if pct < 0.75: return "B1"
    if pct < 0.9:  return "B2"
    return "C1"

if st.button("Get Result"):
    score = 0
    wrong_skills = []

    for ans, item in zip(user_answers, QUESTIONS):
        if ans == item["answer"]:
            score += 1
        else:
            wrong_skills.append(item["skill"])

    st.write(f"Score: {score}/{len(QUESTIONS)}")
    st.write("Estimated Level:", cefr_from_score(score, len(QUESTIONS)))

    if wrong_skills:
        st.write("Weak areas to practice:")
        for s in sorted(set(wrong_skills)):
            st.write("- ", s)
    else:
        st.success("Excellent! No weak areas detected in this short test.")
