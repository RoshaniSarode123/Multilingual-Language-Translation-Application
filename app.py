import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Configure page
st.set_page_config(page_title="Multilingual Translator", page_icon="🌍", layout="centered")

# Custom CSS for better aesthetics
st.markdown("""
<style>
    /* Import modern typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    /* Global styling */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        font-family: 'Inter', sans-serif;
        color: #f1f5f9;
    }
    
    /* Header typography */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(to right, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 800;
        margin-bottom: 10px;
        letter-spacing: -1px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 300;
    }

    /* Glassmorphism containers for elements */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #f8fafc !important;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #818cf8 !important;
        box-shadow: 0 0 0 2px rgba(129, 140, 248, 0.2);
    }
    
    /* Style Selectboxes */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: white !important;
    }
    
    /* Style Primary Button */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6) !important;
    }
    
    /* Style translation result container */
    .stCodeBlock {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(148, 163, 184, 0.2) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'>🌍 Multilingual Translator</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Translate text instantly across multiple languages with text-to-speech support.</div>", unsafe_allow_html=True)

# Language selection
languages = GoogleTranslator().get_supported_languages(as_dict=True)
lang_names = list(languages.keys())
lang_names_capitalized = [lang.capitalize() for lang in lang_names]

col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox("Source Language", ["Auto Detection"] + lang_names_capitalized, index=0)
    source_lang = "auto" if source_lang_name == "Auto Detection" else languages[source_lang_name.lower()]

with col2:
    try:
        default_index = lang_names_capitalized.index("Spanish")
    except ValueError:
        default_index = 0
    target_lang_name = st.selectbox("Target Language", lang_names_capitalized, index=default_index)
    target_lang = languages[target_lang_name.lower()]

# Input Text
source_text = st.text_area("Enter text to translate:", height=150, placeholder="Type or paste your text here...")

# Translation Logic
if st.button("Translate", type="primary", use_container_width=True):
    if source_text.strip():
        with st.spinner("Translating..."):
            try:
                # Perform translation
                translator = GoogleTranslator(source=source_lang, target=target_lang)
                translated_text = translator.translate(source_text)
                
                # Display Results
                st.success("Translation Successful!")
                
                st.markdown("### Translated Text:")
                # Use st.code for easy copy-to-clipboard functionality
                st.code(translated_text, language="text")
                
                # Text-to-Speech
                st.markdown("### Audio Pronunciation:")
                try:
                    tts = gTTS(text=translated_text, lang=target_lang, slow=False)
                    audio_file_path = "temp_audio.mp3"
                    tts.save(audio_file_path)
                    
                    with open(audio_file_path, "rb") as audio_file:
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format="audio/mp3")
                        
                    os.remove(audio_file_path)
                except Exception as e:
                    st.warning(f"Text-to-speech is not supported for {target_lang_name} or an error occurred. ({e})")
                    
            except Exception as e:
                st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text to translate.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #6b7280; font-size: 0.8rem;'>Powered by Python, Streamlit, Google Translate API & gTTS</div>", unsafe_allow_html=True)
