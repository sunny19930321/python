
#coding=utf-8
"""
今天习题：

1 字符串:

a = 'abcd'

用2个方法取出字母d

2：

a = 'jay'

b = 'python'

用字符串拼接的方法输出：

my name is jay,i love python.

"""

a = 'abcd'
print a[a.find('d')]
print a[a.index('d')]

a = 'jay'

b = 'python'

print "my name is %s,i love %s" % (a, b)
