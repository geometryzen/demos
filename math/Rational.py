from units import *

try:
    x = Rational(1,2,3)
except AssertionError as e:
    print e
else:
    print "Rational() takes exactly 2 arguments (3 given)"

try:
    Rational(1.1, 2)
except TypeError as e:
    print e
else:
    print "numerator must be an int."

try:
    Rational(1, 2.2)
except TypeError as e:
    print e
else:
    print "denominator must be an int."

a = Rational(1,3)
print a
b = Rational(5,2)
print b
print a + b
print a - b
print a * b
print a / b
