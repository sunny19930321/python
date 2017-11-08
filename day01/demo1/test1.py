import stand
import sys
print stand.new_str

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
str2 = str1.lower()
print str2