# -*- coding: utf-8 -*-
# @Time    : 2022/8/27 19:28
# @Author  : lee
# @File    : pdf.py
import pdfplumber

with pdfplumber.open('浮山县气象局货物项目DD22082614579120_YgHmvE.pdf') as pdf:
    # for page in pdf.pages:
    print(pdf.pages[0].extract_table()[1])
    print(pdf.pages[0].extract_table()[1][-1])


    # data = ''.join(page.extract_text() for page in pdf.pages)




# import pdfplumber
#
# # 读取pdf文件，保存为pdf实例
# pdf = pdfplumber.open("中国传媒大学货物项目DD22082710583320_vplBBa.pdf")
#
# # 访问第二页
# first_page = pdf.pages[1]
#
# # 自动读取表格信息，返回列表
# table = first_page.extract_table()
# print(table)
