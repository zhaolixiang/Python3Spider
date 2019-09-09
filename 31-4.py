import json

data = [{
    'name': 'Mark',
    'gender': '男',
    'birthday': '1992-05-04'
}]

with open('31-4.json','w',encoding='utf-8') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))