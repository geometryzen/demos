import numpy as np

x = np.array([1,2,3,4])
print x.strides

y = np.zeros((2,3,4))
print y.strides
print y.strides[0]