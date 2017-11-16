#coding=utf-8
a = "aAsmr3idd4bgs7Dlsf9eAF"
b = ""
print a.upper()
print a.lower()

print a.swapcase()
for x in range(0,10):
    if str(x) in a:
        b = b + str(x)
print b

c = a.lower()
print {'a':c.count("a"),'b':c.count('b')}

print a
l1 = list(a.lower())
new_l1 = []
for l in l1:
    if l not in new_l1:
        new_l1.append(l)
print "".join(new_l1)
#1.5
new_l2 = list(a)
r = reversed(new_l2)
print "".join(list(r))

#16

new_list3=list(a)
for x in range(0,10):
    if str(x) in a:
        new_list3.remove(str(x))

print( ''.join( sorted( new_list3 ,key = lambda x : ord( x.lower( ) ) * 2 + x.islower( ) ) ) )


#17
count = 0
for x in "boy":
    if x in a:
        count +=1
else:
    if count == 3:
        print True
    else:
        print False
#18
s = ['boy','girl','bird','dirty']
all = "".join(set("".join(s)))
count = 0
for x in all:
    if x in a:
        count += 1
else:
    if len(all) == count:
        print True
    else:
        print False

#19
a = "aAsmr3idd4bgs7Dlsf9eAF"
word = ""
max = 0
for x in a:
    if max < a.count(x):
        max = a.count(x)
        word = x
else:
    print word + ":" + str(max)

#2
# import this
# print str(help(this)).count("be")
# print str(help(this)).count("is")
# print str(help(this)).count("than")

#3
c = 102324123499123
print c  >> 10
print c  >> 10 >> 10

#4
a4 = [1, 2, 3, 6, 8, 9, 10, 14, 17]
a5 = []
print str(a4)[1:-1].replace(', ','')
for x in a4:
    a5.append(str(x))
else:
    print "".join(a5)

