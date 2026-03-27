import pyttsx3
import threading

engine = pyttsx3.init()

def _speak(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    thread = threading.Thread(target=_speak, args=(text,))
    thread.start()