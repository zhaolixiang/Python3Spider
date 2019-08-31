import urllib.request

request=urllib.request.Request('https://httpbin.org/get')
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
