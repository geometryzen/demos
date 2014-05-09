from e3ga import *
from units import *

def show(name, thing):
    print "%s => %s" % (name, thing)

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)
I_3 = e1 * e2 * e3
print e1

# Conventionally, we think of the angular velocity as a vector.
# Would be nice to have radians in units here!
print 5 * e3
omegaAxial = 5 * e3 / second

print omegaAxial

show("omega (axial)", omegaAxial)

# If we treat it as a bivector we would have
omega = I_3 * omegaAxial

show("omega", omega)

# The rate of change of a vector is the left contraction of the vector with omega
show("e1 << omega", e1 << omega)
show("e2 << omega", e2 << omega)
show("e3 << omega", e3 << omega)
