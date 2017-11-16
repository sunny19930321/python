#coding=utf-8
a = "aAsmr3idd4bgs7Dlsf9eAF"
print a.swapcase()
a = "aAsmr3idd4bgs7Dlsf9eAF"
print ''.join(s for s in a if a.isdigit())
a = "aAsmr3idd4bgs7Dlsf9eAF"
print dict([(x,a.count(x)) for x in set(a)])