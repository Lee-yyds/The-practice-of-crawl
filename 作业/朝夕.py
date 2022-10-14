# -*- coding: utf-8 -*-
# @Time    : 2022/8/27 15:01
# @Author  : lee
# @File    : 朝夕.py
import hashlib


def md5_test2(a):
    md5 = hashlib.md5()
    md5.update(f'{a}'.encode('utf-8'))
    print(md5.hexdigest())


if __name__ == '__main__':
    md5_test2(123456)






