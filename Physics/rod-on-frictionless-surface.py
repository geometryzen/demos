from e3ga import *
from units import *

e1 = VectorE3(1,0,0) # Imagine pointing to the right
e2 = VectorE3(0,1,0) # Imaging going into the screen
e3 = VectorE3(0,0,1) # Imaging pointing upwards

# Force is 6 N to the right
F = 6 * newton * e1

# Moment arm is 0.5 m upwards
r = 0.5 * meter * e2

# As a bivector, the torque is given by
N = r.cross(F)

print N

# Moment of inertia for a rod of 300 grams, 1 meter long
I = (300 * gram) * (meter ** 2) / 12

print I


alpha = (0.5 * meter) * (6 * newton) / ((0.3 * kilogram * meter ** 2)/12)

print alpha
print N / I
