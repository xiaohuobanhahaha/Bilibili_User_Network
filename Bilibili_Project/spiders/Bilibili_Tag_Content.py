# -*- coding: utf-8 -*-
import scrapy
import json
from Bilibili_Project.items import Tag_Content
import time

def Build_Link_Tag(aid):
    Link = 'https://api.bilibili.com/x/tag/archive/tags?aid=' + str(aid)
    return Link

def Match_Tag(tag):
    Dictionary = {'影评', '几分钟解说', '电影解说', '影视杂评', '电影杂谈',
                  '几分钟影评', '几分钟看电影', '影视杂谈'
                  }
    for i in Dictionary:
        if tag == i:
            return 1
    return 0


class BilibiliTagContentSpider(scrapy.Spider):
    name = 'Bilibili_Tag_Content'
    aid = 31881071
    custom_settings = {
        'ITEM_PIPELINES': {'Bilibili_Project.pipelines.Bilibili_Tag': 200
                           }
    }
    Link = 'https://api.bilibili.com/x/tag/archive/tags?aid=' + str(aid)
    start_urls = [Link]

    def parse(self, response):
        if response.status==200:
            text_data = json.loads(response.text)
            item = Tag_Content()
            try:
                for j in text_data['data']:
                    tag_name = j['tag_name']
                    if Match_Tag(tag_name) == 1:
                        for i in text_data['data']:
                            item['aid']= self.aid
                            item['tag_name'] = i['tag_name']
                            item['tag_id'] = i['tag_id']
                            item['ctime'] = i['ctime']
                            item['view'] = i['count']['view']
                            item['use'] = i['count']['use']
                            item['atten'] = i['count']['atten']
                            item['likes'] = i['likes']
                            item['hates'] = i['hates']
                            item['attribute'] = i['attribute']
                            yield item
                        break
                    else:
                        pass
            except Exception as e:
                pass
            if self.aid > 31890000:
                quit()
            self.aid += 1
            yield scrapy.Request(url=Build_Link_Tag(self.aid), callback=self.parse)
        else:
            print('连不上了')
            print(response.status)
            return



