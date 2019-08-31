from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
import urllib

rp=RobotFileParser()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req=urllib.request.Request(url='https://www.jianshu.com/robots.txt',headers=headers)
data=urllib.request.urlopen(req).read().decode('utf-8')
print(data)
rp.parse(data.split('\n'))
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
