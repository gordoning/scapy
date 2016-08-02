# encoding:utf-8
'''
by 2016-07-26
生产消费者模式（线程）
商店不断地生产啤酒
消费者不断地喝掉啤酒
'''

import logging
import datetime
import logging
import time
import random
import threading

# amount_of_beer
amount_of_beer = 0
conditon = threading.Condition()

# store: producting beer, add amount_of_beer without a break
class BeerStore(threading.Thread):
    def __init__(self,name):
        self.store_name = name
        threading.Thread.__init__(self)
        # start is necessary
        self.start()

    def run(self):

        # keep producing more and more beers, then notify other threads to consume the beers
        while True:
            global conditon
            global amount_of_beer
            produce = 10
            conditon.acquire()
            amount_of_beer += produce
            conditon.notify()
            print "PP:produce:%s.remain:%s" % (produce, amount_of_beer)
            time.sleep(1)
            conditon.release()

# consumer: cumsuming beer, sub amount_of_beer without a bread
class BeerConsumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    # keep consuming the beers, until the need_of_beer greater than the amount of the beers
    def run(self):

        while True:
            global conditon
            global amount_of_beer
            need_of_beer = 50
            conditon.acquire()
            while need_of_beer>amount_of_beer:
                conditon.wait()
            amount_of_beer -= need_of_beer
            print "CC:consume:%s.remain:%s"%(need_of_beer,amount_of_beer)
            time.sleep(1)
            conditon.release()

# start the bussiness: run BeerStore and run Consumer
def start_business():
    for i in range(3):
        consumer = BeerConsumer()
    store = BeerStore('linguoyang')
    store.run()
    for i in range(3):
        consumer.run()



if __name__ == "__main__":
    start_business()