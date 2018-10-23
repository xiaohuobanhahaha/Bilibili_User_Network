# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import csv

class Bilibili_Tag(object):
    def open_spider(self,spider):
        self.f = open('bilibili_tag.json', 'w')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        return item
    def close_spider(self,spider):
        self.f.close()

class Bilibili_Comment(object):
    def open_spider(self,spider):
        self.f = open('bilibili_Comment.json', 'w')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        return item
    def close_spider(self,spider):
        self.f.close()

class Bilibili_Dm(object):
    def open_spider(self,spider):
        self.out = open("bilibili_Dm.csv", "w")
        self.writer = csv.writer(self.out)
    def process_item(self, item, spider):
        #字符传进入的
        self.writer.writerow(item['content'])
        return item
    def close_spider(self,spider):
        self.out.close()

class Bilibili_Info(object):
    def open_spider(self,spider):
        self.f = open('bilibili_Info.json', 'w')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        return item
    def close_spider(self,spider):
        self.f.close()