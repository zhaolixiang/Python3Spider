import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

html=requests.get(url,headers=headers).text

doc=pq(html)
items=doc('.ExploreSpecialCard.ExploreHomePage-specialCard').items()
for item in items:
    # 专题名称
    question=item.find('.ExploreSpecialCard-title').text()
    file=open('31-1.txt','a',encoding='utf-8')
    file.write(question)
    file.write('\n'+'='*50+'\n')
    file.close()

