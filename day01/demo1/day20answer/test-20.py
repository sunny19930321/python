#coding=utf-8
import linecache
import time

now = time.time() #代码开始时间
"""
文件夹里有一个twitter数据挖掘的片段，每一行则是一个tweets（微博），里面有该微博的相关字段信息。
"""
"""
@:author
@:param a
"""
# a = open('/Users/yodo1/code-liyang/python/day01/demo1/t.txt','r')
#
# def test1(a):
#     count = 0
#     uidlist = []
#     for line in a.readlines():
#         if line.split(',')[1] != "":
#             uidlist.append(line.split(',')[1])
#     print set(uidlist)
#     return len(set(uidlist))
# print test1(a)

# 前期准备，整理数据
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')


keys = {data_keys[k]:k for k in xrange(0,len(data_keys))}

f = linecache.getlines('/Users/yodo1/code-liyang/python/day01/demo1/t.txt')

lines = [x[1:-1].split('","') for x in f] #拆分

#1 输出用户总数

users = set([line[keys['username']] for line in lines])

user_total = len(set(users))

print  user_total
assert type(user_total) == int

#2 每一个用户的名字 list

users = list(users)
print users
assert type(users) == list