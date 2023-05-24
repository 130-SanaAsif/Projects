import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import json
from bs4 import BeautifulSoup


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
        speak("Good Morning!")
    elif hour>=12 and hour<=24:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("Myself Elsa how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def search_youtube(query):
    speak(f"Searching YouTube for {query}...")

    # Make a request to the YouTube Data API to retrieve search results
    API_KEY = "YOUR_YOUTUBE_API_KEY"
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={API_KEY}"
    response = requests.get(search_url)
    json_data = json.loads(response.text)

    # Extract the video ID of the first search result
    video_id = json_data["items"][0]["id"]["videoId"]

    # Construct the video URL and open it in the web browser
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    webbrowser.open(video_url)

def play_youtube_video():
    speak("What video would you like to search for?")
    command = takeCommand()
    search_youtube(command)

def close_vscode():
    speak("Closing VS Code...")
    os.system("taskkill /F /IM Code.exe")

def search_google(query):
    speak(f"Searching {query} on google.")
    query = query.replace(" ","+")
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    webbrowser.open(search_url)
    soup = BeautifulSoup(response.text,"html.parser")
    search_results = soup.find_all("div",class_="yuRUbf")
    if search_results:
        result_text = "Here are the top search results:\n"
        for i in range(min(3, len(search_results))):
            result_text += f"{i + 1}. {search_results[i].a.get_text()}\n"
        speak(result_text)
    else:
        speak("No search results found.")

def search_on_google():
    speak("What would you like to search for?")
    query = takeCommand()
    search_google(query)

if __name__ == "__main__":
    speak("Hello Ma'am!")
    wishMe()

    while(True):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'search on google' in query:
            search_on_google()
        elif 'open udemy' in query:
            webbrowser.open("udemy.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Ma'am, the time is {strTime}")
        elif 'open chat gpt' in query:
            webbrowser.open("chat.openai.com")
        elif 'open vs code' in query:
            codePath = "C:\\Users\\SANA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'close vs code' in query:
            close_vscode()
        elif 'go to sleep' in query:
            speak("Going to sleep")
            break
        