# coding=utf-8

import linecache
from linecache import getline
import linecache as line
from linecache import getline as line

import urllib

d = urllib.urlopen("http://www.baidu.com")
print d.read()

import time

time.time()

import datetime

import os

os.system("ls -al")

import pickle
#
# import bsddb  #key=>value



import logging

d = datetime.datetime
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
print d.today()


# datetime.datetime.strftime()
#
# dayto = d - datetime.timedelta(days=d.day)
# date_from = datetime.datetime(dayto.year, dayto.month, 1, 0, 0, 0)
# date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
# print u'前一个月:' + str(dayto) + str(dayto)
# print '---'.join([str(date_from), str(date_to)])

import datetime
today = datetime.date.today()
day2 = today - datetime.timedelta(days=30)
print '\n1.3:'
print today
print day2


# import os
# print os.system("ping www.baidu.com")

def kouzhang(dirpwd):
    List1 = []
    List2 = os.listdir(dirpwd)

    for x in List2:
        index = x.rfind('.')  # 寻找最后一个小数点的坐标
        List1.append(x[index:])

    List3 = List1[:]
    List3 = set(List3)
    List3 = list(List3)

    print '去重之前:%s' % List1
    return '去重之后:%s' % List3


print kouzhang("./")

import pickle, random


def xulie(dirname, info):
    if not os.path.exists(dirname):
        return 'Not found!'
    a = pickle.dumps(info)  #序列化
    filename = ''
    for i in range(10):
        filename = filename + random.choice('abcedfghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890')
    filepath = os.path.join(dirname, filename)
    f = open(filepath, 'a+')
    f.write(a)
    f.flush()
    f2 = open(filepath,"r").read()
    print f2
    print pickle.loads(f2)#反序列化
    f.close()



a = [1, 2, 3, 4, 5, 6, 7]
xulie('./', a)
