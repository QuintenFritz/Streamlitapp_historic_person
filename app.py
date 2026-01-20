import streamlit as st
import random

# -----------------------------
# Historic people dataset
# -----------------------------
HISTORIC_PEOPLE = [
    {"name": "Leonardo da Vinci", "birth_year": 1452},
    {"name": "Napoleon Bonaparte", "birth_year": 1769},
    {"name": "Cleopatra", "birth_year": -69},   # BCE
    {"name": "Albert Einstein", "birth_year": 1879},
    {"name": "Joan of Arc", "birth_year": 1412},
    {"name": "George Washington", "birth_year": 1732},
    {"name": "Julius Caesar", "birth_year": -100},
    {"name": "Isaac Newton", "birth_year": 1643},
]

# -----------------------------
# Session state en laat een scheet
# -----------------------------
if "person" not in st.session_state:
    st.session_state.person = random.choice(HISTORIC_PEOPLE)
    st.session_state.guessed = False

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Guess the Birth Year", layout="centered")

st.title("🕰️ Guess the Birth Year!")

st.markdown(
    """
    ### 👤 Historic Figure
    """
)

# Big bold name
st.markdown(
    f"""
    <div style="font-size:48px; font-weight:800; text-align:center; margin:30px 0;">
        {st.session_state.person["name"]}
    </div>
    """,
    unsafe_allow_html=True,
)

# Guess input
guess = st.slider(
    "What year were they born?",
    min_value=-500,
    max_value=2000,
    value=1500,
    step=1,
)

# Submit
if st.button("Submit Guess"):
    st.session_state.guessed = True

# -----------------------------
# Results
# -----------------------------
if st.session_state.guessed:
    actual = st.session_state.person["birth_year"]
    diff = abs(guess - actual)
    score = max(0, 100 - diff)

    st.markdown("### 📜 Result")
    st.write(f"**Born:** {actual} {'BCE' if actual < 0 else 'CE'}")
    st.write(f"**Your guess:** {guess}")
    st.write(f"**Difference:** {diff} years")

    if diff == 0:
        st.success("🎯 Perfect!")
    elif diff <= 10:
        st.success("🔥 Very close!")
    elif diff <= 50:
        st.warning("👍 Not bad!")
    else:
        st.error("😬 Way off!")

    st.metric("Score", score)

    if st.button("Next Person ➡️"):
        st.session_state.person = random.choice(HISTORIC_PEOPLE)
        st.session_state.guessed = False
        st.rerun()

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
