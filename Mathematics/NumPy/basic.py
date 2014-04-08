import numpy as np
from e3ga import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(2,0,0)
e3 = VectorE3(3,0,0)
e4 = VectorE3(4,0,0)
e5 = VectorE3(5,0,0)
e6 = VectorE3(6,0,0)

x = np.array([[e1,e2,e3],[e4,e5,e6]])
print type(x)
print x.shape
print x.sizes
print type(x[1,2])
print x[1,2]