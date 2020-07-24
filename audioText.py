
import speech_recognition as sr
import time

r = sr.Recognizer()

# content in AudioFile is editable!.
with sr.AudioFile('C:\\Users\\mati12\\Music\\WhatsApp Ptt 2020-07-20 at 00.33.48.wav') as source:
    audio = r.listen(source)

    try:
        print("Reading audio file. Please, wait a moment...")
        text = r.recognize_google(audio, language='es-ES')
        time.sleep(1.5)
        print(text)
    except:
        print("I am sorry! I can not understand!")
