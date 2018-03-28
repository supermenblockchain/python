for x in range(100):
    print x
for y in xrange(10):
    print y

z = (1,2,"abc",3,5)
for o in z:
    print o
else:
    print "forLoop over"
    
a = 1
while a < 100:
    print a
    """if a < 50:continue"""
    a += 1
else:
    print "over!!"