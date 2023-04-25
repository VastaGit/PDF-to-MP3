from gtts import gTTS 
import os
from pdfminer import high_level

language = "en" #setting language settings
file_name = "sample" #declaring your file name
with open(f'{file_name}.pdf', 'rb') as f:
    text = high_level.extract_text(f) #extracting text from pdf file

#this was added in features branch

speech = gTTS(text = text, lang = language, slow = False) #setting speech parameters
print("Processing...")
speech.save(f"{file_name}.mp3")
os.system(f"start {file_name}.mp3")
print('Done!')