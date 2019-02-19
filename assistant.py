# Patrick Guha

import speech_recognition as sr
from datetime import datetime
import time
import os
from gtts import gTTS
import webbrowser
# import requests
# import json
from tkinter import *


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
        LABEL = Label(ROOT, text="I am fine")
        LABEL.pack()

    if "time" in data:
        tm = datetime.now()
        speak(tm.strftime("%I:%M%p"))
        LABEL = Label(ROOT, text=tm.strftime("%I:%M%p"))
        LABEL.pack()

    if "date" in data:
        now = datetime.now()
        speak(now.strftime("%A,%d %B,%Y"))
        LABEL = Label(ROOT, text=now.strftime("%A,%d %B,%Y"))
        LABEL.pack()

    if "news" in data:
        speak("Coming right up")
        LABEL = Label(ROOT, text="Coming right up")
        LABEL.pack()
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
        LABEL = Label(ROOT, text="Hold on, I will show you where " + location + " is.")
        LABEL.pack()


ROOT = Tk()
LOOP_ACTIVE = True
time.sleep(2)
speak("Hi, what can I do for you?")
while LOOP_ACTIVE:
    ROOT.update()
    data = recordAudio()
    USER_INPUT = data
    if USER_INPUT == "exit":
        ROOT.quit()
        LOOP_ACTIVE = False
    else:
        LABEL = Label(ROOT, text=USER_INPUT)
        LABEL.pack()
    jarvis(data)


'''
# initialization
time.sleep(2)
speak("Hi, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
'''


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







