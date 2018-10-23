# -*- coding: utf-8 -*-
import scrapy
from Bilibili_Project.items import Dm_Content
from bs4 import BeautifulSoup

class BilibiliDmContentSpider(scrapy.Spider):
    name = 'Bilibili_Dm_Content'
    custom_settings = {
        'ITEM_PIPELINES': {'Bilibili_Project.pipelines.Bilibili_Dm': 200
                           }
    }
    cid =55757542
    Link = 'https://api.bilibili.com/x/v1/dm/list.so?oid=' + str(cid)
    start_urls = [Link]

    def parse(self, response):
        web_data = BeautifulSoup(response.text,'lxml')
        item = Dm_Content()
        #xml格式，xpath 怎么拿 ，使用Bs 速度会减慢很多
        for i in web_data.find_all('d'):
            item['content'] = i.string
            yield item

