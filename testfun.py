def f1():
    print 888
#f1()

def f2(a):
    print a
#f2(1)
#f2('abcd')

def f3(a=1,b=2,c=3):
    """this is a block remark one line remark is # """
    print 'a',a
    print 'b',b
    print 'c=%d'%c

#f3(5)
#f3(6,7)
#f3(6,6,6)
print f3(b=8,c=9)
