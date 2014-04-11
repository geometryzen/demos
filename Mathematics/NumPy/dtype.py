import numpy as np

a = np.array([1, 4, 5, 8], float)

print a
print type(a)
print a[0]
print type(a[0])
print a[:2]
print a[3]
a[0] = 5.
print a

a = np.array([[1,2,3],[4,5,6]], float)
print a
print a[0,0]
print a[0,1]

# The parser does not seem to appreciate this.
#print a[1,:]

print a.shape
print a.dtype

print len(a)

print 2 in a
print 0 in a

a = np.array(range(10), float)
print a
b = a.reshape((5,2))
print b
print b.shape

c = b.copy()
print c
print type(c)
print c[3]
c[0] = 7
print c
print b