import sys

import demo1.main.stand

print demo1.main.day07.stand.new_str

d = [1,2,3]

count = sys.getrefcount(d)
print count
a = 1
b = 1
c = 2
d = 4
if (a == b) and (c == d):
    print "ok"
else:
    print "no"
    # del a,b,c,d

str1 = "abc"
str2 = str1.replace("b","d")
print str2
a = 10
print "my name is %d"% a
print "my name is %s %s" % ("liyang","haimeimei")

a = "a"
b = "qfwargetrsg"
c = "fwaregfsr"
"".join([a,b,c])

d = open("demo.txt", 'r')#model: w,r,append
# d.write("hi liyang \n")
d.read(10000)
d.seek(0)
print d.read(1000)