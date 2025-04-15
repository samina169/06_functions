import streamlit as st
import random

# Title of the app
st.title("Random Sentence Generator")

# Predefined lists of subjects, verbs, and objects
subjects = ["The cat", "A dog", "The teacher", "A child", "The car"]
verbs = ["jumps", "runs", "sleeps", "eats", "drives"]
objects = ["over the fence", "in the park", "on the road", "under the table", "with joy"]

# Button to generate a sentence
if st.button("Generate Sentence"):
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    sentence = f"{subject} {verb} {obj}."
    st.write(sentence)
