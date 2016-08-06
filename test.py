# coding:utf-8
'''
by 2016-07-20
唐诗三百首
'''

import urllib
import urllib2
import logging
import datetime
import logging
import cookielib
import HTMLParser
import re
import scrapy

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename="scrapy_douban_1.log",
                    filemode='w')



class lgy_spider(scrapy.Spider):
    name = "linguoyang_spider"
    start_urls = ["http://news.baidu.com"]

    def parse(self, response):
        for href in response.css('@pane-news div ul li[1] strong a : attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=news_content)

    def news_content(self,response):
        yield {
            'title':123
        }

