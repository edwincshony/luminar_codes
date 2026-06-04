import streamlit as st

st.title("EMI")

loan_amount=st.number_input("enter your loan amount")
loan_tenture = st.number_input("enter no.of years")
interest_rate = st.number_input("enter interest rate")

i_r = interest_rate/1200

monthly= loan_tenture*12

if st.button("calculate emi"):
    result=(loan_amount*i_r*(1+(i_r))**monthly)/(((1+i_r)**(monthly))-1)
    st.write(result)