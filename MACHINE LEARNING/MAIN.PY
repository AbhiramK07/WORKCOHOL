import streamlit as st
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Grade Predictor")

hours = st.number_input("Hours studied", min_value = 0.0)

if st.button("Predict"):
    input_data = np.array([[hours]])
    predict_data = model.predict(input_data)[0]

    st.success(f"Predicted grade: {predict_data:.2f}")

