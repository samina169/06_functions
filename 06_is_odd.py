import streamlit as st

# Title of the app
st.title("Check if a Number is Odd")

# Input for the number to check
number = st.number_input("Enter a number:", value=1)

if st.button("Check"):
    if number % 2 != 0:
        st.write(f"{number} is an odd number.")
    else:
        st.write(f"{number} is not an odd number.")
