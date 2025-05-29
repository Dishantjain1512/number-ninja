import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

# Initialize session state
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.title("🎯 Number Guessing Game")
st.write("Guess a number between **1 and 100**.")

if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.secret_number:
            st.success(f"🎉 Correct! You guessed the number in {st.session_state.attempts} tries.")
            st.session_state.game_over = True
        elif guess < st.session_state.secret_number:
            st.info("Too low! Try a higher number.")
        else:
            st.info("Too high! Try a lower number.")
else:
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
