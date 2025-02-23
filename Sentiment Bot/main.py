import streamlit as st
from transformers import pipeline

sentiment_pipe = pipeline('sentiment-analysis')

st.title("Sentimental Analysis")

user_input = st.text_input("Enter your text")

if st.button("Get Sentiment"):
    if user_input:
        result = sentiment_pipe(user_input)

        st.write(result[0]['label'])
