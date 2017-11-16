# encoding=utf-8
"""
##习题1：


列表a = [11,22,24,29,30,32]


1 把28插入到列表的末端


2 在元素29后面插入元素57


3 把元素11修改成6


3 删除元素32


4 对列表从小到大排序


##习题2：


列表b = [1,2,3,4,5]


1 用2种方法输出下面的结果：


[1,2,3,4,5,6,7,8]




2 用列表的2种方法返回结果：[5,4]


3 判断2是否在列表里


##习题3：


b = [23,45,22,44,25,66,78]


用列表解析完成下面习题：


1 生成所有奇数组成的列表


2 输出结果: ['the content 23','the content 45']


3 输出结果: [25, 47, 24, 46, 27, 68, 80]


##习题4：


用range方法和列表推导的方法生成列表：


[11,22,33]




##习题5：


已知元组:a = (1,4,5,6,7)


1 判断元素4是否在元组里


2 把元素5修改成8


##习题6：


已知集合:setinfo = set('acbdfem')和集合finfo = set('sabcdef')完成下面操作：


1 添加字符串对象'abc'到集合setinfo


2 删除集合setinfo里面的成员m


3 求2个集合的交集和并集


##习题7：


用字典的方式完成下面一个小型的学生管理系统。


1 学生有下面几个属性：姓名，年龄，考试分数包括：语文，数学，英语得分。


比如定义2个同学：


姓名：李明，年龄25，考试分数：语文80，数学75，英语85


姓名：张强，年龄23，考试分数：语文75，数学82，英语78


2 给学生添加一门python课程成绩，李明60分，张强：80分


3 把张强的数学成绩由82分改成89分


4 删除李明的年龄数据


5 对张强同学的课程分数按照从低到高排序输出。


6 外部删除学生所在的城市属性，不存在返回字符串 beijing

"""
# 习题1：
a = [11, 22, 24, 29, 30, 32]
a.append(28)
print a

a.insert(a.index(29) + 1, 57)
print a

a[a.index(11)] = 6
print a

a.remove(32)
print a

a.sort()
print a

# 习题2
b = [1, 2, 3, 4, 5]

c = [6, 7, 8]

b = b + c
print b

b = [1, 2, 3, 4, 5]
b.extend(c)
print b

b = [1, 2, 3, 4, 5]
# d  = b.reverse()
c = b[-2:]
print list(reversed(c))

b = [1, 2, 3, 4, 5]
b.sort(cmp=None, key=None, reverse=True)
c = b[:2]
print c

b = [1, 2, 3, 4, 5]
d = b[::-1]
print d[:2]

b = [1, 2, 3, 4, 5]
if 2 in b:
    print False
else:
    print True

# 习题3
b = [23, 45, 22, 44, 25, 66, 78]

d = [x for x in b if x % 2 != 0]
print d

d = ['the content %d' % x for x in b if x == 23 or x == 45]
print d

d = [x + 2 for x in b]
print d

# 习题4


d = [x * 11 for x in range(1, 4)]
print d
# 习题5
a = (1, 4, 5, 6, 7)
if a.count(10) == 0:
    print False
else:
    print True

b = list(a)
b[2] = 8
print tuple(b)
#习题6
setinfo = set('acbdfem')
finfo = set('sabcdef')
setinfo.add("abc")
print setinfo
setinfo.remove('m')
print setinfo

s = setinfo & finfo
d = setinfo | finfo
print s,d
#习题7
stu = {'name':'liyang','age':20,'score1':80,'score2':75,'score3':85}
print stu