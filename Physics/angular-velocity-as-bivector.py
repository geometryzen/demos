from e3ga import *
from units import *

def show(name, thing)
    print "%s => $s" % (name, thing)

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)
I_3 = e1 * e2 * e3

# Conventionally, we think of the angular velocity as a vector.
# Would be nice to have radians in units here!
omegaAxial = 5 * e3 / second

print omegaAxial

show("omega (axial)", omegaAxial)