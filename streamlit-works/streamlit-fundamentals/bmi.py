import streamlit as st 
st.title("BMI")
weight = st.number_input("Enter the weight: ")
height = st.number_input("Enter the height cm: ")

height_in_m = height / 100

if st.button("bmi"):
    bmi = weight/(height_in_m)**2
    st.write(f"bmi result is: {bmi}")
