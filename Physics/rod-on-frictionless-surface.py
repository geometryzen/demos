from e3ga import *
from units import *

def show(measure, name):
    print "%s => %s" % (measure, name)

e1 = VectorE3(1,0,0) # Imagine pointing to the right
e2 = VectorE3(0,1,0) # Imaging going into the screen
e3 = VectorE3(0,0,1) # Imaging pointing upwards

# Force is 6 N to the right
F = 6 * newton * e1

# Moment arm is 0.5 m upwards
r = 0.5 * meter * e3

# As a vector, the torque is given by
N = - e1 * e2 * e3 * (r ^ F)

print N

# Moment of inertia for a rod of 300 grams, 1 meter long
I = (300 * gram) * (meter ** 2) / 12

print I


alpha = N/I

print sow(alpha, "alpha")
