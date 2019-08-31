import requests
data={
    'name':'mark',
    'age':18
}
r=requests.get('http://httpbin.org/get',params=data)
print(r.text)