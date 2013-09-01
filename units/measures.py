from e3ga import *
from units import *

velocity = VectorE3(0,0,0) * meter / second ** 2
mass = ScalarE3(10) * kilogram

print velocity

momentum = mass * velocity

x = momentum * velocity

print "meter => " + str(meter)
print "meter * meter  => " + str(meter * meter)
print "meter + meter  => " + str(meter + meter)
print "meter * second => " + str(meter * second)
print "meter + second => " + str(meter + second)
