# -*- coding: utf-8 -*-
import os
import urllib2
import logging
import re


# 自定义异常类
class InvalidUrlException(Exception):
    pass


def init_log():
    fmt = '%(asctime)s %(name)s %(filename)s(%(funcName)s[line:%(lineno)d]) %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=fmt,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=os.path.join('logs.txt'),
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def url_content(url):
    s = ''
    # 用正则表达式判断url是否合法，否则抛出异常
    if not re.match(r'^https?:/{2}\w.+$', url):
        raise InvalidUrlException('Invalid url.')

    try:
        s = urllib2.urlopen(url).read()
    except urllib2.HTTPError, e:
        if e.code == 404:
            logging.error('url is not found')
        else:
            logging.error('http error:%d' % e.code)
        return None
    return s


if __name__ == '__main__':
    init_log()
    logging.info('start')

    test_url1 = 'invalidurl'
    test_url2 = 'http://wdpage'
    test_url2 = 'http://www.baidu.com/'

    cnt = ''

    try:
        cnt = url_content(test_url2)
    except InvalidUrlException, e:
        logging.error(e)

    if cnt:
        # print cnt
        pass
    logging.info('end')