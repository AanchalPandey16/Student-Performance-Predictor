import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.set_page_config(
    page_title="Student Performance Predictor", 
    layout="centered"
)
st.title("Student Performance Predictor")
st.write(
    """
    This app predicts a student's **Performance Index** using a trained 
    Multiple Linear Regression model.  
    Adjust the sliders below to simulate different scenarios.
    """
)

st.subheader("Enter Student Details")

hours_studied = st.slider("Hours Studied per Day", 0, 12, 5)
previous_score = st.slider("Previous Academic Score (%)", 0, 100, 75)
sleep_hours = st.slider("Average Sleep Hours", 0, 12, 7)
practice_tests = st.slider("Number of Practice Tests Taken", 0, 20, 5)
extracurricular = st.selectbox("Extracurricular Participation", ["Yes", "No"])

extracurricular_num = 1 if extracurricular == "Yes" else 0

features = np.array([[hours_studied, previous_score, sleep_hours, practice_tests, extracurricular_num]])

if st.button("Predict Performance Index"):
    prediction = model.predict(features)
    st.success(f"Predicted Performance Index: **{prediction[0]:.2f}**")
