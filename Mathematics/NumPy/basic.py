import numpy as np
from e3ga import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(2,0,0)
e3 = VectorE3(3,0,0)
e4 = VectorE3(4,0,0)
e5 = VectorE3(5,0,0)
e6 = VectorE3(6,0,0)
e7 = VectorE3(6,0,0)
e8 = VectorE3(6,0,0)

x = np.array([[
               ['a','b','c','d'],
               ['e','f','g','h']
              ],
              [
               ['i','j','k','l'],
               ['m','n','o','p']
              ],
              [
               ['q','r','s','t'],
               ['u','v','w','x']
              ]
             ])
print type(x)
print x.shape
print x.sizes
print x.buffer
print type(x[1,2])
print x[0,1]