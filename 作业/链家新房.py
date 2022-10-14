# -*- coding: utf-8 -*-
# @Time    : 2022/8/27 9:38
# @Author  : lee
# @File    : 链家新房.py
import requests
from pprint import pprint


headers = {
    "Referer": "https://bj.fang.lianjia.com/loupan/pg2/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63",
}

url = "https://bj.fang.lianjia.com/loupan/pg2/"
params = {
    "_t": "1"
}
for i in range(10):
    response = requests.get(url, headers=headers, params=params)
    mlist = response.json()['data']['list']

    for item in mlist:
        address = item['address']
        address_remark=item['address_remark']
        average_price=item['average_price']
        resblock_name=item['resblock_name']
        print(address, address_remark, average_price, resblock_name)

