# Patrick Guha

import pyaudio
import speech_recognition as sr
from datetime import datetime
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

    if "time" in data:
        tm = datetime.now()
        speak(tm.strftime("%I:%M%p"))

    if "date" in data:
        now = datetime.now()
        speak(now.strftime("%A,%d %B,%Y"))

    if "news" in data:
        webbrowser.open('https://news.google.com')

    # adding the joke part always says a joke and messes up
    # maybe need to download archive as a json and import to avoid request
    '''
    if "joke" or "jokes" in data:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        joke = json.loads(response.text)
        speak(joke["setup"])
        speak(joke["punchline"])
    '''

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on, I will show you where " + location + " is.")



# initialization
time.sleep(2)
speak("Hi, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)

'''
while 1:
    usrinput = input("Press A to ask me something or B to quit: ")
    if usrinput == "A":
        speak("What can I do for you?")
        data = recordAudio()
        jarvis(data)
    elif usrinput == "B":
        break
'''







