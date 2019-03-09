# Patrick Guha, Abel Philips, Mason Valicek

import speech_recognition as sr
from datetime import datetime
import time
import os
from gtts import gTTS
import webbrowser
import random
from tkinter import *
from weather import getWeather


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
        #LABEL = Label(ROOT, text="I am fine")
        #LABEL.pack()

    # previously it was if "joke" or "jokes" in data
    # thus caused the joke case to run every time! Deleting or "jokes" fixed the issue
    if "joke" in data:
        # get a random number between 0 and 75 to get a random joke
        ranNum = random.randint(0, 75)
        # preload joke before request
        jokeDict = eval(open("dict.txt").read())
        setUpline = jokeDict[ranNum]["setup"]
        punchy = jokeDict[ranNum]["punchline"]
        speak(setUpline)
        speak(punchy)

    if "time" in data:
        tm = datetime.now()
        speak("The time is " + tm.strftime("%I:%M%p"))
        #LABEL = Label(ROOT, text=tm.strftime("%I:%M%p"))
        #LABEL.pack()

    if "date" in data:
        now = datetime.now()
        speak("Today is " + now.strftime("%A,%d %B,%Y"))
        #LABEL = Label(ROOT, text=now.strftime("%A,%d %B,%Y"))
        #LABEL.pack()

    if "news" in data:
        speak("Coming right up")
        #LABEL = Label(ROOT, text="Coming right up")
        #LABEL.pack()
        webbrowser.open('https://news.google.com')


    if "weather" in data:
            speak(str(getWeather()))



'''
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









