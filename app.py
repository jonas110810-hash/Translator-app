import streamlit as st
from google import genai

st.set_page_config(page_title="Pro-Translator AI", page_icon="🌐")

st.title("Pro-Translator AI")

api_key = st.secrets["AIzaSyArZY1fip9mTUm21SwEBkKBrOs6x_oQEQI"]
client = genai.Client(api_key=api_key)

text = st.text_area("Enter text to translate:", height=150)
lang = st.selectbox("Translate to:", ["Tamil", "Hindi", "French", "German", "Spanish"])
tone = st.radio("Tone:", ["Casual", "Formal"], horizontal=True)

if st.button("Translate"):
    if text:
        prompt = f"Translate the following text into {lang} using a {tone} tone. Provide only the translation:\n\n{text}"
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            st.subheader("Translation:")
            st.success(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text first!")
