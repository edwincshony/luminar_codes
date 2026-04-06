import streamlit as st 

st.title("Addition")


num1 = st.text_input("Enter number 1: ")
num2 = st.text_input("Enter number 2: ")

btn_add = st.button("Add")

if btn_add:

    aresult = int(num1) + int(num2)

    st.write(f"Addition result is: {num1}+{num2} = {aresult}")
