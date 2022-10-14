import time

import requests
import pymongo
from multiprocessing import Pool

client = pymongo.MongoClient(host='localhost', port=27017)
collection = client['新发地']['list']


def get_data(num):
    headers = {
        "Origin": "http://www.xinfadi.com.cn",
        "Referer": "http://www.xinfadi.com.cn/index.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63",
    }
    url = "http://www.xinfadi.com.cn/getCat.html"
    data = {
        "prodCatid": num
    }
    response = requests.post(url, headers=headers, data=data, verify=False)
    p_li = response.json()['list']
    for item in p_li:
        prodName = item['prodName']
        proplace = item['place']
        highPrice = item['highPrice']
        lowPrice = item['lowPrice']
        pubDate = item['pubDate']
        collection.insert_one({'prodName': prodName, 'proplace':proplace, 'highPrice':highPrice, 'lowPrice':lowPrice, 'pubDate':pubDate})


if __name__ == '__main__':
    start_time = time.time()
    num = 1186
    page = []
    for i in range(5):
        page.append(num+i)
    print(page)
    pool = Pool(processes=5)
    pool.map(get_data, page)
    pool.close()
    end_time = time.time()
    print(end_time-start_time)





