# -*- coding: utf-8 -*-
# time: 2022/10/27 21:47
# file: yaojianju.py
# author: LyChow
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def getContent():
    count = 0
    while True:
        option = Options()
        # 为Chrome配置无头模式
        # option.add_argument("--headless")
        # 防止被检测
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        # 实例化浏览器
        web = webdriver.Chrome(chrome_options=option)
        # web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     "source": """
        #                     Object.defineProperty(navigator, 'webdriver', {
        #                       get: () => undefined
        #                     })
        #                   """
        # })
        web.get('http://scxk.nmpa.gov.cn:81/xk')
        page_text = web.page_source
        print(page_text)
        # html_content = etree.HTML(page_text)
        # items_content = html_content.xpath('/html/body//ul[@id="gzlist"]/li')
        # web.close()
        # if len(items_content) > 0:
        #     return page_text
        # print('未获取到数据，睡眠', (10 + count * 5), '秒')
        time.sleep(10 + count * 5)
        count += 1


if __name__ == '__main__':
    content = getContent()
    # html = etree.HTML(content)
    # items = html.xpath('/html/body//ul[@id="gzlist"]/li')
    # for item in items:
    #     print(item.xpath('./dl/@title')[0])
