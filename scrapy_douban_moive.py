# encoding:utf-8
'''
by 2016-07-17
豆瓣的热门电影
'''

import urllib
import urllib2
import logging
import datetime
import logging
import cookielib
import HTMLParser

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename="scrapy_douban_1.log",
                    filemode='w')

# 解析抓取的电影网页
class MovieParse(HTMLParser.HTMLParser):

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.movies = []

    # 根据HTML元素和元素中的属性，来抽取想要的内容。attrs是一个存取数组：【（key,value）,(key,value)]
    def handle_starttag(self, tag, attrs):
        # 获取电影中某个属性的信息，如电影名称，电影评分
        def movie_content(attr_list,attrname):
            for key,value in attr_list:
                if key == attrname:
                    return value
            return None

        # 判断网页中的元素，是否为电影相关的内容。如果是，则抓取；如果不是，则不抓取
        if tag == 'li' and movie_content(attrs,"data-title") and movie_content(attrs,"data-category") == "nowplaying":
            movie = {}
            movie["data-title"] = movie_content(attrs, "data-title")
            movie["data-score"] = movie_content(attrs, "data-score")
            movie["data-star"] = movie_content(attrs, "data-star")
            movie["data-release"] = movie_content(attrs, "data-release")
            movie["data-actors"] = movie_content(attrs, "data-actors")
            # 将电影的信息，存到电影列表中，同时打印出电影信息
            self.movies.append(movie)
            print "%s--评分：%s--%s"%(movie["data-title"],movie["data-score"],movie["data-actors"])

# 抓取电影，
# 输入：url
# 解析网页
def scrapy_movie():

    # 设置一个请求，包括headers，data
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # value = {"username":"linguoyang2008@126.com","password":"642180wolf"}
    req = urllib2.Request(url="https://movie.douban.com/nowplaying/suzhou/",headers=headers)
    # opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))

    # 正式请求
    try:
        response = urllib2.urlopen(req,timeout=20)
    except urllib2.HTTPError,e:
        logging.info(e)
    else:
        page_content = response.read()
        response.close()

    # 解析网页
    page_movie = MovieParse()
    page_movie.feed(page_content)

if __name__ == "__main__":
    scrapy_movie()