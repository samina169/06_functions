import streamlit as st

# Title of the app
st.title("Get Your Name")

# Input for the user's name
name = st.text_input("Enter your name:")

if st.button("Submit"):
    st.write(f"Hello, {name}! Welcome to the app!")
