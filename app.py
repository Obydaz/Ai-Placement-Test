import random
import streamlit as st

# ----------------------------
# PAGE SETUP
# ----------------------------
st.set_page_config(page_title="AI Placement Test (Mixed)", layout="centered")
st.title("AI Placement Test (Mixed: A1–B1 + 2 B2)")
st.write("20 questions total: 5 Reading, 8 Grammar (includes 2 B2), 7 Vocabulary.")
st.caption("Click “Generate New Test” to get a different set of questions.")

# ----------------------------
# RE-GENERATE BUTTON
# ----------------------------
if st.button("🔄 Generate New Test"):
    st.session_state.clear()
    st.rerun()

# ----------------------------
# READING PASSAGE
# ----------------------------
st.header("Section 1: Reading Comprehension (5 Questions)")

PASSAGE = """
Sara is 14 years old and she lives in a small town. Every weekday, she wakes up at 6:30 a.m. and gets ready for school.
She usually eats eggs or bread for breakfast and drinks a cup of tea. Then she walks to the bus stop with her friend.
School starts at 8:00 a.m.

After school, Sara sometimes helps her mother at home, but on Tuesdays and Thursdays she goes to an English club.
At the club, students play games, watch short videos, and practice speaking. Sara likes the club because she feels more
confident when she speaks English. She also learns new words every week. On weekends, Sara studies for two hours and then
she meets her cousins or plays sports in the park.
"""
st.write(PASSAGE)

# ----------------------------
# QUESTION POOLS
# ----------------------------

READING_POOL = [
    {"q": "How does Sara go to school?",
     "options": ["She walks all the way.", "She goes by bus.", "She goes by car."],
     "answer": "She goes by bus.",
     "skill": "Reading - detail (A1/A2)"},
    {"q": "When does school start?",
     "options": ["6:30 a.m.", "8:00 a.m.", "9:00 a.m."],
     "answer": "8:00 a.m.",
     "skill": "Reading - detail (A1)"},
    {"q": "What does Sara usually drink for breakfast?",
     "options": ["Milk", "Tea", "Juice"],
     "answer": "Tea",
     "skill": "Reading - detail (A1)"},
    {"q": "When does Sara go to the English club?",
     "options": ["On Tuesdays and Thursdays.", "On Mondays and Wednesdays.", "Only on weekends."],
     "answer": "On Tuesdays and Thursdays.",
     "skill": "Reading - detail (A2)"},
    {"q": "What do students do at the English club?",
     "options": ["They only write essays.", "They play games, watch videos, and practice speaking.", "They only read long books."],
     "answer": "They play games, watch videos, and practice speaking.",
     "skill": "Reading - detail (A2)"},
    {"q": "Why does Sara like the English club?",
     "options": ["Because she gets free food.", "Because she feels more confident speaking English.", "Because there is no homework."],
     "answer": "Because she feels more confident speaking English.",
     "skill": "Reading - main idea (A2/B1)"},
    {"q": "What does Sara do on weekends?",
     "options": ["She studies and then meets cousins or plays sports.", "She works at a café all day.", "She travels every weekend."],
     "answer": "She studies and then meets cousins or plays sports.",
     "skill": "Reading - sequence/detail (A2/B1)"},
    {"q": "What helps Sara improve her English?",
     "options": ["Practicing speaking at the club.", "Sleeping in class.", "Buying new clothes."],
     "answer": "Practicing speaking at the club.",
     "skill": "Reading - inference (B1)"},
]

GRAMMAR_POOL = [
    # A1–B1
    {"q": "She ____ to school every weekday.", "options": ["go", "goes", "going"], "answer": "goes", "skill": "Present Simple (A1)"},
    {"q": "They ____ football yesterday.", "options": ["play", "played", "playing"], "answer": "played", "skill": "Past Simple (A2)"},
    {"q": "I ____ a sandwich now.", "options": ["eat", "am eating", "eats"], "answer": "am eating", "skill": "Present Continuous (A2)"},
    {"q": "There ____ two books on the desk.", "options": ["is", "are", "be"], "answer": "are", "skill": "There is/are (A1/A2)"},
    {"q": "He ____ like coffee.", "options": ["don't", "doesn't", "isn't"], "answer": "doesn't", "skill": "Negatives (A1/A2)"},
    {"q": "She is ____ than her sister.", "options": ["tall", "taller", "tallest"], "answer": "taller", "skill": "Comparatives (A2)"},
    {"q": "I have lived here ____ 2020.", "options": ["for", "since", "from"], "answer": "since", "skill": "For/Since (B1)"},
    {"q": "If it rains, we ____ at home.", "options": ["stay", "stayed", "would stay"], "answer": "stay", "skill": "First Conditional (B1)"},
    {"q": "I went to bed early because I ____ tired.", "options": ["was", "were", "am"], "answer": "was", "skill": "Past of 'be' (A1/A2)"},
    {"q": "We ____ to the park every Friday.", "options": ["go", "goes", "went"], "answer": "go", "skill": "Present Simple (A1)"},

    # B2 (we will force exactly 2 of these)
    {"q": "Hardly ____ the lesson when the bell rang.", "options": ["I had finished", "had I finished", "I finished"],
     "answer": "had I finished", "skill": "Inversion (B2)", "is_b2": True},
    {"q": "By next month, she ____ here for two years.", "options": ["will live", "will have lived", "has lived"],
     "answer": "will have lived", "skill": "Future Perfect (B2)", "is_b2": True},
    {"q": "No sooner ____ home than it started to rain.", "options": ["I arrived", "had I arrived", "I had arrived"],
     "answer": "had I arrived", "skill": "Inversion (B2)", "is_b2": True},
]

