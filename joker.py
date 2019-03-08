import requests
import json


def getJoke():
    #response = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"})
    #https://official-joke-api.appspot.com/random_joke
    #https://icanhazdadjoke.com/
    #joke = json.loads(response.text)

    #setup = joke["setup"]
    #punchline = joke["punchline"]

    #funny = joke["joke"]
    #print(funny)

    #return funny

    with open('index.json') as json_data:
        d = json.load(json_data)

    print(d)



getJoke()

