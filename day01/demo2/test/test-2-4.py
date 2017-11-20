"""
lambda
"""

d = lambda  x:x+1 if x >0 else "error"
print d(2)
print d(4)
def e(x):
    return x + 1

g = lambda x:[(x,i) for i in xrange(0,10)]

print g(10)

d = [1,2,3,4,5]

g = filter(lambda x:x > 3,d)

print g


def func1(k1='',k2='',k3=''):
    return k1,k2,k3


print func1(k2="111",k1="1234",k3="111111")

"""
*kargs 元组
**kwargs 字典
参数位置
1.先是位置匹配的参数
2.再是关键字匹配的参数
3.搜集匹配的元祖参数
4.参数顺序

"""


