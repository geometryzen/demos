from e3ga import *
from units import *

print repr(radian)

s = ScalarE3(1)

print repr(s)

m = Measure(s, radian)

print repr(m)
