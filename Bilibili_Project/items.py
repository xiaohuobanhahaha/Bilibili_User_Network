# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 4个api页面item

# 评论item分为page层面，楼层，评论的回复3个层面
class Comment_Content_Page(scrapy.Item):
    acount = scrapy.Field()
    count = scrapy.Field()
    num = scrapy.Field()
    size = scrapy.Field()

class Comment_Content_Floor(scrapy.Item):
    rpid = scrapy.Field()
    mid = scrapy.Field()
    count = scrapy.Field()
    rcount = scrapy.Field()
    floor = scrapy.Field()
    ctime = scrapy.Field()
    like = scrapy.Field()
    uname = scrapy.Field()
    sex = scrapy.Field()
    sign = scrapy.Field()

# tag item
class Tag_Content(scrapy.Item):
    aid = scrapy.Field()
    tag_id = scrapy.Field()
    tag_name = scrapy.Field()
    ctime = scrapy.Field()
    view = scrapy.Field()
    use = scrapy.Field()
    atten = scrapy.Field()
    likes = scrapy.Field()
    hates = scrapy.Field()
    attribute = scrapy.Field()

#视频信息 item
class Information_Content(scrapy.Item):
    videos = scrapy.Field()
    titile = scrapy.Field()
    pubdate = scrapy.Field()
    ctime = scrapy.Field()
    tname = scrapy.Field()
    duration = scrapy.Field()
    cid = scrapy.Field()
    view = scrapy.Field()
    danmaku = scrapy.Field()
    favorite = scrapy.Field()
    coin = scrapy.Field()
    share = scrapy.Field()
    now_rank = scrapy.Field()
    his_rank = scrapy.Field()
    like = scrapy.Field()
    dislike = scrapy.Field()
    owner_mid = scrapy.Field()
    owner_name = scrapy.Field()

#弹幕信息 item
class Dm_Content(scrapy.Item):
    content = scrapy.Field()