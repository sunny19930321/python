#coding=utf-8
# import threading

# def test():
#     print 1
#
# a = threading.Thread(target=test)
# b = threading.Thread(target=test)
# a.start()
# b.start()
#
# a.join()
# b.join()


import time
# def test1(p):
#     time.sleep(0.001)
#     print p
# ts = []
#
# for i in xrange(0,100):
#     th = threading.Thread(target=test1,args=[i])
#     th.start()
#     ts.append(i)

# for i in ts:


print "end"

"""
数据库连接池
"""

# num = 0
#
# def test2():
#     global num
#     num += 1
#     print num
# for i in xrange(0,100):
#     th = threading.Thread(target=test2,args=[i])
#     th.start()




# def a():
#     print "a again"
#     time.sleep(2)
#     print 'a end'
#
# def b():
#     print "b again"
#     time.sleep(2)
#     print 'b end'


# b_time = time.time()
# a()
# b()

# print time.time() - b_time

# b_time = time.time()
# _a = threading.Thread(target=a)
# _b = threading.Thread(target=a)
# _a.start()
# _b.start()
#
# _a.join()
# _b.join()
#
# print time.time() - b_time

import threading
# mlock = threading.RLock()
#
# num = 0
# def a1():
#     global num
#     mlock.acquire()
#     num += 1
#     mlock.release()
#     print num
#
# for i in xrange(0,100):
#     th = threading.Thread(target=a1)
#     th.start()

# def test():
#     i = 0
#     a = 4
#     while i < a:
#         """0,1,2,3"""
#         x = yield i
#         i += 1
# print range(0,5)
# print xrange(0,5)
# for i in test():
#     print i
#
# def test():
#     x = yield '第一部'
#     print 'hahha'
#
#     x = yield


mlock = threading.Lock()

num = 500

def a():
    global num
    for i in xrange(0,100):
        mlock.acquire()
        num += 1
        mlock.release()
l = []
for i in xrange(0,10):
    d = threading.Thread(target=a)
    d.start()
    l.append(d)
for i in l:
    i.join()
print u"当天最后的总账为: %s块" %(num)