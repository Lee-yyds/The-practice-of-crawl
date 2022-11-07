# -*- coding: utf-8 -*-
# time: 2022/10/27 20:37
# file: sel.py
# author: LyChow
from selenium import webdriver
from selenium.webdriver.common.by import By


# 实例化浏览器
driver = webdriver.Chrome()
# 获取网站
driver.get('https://www.baidu.com')


# find_element用法
driver.find_element(By.ID, 'kw').send_keys('selenium')
driver.find_element(By.ID, 'su').click()


# 输出当前页面源码
# print(driver.page_source)
# 提取当前页面的cookie
print(driver.get_cookies())
# 获取当前页面的截屏
driver.get_screenshot_as_file('123.png')
# 获取当前访问的地址
print(driver.current_url)


# 退出当前页面
# driver.quit()

