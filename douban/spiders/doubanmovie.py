#encoding=utf-8
import scrapy
import re
import sys
import json
from douban.items import DoubanMovie
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class DoubanmovieSpider(scrapy.Spider):
    name = "doubanmovie"
    #allowed_domains = ["https://movie.douban.com/"]
    start_urls = (
        'https://movie.douban.com/j/search_subjects?type=movie&tag=%E9%9F%A9%E5%9B%BD&sort=rank&page_limit=20&page_start=0',
    )
    page = 0

    def parse(self, response):
        item = DoubanMovie()
        page = self.page
        jdict = json.loads(response.body)
        jcontent = jdict['subjects']
        if jcontent:
            for each in jcontent:
                item['rate'] = each['rate']
                item['title'] = each['title']
                item['url'] = each['url']
                yield item
            self.page += 20
            nextPage = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E9%9F%A9%E5%9B%BD&sort=rank&page_limit=20&page_start={}'.format(page)
            yield scrapy.http.Request(nextPage, callback=self.parse) 
