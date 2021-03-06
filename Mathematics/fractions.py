from fractions import *

def assertEqual(actual, expect):
    if expect == actual:
        pass
    else:
        print {"actual": actual, "expect": expect}

try:
    x = Fraction(1,2,3)
except AssertionError as e:
    assertEqual(str(e),"AssertionError: Fraction() takes exactly 2 arguments (3 given) on line 10")
else:
    print "Expecting error"

try:
    Fraction(1.1, 2)
except TypeError as e:
    assertEqual(str(e),"TypeError: numerator must be a <type 'int'> on line 17")
else:
    print "Expecting error"

try:
    Fraction(1, 2.2)
except TypeError as e:
    assertEqual(str(e),"TypeError: denominator must be a <type 'int'> on line 24")
else:
    print "Expecting error"

try:
    Fraction(1, 0)
except ZeroDivisionError as e:
    assertEqual(str(e),"ZeroDivisionError: denominator must not be zero on line 31")
else:
    print "Expecting ZeroDivisionError"

a = Fraction(2,3)
b = Fraction(5,2)

assertEqual(str(a),"2/3")
assertEqual(repr(a),"Fraction(2,3)")
assertEqual(a.numerator, 2)
assertEqual(a.denominator, 3)
assertEqual(a.numer, 2)
assertEqual(a.denom, 3)

assertEqual(a, a)

assertEqual(Fraction(16, -10).numer, -8)
assertEqual(Fraction(16, -10).denom, 5)

assertEqual(Fraction(123).numer, 123)
assertEqual(Fraction(123).denom, 1)

assertEqual(Fraction().numer, 0)
assertEqual(Fraction().denom, 1)

assertEqual(a + b, Fraction(19, 6))
assertEqual(a - b, Fraction(-11, 6))
assertEqual(a * b, Fraction(5, 3))
assertEqual(a / b, Fraction(4, 15))

assertEqual(a + 2, Fraction(8, 3))
assertEqual(2 + a, Fraction(8, 3))
assertEqual(a - 2, Fraction(-4, 3))
assertEqual(2 - a, Fraction(4, 3))
assertEqual(a * 2, Fraction(4, 3))
assertEqual(2 * a, Fraction(4, 3))
assertEqual(a / 2, Fraction(1, 3))
assertEqual(2 / a, Fraction(3, 1))

try:
    a / 0
except ZeroDivisionError as e:
    assertEqual(str(e),"ZeroDivisionError: denominator must not be zero on line 73")
else:
    print "Expecting ZeroDivisionError"

try:
    a / Fraction(0, 1)
except ZeroDivisionError as e:
    assertEqual(str(e),"ZeroDivisionError: denominator must not be zero on line 80")
else:
    print "Expecting ZeroDivisionError"

try:
    2 / Fraction(0, 1)
except ZeroDivisionError as e:
    assertEqual(str(e),"ZeroDivisionError: denominator must not be zero on line 87")
else:
    print "Expecting ZeroDivisionError"

print "Done!"
