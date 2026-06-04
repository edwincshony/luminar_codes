# streamlit > title("heading")

# pip install streamlit

import streamlit as st 

st.title("Hello world")


num1 = st.number_input("Enter the number 1:", key="first_number")
num2 = st.number_input("Enter the number 2:", key="second_number")

# python -m streamlit run app.py