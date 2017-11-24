# coding=utf-8

import sys
import logging

logger = logging.getLogger()

logfile = 'test.log'
hdlr = logging.FileHandler('sendlog.txt')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

hdlr.setFormatter(formatter)

logger.addHandler(hdlr)

logger.setLevel(logging.NOTSET)

logger.debug("liyang is a good boy")
logger.warning("liyang is a good boy")

d = open("/Users/yodo1/code-liyang/python/day01/demo2/test2/exception/sendlog.txt", 'r')

d.read()
d.close()

# with 方法

with open('a', 'r') as a:
    e = a.read()
print 4


class sth(object):
    def __init__(self, xixi):
        self.a = xixi

    def __enter__(self):
        print u"hahah"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print u"hahha 出来了"



with sth as s:
    pass
