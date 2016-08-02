# encoding:utf-8
'''
by 2016-07-18
登陆豆瓣，突破验证码的障碍
'''

import urllib
import urllib2
import logging
import datetime
import logging
import cookielib
import HTMLParser
import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename="scrapy_douban_1.log",
                    filemode='w')

# 解析登陆页面
class DoubanParse(HTMLParser.HTMLParser):

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.verify_url = ""
        self.captcha_id = ""
        self.captcha_solution = ""

    # 获取验证码和验证id
    def handle_starttag(self, tag, attrs):
        # 获取页面中特定属性的信息
        def attr_content(attr_list,attrname):
            for key,value in attr_list:
                if key == attrname:
                    return value
            return None

        # 找到验证码的地址
        if tag == 'img' and attr_content(attrs,"id") == "captcha_image":
            self.verify_url = attr_content(attrs,"src")
            print self.verify_url
            self.captcha_solution = raw_input("请输入正确的验证码：")

        # 找到验证码的id
        if tag == 'input' and attr_content(attrs, "name") == "captcha-id":
            self.captcha_id = attr_content(attrs, "value")


def login_douban():

    # 打开登录页
    headers = {"User_Agent":"ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
               "Referer":"http://yun.baidu.com/?ref=PPZQ",
               "Host":"www.douban.com",
                "Upgrade-Insecure-Requests":1}
    req = requests.get("https://accounts.douban.com",headers=headers)

    # 解析登陆页的基本信息，得到以下信息：验证码和验证id
    douban_parser = DoubanParse()
    douban_parser.feed(req.text)
    captcha_solution = douban_parser.captcha_solution
    captcha_id = douban_parser.captcha_id

    # 设置需要提交的数据，包括用户名/密码/验证码等信息
    params = {"source": None, "redir": "https://accounts.douban.com/",
              "form_email": "linguoyang2008@126.com",
              "form_password": "642180wolf",
              "captcha-solution": captcha_solution,
              "captcha-id":captcha_id,
              "login":"登陆"}

    # 这里设计一个post请求，提交data数据，headers数据，若一切正确，则返回结果
    req_2 = requests.post("https://accounts.douban.com/login", data = params, headers=headers)
    print req_2.json()

if __name__ == "__main__":
    login_douban()