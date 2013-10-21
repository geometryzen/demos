from e3ga import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)

# Endpoints of the Barycentric Line.
a1 = i + j
a2 = 3 * i + 4 * j

# The Barycentric coordinates sum to unity.
t1 = 0.6
t2 = 0.4

# Compute the vector from the coordinates.
a = t1 * a1 + t2 * a2

print a
# Verify theat a does actually lie on the line.
print (a2 - a1) * (0.8 / 2.0) + a1
# Alternatively.
print a ^ a1 ^ a2
# Reconstruct a from ratios of outer products with alternating signs and one missing in numerator.
print ((a ^ a2)/(a1 ^ a2)) * a1 - ((a ^ a1)/(a1 ^ a2)) * a2
