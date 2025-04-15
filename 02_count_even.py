import streamlit as st

# Title of the app
st.title("Count Even Numbers")

# Input for the maximum number
max_number = st.number_input("Enter a maximum number:", min_value=1, value=10)

if st.button("Count Even Numbers"):
    st.write("Even numbers up to", max_number, ":")
    even_numbers = [num for num in range(2, max_number + 1, 2)]  # Generate even numbers
    st.write(even_numbers)
