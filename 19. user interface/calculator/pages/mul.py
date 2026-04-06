import streamlit as st 

st.title("Multiplication")


num1 = st.text_input("Enter number 1: ")
num2 = st.text_input("Enter number 2: ")

btn_mul = st.button("Muliply")

if btn_mul:

    aresult = int(num1) * int(num2)

    st.write(f"Multiplication result is: {num1}*{num2} = {aresult}")
