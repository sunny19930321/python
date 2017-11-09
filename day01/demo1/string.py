#coding=utf-8

def some_method():
    """
    @author:liyang
    :return:

    """
    print "this is liyang'"
    print 'this is dog"'
    print """
    hahahhah
    njahdv
    vkeaho'v
    """
    print "this is my %d %s" % (3,"apple")

    b = "this is {} {}".format("my","apple")
    print b
    c = "this is {1} {0}".format( "apple","my")
    print c

    d = "this is {key1} {value1}".format(value1="apple", key1 = "my")
    print d

    d = "this is %(key1)s %(value1)s" % {'value1':"apple", 'key1':"my"}
    print d

    """习题"""
    a = 'pyer'
    b = 'apple'

    test = "my name is {}, i love {}. ".format(a,b)
    print test
    test = "my name is %(name)s, i love %(fruits)s." % {'name':a, 'fruits':b}
    print test

some_method()