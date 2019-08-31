from urllib.parse import urlunparse,urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote

data=['http','www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

result=urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)


data=['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))


print(urljoin('http://www.baidu.com','Mark.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))


params={
    'name':'mark',
    'agr':18
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)

query='name=mark&age=19'
print(parse_qs(query))


query='name=mark&age=19'
print(parse_qsl(query))


keyword='壁纸'
url='https://www.baidu.com/s?wd='+quote(keyword)
print(url)

print(unquote(url))


