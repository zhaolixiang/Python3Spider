import requests

r=requests.get('https://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png')
with open('baidu.png','wb') as f:
    f.write(r.content)
