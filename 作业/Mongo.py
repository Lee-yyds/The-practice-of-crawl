# -*- coding: utf-8 -*-
# @Time    : 2022/7/31 16:27
# @Author  : lee
# @File    : Mongo.py
import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)
collection = client['beike']['list']
for i in range(10):
    collection.insert_one({"address": i, "name": 2*i})
