import streamlit as st

st.set_page_config(page_title="AI Placement Test (Mixed)", layout="centered")
st.title("AI Placement Test (Reading + Grammar + Vocabulary)")

# ----------------------------
# 1) READING COMPREHENSION
# ----------------------------
st.header("Section 1: Reading Comprehension")

PASSAGE = """
Maya is a university student who works part-time in a small café. She starts her day early, checks her messages,
and takes the bus to campus. After classes, she goes to the café and works for four hours. Maya enjoys the job
because she meets many people and practices her communication skills. However, it can be tiring when the café is
busy. To stay healthy, she tries to sleep well and drink enough water. On weekends, she studies at home and
sometimes visits her family.
"""

st.write(PASSAGE)

READING_QS = [
    {
        "q": "Why does Maya enjoy her job at the café?",
        "options": [
            "Because she gets free food every day.",
            "Because she meets people and practices communication.",
            "Because she does not have classes anymore."
        ],
        "answer": "Because she meets people and practices communication.",
        "skill": "Reading - main idea"
    },
    {
        "q": "What does Maya do on weekends?",
        "options": [
            "She works at the café all day.",
            "She studies at home and sometimes visits her family.",
            "She travels to another city every weekend."
        ],
        "answer": "She studies at home and sometimes visits her family.",
        "skill": "Reading - detail"
    },
    {
        "q": "What helps Maya stay healthy?",
        "options": [
            "Sleeping well and drinking enough water.",
            "Eating only sweets at the café.",
            "Studying all night without rest."
        ],
        "answer": "Sleeping well and drinking enough water.",
        "skill": "Reading - inference/detail"
    },
]

reading_answers = []
for i, item in enumerate(READING_QS, start=1):
    choice = st.radio(f"R{i}. {item['q']}", item["options"], key=f"r{i}")
    reading_answers.append(choice)

# ----------------------------
# 2) GRAMMAR
# ----------------------------
st.header("Section 2: Grammar")

GRAMMAR_QS = [
    {
        "q": "She ____ to campus by bus every day.",
        "options": ["go", "goes", "going"],
        "answer": "goes",
        "skill": "Present Simple"
    },
    {
        "q": "They ____ dinner when I called them.",
        "options": ["have", "were having", "has"],
        "answer": "were having",
        "skill": "Past Continuous"
    },
    {
        "q": "If I ____ more time, I would read more books.",
        "options": ["have", "had", "will have"],
        "answer": "had",
        "skill": "Second Conditional"
    },
]

grammar_answers = []
for i, item in enumerate(GRAMMAR_QS, start=1):
    choice = st.radio(f"G{i}. {item['q']}", item["options"], key=f"g{i}")
    grammar_answers.append(choice)

# ----------------------------
# 3) VOCABULARY
# ----------------------------
st.header("Section 3: Vocabulary")

VOCAB_QS = [
    {
        "q": "Choose the best meaning of 'tiring' in the passage:",
        "options": ["fun", "making you feel tired", "expensive"],
        "answer": "making you feel tired",
        "skill": "Meaning in context"
    },
    {
        "q": "Choose the best word: She ____ her messages in the morning.",
        "options": ["checks", "checkers", "checking"],
        "answer": "checks",
        "skill": "Common verb usage"
    },
    {
        "q": "Which word is closest in meaning to 'enough'?",
        "options": ["a lot", "sufficient", "dangerous"],
        "answer": "sufficient",
        "skill": "Synonym"
    },
]

vocab_answers = []
for i, item in enumerate(VOCAB_QS, start=1):
    choice = st.radio(f"V{i}. {item['q']}", item["options"], key=f"v{i}")
    vocab_answers.append(choice)

# ----------------------------
# SCORING + LEVEL ESTIMATE
# ----------------------------
def estimate_level(pct: float) -> str:
    if pct < 0.35: return "A1"
    if pct < 0.55: return "A2"
    if pct < 0.75: return "B1"
    if pct < 0.9:  return "B2"
    return "C1"

if st.button("Get Result"):
    score = 0
    total = len(READING_QS) + len(GRAMMAR_QS) + len(VOCAB_QS)
    weak_skills = []

    # Reading
    for ans, item in zip(reading_answers, READING_QS):
        if ans == item["answer"]:
            score += 1
        else:
            weak_skills.append(item["skill"])

    # Grammar
    for ans, item in zip(grammar_answers, GRAMMAR_QS):
        if ans == item["answer"]:
            score += 1
        else:
            weak_skills.append(item["skill"])

    # Vocabulary
    for ans, item in zip(vocab_answers, VOCAB_QS):
        if ans == item["answer"]:
            score += 1
        else:
            weak_skills.append(item["skill"])

    pct = score / total
    st.subheader("Result")
    st.write(f"Score: {score}/{total} ({pct:.0%})")
    st.write("Estimated Level:", estimate_level(pct))

    if weak_skills:
        st.write("Weak areas:")
        for s in sorted(set(weak_skills)):
            st.write("- ", s)
    else:
        st.success("Excellent — no weak areas detected in this short test.")
