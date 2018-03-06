# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class TbaospiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



from selenium import webdriver
from scrapy.http import HtmlResponse
class JSpageMiddlewares(object):
    '''通过Chrome请求动态网页'''
    def __init__(self):
        # 初试化打开chromedriver，让其只属于该类，爬取中只在一个浏览器窗口中执行
        self.browser = webdriver.Chrome(executable_path="D:/浏览器/Chrome/chromedriver.exe")
        super(JSpageMiddlewares,self).__init__()

    def process_request(self, request, spider):
        if spider.name =="TBspider":
            self.browser.get(request.url)
            self.browser.implicitly_wait(10)

        #遇到HtmlResponse就不会执行downloader，直接返会spider
        return HtmlResponse(self.browser.current_url,body=self.browser.page_source,encoding="utf-8",request=request)
