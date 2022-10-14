# -*- coding: utf-8 -*-
# @Time    : 2022/8/27 19:34
# @Author  : lee
# @File    : tes.py
import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://mkt.zycg.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://mkt.zycg.gov.cn/mall-view/electronic",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "^\\^Chromium^^;v=^\\^104^^, ^\\^",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^"
}

url = "https://mkt.zycg.gov.cn/proxy/trade-service/mall/electronic/receipt/info/page/list"
data = {
    "pageNum": "4",
    "pageSize": "10",
    "platformId": "20"
}
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)