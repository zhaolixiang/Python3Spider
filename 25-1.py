import requests

files={'files':open('baidu.png','rb')}
r=requests.post('http://httpbin.org/post',files=files)
print(r.text)