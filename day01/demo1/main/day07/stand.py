#coding=utf-8
#上面是定义编码格式，中文需要
"这是个python demo"
import time
new_str = "这是一个全局变量"
# print "hello world"
# a = 1
# b = 2
# if a == b:
#     print '好的'
# else:
#     print '不好的'
print time.time()
a = "中国人".decode("utf-8")

print len(a)
"""
多行注释
"""
def hello():
    return "hello world"

if __name__ == "__main__":
    print hello()