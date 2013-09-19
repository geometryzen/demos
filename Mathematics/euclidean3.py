# Euclidean3 is the multivector used to represent the Geometric Algebra of 3D Euclidean space.
# It can be found in the e3ga module.
# It is also part of the three module where it unifies the Vector3 and Quaternion numbers.
from three import *

# The following function is provided for testing purposes.
def assertEqual(actual, expect):
    if expect == actual:
        pass
    else:
        print {"actual": actual, "expect": expect}

# Euclidean3 forms a Linear or Vector Space of 2**3=8 dimensions.

# Most of the time, you will want to construct scalars, vectors or rotors.
mass = Euclidean3(1, 0, 0, 0, 0, 0, 0, 0)
print mass