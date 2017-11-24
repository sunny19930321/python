# coding=utf-8
import logging

logger = logging.getLogger()

logfile = 'test.log'
hdlr = logging.FileHandler('log.txt')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

hdlr.setFormatter(formatter)

logger.addHandler(hdlr)

logger.setLevel(logging.NOTSET)

class MyException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


class Fileinfo(object):
    def __init__(self, filename):
        self.filename = filename
        if not isinstance(self.filename, str):
            raise MyException("filename is not str")

    def __enter__(self):
        print "enter"
        try:
            d = open(self.filename,"r")
            logger.debug(self.filename)
            result = d.read()
            d.close()
            return result
        except IOError:
            logger.error("文件不存在")
            raise MyException("文件不存在")


    def __exit__(self, exc_type, exc_val, exc_tb):
        print "exit"


# with Fileinfo("/Users/yodo1/code-liyang/python/day01/demo2/test2/exception/sendlog1.txt") as f:
#     pass

# with Fileinfo(2) as f:
#     pass


import urllib

info = ['https://www.baidu.com', 'http://wdpage', 'http://www.taobao.com']

def get_page(listindex):
    if not isinstance(listindex,int):
        raise MyException("listindex is not int")
    try:
        urlinfo = info[listindex]
        openurl = urllib.urlopen(urlinfo)
    except IndexError,e:
        if e.code == 404:
            logger.error(urlinfo + "url 404 not found")
            raise Exception('url 404 not found')
        else:
            logger.debug("数组越界")
    else:
        return openurl.read()
print get_page(1)


# try:
#     code = urllib.urlopen('htt://blog.bluerain.io').getcode()
# except IOError, e:
#     if e.args[1] == 'unknown url type':
#         raise Exception('URL格式错误：未知的协议。')



