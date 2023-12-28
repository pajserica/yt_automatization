from gtts import gTTS
import os

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f'start {filename}')

text = "Hello, this is a test of the text-to-speech function."
filename = "test.mp3"
text_to_speech(text, filename)
