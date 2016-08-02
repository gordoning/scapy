# encoding:utf-8
'''
by 2016-07-27
爬取贴吧链接里面的头像,用户名作为头像图片的名称'''

import urllib
import urllib2
import logging
import cookielib
import HTMLParser
import requests

# 获取某个html属性的内容，如href = "http://www.baidu.com"
def attr_content(attr_list, attrname):
    for key, value in attr_list:
        if key == attrname:
            return value
    return None

# 解析页面所有发帖者的用户名
class AuthorParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)

        # parser tag
        self.is_tag = False
        self.is_a = True

        # author
        self.author_name = ""
        self.author_url = ""
        self.author_list = []

    def handle_starttag(self, tag, attrs):
        if tag == "div" and attr_content(attrs,"class")=="threadlist_author pull_right":
            self.is_tag = True

        if tag == "a" and attr_content(attrs,"class") == "frs-author-name j_user_card ":
                self.is_a = True

    def handle_endtag(self, tag):
        if tag == "div":
            self.is_tag = False

        if tag == "a":
            self.is_a = False

    def handle_data(self, data):
        if self.is_tag and self.is_a:
            self.author_name = data
            if data not in self.author_list:
                # 将获取的姓名，加入到列表中
                self.author_list.append(data)



def get_author_list(url):
    # headers
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
        "Referer": "http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5",
        }

    # 爬取贴吧的内容
    tieba_content = requests.get(url=url,headers=headers)

    # 解析爬取的内容，获取所有发帖人的用户名
    author_parser = AuthorParser()
    author_parser.feed(tieba_content.text)

    print "#" * 20
    print "所有的发帖人如下：用户名+头像地址"
    print "#" * 20

    # 根据发帖作者的用户名，获取它的头像地址，再将其保存到文件夹中
    import urllib
    import sys
    #初始化：所有发帖作者的url的统一部分
    a_author_url = "http://tieba.baidu.com/home/get/panel?ie=utf-8"
    #初始化：所有发帖作者头像的url的统一部分
    a_author_pic_url = "http://tb.himg.baidu.com/sys/portrait/item/"

    #获取每个用户名的头像
    for i in author_parser.author_list:
        # encode to utf-8
        pamas = {"un":i.encode('utf-8')}
        author_url = a_author_url + "&" + urllib.urlencode(pamas)
        author_content = requests.get(url=author_url,headers=headers)
        author_pic_url_tag = author_content.json()["data"]["portrait"]
        author_pic_url = a_author_pic_url + author_pic_url_tag


        print i
        print author_pic_url

        import os
        author_dir = "author/"
        if not os.path.isdir(author_dir):
            os.mkdir(author_dir)
        fname = i
        with open(author_dir + fname+".jpg", 'wb') as file:
            file.write(requests.get(author_pic_url).content)

    print "#" * 20
    print "所有的头像，均保存在文件夹中：author/"
    print "#" * 20

if __name__ == "__main__":
    get_author_list("http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5")

