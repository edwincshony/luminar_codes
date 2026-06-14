import joblib
import streamlit as st

model = joblib.load("model.pkl")

scaler= joblib.load("scaler.pkl")

features = ['StudyTimeWeekly', 'Absences', 'ParentalSupport', 'Tutoring']
values=[]
for f in features:
    
    f = st.number_input(f"enter {f}")
    values.append(f)
    
if st.button("predict"):
    
    result = model.predict(scaler.transform([values]))
    print(result)
    
    st.write(result)