# -*- coding: utf-8 -*-
import scrapy
from Bilibili_Project.items import Comment_Content_Page
from Bilibili_Project.items import Comment_Content_Floor
import json


class BilibiliCommentContentSpider(scrapy.Spider):
    name = 'Bilibili_Comment_Content'

    custom_settings = {
        'ITEM_PIPELINES': {'Bilibili_Project.pipelines.Bilibili_Comment': 200
                           }
    }
    aid = 31881071
    np =1
    Link = 'https://api.bilibili.com/x/v2/reply?pn=' + str(np) + '&type=1&oid=' + str(aid) + '&sort=0'
    start_urls = [Link]

    def parse(self, response):
        text_data = json.loads(response.text)
        item = Comment_Content_Page()
        item1 = Comment_Content_Floor()
        item['acount'] = text_data['data']['page']['acount']
        item['count'] = text_data['data']['page']['count']
        item['num'] =text_data['data']['page']['num']
        item['size'] =text_data['data']['page']['size']
        #item 储存结构
        # reply 分层分楼，按照父 楼层遍历
        # 遍历当前页的所有评论
        for i in text_data['data']['replies']:
            item1['rpid'] =i['rpid']
            item1['mid']= i['mid']
            item1['count'] = i['count']
            item1['rcount'] = i['count']
            item1['floor']= i['floor']
            item1['ctime']= i['ctime']
            item1['like'] =i['like']
            item1['uname']= i['member']['uname']
            item1['sex']= i['member']['sex']
            item1['sign']=i['member']['sign']
            yield item1

        if item['num']*item['size']<item['count']:
            self.np += 1
            self.Link = 'https://api.bilibili.com/x/v2/reply?pn=' + str(self.np) + '&type=1&oid=' + str(self.aid) + '&sort=0'
            yield scrapy.Request(url=self.Link, callback=self.parse)

