from units import *
from e2ga import *

r = VectorE2(3,4) * meter

print meter
print type(meter)
print type(meter.quantity)
print type(meter.uom)

print 123 * kilogram * meter / second ** 2