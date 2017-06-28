#encoding=utf-8
import scrapy
import re
import sys
from douban.items import DoubanItem
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class DbbookSpider(scrapy.Spider):
    name = "dbbook"
    #allowed_domains = ["https://www.douban.com/doulist/1264675/"]
    start_urls = (
        'https://www.douban.com/doulist/1264675/',
    )
    #URL = 'https://www.douban.com/doulist/1264675/?start=PAGE&sort=seq&sub_type='

    def parse(self, response):
	item = DoubanItem()
        selector = scrapy.Selector(response)
        books = selector.xpath('//div[@class="bd doulist-subject"]')
        for each in books:
            title = each.xpath('div[@class="title"]/a/text()').extract()[0]
            rate = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            author = re.search('<div class="abstract">(.*?)<br',each.extract(),re.S).group(1)
            title = title.replace(' ','').replace('\n','')
            author = author.replace(' ','').replace('\n','')
	    item['title'] = title
            item['rate'] = rate
            item['author'] = author
            yield item
	    nextPage = selector.xpath('//span[@class="next"]/link/@href').extract()
            #print "nextPage is  " , nextPage
	    if nextPage:
		next = nextPage[0]
		#print next
		yield scrapy.http.Request(next,callback=self.parse)
