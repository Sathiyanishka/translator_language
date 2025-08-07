import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()

st.title("🌍 AI-Powered Real-Time Translator")
st.markdown("Break language barriers and communicate globally!")

# Input
text = st.text_input("Enter text to translate:")

# Language options
languages = {'English': 'en', 'Tamil': 'ta', 'Hindi': 'hi', 'French': 'fr', 'Spanish': 'es', 'Chinese': 'zh-cn'}
target_lang = st.selectbox("Select target language", list(languages.keys()))

if st.button("Translate"):
    translated = translator.translate(text, dest=languages[target_lang])
    st.success(f"🔁 Translated Text ({target_lang}): {translated.text}")

    # Text-to-speech
    tts = gTTS(translated.text, lang=languages[target_lang])
    tts.save("output.mp3")
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")
