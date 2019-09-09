from urllib.parse import urlencode
import requests
import time
import os
from hashlib import md5
from multiprocessing import Pool

base_url='https://www.toutiao.com/api/search/content/?'

headers={
    # 打开链接，复制cookie就可以了
    'cookie':'tt_webid=6734577111727752712; s_v_web_id=6ddb001d2d27ac086d983e04ad1c05b0; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=rv5eej3uk1568015931672; tt_webid=6734577111727752712; csrftoken=b37d93547b30ce486bf294bd555d6c7c',
    'Host':'www.toutiao.com',
    'Referer':'https://www.toutiao.com/search/?keyword=%E8%B7%AF%E4%BA%BA',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

def get_page(offset):
    #获取当前毫秒级时间戳
    timestamp=int(round(time.time()*1000))
    params={
        'aid':24,
        'app_name':'web_search',
        'offset':offset,
        'format':'json',
        'keyword':'路人',
        'autoload':'true',
        'count':'20',
        'en_qc':1,
        'cur_tab': '1',
        'from':'search_tab',
        'pd':'synthesis',
        'timestamp':timestamp
    }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        print('报错了')
    return None


def get_images(json):
    if json and json.get('data'):
        for item in json.get('data'):
            title=item.get('title')
            images=item.get('image_list')
            # 剔除脏数据
            if title and images:
                for image in images:
                    yield {
                        'image':image.get('url'),
                        'title':title
                    }

def save_image(item):
    path='36-1/'+item.get('title')
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        response=requests.get(item.get('image'))
        if response.status_code==200:
            file_path='{0}/{1}.{2}'.format(path,md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('这个文件已经存在',file_path)
    except requests.ConnectionError:
        print('报错图片失败了')


def main(offset):
    json = get_page(offset)
    for img in get_images(json):
        save_image(img)

start=1
end=20
if __name__ == '__main__':
    pool=Pool(3)
    groups=([x*20 for x in range(start,end+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()