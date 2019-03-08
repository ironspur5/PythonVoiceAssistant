import json
import pandas as pd

def retjoke():
    with open('index.json') as json_data:
        d = json.load(json_data)
        df = pd.DataFrame(d)

    subdf = df[df['id'].isin([7])]
    setUp = str(subdf.setup)
    punch = str(subdf.punchline)
    return setUp, punch


#print(setUp)
#print(punch)



