import streamlit as st
from google import genai

# Setup the app title
st.title("Pro-Translator AI")

# Get key securely from Streamlit Secrets
api_key = st.secrets["AIzaSyC8JuD7fp5cF7jc3q0Lhxpct3DZvwIVswI"]
client = genai.Client(api_key=api_key)

# Interface
text = st.text_area("Enter text to translate:")
lang = st.selectbox("Translate to:", ["Tamil", "Hindi", "French", "German"])
tone = st.radio("Tone:", ["Casual", "Formal"])

if st.button("Translate"):
    if text:
        prompt = f"Translate this to {lang} in a {tone} tone: {text}"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        st.write(response.text)
    else:
        st.warning("Please enter some text first!")
