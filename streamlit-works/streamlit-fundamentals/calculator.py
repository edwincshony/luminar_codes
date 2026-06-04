import streamlit as st 
st.title("Calculator")
num1 = st.number_input("Enter the number1: ")
num2 = st.number_input("Enter the number2: ")
if st.button("Add"):
    
    aresult = int(num1) + int(num2)

    st.write(f"Addition result is: {num1}+{num2} = {aresult}")
elif st.button("Sub"):
    
    sresult = int(num1) - int(num2)

    st.write(f"Addition result is: {num1}-{num2} = {sresult}")

elif st.button("Mul"):
    
    mresult = int(num1) * int(num2)

    st.write(f"Addition result is: {num1}*{num2} = {mresult}")
elif st.button("Div"):
    
    dresult = int(num1) // int(num2)

    st.write(f"Addition result is: {num1}-{num2} = {dresult}")