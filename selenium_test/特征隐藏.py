# -*- coding: utf-8 -*-
# time: 2022/10/27 21:17
# file: 特征隐藏.py
# author: LyChow
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()

# 禁止图片
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)

# 无头模式 在后台运行
# options.add_argument("-headless")

# 通过设置user-agent
# user_ag = '123456'
# options.add_argument('user-agent=%s' % user_ag)

# 隐藏"Chrome正在受到自动软件的控制"
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 检测绕过
options.add_argument('--disable-blink-features=AutomationControlled')


# 设置代理
# options.add_argument('proxy-server=' +'192.168.0.28:808')



# **************
# 初始化配置
driver = webdriver.Chrome(chrome_options=options)

# 将浏览器最大化显示
# browser.maximize_window()
# 设置宽高
# browser.set_window_size(480, 800)

# 通过js新打开一个窗口
# driver.execute_script('http://scxk.nmpa.gov.cn:81/xk/");')

# 获取网站
driver.get('http://scxk.nmpa.gov.cn:81/xk/')
# find_element用法
driver.find_element(By.ID, 'searchtext').send_keys('苏妆20180001')
driver.find_element(By.ID, 'searchInfo').click()
time.sleep(1)
print(driver.page_source)

