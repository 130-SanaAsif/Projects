import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("A very delightful Good Morning!")
    elif hour>=12 and hour<=24:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("Myself Elsa how may I help you?")
if __name__ == "__main__":
    speak("Hello Ma'am!")
    wishMe()