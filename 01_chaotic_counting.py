import streamlit as st
import random
import time

# Title of the app
st.title("Chaotic Counting")

# Input for the maximum number
max_number = st.number_input("Enter a maximum number:", min_value=1, value=10)

if st.button("Start Counting"):
    st.write("Counting chaotically...")
    for i in range(max_number):
        # Generate a random number to display
        chaotic_number = random.randint(1, max_number)
        st.write(chaotic_number)
        time.sleep(0.5)  # Pause for half a second between counts
