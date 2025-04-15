import streamlit as st

# Title of the app
st.title("Double a Number")

# Input for the number to double
number = st.number_input("Enter a number to double:", value=1.0)

if st.button("Double It"):
    doubled_value = number * 2  # Calculate the doubled value
    st.write(f"The doubled value is: {doubled_value}")
