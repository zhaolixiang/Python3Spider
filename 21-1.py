from urllib import request,error

try:
    response=request.urlopen('http://markmarkmark.com/mark',timeout=10)
except error.URLError as e:
    print(e.reason)