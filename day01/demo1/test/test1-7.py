# coding=utf-8
""""
一.已经字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。

"""
s = "i,am,lilei"

t1 = s[s.find('am')] + s[s.find('am') + 1]
print t1
t1 = s[s.index('am')] + s[s.index('am') + 1]
print t1
"""
三.bool("2012" == 2012) 的结果是什么。
"""
print bool("2012" == 2012)  # False

"""
已知一个文件 test.txt，内容如下：

____________
2012来了。
2012不是世界末日。
2012欢乐多。
_____________
1.请输出其内容。
2.请计算该文本的原始长度。
3.请去除该文本的换行。
4.请替换其中的字符"2012"为"2013"。
5.请取出最中间的长度为5的子串。
6.请取出最后2个字符。
7.请从字符串的最初开始，截断该字符串，使其长度为11.
8.请将{4}中的字符串保存为test1.py文本.
"""
a = open("demo.txt", 'r')


def get_length():
    a.seek(0)
    length = len(a.read())
    return length


def get_center():
    a.seek(0)
    length = len(a.read())
    if length % 2 == 0:
        return length / 2
    else:
        # print (length + 1) / 2
        return (length + 1) / 2


print a.read()

a.seek(0)
print len(a.read())

a.seek(0)
print a.read().replace("\n", "")

a.seek(0)
b = a.read().replace("2012", "2013")
print b

center1 = get_center()
a.seek(0)
str = a.read().decode('utf-8')
print str[(center1 - 1):(center1 + 5)]

a.seek(0)
print a.read()[get_length() - 2:get_length()]

a.seek(0)
print a.read()[:11]

c = open("demo.txt", 'append')
c.write(b)

"""
六.已知如下代码

________

a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' %a
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
________

1.请给出str对象"中文编程"的引用计数
2.请给出str对象"python编程"的引用计数


"""
a = "中文编程"
print len(a)
b = a
c = a
a = "python编程"
b = '%s' % a
d = "中文编程"
e = a
c = b
b2 = a.replace("中", "中")

"""
七.已知如下变量
________
a = "字符串拼接1"
b = "字符串拼接2"
________

1.请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
2.请将a与b拼接成字符串c，并用逗号分隔。
3.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
 
"""
a = u"字符串拼接1"
b = u"字符串拼接2"

print a + b

print a + "," + b

ab = a + b
ablen = len(a+b)

print ab[6:7]


"""
八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。

1.包含0-9的数字。
2.所有小写字母。
3.所有标点符号。
4.所有大写字母和小写字母。
5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。


"""



"""
九.已知字符串
________

a = "i,am,a,boy,in,china"
________

1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
2.请使用2种办法取出其间的字符"boy"和"china"。
3.请找出第一个"i"出现的位置。
4.请找出"china"中的"i"字符在字符串a中的位置。
5.请计算该字符串一共有几个逗号。
"""
sex = "boy"
contry = "china"
a = "i,am,a,{},in,{}".format(sex,contry)
print a

print a.find('i')

print a.find('china') + "china".find('i')

print  a.count(',')

