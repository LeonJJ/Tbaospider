# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class TbaospiderPipeline(object):
    def __init__(self):
        '''链接MongoDB并创建存储数据库'''
        host = '127.0.0.1'
        port = 27017
        conn = pymongo.MongoClient(host=host,port=port)
        dbname =conn['Tbao']
        self.post_info = dbname['text']

    def process_item(self, item, spider):
        for i in range(len(item["title"])):
            title =item["title"][i].strip()
            price = item["price"][i]
            buy_num = item["buy_num"][i].replace("人付款","")
            dict = {
                "title":title,
                "price":price,
                "buy_num":buy_num
            }
            self.post_info.insert(dict)
        return item
