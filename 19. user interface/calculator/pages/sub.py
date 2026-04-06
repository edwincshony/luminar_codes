import streamlit as st 

st.title("Subtraction")


num1 = st.text_input("Enter number 1: ")
num2 = st.text_input("Enter number 2: ")

btn_sub = st.button("Subtract")

if btn_sub:

    aresult = int(num1) - int(num2)

    st.write(f"Subtraction result is: {num1}-{num2} = {aresult}")
