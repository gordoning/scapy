# encoding:utf-8
'''
by 2016-07-15
批量爬取网站上的股票信息
Input：
a,多个股票的代码或名称
b，起始日期
c,截至日期
Output：
a，文件
b，文件中是一段时间内的股票详情（开盘价/收盘价/时间等）
'''

import urllib
import logging
import datetime

# 输入：股票列表，起始日期，截至日期
def get_stock(stock_list,start,end):

    # key-value处理：起始日期（月，日，年），截至日期（月，日，年）
    parms = {'a':start.month-1,'b':start.day,'c':start.year,'d':end.month,'e':end.day,'f':end.year}

    # 每获取一个股票的所有信息，输出到一个txt文件中
    for i in stock_list:
        url = "http://ichart.yahoo.com/table.csv?"
        # 将key-value进行转码，并将其整合到url中
        qs = urllib.urlencode(parms)
        url = url + "s=" + i + "&" + qs +"&g=d&ignore=.csv"
        # 输出股票信息，将其放到文件中
        fname = i+".txt"
        urllib.urlretrieve(url,fname)

if __name__ == "__main__":
    start = datetime.date(2016,5,15)
    end = datetime.date(2016,6,16)
    stock_list = ["600000.SS","ibm"]
    #调用获取
    get_stock(stock_list,start,end)