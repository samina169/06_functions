import streamlit as st

# Title of the app
st.title("Average Calculator")

# Input for numbers
numbers = st.text_input("Enter numbers separated by commas:")

if numbers:
    # Convert the input string to a list of numbers
    num_list = [float(num) for num in numbers.split(",")]
    
    # Calculate the average
    average = sum(num_list) / len(num_list)
    
    # Display the result
    st.write(f"The average is: {average}")
