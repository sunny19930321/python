import linecache

print linecache.getline("demo.txt",'r')
a = open("demo.txt",'r')
a.seek(0)
print a.read(1)


a = open("demo.txt",'w')
a.write("500")

a = open("demo.txt",'r')
print a.read()