# Patrick Guha

import pyaudio
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from pygame import mixer

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    #os.system("mpg321 audio.mp3")
    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.play()



def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
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

        print("i am fine")

    if "what time is it" in data:
        speak(ctime())
        print(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        print("it is here")
        #speak("Hold on Frank, I will show you where " + location + " is.")
        #os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


# initialization
# while 1:
time.sleep(2)
speak("Hi Frank, what can I do for you?")
time.sleep(2)
data = recordAudio()
jarvis(data)



