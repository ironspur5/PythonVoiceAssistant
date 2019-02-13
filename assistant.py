# Patrick Guha

import pyaudio
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import webbrowser
import requests
import json


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")
        print("I am fine")

    if "time" or "date" in data:
        speak(ctime())
        print(ctime())

    if "news" in data:
        webbrowser.open('https://news.google.com')

    if "joke" or "jokes" in data:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        joke = json.loads(response.text)
        speak(joke["setup"])
        speak(joke["punchline"])


# main
while 1:
    usrinput = input("Press A to ask me something or B to quit: ")
    if usrinput == "A":
        speak("What can I do for you?")
        data = recordAudio()
        jarvis(data)
    elif usrinput == "B":
        break




