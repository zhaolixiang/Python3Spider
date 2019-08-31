from urllib import request,error
import socket

try:
    response=request.urlopen('http://markmarkmark.com/mark',timeout=3)
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
else:
    print('Request Successfully')