import streamlit as st

# Title of the app
st.title("Print Divisors of a Number")

# Input for the number to find divisors
number = st.number_input("Enter a number:", value=1)

if st.button("Find Divisors"):
    if number > 0:
        divisors = [i for i in range(1, number + 1) if number % i == 0]  # Find divisors
        st.write(f"The divisors of {number} are: {divisors}")
    else:
        st.write("Please enter a positive integer.")
