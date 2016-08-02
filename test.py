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
import requests
import re

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename="scrapy_douban_1.log",
                    filemode='w')


# 获取页面中特定属性的信息
def attr_content(attr_list, attrname):
    for key, value in attr_list:
        if key == attrname:
            return value
    return None


# 解析登陆页面
class TangshiParse(HTMLParser.HTMLParser):

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.is_ul = False
        self.is_a = False
        self.current_tangshi = {}
        self.tangshi_list = []

    def handle_starttag(self, tag, attrs):

        # 匹配ul
        if tag == 'ul' and attr_content(attrs,"class") == "m-dot-list-2 f-cb":
            self.is_ul = True

        if self.is_ul and tag == 'a':
            self.current_tangshi["src"] = attr_content(attrs,"href")
            self.is_a = True

    def handle_endtag(self, tag):
        if tag == 'ul':
            self.is_ul = False

        if tag == 'a':
            self.is_a = False

    def handle_data(self, data):
        if self.is_ul and self.is_a:
            # print self.regx.findall(data)
            if re.match(r'\(',data):
                data2 = data.replace('(','')
                data2 = data2.replace(')','')
                self.current_tangshi['autor'] = data2
            else:
                self.current_tangshi['title'] = data
                self.tangshi_list.append(self.current_tangshi)
                self.current_tangshi = {}

def parse_page_content(content):
    tangshi_parser = TangshiParse()
    tangshi_parser.feed(content)
    print tangshi_parser.tangshi_list.__len__()
    for i in tangshi_parser.tangshi_list:
        print "%s"%i['title']

# 获取网页源内容
def get_content(url):

    resp = requests.get(url)
    return resp.content


if __name__ == "__main__":
    page_content = get_content("http://www.fanw8.com/gushi/tangshi/")
    tangshi_table = parse_page_content(page_content)