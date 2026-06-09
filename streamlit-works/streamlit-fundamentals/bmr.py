import streamlit as st
st.title("bmr")
gender=st.text_input("enter gender:")
height=st.number_input("enter height in cm:")
weight=st.number_input("enter weight in kg")
age=st.number_input("enter age in year")
if st.button('bmr'):
    if gender=='male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    st.write(bmr)