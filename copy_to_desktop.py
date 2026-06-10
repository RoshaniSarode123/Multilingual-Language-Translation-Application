import os
import shutil

src_dir = r"C:\Users\SHIVANI\.gemini\antigravity\scratch\language_translator"
dest_dir = r"C:\Users\SHIVANI\Desktop\Language_Translator_App"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for item in os.listdir(src_dir):
    src_path = os.path.join(src_dir, item)
    dest_path = os.path.join(dest_dir, item)
    if os.path.isfile(src_path) and item != "copy_to_desktop.py":
        shutil.copy2(src_path, dest_path)

print("Files successfully copied to Desktop!")
