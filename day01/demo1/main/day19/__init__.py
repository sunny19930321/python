#coding=utf-8
import string

"""
key=string.upper
"""
# sorted()

c = string.maketrans('lei', 'IEI')

d = 'lilei'

print d.translate(c)


def test():
    print 'test'
    return  '1423'
print test()


def test1(a=4):
    return a
print test1(a=6)

b = 3
def a():
    b = 4
    return b
print a()


def test2(**kr):
    return kr
print test2(a=0,b=1,c=3)

def test(*z,**kr):
    return z,kr
print test(1,4,12,5,[1,2,3,4],a=0,b=2)





