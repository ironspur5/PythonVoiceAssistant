import json

def jsonConvert2Dict():
    with open('index.json') as json_data:
        dictionary = json.load(json_data)

    f = open("dict.txt", "w")
    f.write(str(dictionary))
    f.close()

jsonConvert2Dict()
