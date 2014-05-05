from e3ga import *
from units import *

e1 = VectorE3(1,0,0) # Imagine to right
e2 = VectorE3(0,1,0) # Imaging into screen
e3 = VectorE3(0,0,1) # Imaging pointing up


alpha = (0.5 * meter) * (6 * newton) / ((0.3 * kilogram * meter ** 2)/12)

print alpha
