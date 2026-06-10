# 🌍 Multilingual Translator Web App

A beautiful, fully functional language translation web application built with **Python** and **Streamlit**. 

## ✨ Features
* **Multilingual Translation:** Powered by the Google Translate API (via `deep-translator`), supporting over 100+ languages.
* **Auto-Language Detection:** Automatically identifies the source language if you aren't sure what it is.
* **Text-to-Speech (TTS):** Generates playable audio pronunciations of the translated text using `gTTS`.
* **Copy to Clipboard:** Features a formatted output box with a built-in one-click copy button.
* **Premium Glassmorphism UI:** Features a custom CSS design system using dark mode gradients, smooth hover animations, and the *Inter* font family.

## 🚀 How It Works Under the Hood

1. **The Frontend (`streamlit`):** The entire user interface, including the text boxes, dropdown menus, and layout columns, is built using the Streamlit library. Custom CSS is injected via `st.markdown` to override the default styles and give it a premium look.
2. **The Translation Engine (`deep-translator`):** When the user clicks "Translate", the text is sent to `GoogleTranslator`, which interfaces with Google's translation servers to return the highly accurate translated string.
3. **The Audio Generation (`gTTS`):** The translated text is passed into the Google Text-to-Speech library, which generates a temporary `.mp3` file. Streamlit's `st.audio` component then reads this file and plays it in the browser, after which the temporary file is immediately deleted to save space.

## 💻 Installation & Running Locally

1. Ensure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. Open the provided `localhost` link in your browser to use the app!
