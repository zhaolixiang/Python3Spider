from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy_handler=ProxyHandler({
    'http':'http://127.0.0.1:1087',
    'https':'https://127.0.0.1:1087'
})

opener=build_opener(proxy_handler)

try:
    response=opener.open('http://httpbin/get')
    print(response.read().decode('utf-8'))
except Exception as e:
    print(e.reason)