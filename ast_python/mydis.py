a = 5;

def f():
    global a
    a = a+1
    print "foo" + str(a)

import dis
print dis.dis(f)
