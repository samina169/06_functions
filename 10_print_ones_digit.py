import streamlit as st

# Title of the app
st.title("Print the Ones Digit of a Number")

# Input for the number
number = st.number_input("Enter a number:", value=0)

if st.button("Get Ones Digit"):
    if number >= 0:
        ones_digit = int(number) % 10  # Calculate the ones digit
        st.write(f"The ones digit of {number} is: {ones_digit}")
    else:
        st.write("Please enter a non-negative integer.")
