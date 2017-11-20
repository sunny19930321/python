#coding=utf-8
def func(*args):
    for x in args:
        if isinstance(x,int):
            pass
        else:
            return "参数有不是数字的"
    a = sorted(args,reverse=True)
    return (a[0],a[len(a)-1])

print func(1,2,3,5,7,8)


def func1(*args):
    argsDict = {x:len(x) for x in args}
    print sorted(argsDict,key = lambda k:k[1],reverse=True)
func1("123","3456")


def get_doc(module):
    return help(module)
import os
#print get_doc(str)

def get_text(f):
    r = open(f,'r')
    return r.read()

#print get_text("/Users/yodo1/code-liyang/python/day01/demo1/笔记")

list1 = []
def get_dir1(path,list_name):
    # list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            get_dir1(file_path,list_name)
        else:
            list_name.append(file_path)
    return list_name
print get_dir1("/Users/yodo1/code-liyang/python/day01",list1)


def get_num(num):
    num_ou = []
    for x in num:
        if isinstance(x,int):
            pass
        else:
            raise Exception("列表里有不是数字的")
        if x%2 == 0:
            num_ou.append(x)
    return num_ou
print get_num([1,3,4,7,8])


import urllib
def get_page(url):
    response = urllib.urlopen(url)
    return response.read()
print get_page("http://www.baidu.com")




def get_max_func(*args):
    max = 0
    for x in args:
        for y in x:
            if max < y:
                max = y
    return max

print get_max_func([1,2,3],[51,6])


import os
def get_dir2(f):
    list2=[]
    if os.path.exists(f):
        return get_dir1(f,list2)
    else:
        return "Not Dir"

print get_dir2("/Users/yodo1/code-liyang/python/day01/demo1")


def func(arg1,arg2):
    return arg1 + arg2
print dir(func.__code__)
print func.__doc__


def get_funcdoc(func):
    s = help(func)
    if str(s) is None:
        return "Not Found"
    else:
        return s
print get_funcdoc('2')


def get_cjsum():
    x = 0
    for y in [x * x for x in range(1,100)]:
        x += y
    return x
print get_cjsum()

a = [1,2,3]

def list_info(list):
   #要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了'''
    a[2] = 5
    return a
print list_info(a)#:返回结果：[1,2,5]

def get_funcname(func):
    return func.__call__
print get_funcname(list_info)
