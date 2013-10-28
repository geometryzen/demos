from e3ga import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)

# Endpoints of the Barycentric Line.
a0 = i + j
a1 = 3 * i + 4 * j

# The Barycentric coordinates sum to unity.
t0 = 0.6
t1 = 0.4

# Compute the vector from the coordinates.
a = t0 * a0 + t1 * a1

print a
# Verify that a does actually lie on the line.
print (a1 - a0) * (0.8 / 2.0) + a0
# Alternatively.
print a ^ a0 ^ a1
# Reconstruct a from ratios of outer products with alternating signs and one missing in numerator.
print ((a ^ a1)/(a0 ^ a1)) * a0 - ((a ^ a0)/(a0 ^ a1)) * a1
