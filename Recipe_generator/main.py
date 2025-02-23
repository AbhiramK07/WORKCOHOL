from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_recipe(ingredients):
    res = model.generate_content(f"Give me the recipe with {ingredients}")
    return res.text


st.title("Recipe Generator")

ingredients = st.text_input("Enter Ingredients (csv)")

if st.button("Get Recipe"):
    if ingredients:
        recipe = generate_recipe(ingredients)
        st.markdown(recipe)
    else:
        st.warning("Please enter some value")