VOCAB_POOL = [
    {"q": "Choose the best meaning of 'confident':", "options": ["shy", "sure of yourself", "angry"],
     "answer": "sure of yourself", "skill": "Meaning (A2)"},
    {"q": "Which word is closest in meaning to 'usually'?", "options": ["never", "often", "angrily"],
     "answer": "often", "skill": "Synonym (A2)"},
    {"q": "Choose the best meaning of 'weekday':", "options": ["Saturday or Sunday", "a day from Monday to Friday", "a holiday"],
     "answer": "a day from Monday to Friday", "skill": "Meaning (A1/A2)"},
    {"q": "Choose the best word: I ____ a cup of tea in the morning.", "options": ["drink", "drive", "draw"],
     "answer": "drink", "skill": "Basic verb (A1)"},
    {"q": "Which word fits best? We ____ videos in class.", "options": ["watch", "wash", "wait"],
     "answer": "watch", "skill": "Common verb (A1/A2)"},
    {"q": "Choose the best meaning of 'practice':", "options": ["do again to improve", "sleep", "forget"],
     "answer": "do again to improve", "skill": "Meaning (A2/B1)"},
    {"q": "Choose the correct word: She ____ new words every week.", "options": ["learns", "learn", "learning"],
     "answer": "learns", "skill": "Word form (A2)"},
    {"q": "Which word is the opposite of 'busy'?", "options": ["quiet", "noisy", "strong"],
     "answer": "quiet", "skill": "Antonym (A2)"},
    {"q": "Choose the best word: I feel ____ when I speak in front of the class.", "options": ["nervous", "nervously", "nerve"],
     "answer": "nervous", "skill": "Word form (A2/B1)"},
]

# ----------------------------
# BUILD A 20-QUESTION TEST
# ----------------------------
READING_QS = random.sample(READING_POOL, 5)

b2_grammar = [q for q in GRAMMAR_POOL if q.get("is_b2")]
non_b2_grammar = [q for q in GRAMMAR_POOL if not q.get("is_b2")]

selected_b2 = random.sample(b2_grammar, 2)
selected_non_b2 = random.sample(non_b2_grammar, 6)
GRAMMAR_QS = selected_non_b2 + selected_b2
random.shuffle(GRAMMAR_QS)

VOCAB_QS = random.sample(VOCAB_POOL, 7)

# ----------------------------
# RENDER QUESTIONS
# ----------------------------
reading_answers = []
for i, item in enumerate(READING_QS, start=1):
    reading_answers.append(st.radio(f"R{i}. {item['q']}", item["options"], key=f"r{i}"))

st.header("Section 2: Grammar (8 Questions)")
grammar_answers = []
for i, item in enumerate(GRAMMAR_QS, start=1):
    grammar_answers.append(st.radio(f"G{i}. {item['q']}", item["options"], key=f"g{i}"))

st.header("Section 3: Vocabulary (7 Questions)")
vocab_answers = []
for i, item in enumerate(VOCAB_QS, start=1):
    vocab_answers.append(st.radio(f"V{i}. {item['q']}", item["options"], key=f"v{i}"))

# ----------------------------
# SCORING
# ----------------------------
def estimate_level(score: int, total: int) -> str:
    pct = score / total
    if pct < 0.35:
        return "A1"
    if pct < 0.55:
        return "A2"
    if pct < 0.75:
        return "B1"
    if pct < 0.90:
        return "B2"
    return "C1"

if st.button("Get Result"):
    score = 0
    total = len(READING_QS) + len(GRAMMAR_QS) + len(VOCAB_QS)
    weak_skills = []

    for ans, item in zip(reading_answers, READING_QS):
        if ans == item["answer"]:
            score += 1
        else:
            weak_skills.append(item["skill"])

    for ans, item in zip(grammar_answers, GRAMMAR_QS):
        if ans == item["answer"]:
            score += 1
        else:
            weak_skills.append(item["skill"])

    for ans, item in zip(vocab_answers, VOCAB_QS):
        if ans == item["answer"]:
            score += 1
        else:
            weak_skills.append(item["skill"])

    st.subheader("Result")
    st.write(f"Score: {score}/{total} ({score/total:.0%})")
    st.write("Estimated Level:", estimate_level(score, total))

    st.write("Section scores:")
    r_score = sum(1 for a, q in zip(reading_answers, READING_QS) if a == q["answer"])
    g_score = sum(1 for a, q in zip(grammar_answers, GRAMMAR_QS) if a == q["answer"])
    v_score = sum(1 for a, q in zip(vocab_answers, VOCAB_QS) if a == q["answer"])
    st.write(f"- Reading: {r_score}/{len(READING_QS)}")
    st.write(f"- Grammar: {g_score}/{len(GRAMMAR_QS)}")
    st.write(f"- Vocabulary: {v_score}/{len(VOCAB_QS)}")

    if weak_skills:
        st.write("Weak areas:")
        for s in sorted(set(weak_skills)):
            st.write("- ", s)
    else:
        st.success("Excellent — no weak areas detected in this test.")
