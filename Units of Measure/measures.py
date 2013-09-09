from e3ga import *
from units import *

def assertEqual(actual, expect):
    if expect == actual:
        pass
    else:
        print {"actual": actual, "expect": expect}

velocity = VectorE3(1,0,0) * meter / second ** 2
mass = ScalarE3(10) * kilogram
print repr(kilogram)
#mass = kilogram * ScalarE3(10)

print velocity

momentum = mass * velocity

x = momentum * velocity

print "meter => " + str(meter)
print "meter * meter  => " + str(meter * meter)
print "meter + meter  => " + str(meter + meter)
print "meter * second => " + str(meter * second)

# The following operation raises
try:
    print "meter + second => " + str(meter + second)
except AssertionError:
    print e
