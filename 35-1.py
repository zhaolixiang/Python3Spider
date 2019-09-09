from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq

base_url='https://m.weibo.cn/api/container/getIndex?'

headers={
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

def get_page(page):
    params={
        'type':'uid',
        'value':'2145291155',
        'containerid':'1076032145291155',
        'page':page
    }
    url=base_url+urlencode(params)
    print(url)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
        else:
            print('请求失败')
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse_page(json):
    if json:
        items=json.get('data').get('cards')
        for item in items:
            item=item.get('mblog')
            weibo={}
            weibo['id']=item.get('id')
            weibo['text']=pq(item.get('text')).text()
            # 点赞数量
            weibo['attitudes']=item.get('attitudes_count')
            # 评论数量
            weibo['comments']=item.get('comments_count')
            # 转发数量
            weibo['reposts']=item.get('reposts_count')
            yield weibo

if __name__ == '__main__':
    for page in range(1,15):
        json=get_page(page)
        for weibo in parse_page(json):
            print(weibo)
