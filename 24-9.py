import requests

data={'name':'mark','age':18}
r=requests.post('http://httpbin.org/post',data=data)
print(r.text)