import numpy as np

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
print x.strides
print x.buffer
print type(x[0,1,2])
#print x[0,1,2]