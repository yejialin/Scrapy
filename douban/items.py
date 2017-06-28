# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rate = scrapy.Field()
    author = scrapy.Field()

class DoubanMovie(scrapy.Item):
    # define the fields for movie item
    rate = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
