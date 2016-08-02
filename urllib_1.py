# encoding:utf-8

'''
by 2016-07-15
学习urlopen , progress, msg=content.info  mgs.headers
'''

import urllib
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename="urllib_1.log",
                    filemode='a+')

# 打印列表的信息
def print_list(list):
    for i in list:
        time.sleep(1)
        print i

# 实时显示进度的信息
def progress(blk,blk_size,total_size):
    print blk
    print blk_size

# 建立HTTP连接
content = urllib.urlopen("http://pic.baidu.com")
msg = content.info()

logging.info("输出头文件信息,good")
# 输出头文件的信息
print msg.headers



# 输出HTTP的状态码
print content.getcode()

print __doc__

# print_list(content.readlines())

# 下载文件