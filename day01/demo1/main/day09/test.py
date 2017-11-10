#encoding=utf-8

def info(a):
    b = a[:]
    print 'd %d' % id(a)
    return a
a = [1,2,3]

print  'start-'
print id(a)
info(a)

print a