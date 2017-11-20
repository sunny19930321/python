#coding=utf-8
#
"""
函数的基本概念
"""

# def func_name():
#     pass



def func1():
    print '13245'
    return None
test = func1()
print type(test)
print test



def func2():
    print 123453


"""
如何执照方法,函数的参数
"""
def add(num1,num2):
    return num1 + num2

print add(1,2)



def add(*num):
    d=0
    for i in num:
        d += i
    return d

print add(1,2,3,4)




def add (num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):
        return num1 * num2
    else:
        return "参数里又不是数字的类型"
print add('a',(1,2,3))




