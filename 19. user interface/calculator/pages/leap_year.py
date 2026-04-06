import streamlit as st 

st.title("Leap year finder")
year = st.number_input("Enter the year to check: ")

btn = st.button("Calculate")

if btn:

    if (year % 100 == 0 and year % 400 ==  0 ) or (year % 100 != 0 and year % 4 ==  0 ):

        st.success(f"{year} is a leap year") 
    else:

        st.error(f"{year} is not a leap year") 