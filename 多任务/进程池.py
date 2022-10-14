# -*- coding: utf-8 -*-
# @Time    : 2022/8/28 23:11
# @Author  : lee
# @File    : 进程池.py
from multiprocessing import Pool
import multiprocessing
from lxml import etree
import requests

maps1 = lambda x: x[0] if x else x


def request(url):
    headers = {
        'user-agent': '123123',
        'Cookie': 'BAIDU_SSP_lcr=https://www.baidu.com/link?url=MHEtdkDrZiaQ_Fo9zGor7bR9k3gFykSpTtWIpPmJXZvJWVEzlFA6DL83dC7m-1qv&wd=&eqid=ee92cf0700010b5000000006622f2938; Hm_lvt_8b80e9af8bc9476c3b2068990922a408=1647257918; ASPSESSIONIDQWDRCSDC=BLCMBEEDPAPHFAICHNJFGGNA; countsql=%5BS%5Fchexi%5Dwhere+1%3D1; fenyecounts=1183; ASPSESSIONIDQWBTBSDD=BHOENMODOFLOPJIFEHAMEHPC; Hm_lpvt_8b80e9af8bc9476c3b2068990922a408=1647326383',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        res.encoding = 'gb2312'
        parse(res)


def parse_xpath(obj, tag):
    html = etree.HTML(obj)
    text = html.xpath(tag)
    return text


def parse(res):
    url = '//ul[@class="goods_list"]/li'
    items = parse_xpath(res.text, url)
    for item in items:
        title = maps1(item.xpath('./p[@class="name"]/a/@title'))
        price = maps1(item.xpath('./p[@class="price_wrap"]/span/text()'))
        print({'品牌': title, '价格': price})
        print('=' * 50)


def run():
    import time
    s = time.time()
    url = 'https://www.2smoto.com/pinpai/'
    res = requests.get(url)
    res.encoding = 'gb2312'
    html = maps1(parse_xpath(res.text, "//a[contains(text(),'尾页')]/@href"))
    count = html.split('=')[-1]
    # https://www.2smoto.com/pinpai.asp?ppt=&slx=0&skey=&page=2
    cpu_count = multiprocessing.cpu_count()
    print("CPU 核心数量是：", cpu_count)
    pool = Pool(processes=8)  # 8个进程
    # for i in range(1,int(count)+1):
    #     url = 'https://www.2smoto.com/pinpai.asp?ppt=&slx=0&skey=&page={}'.format(i)
    #     pool.apply_async(request, (url,))
    pool.map(request,
             ('https://www.2smoto.com/pinpai.asp?ppt=&slx=0&skey=&page={}'.format(i) for i in range(1, int(count) + 1)))
    pool.close()  # 关闭进程池，关闭之后，不能再向进程池中添加进程
    pool.join()  # 当进程池中的所有进程执行完后，主进程才可以继续执行。
    print('程序耗时{}'.format(time.time() - s))


if __name__ == '__main__':
    run()
