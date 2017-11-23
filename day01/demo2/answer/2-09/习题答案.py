#encoding=utf-8

import urllib
import random
import os

def save_url_content(url,folder_path=None):	
	if not (url.startswith('http://') or url.startswith('https://') ):
		return u'url地址不符合规格'
	if not os.path.isdir(folder_path):
		return u'folder_path非文件夹'
	d = urllib.urlopen(url)
	content = d.read()
	rand_filename = 'test_%s'%random.randint(1,1000)
	file_path = os.path.join(folder_path,rand_filename)
	d = open(file_path,'w')
	d.write(content)
	d.close()
	return file_path


def get_url_count(url):
	if not (url.startswith('http://') or url.startswith('https://') ):
		return u'url地址不符合规格'
	d = urllib.urlopen(url)
	content = d.read()
	return len(content.split('<a href=')) - 1

print get_url_count('http://news.baidu.com/')
