# encoding:utf-8
'''
by 2016-07-17
学习爬虫的基本概念：logging/Request/cookielib.CookieJar/HTTPCookieProcessor/.build_opener/
'''

import urllib
import urllib2
import logging
import datetime
import logging
import cookielib

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename="scrapy_douban_1.log",
                    filemode='w')

def scrapy():

    # 设置一个请求
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    value = {"username":"linguoyang2008@126.com","password":"642180wolf"}
    req = urllib2.Request(url="http://www.douban.com",data=urllib.urlencode(value),headers=headers)
    # opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))

    # 设置cookie信息
    cookie_jar = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cookiejar=cookie_jar)

    # 设置打开的门
    opener = urllib2.build_opener(cookie_handler,urllib2.HTTPHandler(debuglevel=1),urllib2.HTTPSHandler(debuglevel=1))
    urllib2.install_opener(opener)

    # 正式请求
    try:
        # 打开一个一个请求，时间超时为3秒钟
        s = opener.open(req,timeout=3)
    except urllib2.HTTPError,e:
        logging.info(e)
    else:
        # print s.read()
        print "#"*50
        print cookie_jar._cookies
        print "#"*50
        s.close()

    # 第二次请求，将用到上边设置的cookies
    s1= opener.open("http://www.douban.com")
    # print s1.read()


if __name__ == "__main__":
    scrapy()