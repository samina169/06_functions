import streamlit as st

# Title of the app
st.title("Print Multiples of a Number")

# Input for the number to find multiples
number = st.number_input("Enter a number:", value=1)
limit = st.number_input("Enter the limit for multiples:", value=10)

if st.button("Find Multiples"):
    if number > 0 and limit > 0:
        multiples = [number * i for i in range(1, limit + 1)]  # Find multiples
        st.write(f"The multiples of {number} up to {limit} are: {multiples}")
    else:
        st.write("Please enter positive integers for both fields.")
