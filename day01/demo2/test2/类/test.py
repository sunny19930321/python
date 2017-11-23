# coding=utf-8

"""


"""


class test(object):
    """
    get 被称之为test对象的方法

    """

    def __init__(self, var1):
        self.var1 = var1
        pass

    def get(self, a):
        return self.var1

    pass


"""
t 是 类 test 的 一个实例
"""
t = test("init test str")
a = 4
print t.get(a)


class student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.score)

    pass


zm = student('zhangming', 20, [69, 88, 100])
print zm.get_name()
print zm.get_age()
print zm.get_course()


class dictclass(object):
    def __init__(self, dic):
        self.dict = dict(dic)

    def del_dict(self, key):
        self.dict.pop(key)
        return self.dict

    def get_dict(self, key):
        if self.dict.has_key(key):
            return self.dict.get(key)
        else:
            return "not found"

    def get_key(self):
        return self.dict.values()

    def update_dict(self, undic):
        self.dict.update(undic)
        return self.dict.values()

    pass


dic = {"122": 122, "12": 12, "2": 2}
d = dictclass(dic)

up_d = {"1234": 1234, "1": 1}
print d.del_dict("12")
print d.get_dict("122")
print d.get_dict("12")
print d.get_key()
print d.update_dict(up_d)

import urllib


class URLTest(object):
    def __init__(self, url):
        if not (url.startswith('http://') or url.startswith('https://')):
            return u'url地址不符合规格'
        # self.url = url
        self.d = urllib.urlopen(url)
        self.content = self.d.read()

    def get_httpcode(self):
        return self.d.code

    def get_htmlcontent(self):
        return self.content

    def get_linknum(self):
        return len(self.content.split('<a href=')) - 1



u = URLTest("https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_6713b96d246045d59155d6c7070ce0c9")

print u.get_httpcode()
print u.get_htmlcontent()
print u.get_linknum()


class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
        '''Tell my details.'''
        print 'Name:"%s" Age:"%s"' % (self.name, self.age),

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

    def tell(self):
        print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.name

    def tell(self):
        print 'Marks: "%d"' % self.marks

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

members = [t, s]
for member in members:
    member.tell()