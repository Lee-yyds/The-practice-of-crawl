# -*- coding: utf-8 -*-
# @Time    : 2022/8/27 10:18
# @Author  : lee
# @File    : selenium--唯品会.py
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Edge()
browser.get("https://category.vip.com/suggest.php?keyword=%E5%8F%A3%E7%BA%A2&ff=235|12|1|1")
print(browser.page_source.encode('utf-8'))
for i in range(1,9):
    time.sleep(random.randint(100, 300) / 1000)
    browser.execute_script('window.scrollTo(0,{})'.format(i * 700))


