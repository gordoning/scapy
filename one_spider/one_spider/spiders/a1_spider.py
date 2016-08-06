# -*- coding: utf-8 -*-
import scrapy
from one_spider.items import OneSpiderItem


class A1SpiderSpider(scrapy.Spider):
    name = "1_spider"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.maiziedu.com/course/list/','http://httpbin.org/html/'
    )

    def parse(self, response):
        filename = response.url.spit('/')[-2]
        with open(filename,'wb') as f:
            f.write(response.body)

        lst = response.xpath("html/div/ul/li[3]/strong/a")
        for li in lst:
            item = OneSpiderItem()
            item['title'] = li.xpath('a/@id').extract()