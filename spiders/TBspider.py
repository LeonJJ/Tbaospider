# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from Tbaospider.items import TbaospiderItem

class TbspiderSpider(scrapy.Spider):
    '''淘宝动态页面信息爬取'''
    name = 'TBspider'
    allowed_domains = ['taobao.com']
    def start_requests(self):
        start_urls = ["https://s.taobao.com/search?q=ipad&imgfile=&commend=all&" \
                      "ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1" \
                      "&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=10&ntoffset=10" \
                      "&p4ppushleft=1%2C48&s={0}".format(str(i)) for i in range(0,100,44)]
        for x in start_urls:
            yield Request(url=x,callback=self.parse)

    def parse(self, response):
        item = TbaospiderItem()
        item["title"] = response.xpath('//div[contains(@class,"row") and contains(@class,"row-2")]/a').xpath('string(.)').extract()
        item["price"] = response.css('.price.g_price.g_price-highlight strong::text').extract()
        item["buy_num"] = response.css('.deal-cnt::text').extract()
        yield item
