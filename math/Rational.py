from units import *

def assertEqual(actual, expect):
    if expect == actual:
        pass
    else:
        print {"actual": actual, "expect": expect}

try:
    x = Rational(1,2,3)
except AssertionError as e:
    assertEqual(str(e),"AssertionError: Rational() takes exactly 2 arguments (3 given) on line 10")
else:
    print "Expecting error"

try:
    Rational(1.1, 2)
except TypeError as e:
    assertEqual(str(e),"TypeError: numerator must be a int on line 17")
else:
    print "Expecting error"

try:
    Rational(1, 2.2)
except TypeError as e:
    assertEqual(str(e),"TypeError: denominator must be a int on line 24")
else:
    print "Expecting error"

a = Rational(1,3)
print a
b = Rational(5,2)
print b
print a + b
print a - b
print a * b
print a / b
