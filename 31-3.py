import json

with open('31-3.json','r') as file:
    str=file.read()
    data=json.loads(str)
    print(data)