from urllib import request,error

try:
    response=request.urlopen('http://markmarkmark.com/mark',timeout=3)
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')