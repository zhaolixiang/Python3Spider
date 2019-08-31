import urllib.request
import urllib.error
import socket

try:
    response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
    print(response.read())
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('Time Out')

