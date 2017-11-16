#coding=utf-8

"""
print "2"
"""

f= open("/Users/yodo1/code-liyang/python/day01/demo1.txt",'w')

print >> f, "hahhahaha"
# print >> f, "xixixixiix"

f.close()

"""

"""
if True:
    print "True"

elif not False:
    print "False"
else:
    print "else"


print 2>3 if True else False

print [4,3][True]

x = 0
while x < 30:
    x += 1
    print x
else:
    print "end"
for x in "i am liyang 2".split(" "):
    print x
print  True and False and False and True