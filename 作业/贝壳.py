# -*- coding: utf-8 -*-
# @Time    : 2022/7/31 23:29
# @Author  : lee
# @File    : 贝壳.py
import json
import pymysql
import requests
import pymongo


def get_data(i):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://cs.fang.ke.com/loupan/pg5/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "^\\^",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^"
    }
    cookies = {
        "select_city": "430100",
        "lianjia_uuid": "f5eda178-eae5-4b93-8700-72865f720f2f",
        "crosSdkDT2019DeviceId": "-c6832t--ivv8ww-1c9qz7iu3mo9yam-fdwp2akfr",
        "digv_extends": "^%^7B^%^22utmTrackId^%^22^%^3A^%^22^%^22^%^7D",
        "lianjia_ssid": "b649507a-4ffb-4c44-a1eb-b1f6683c3431",
        "digData": "^%^7B^%^22key^%^22^%^3A^%^22loupan_index^%^22^%^7D",
        "lj_newh_session": "eyJpdiI6IjhYY1ZHNm9MSFpINUhBdFpBaDRacGc9PSIsInZhbHVlIjoiZUMzSURJUHNSSDRKYnFZWE8wNGJIckhPamZKVjJmZ2tVSDg2RmxGejZ2c1gxQWV3VlJIMnVtcWZscHB5N25OUVdRZFRMZ3BybFFXS3puaTBDOG41SWc9PSIsIm1hYyI6ImI5ZDdkZTY1YzBhNTUyNGIxNmMzNmRhNTA5ODRiM2MwOGE2MDAwOWE1MmJlOWNkNjMwNmQzZDBjZTNlZTNhMTIifQ^%^3D^%^3D"
    }
    url = f"https://cs.fang.ke.com/loupan/pg{i}/"
    params = {
        "_t": "1"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    return response.text

def save_data_mongo(data):
    client = pymongo.MongoClient(host='localhost', port=27017)
    collection = client['beike']['list']
    # collection.insert_one({'a': 1})
    collection.insert_one(data)


def save_data_mysql():
    global db
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456',database='test2', charset='utf8')

    cursor = db.cursor()
    sql1 = f"insert into test1 VALUES ('{address}', '{average_price}');"
    cursor.execute(sql1)
    db.commit()



if __name__ == '__main__':
    for num in range(1, 80):
        res = get_data(num)
        res = json.loads(res)
        ls = res['data']['list']
        for item in ls:
            address = item['address']
            average_price = item['average_price']
            print(address, average_price)
            save_data_mongo({"address": address, 'average_price': average_price})
            save_data_mysql()
    db.close()





