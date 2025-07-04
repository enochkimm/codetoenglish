import os
from dotenv import load_dotenv
import openai
import streamlit as st
from llm_translate import translate_code  # Make sure this function uses openai API

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App UI
st.set_page_config(page_title="Code to English Translator", layout="centered")
st.title("Code to English Translator")
st.write("Enter your Python or Java code below and get a simple English explanation.")

code_input = st.text_area("Paste your code here:", height=200)
language = st.selectbox("Select language:", ["Python", "Java"])

if st.button("Translate to English"):
    if code_input.strip() == "":
        st.warning("Please enter some code to translate.")
    else:
        with st.spinner("Translating..."):
            try:
                explanation = translate_code(code_input, language.lower())
                st.success("English Explanation:")
                st.write(explanation)
            except Exception as e:
                st.error(f"Error: {e}")
