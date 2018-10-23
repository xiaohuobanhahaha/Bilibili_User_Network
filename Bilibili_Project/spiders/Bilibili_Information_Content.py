# -*- coding: utf-8 -*-
import scrapy
import json
from Bilibili_Project.items import Information_Content

class BilibiliInformationContentSpider(scrapy.Spider):
    name = 'Bilibili_Information_Content'
    aid = 31881071
    custom_settings = {
        'ITEM_PIPELINES': {'Bilibili_Project.pipelines.Bilibili_Info': 200
                           }
    }
    Link = 'https://api.bilibili.com/x/web-interface/view?aid=' + str(aid)
    start_urls = [Link]

    def parse(self, response):
        text_data = json.loads(response.text)['data']
        item = Information_Content()
        # 是否存在合集问题，分集信息目前被整合到合集当中
        item['videos'] = text_data['videos']
        item['titile'] = text_data['title']
        item['pubdate'] = text_data['pubdate']
        item['ctime'] = text_data['ctime']
        item['tname'] = text_data['tname']
        item['duration'] = text_data['duration']
        item['cid'] = text_data['cid']
        item['view'] = text_data['stat']['view']
        item['danmaku'] = text_data['stat']['danmaku']
        item['favorite'] = text_data['stat']['favorite']
        item['coin'] = text_data['stat']['coin']
        item['share'] = text_data['stat']['share']
        item['now_rank'] = text_data['stat']['now_rank']
        item['his_rank'] = text_data['stat']['his_rank']
        item['like'] = text_data['stat']['like']
        item['dislike'] = text_data['stat']['dislike']
        item['owner_mid'] = text_data['owner']['mid']
        item['owner_name'] = text_data['owner']['name']
        yield item