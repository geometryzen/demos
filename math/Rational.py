from units import *

try:
    x = Rational(1,2,3)
except AssertionError as e:
    print repr(e)
    print e
    #print "I/O error({0}): {1}".format(e.errno, e.strerror)
else:
    print "Expecting a Rational constructed with three arguments to raise an error."

a = Rational(1,3)
print a
b = Rational(5,2)
print b
print a + b
print a - b
print a * b
print a / b
