from e3ga import *
from units import *
import sys

def show(name, measure):
    print "%s => %s" % (name, measure)

e1 = VectorE3(1,0,0) # Imagine pointing to the right
e2 = VectorE3(0,1,0) # Imaging going into the screen
e3 = e1.cross(e2)    # Imaging pointing upwards

# Force is 6 N to the right
F = 6 * newton * e1

show("force, F", F)

# Moment arm is 0.5 m upwards
r = 0.5 * meter * e3

show("moment arm, r", r)

# As a vector, the torque is given by
N = - e1 * e2 * e3 * (r ^ F)
# FIXME: We've lost the cross product on Euclidean3 because we have now got a measure.
N = r.cross(e1) * 6 * newton

show("torque, N = r x F", N)

# Moment of inertia for a rod of 300 grams, 1 meter long
I = (300 * gram) * (meter ** 2) / 12

show("moment of inertia, I = M * (L ** 2)/12", I)


alpha = N / I

show("angular acceleration, alpha = N / I", alpha)

print e3.cross(e1)
print r.cross(e1)
